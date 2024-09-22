:: Change directory to the script's directory
CD %~dp0
:: Activate the virtual environment and run the main script
call .venv\Scripts\activate.bat
:: Run the main script
python haptics_lab_py\run\main.py

