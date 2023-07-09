import subprocess
import venv

def create_venv(venv_path):
    """
    Creates a virtual environment at the specified path.

    Args:
        venv_path (str): The path where the virtual environment should be created.
    """
    venv.create(venv_path, with_pip=True)


def install_requirements(activate_path, requirements_file):
    """
    Installs the required packages from a requirements file.

    Args:
        activate_path (str): The path to the activation script of the virtual environment.
        requirements_file (str): The path to the requirements file.

    Raises:
        Exception: If an error occurs during the installation process.
    """
    subprocess.call(f'call {activate_path} && pip install -r {requirements_file}', shell=True)


venv_path = '.venv'
requirements_file = 'src/requirements.txt'

create_venv(venv_path)
activate_script = 'Scripts\\activate.bat'
activate_path = f'{venv_path}/{activate_script}'

install_requirements(activate_path, requirements_file)

