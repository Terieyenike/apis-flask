from flask import Flask, request


app = Flask(__name__)

student = []

@app.get("/api/v1.0/students")
def students():
  return student

@app.post("/api/v1.0/students")
def create_student():
  name = request.form['name']
  country = request.form['country']
  city = request.form['city']
  skills = request.form['skills'].split(', ')
  bio = request.form['bio']
  birthyear = request.form['birthyear']
  details = {
    'name': name,
    'country': country,
    'city': city,
    'birthyear': birthyear,
    'skills': skills,
    'bio': bio,
  }
  student.append(details)
  return details