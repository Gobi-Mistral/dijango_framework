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
	python manage.py jenkins %~1
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
	
:updated_env_file
	sed -i "s|^%~1=.*|%~1=%~2|" .env
	timeout /t 3 /nobreak
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
	echo Desktop Test - Testing Desktop Apps
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_003_interface_test_server
	CALL :backup_report Desktop_Apps
	EXIT /B %ERRORLEVEL%
	
:Different_Web_Browser_Test
	echo ==============================================================================
	echo Chrome Browser Test - Testing Asus Login with Chrome Browser
	echo ==============================================================================
	CALL :updated_env_file PLATFORM WEB
	CALL :updated_env_file BROWSER CHROME
	CALL :run_test dijango_framework.test_modules.test_web_apps
	CALL :backup_report Chrome_Browser_Asus_Router
	
	echo ==============================================================================
	echo Firefox Browser Test - Testing Asus Login with Firefox Browser
	echo ==============================================================================
	CALL :updated_env_file PLATFORM WEB
	CALL :updated_env_file BROWSER FIREFOX
	CALL :run_test dijango_framework.test_modules.test_web_apps
	CALL :backup_report Firefox_Browser_Asus_Router
	
	echo ==============================================================================
	echo Edge Browser Test - Testing Asus Login with Edge Browser
	echo ==============================================================================
	CALL :updated_env_file PLATFORM WEB
	CALL :updated_env_file BROWSER EDGE
	CALL :run_test dijango_framework.test_modules.test_web_apps
	CALL :backup_report EDGE_Browser_Asus_Router
	
	EXIT /B %ERRORLEVEL%
	
:Desktop_Different_Apps_Test
	echo ==============================================================================
	echo Desktop Test 1 - Testing Windows10 Calculator App
	echo ==============================================================================
	CALL :updated_env_file PLATFORM DESKTOP
	CALL :updated_env_file DESKTOP_APP Microsoft.WindowsCalculator_8wekyb3d8bbwe!App
	rem sed -i 's/^DESKTOP_APP=.*/DESKTOP_APP=Microsoft.WindowsCalculator_8wekyb3d8bbwe!App/' .env
	rem timeout /t 3 /nobreak
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_001_calculator_app
	CALL :backup_report Desktop_App_Calculator
	
	echo ==============================================================================
	echo Desktop Test 2 - Testing Activation Key Generator App
	echo ==============================================================================
	CALL :updated_env_file DESKTOP_APP D://Software_Installation//ScripTalk//Activation_Key_Generator.exe
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_002_activation_key_generator
	CALL :backup_report Desktop_App_Activation_Key_Generator
	
	echo ==============================================================================
	echo Desktop Test 3 - Testing Test Data Server App
	echo ==============================================================================
	CALL :updated_env_file DESKTOP_APP D://Software_Installation//ScripTalk//InterfaceTestServer.exe
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_003_interface_test_server
	CALL :backup_report Desktop_App_Test_Data_Server
	
	echo ==============================================================================
	echo Desktop Test 4 - Testing Windows10 Groove Music App
	echo ==============================================================================
	CALL :updated_env_file DESKTOP_APP Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic
	CALL :run_test dijango_framework.test_modules.test_desktop_app.TestDesktop.test_004_desktop_groove_music_app
	CALL :backup_report Desktop_App_Groove_Music
	
	EXIT /B %ERRORLEVEL%

:repeat_run_test
	SET cnt=1
	SET TEST_COUNT=3

	echo ==============================================================================
	echo Repeat Test Iteration Start - %cnt% End - %TEST_COUNT%	
	echo ==============================================================================
	REM SET /P "RUN_TEST="

	:continue_loop
	if %cnt% leq %TEST_COUNT% (
		echo "*** TEST ITERATION (%cnt%) ***"	
		
		CALL :Different_Web_Browser_Test
		CALL :Desktop_Different_Apps_Test

		ping 127.0.0.1 -n 2 > nul

		SET /A "cnt = cnt + 1"

		goto :continue_loop
	)
	SET cnt=1
	SET TEST_COUNT=1
	EXIT /B %ERRORLEVEL%