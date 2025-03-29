# Quantum Operations with Flask API

This project implements a simple Flask API that performs quantum operations using `numpy` for simulating quantum circuits and operations. The application also provides an API for user registration and stores their data in an SQLite database.

## Features
- **User Registration API**: Allows user registration with basic username and password, storing data in an SQLite database.
- **Quantum Operations API**: Simulates quantum circuits and performs quantum operations using `numpy` to handle qubits and quantum states.

## Project Structure

- **/v1/**: Contains version 1 of the project with basic user registration and quantum operations.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quantum-operations-flask-api.git
   ```
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Run the application:
    ```bash
    python app.py
    ```

## Endpoints

### POST /register: User registration
This endpoint registers a new user.

Response:
   ```json
    {
      "message": "User registered successfully"
    }
   ```

### GET /quantum: Perform quantum operations (simulated)
This endpoint simulates quantum operations.

Response:
   ```json
    {
      "message": "Quantum circuit executed successfully"
    }
   ```

## Copyright

Copyright © 2025 Stas Kozosvyst (StasX). All rights reserved.

This project is licensed under the MIT License - see the LICENSE file for details.
