**Automation of Digilens test cases**

![Screenshot](test_setup.jpg)

This document explains about the pre-requisites and test setup required to carry out the automated tests based on the configurations

All the configuration variables are defined in the .env file which are necessary for the automated test execution. This file need to be updated prior to running the automation test suite. 

**Pre-Requisites**

Following softwares should be installed on the Windows PC based on the project requirement: ** For Example ** - The Appium Python Client depends on Selenium Python binding, Becuase the Selenium Python binding update might affect the Appium Python Client behavior. For example, some changes in the Selenium binding could break the Appium client.

- Python 3.8 or latest version
- Appium Server (1.22.3-4) or latest version
- selenium==4.0.0
- Appium-Python-Client==2.0.0
- Chrome browser latest version - (Download the same version of selenium driver for all browsers based on requirements)
- Firefox browser latest version
- Edge browser latest version

Following android apps are installed on the device based on project requirement: (For example)

- Chrome Browser (Same as windows chrome version)

**Confiure Before Execution of Automation test suite**

- Update the Environment variables prior to running the automation test suite
  - PLATFORM -> Update the Platform name based on test execution. Platform are available for "WEB", "ANDROID" and "DESKTOP"
  - PLATFORM_NAME, PLATFORM_VER, DEVICE_NAME -> Update the device details based on the device under test
  - DEVICE_APP_NAME -> Device Apps are available for "Native" and "Hybrid" - Hybrid will open configured browsers, Native will 					   open default or installed apps
  - DEVICE_APP_PACKAGE, DEVICE_APP_ACTIVITY, DEVICE_BROWSER_NAME -> Update the device details based on the device under test
  - APPIUM_SERVER -> Appium server link
  - BROWSER_URL -> URL to access the app from the browser for basic sample test
  - APP_USERNAME -> App username
  - APP_PASSWORD -> App password
  - BROWSER -> Update the Browser name based on test execution. Browsers are available for "CHROME", "FIREFOX" and "EDGE"

**Execution of Automation test suite**

- Start the Appium server on Windows PC for running android test 
- Clone the automation test suite from GitHub using the following command
  - git clone https://github.com/digilens-ar/device-test-automation.git
- Open windows command prompt and navigate to the project root directory
- Execute the following commands to install the Python dependent modules by creating a virtual environment
  - python -m venv venv
  - venv\Scripts\activate.bat
  - pip install -r requirements.txt -> This will install all the dependent packages
- Execute the following command to run the automated tests
  - python manage.py test -> This will start the execution of automated tests
- Execute the following command to run the automated tests for a specific module
  - python manage.py test dijango_framework.test_modules.test_browser -> This will execute the sample test on the configured   web browser
  - python manage.py test dijango_framework.test_modules.test_android_device -> This will execute the sample tests on the configured android device
  