import subprocess
import venv

venv_path = '.venv'
requirements_file = 'requirements.txt'

venv.create(venv_path, with_pip=True)
activate_script = 'Scripts\\activate.bat'
activate_path = f'{venv_path}/{activate_script}'

subprocess.call(f'call {activate_path} && pip install -r {requirements_file}', shell=True)