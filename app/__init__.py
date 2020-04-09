from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

# local import
from instance.config import app_config

# initialize SQLAlchemy
db = SQLAlchemy()

def create_app(config_name):
    """App Factory. Produces different app configurations based on the config passed"""
    
    from app.views import bucketlists_bp

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(bucketlists_bp)

    return app
