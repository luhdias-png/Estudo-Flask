from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['SECRET_KEY']= "147852369"                          #Token de segurança

database = SQLAlchemy(app)
migrate = Migrate(app, database)

from estudo.views import homepage
from estudo.models import Contato