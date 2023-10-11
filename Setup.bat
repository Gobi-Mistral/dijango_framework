@echo off	

set ROOT_DIR=%~dp0

CALL :create_and_activate_venv
CALL :deactivate_venv

EXIT /B 0

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