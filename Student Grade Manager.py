class Student : 
    count  = 0 
    stu_avg = []
    def __init__ ( self , name , grades ) : 
        self.name = name 
        self.grades = grades
        Student.count +=1
        Student.stu_avg = Student.stu_avg + self.grades
    @classmethod
    def class_average(cls) :
        try : 
            summation =  0
            avg = 0 
            for i in cls.stu_avg : 
                summation += i
            return f' The overall Avg is : {summation/len(cls.stu_avg)}'
        except  ZeroDivisionError  : 
            print("wrong input")
            
    @classmethod
    def students_tracker (cls) : 
        return f" number of students -> {cls.count}"
    
    def __str__(self)  :
        return f"{self.name} has the following grades - > {self.grades}"
    
    def add_grade(self , grade) : 
        self.grades.append(grade)
        
    def avarage(self) :
        avg = 0
        summation = 0
        for i in self.grades : 
            summation = summation + i
        return f"The Avarage is : {summation / len(self.grades)}"
        
    def describe(self) : 
        return f"{self.name} and {self.avarage().lower()} Gpa"
              
students = []
print("     0- Add a student\n 1-Display the number of students \n 2-Display the Avgarge of a specific student \n 3-Display the Overall Avarage \n 4-Describe a Student \n 5-Exit ")
stop = False
while not stop : 
     try:
         choice = int(input("enter your choice : "))
         if choice == 0 : 
             grades =  []
             name = input("Enter the student's name : ")
             i = 0 
             while i  < 3 : 
                 try : 
                     grade = int(input("Enter the student's grades (max 3) : "))
                     i += 1 
                     grades.append(grade)
                 except ValueError : 
                     print("enter a number please")
             student  = Student (name , grades)
             students.append(student)
         elif choice == 1 :
             print(Student.students_tracker())

         elif choice == 2  :
             student_name = input("Enter the studnet's name : ")
             found  = False
             x = 0
             for i in students : 
                     if student_name == i.name : 
                         found = True
                         break
                     x+=1
             if found == True :
                  print(i.avarage())
             else: 
                 print("the student is not found")

         elif choice == 3 : 
             print(Student.class_average())
         elif choice == 4:
             student_name = input("Enter the studnet's name : ")
             found  = False
             for i in students : 
                     if student_name == i.name : 
                         found = True
                         break 
             if found == True :
                  print(i.describe())
             else: 
                 print("the student is not found")
         elif choice == 5 : 
             print('Thanks for beign here!! ')
             break
     except ValueError : 
         print("wrong input my friend ! , Only integers allowed ")