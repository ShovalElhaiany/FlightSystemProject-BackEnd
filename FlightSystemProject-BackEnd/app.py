from src.create_app import init_app
from src.my_app import app

if __name__ == '__main__':
        init_app()
        app.run(debug=True, host='0.0.0.0')