from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Db configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_MODIFICATION_TRACK"] = False

db = SQLAlchemy()
db.init_app(app)


# Database model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean)


# Routes
@app.route('/')
def index():
    return {"message": "Hello welcome to my flask API"}



# Entry point
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")

