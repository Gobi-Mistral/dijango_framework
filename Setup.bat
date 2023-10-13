@echo off

set argC=0

for %%x in (%*) do Set /A argC+=1

if %argC% NEQ 1 (
	echo ---------------------------------
	echo Usage: %0 option
	echo E-g: %0 Android_Apps_Test
	echo ---------------------------------
	echo Following are the options available
	echo -----
	echo setup_environment
	echo -----
	echo Web_Browser_Test
	echo Android_Apps_Test
	echo Desktop_Apps_Test
	exit /B 0
)	

set ROOT_DIR=%~dp0

set user_input=%1

CALL :setup_environment

CALL :%user_input%

CALL :deactivate_venv

EXIT /B 0

:setup_environment
	if not exist venv\ (
		CALL :create_and_activate_venv
	) else (
		CALL :activate_venv
	)
	
	EXIT /B %ERRORLEVEL%
	
:create_and_activate_venv
	echo Creating the Python virtual environment
	python -m venv venv

	CALL :activate_venv

	echo Installing the recessary python packages
	pip install -r requirements.txt

	EXIT /B %ERRORLEVEL%

:activate_venv
	echo Activating the Python virtual environment
	CALL venv\Scripts\activate.bat

	EXIT /B %ERRORLEVEL%
	
:deactivate_venv
	echo Deactivating the Python virtual environment
	CALL venv\Scripts\deactivate.bat

	EXIT /B %ERRORLEVEL%
	
:run_test
	python manage.py test %~1
	if %ERRORLEVEL% EQU 0 (
		echo "****** %~1 (%cnt%) - PASS"
	) else (
		echo "###### %~1 (%cnt%) - FAIL"
	)
	EXIT /B %ERRORLEVEL%	
	
:backup_report
	set report_name=Report_%~1	

	copy reports\junit.xml reports\%report_name%.xml
	
	EXIT /B %ERRORLEVEL%
	
:Web_Browser_Test
	echo Web Browser Test - Testing Asus Router
	CALL :run_test dijango_framework.test_modules.test_web_apps
	CALL :backup_report Browser_Asus_Router
	EXIT /B %ERRORLEVEL%
	
:Android_Apps_Test
	echo Android Test - Testing Android Settings
	CALL :run_test dijango_framework.test_modules.test_android_apps
	CALL :backup_report Android_Settings
	EXIT /B %ERRORLEVEL%
	
:Desktop_Apps_Test
	echo Android Test - Testing Desktop Apps
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_002_activation_key_generator
	CALL :backup_report Desktop_Apps
	EXIT /B %ERRORLEVEL%