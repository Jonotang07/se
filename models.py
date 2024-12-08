from flask import Flask, render_template, request
import sqlite3

def all_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute('SELECT "student_pass", "first_name", "last_name", "email", "gender" FROM students')
    students = cursor.fetchall()
    return students


def delete_student(student_pass):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE student_pass = ?", (student_pass,))
    connection.commit()

def new_student(firstname, lastname, email, gender):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, gender) VALUES (?, ?, ?, ?)", (firstname, lastname, email, gender))
    connection.commit()

def update_student(student_pass, firstname, lastname, email, gender):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET first_name=?, last_name=?, email=?, gender=? WHERE student_pass=?", (firstname, lastname, email, gender, student_pass))
    connection.commit()