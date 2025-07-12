from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from models.models import db, User

# Initialize app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

# Database
db.init_app(app)

# Login Manager
login_manager = LoginManager()
login_manager.login_view = 'user_routes.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
from routes.user_routes import bp as user_routes
from routes.swap_routes import bp as swap_routes
from routes.admin_routes import bp as admin_routes

app.register_blueprint(user_routes)
app.register_blueprint(swap_routes)
app.register_blueprint(admin_routes)

@app.route('/')
def home():
    return "<h1>Welcome to Skill Swap Platform</h1><p>Please <a href='/login'>log in</a> or <a href='/register'>register</a>.</p>"

# Run
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
