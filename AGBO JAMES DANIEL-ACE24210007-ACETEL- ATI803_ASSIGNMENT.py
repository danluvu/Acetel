# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 21:27:32 2025

@author: Agbo James Daniel, ACE24210007, MSc Artificial Intelligence
"""

import csv #To import CSV library

class Assessment: #Student Assesment Class (Assignments and Exam)
    def __init__(self, assignments, exam):
        self.assignments = assignments
        self.exam = exam

    def total_assignments_score(self):   #Assignments computation function
        return sum(self.assignments) / len(self.assignments)  #Average Assignment

class Student:                  #Student information
    def __init__(self, student_id, name, assessment):
        self.student_id = student_id
        self.name = name
        self.assessment = assessment

    def total_final_score(self): #Total Assesment score
        assign_score = self.assessment.total_assignments_score() #average assignment score 
        return round((assign_score * 0.4) + (self.assessment.exam * 0.6), 2) #student final score

def load_students(filename): #To load file
    student_list = [] #create student list
    with open(filename, 'r') as f: #to open & read the file
        reader = csv.DictReader(f) #An object to maps each row value to a column name (key)
        for row in reader:
            assignments = [float(row['Assignment1']), float(row['Assignment2']), float(row['Assignment3'])]
            exam = float(row['Exam'])
            assess = Assessment(assignments, exam)
            student = Student(row['StudentID'], row['Name'], assess)
            student_list.append(student)
    return student_list

def save_final_scores(students, filename): #Funtion to save the computation
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Final Score'])
        for s in students:
            final = s.total_final_score()
            print(f"{s.name}: {final}")
            writer.writerow([s.name, final])

students = load_students('students.csv')
save_final_scores(students, 'final_scores.csv')


