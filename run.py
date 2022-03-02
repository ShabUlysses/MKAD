from flask import Flask

from app.main_module import main


def create_app():  # Create application with Flask
    app = Flask(__name__)
    app.register_blueprint(main)  # Register blueprint
    return app


app = create_app()

if __name__ == '__main__':
    app.debug = 1
    app.run(host='0.0.0.0')


