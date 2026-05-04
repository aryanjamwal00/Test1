from flask import Flask
from flask_cors import CORS
from models import db
from routes.auth import auth_bp
from routes.opportunity import opp_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(opp_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)