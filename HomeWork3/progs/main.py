from packages.H10_3 import *
students = Students(input("Enter student's data filename: "))
students.load_data()
students.sort_data()
students.print_data()