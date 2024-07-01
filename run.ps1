py -m venv .venv
.venv/scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
$Env:FLASK_DB_HOST='localhost'
$Env:MYSQL_NAME='flights_system_db'
$Env:MYSQL_ROOT_PASSWORD='password'
python app.py