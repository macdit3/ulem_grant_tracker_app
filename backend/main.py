from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Grant Tracker API",
        "about": "This is a prototype for the grant tracking API",
        "author": "MSIMBO",
        "version": "0.0.1"
    }

# Donors endpoint
@app.get("/donors")
def read_donors():
    return [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Jane", "last_name": "Smith"}
    ]

# Programs endpoint
@app.get("/programs")
def read_programs():
    return [
        {"name": "Program 1"},
        {"name": "Program 2"},
        {"name": "Program 3"},
        {"name": "Program 4"}
    ]

