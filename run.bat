@REM Application run script

py src/deploy_env.py
.venv/scripts/activate
python.exe -m pip install --upgrade pip
python app.py