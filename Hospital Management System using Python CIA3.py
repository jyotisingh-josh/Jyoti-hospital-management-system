Hospital Management System using Python
Student Details

Course: Programming with Python
Project Title: Hospital Management System
Student Name: Jyoti Singh
Institution: Christ University
Year: 2026

Abstract

The Hospital Management System is a simple Python-based project developed to manage hospital operations such as patient records, doctor information, appointments, and payments.

The system uses basic Python concepts including functions, loops, conditional statements, and file handling. All records are stored in text files, making the system easy to implement and understand.

This project demonstrates how programming can be used to automate small hospital management tasks.

1. Introduction

Hospitals manage a large amount of information daily, including patient details, doctor information, appointments, and billing records. Managing these records manually can be time-consuming and may lead to errors.

A Hospital Management System helps in organizing and storing hospital data efficiently. It allows administrators to easily manage patient records, doctor information, and appointment schedules.

This project implements a simple Hospital Management System using Python. The system uses file handling to store data and provides a menu-driven interface for easy interaction.

2. Problem Statement

Many small hospitals and clinics still maintain records manually, which leads to problems such as:

Difficulty in managing patient information

Loss or misplacement of records

Time-consuming appointment management

Lack of proper payment tracking

Therefore, there is a need for a simple digital system that can store and manage hospital records efficiently.

3. Objectives of the Project

The main objectives of this project are:

To develop a hospital management system using Python

To store patient and doctor information using file handling

To manage appointments between doctors and patients

To track patient payment records

To demonstrate basic Python programming concepts

4. System Modules

The Hospital Management System consists of the following modules.

Patient Management

Add patient

Display patients

Update patient details

Delete patient record

Doctor Management

Add doctor

Display doctor information

Appointment Management

Book appointment

Display appointments

Payment Management

Record patient payments

5. Python Concepts Used

This project uses the following Python topics:

Variables

Input and Output

Functions

Conditional Statements

Loops

File Handling

String Operations

Random Module

Menu Driven Programming

6. File Structure

The system stores data using text files.

patients.txt
doctors.txt
appointments.txt
payments.txt

Example patient record:

P101,John,9876543210,Fever
7. Program Implementation
Add Patient
def add_patient():
    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    phone = input("Enter Phone Number: ")
    disease = input("Enter Disease: ")

    file = open("patients.txt","a")
    file.write(f"{patient_id},{patient_name},{phone},{disease}\n")
    file.close()

    print("Patient Added Successfully")

Explanation:
This function collects patient details and stores them in patients.txt using append mode.

Display Patients
def display_patients():
    print("PATIENT LIST")

    file = open("patients.txt","r")
    print(file.read())
    file.close()

Explanation:
This function reads and displays all patient records from the file.

Add Doctor
def add_doctor():
    doc_id = input("Enter Doctor ID: ")
    doc_name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")

    file = open("doctors.txt","a")
    file.write(f"{doc_id},{doc_name},{specialization}\n")
    file.close()

    print("Doctor Added Successfully")

Explanation:
This function stores doctor information in doctors.txt.

Book Appointment
import random

def book_appointment():
    appointment_id = random.randint(100,999)

    patient_id = input("Enter Patient ID: ")
    doctor_id = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date: ")

    file = open("appointments.txt","a")
    file.write(f"{appointment_id},{patient_id},{doctor_id},{date}\n")
    file.close()

Explanation:
This function generates a random appointment ID and stores appointment details in appointments.txt.

8. Advantages

Simple and easy to use

Reduces manual record keeping

Demonstrates Python programming concepts

Stores data in structured format

9. Limitations

Uses text files instead of a database

No graphical interface

Suitable for small-scale systems only

10. Future Enhancements

The system can be improved by adding:

A database such as MySQL

A graphical interface using Tkinter

Login authentication

Data analysis and reporting features

11. Conclusion

The Hospital Management System demonstrates how Python can be used to build a simple application for managing hospital data.

The project successfully implements patient management, doctor management, appointment booking, and payment tracking using basic Python programming techniques.