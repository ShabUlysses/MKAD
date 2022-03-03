from flask import Flask

from app.main import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app


app = create_app()

if __name__ == '__main__':
    app.debug = 1
    app.run(host='0.0.0.0')


