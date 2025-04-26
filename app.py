from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from Test import Test

app = Flask(__name__)
app.config.from_object(Config)
db: SQLAlchemy = SQLAlchemy(app)

# Sample data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]


# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# Route to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    print(Test.square(10))
    return jsonify(users_list)


if __name__ == '__main__':
    app.run(debug=True)
