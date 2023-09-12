"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Malak Anwar Elmasry
Delivery Date : 24-8-2023
"""

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark(user_input)
import uuid
import sys


class Course:

    def _init_(self):
        self.course_id = uuid.uuid4()
        self.course_name = input("Enter the course name: ")
        self.course_mark = float(input('Enter your mark'))

    def getCourseName(self):
        return self.course_name

    def getcoursemark(self):
        return course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    student_num = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user_inout)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def _init_(self):
        self.student_id = uuid.uuid4()
        self.student_name = input("Enter student name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")
        self.student_number = int(input("Enter student number: "))
        self.courses_list = []
        self.student_num += 1

    # TODO 5 define a method to enroll new course to student courses list

    # method to get_student_details as dict
    def enroll_new_course(self):
        new_course = Course(course_mark)
        self.courses_list.append(new_course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for c in self.courses_list:
            print(c.getCourseName(), "\t", c.getcoursemark())

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        sum_mark = 0
        for x in self.courses_list:
            sum += x.getcoursemark()
        average = sum_mark / len(self.courses_list)
        return average


# in Global Scope
# TODO 8 declare empty students list
student_list = list()
while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        # student_number = input("Enter Student Number")
        # student_name = input("Enter Student Name")
        # while True:
        #     try:
        #         student_age = int(input("Enter Student Age"))
        #         break
        #     except:
        #         print("Invalid Value")

        # TODO 10 create student object and append it to students list
        new_student = Student()
        student_list.append(new_student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = int(input("Enter Student Number"))
        for item in student_list:
            if student_number == item.student_num:
                student_list.remove(item)
                print(student_list)
                break
            else:
                print("Student Not Exist")
                break
        # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")

        # TODO 12 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
        x = 0
        for item in student_list:
            if student_number == item.student_num:
                print(item.student_id, item.student_num, item.student_name)
                x = 1
                break
        if x == 0:
            print("Not Exists")


    elif selection == 4:
        student_number = input("Enter Student Number")

        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
        sum = 0
        for item in student_list:
            if student_number == item.student_num:
                sum += item
            else:
                print("Student Not Exist")
                break
        average = sum / len(student_list)
        print(average)

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 14 ask user to enter course name and course mark then create coures object then append it to target student courses
        course_name = input('Enter your course name')
        course_mark = input('Enter your mark')
        newcourse = (student_number, course_name, course_mark)
        for x in student_list:
            if x.student_num == student_number:
                x.courses_list.append(newcourse)

    else:
        # TODO 15 call a function to exit the program
        sys.exit()
