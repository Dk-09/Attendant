from flask import Flask, session, cli
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import logging


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECRET_KEY'] = "a7158782b8d58643f8fd5c5f"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # Disable sql_alchemy warning
app.config['TEMPLATES_AUTO_RELOAD']=True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "loginpage"
login_manager.login_message_category = "info"
login_manager.session_protection = "strong"
log = logging.getLogger('werkzeug') # Disable request detail
log.disabled = True
cli.show_server_banner = lambda *_: None # Remove warning


from main import routes
