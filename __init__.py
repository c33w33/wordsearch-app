import os
from flask import Flask


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,
                template_folder="templates", static_folder="static")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        import routes

    return app
