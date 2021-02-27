import os

from flask import Flask, redirect, url_for, render_template


def create_app(test_config=None):
    #craate and cofig the globall settings webappsite
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )

    if test_config is None:
        #cargar las instancias de config, si estas excisten cuando no estamos probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # cargar el test si este ha pasado en
        app.config.from_mapping(test_config)

    # asegurar si el folder que contiene la instancia existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    from . import auth
    app.register_blueprint(auth.bp)
    db.init_app(app)

    return app

    # a simplemente el inicio de la configuracion dira hola para probrar la logica del site

    @app.route('/hello')
    def hello():
        return 'hola'

    return app
