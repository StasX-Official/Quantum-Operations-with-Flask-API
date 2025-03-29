from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import sqlite3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"message": "User already exists"}), 400
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/quantum', methods=['GET'])
def quantum():
    try:
        state = np.array([1, 0])
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        state = np.dot(H, state)
        
        CNOT = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        state = np.dot(CNOT, np.kron(state, state))
        
        state = np.round(state, 6)

        probabilities = np.abs(state)**2
        
        return jsonify({
            "message": "Quantum circuit executed successfully",
            "final_state": state.tolist(),
            "probabilities": probabilities.tolist()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
