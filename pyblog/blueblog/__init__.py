# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueblog import config

app = Flask('blueblog')
app.config.from_object(config)
db = SQLAlchemy(app)


from blueblog.blueprints.auth import auth_bp   
app.register_blueprint(auth_bp, url_prefix='/auth')