from flask import Flask, render_template
from flask_cors import CORS
from config import config
from flask_login import LoginManager


#Routes

from routes import User

app = Flask(__name__)

app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



##CORS(app, resources={"*":{"origins": "http://localhost:3000"}})

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints 
    app.register_blueprint(User.main, url_prefix='/api/users')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
