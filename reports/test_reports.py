import smtplib
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

import openpyxl
import pandas as pd
import os
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import xml.etree.ElementTree as ET
from pathlib import Path
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from openpyxl import Workbook
from openpyxl.chart import PieChart, BarChart, Reference

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
print(f"Project directory: {ROOT_DIR}")
report_directory = str(ROOT_DIR) + "/reports/"
report_file = report_directory + "Test_Report.xlsx"
report_file_name = "Test_Report.xlsx"
report_file_junit = report_directory + "junit.xml"

test_mail_id = "mailidforautomationtesting@gmail.com"
test_mail_password = "qtbkcwkxepobddpb"

test_sum = {}

def get_report_module_name(file_name, occurance, seperator):
    split_items = file_name.split(seperator)
    # print(all_split)
    return seperator.join(split_items[0:occurance])

def create_excel_report_as_per_junit_xml():
    # Excel reports are created with high level according to the generated junit.xml - Include pass, fail, error, skip count and reason of failures
    print(f"Report directory: {report_directory}")
    file_names_frm_dir = os.listdir(report_directory)
    test_module_name = ""
    excel_sheet_name = ""
    read_data_frm_xml_3 = []
    all_modules_test_result = []

    test_summary = {}
    module_names = []
    total_cnt = []
    pass_cnt = []
    sum_fail = []
    error_cnt = []
    skip_cnt = []
    execution_time = []

    for file_name in file_names_frm_dir:
        # print(file_name)

        if ".xml" in file_name:
            if file_name != "junit.xml":
                print(f"Processing the report {file_name}")
                excel_sheet_name = get_report_module_name(file_name, 3, "_")
                xml_file = report_directory + file_name
                tree = ET.parse(xml_file)

                root = tree.getroot()

                test_module = []
                test_case_id = []
                test_status = []
                test_info = []

                errors = root.attrib.get('errors', '')
                tests = root.attrib.get('tests', '')
                time = root.attrib.get('time', '')
                failures = root.attrib.get('failures', '')
                skips = root.attrib.get('skips', '')
                passed = int(tests) - int(errors) - int(failures) - int(skips)
                seconds = float(time)
                hours = int(seconds // 3600)
                minutes = int((seconds % 3600) // 60)
                remaining_seconds = int(seconds % 60)
                time_format = "{:02d}h {:02d}m {:02d}s".format(hours, minutes, remaining_seconds)
                # time_format = float(seconds // 60)

                module_names.append(excel_sheet_name)
                total_cnt.append(int(tests))
                pass_cnt.append(passed)
                sum_fail.append(int(failures))
                error_cnt.append(int(errors))
                skip_cnt.append(int(skips))
                execution_time.append(time_format)

                for testcase in root.iter('testcase'):
                    name = testcase.attrib['name']
                    classname = testcase.attrib['classname']
                    module = classname.split(".")[2].strip().replace("test_", "")
                    test_module_name = module
                    status = "PASS"
                    info = "-"
                    failure_elem = testcase.find('failure')
                    if failure_elem is not None:
                        status = "FAIL"
                        error_message = failure_elem.attrib['message']
                        error_details = failure_elem.text
                        info = error_message

                    error_elem = testcase.find('error')
                    if error_elem is not None:
                        status = "ERROR"
                        error_message = error_elem.attrib['message']
                        error_details = error_elem.text
                        info = error_message

                    skipped_elem = testcase.find('skipped')
                    if skipped_elem is not None:
                        status = "SKIP"
                        error_message = skipped_elem.attrib['message']
                        error_details = skipped_elem.text
                        info = error_message

                    test_module.append(module)
                    test_case_id.append(name)
                    test_status.append(status)
                    test_info.append(info)

                module_test_result = {'Module': test_module,
                                      'Test Cases': test_case_id,
                                      'Status': test_status,
                                      'Info': test_info
                                      }

                xml_module_test_result = {test_module_name: module_test_result}
                xml_individual_module_result = {excel_sheet_name: xml_module_test_result}
                all_modules_test_result.append(xml_individual_module_result)

    test_summary = {'Module': module_names,
                    'TOTAL': total_cnt,
                    'PASS': pass_cnt,
                    "FAIL": sum_fail,
                    'SKIP': skip_cnt,
                    "ERROR": error_cnt,
                    "DURATION": execution_time
                    }

    # print(f"Test Summary Data {test_summary}")
    # print(all_modules_test_result)
    writer = pd.ExcelWriter(report_file, engine='openpyxl')
    df_sheet = pd.DataFrame(test_summary)
    df_sheet.to_excel(writer, sheet_name='Summary', index=False)

    for individual_module_result in all_modules_test_result:
        for module_result in individual_module_result:
            print(f"Parsing the results for the module {module_result}")
            module_test_result = individual_module_result[module_result]
            for module_name in module_test_result:
                print(f"Logging the results for the module {module_name}")
                module_test_report = module_test_result[module_name]
                df_sheet = pd.DataFrame(module_test_report)
                df_sheet.to_excel(writer, sheet_name=module_name, index=False)

    workbook = writer.book
    workbook.save(report_file)

    return test_summary

def send_excel_report_to_mail():
    # Sending the generated Excel report to the configured mail id
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = test_mail_id
    receiver_email = test_mail_id
    password = test_mail_password
    subject = "Test Reports on " + datetime.now().strftime("%A, %d %B %Y %I:%M %p")
    body = "Test execution is completed, find the detailed reports."

    # Configuration Details
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(report_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % report_file_name)

    msg.attach(part)

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        status = "Email sent successfully!"
        print(status)
    except Exception as e:
        # Print any error messages to stdout
        print("Exception ", e)

def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    test_cases = []
    for testcase in root.iter('testcase'):
        test_case = {
            'name': testcase.attrib['name'],
            'status': 'pass' if len(testcase.findall('failure')) == 0 else 'fail'
        }
        test_cases.append(test_case)

    return test_cases

def create_bar_chart(test_cases):
    status_counts = {'pass': 0, 'fail': 0}
    for test_case in test_cases:
        status_counts[test_case['status']] += 1

    statuses = list(status_counts.keys())
    counts = list(status_counts.values())

    plt.bar(statuses, counts, color=['green', 'red'])
    plt.xlabel('Test Status')
    plt.ylabel('Count')
    plt.title('Test Status Distribution')
    # plt.show()
    plt.savefig('bar_chart.png')

def create_pie_chart(test_cases):
    status_counts = {'pass': 0, 'fail': 0}
    for test_case in test_cases:
        status_counts[test_case['status']] += 1

    statuses = list(status_counts.keys())
    counts = list(status_counts.values())

    plt.pie(counts, labels=statuses, colors=['green', 'red'], autopct='%1.1f%%')
    plt.title('Test Status Distribution')
    # plt.show()
    plt.savefig('pie_chart.png')

def pie_and_bar_chart(test_sum):
    # Create DataFrames from the dictionary
    test_summary_no_module = pd.DataFrame(test_sum)
    # test_summary_no_module = test_summary_df.drop('Module', axis=1)

    # Create Pie Chart
    status_totals = test_summary_no_module.iloc[0, 1:]  # Extracting the first row excluding the 'Module' column
    labels = status_totals.index

    plt.figure(figsize=(8, 6))
    plt.pie(status_totals, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Test Status Distribution')
    plt.axis('equal')
    # plt.show()
    plt.savefig('pie_chart_1.png')

    # Create Bar Chart
    plt.figure(figsize=(10, 6))
    test_summary_no_module.plot(kind='bar')#, x='Module')
    plt.title('Test Summary')
    # plt.xlabel('Module')
    plt.xlabel(test_sum['Module'])
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()
    plt.savefig('bar_chart_1.png')

def insert_pie_bar_chart_in_excel_report():
    wb = Workbook()
    ws = wb.active

    # Insert pie chart
    img_pie = openpyxl.drawing.image.Image('pie_chart_1.png')
    ws.add_image(img_pie, 'A5')  # Adjust the cell where you want to place the chart

    # Insert bar chart
    img_bar = openpyxl.drawing.image.Image('bar_chart_1.png')
    ws.add_image(img_bar, 'A5')  # Adjust the cell where you want to place the chart

    # Save the Excel file
    wb.save('Test_Report_1.xlsx')


if __name__ == "__main__":
    # Assuming your JUnit XML file is 'junit_report.xml'
    file_path = report_file_junit

    # Parsing JUnit XML file
    test_cases = parse_junit_xml(file_path)

    # Creating bar and pie charts
    create_bar_chart(test_cases)
    create_pie_chart(test_cases)

    test_sum = create_excel_report_as_per_junit_xml()
    print("Test Sum ", test_sum)

    # Get all the keys from the dictionary and remove the last one
    if len(test_sum) > 0:
        last_key = list(test_sum.keys())[-1]
        test_sum.pop(last_key)

    print("Test : ",test_sum)

    pie_and_bar_chart(test_sum)

    insert_pie_bar_chart_in_excel_report()