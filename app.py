from flask import Flask, request, jsonify
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

@app.route('/tasks', methods=["GET"])
def all_tasks():
    tasks = Task.query.all()

    return jsonify({
                "message": "Tasks fetched successfully", 
                "tasks": [
                    {
                        'id': str(t.id), 
                        'title': t.title, 
                        'description': t.description
                    }
                    for t in tasks
                ]
            })

@app.route('/create', methods=["POST"])
def create_task():
    if request.method == "POST":
        data = request.get_json()

        # getting the input data inform of json
        title = data.get('title')
        description = data.get('description')
        completed = data.get('completed')

        new_task = Task(
                title=title,
                description=description,
                completed=completed
                )
        db.session.add(new_task)
        db.session.commit()

        return {"message": f"Task <{Task.title}> added successfully"}


@app.route('/edit', methods=["POST"])
def edit_task(task_id):
    tasks = Task.query.filter_by(id=task_id)
    
    # Json format
    data = request.get_json()

    # Editing the files
    tasks.title = data.get('title')
    tasks.description = data.get('description')
    tasks.completed = data.get('completed')

    db.session.commit()

    return {"message": f"Task <{Task.title}> updated successfully"}

@app.route('/delete', methods=["POST"])
def delete_task(task_id):
    tasks = Task.query.filter_by(id=task_id)

    db.session.delete()

    return {"message": "Deleted Successfully"}

# Entry point
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")

