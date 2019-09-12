class student:
   
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None

    def validate_marks(self):
        if self.__marks>=0 and self.__marks <=100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False

    def get__student_id(self):
        return self.__student_id
    def set__student_id(self,s_id):
        self.__student_id=s_id

    def get__marks(self):
        return self.__marks
    def set__marks(self,m):
        self.__marks=m

    def get__age(self):
        return self.__age
    def set__age(self,a):
        self.__age=a

n=int(input("Enter the no. of students : "))
s_list=list()
for i in range(n):
    s_list.append(student())


    sid=int(input("Enter the Student Id : "))
    s_list[i].set__student_id(sid)
    age=int(input("Enter the Age : "))
    s_list[i].set__age(age)
    marks=int(input("Enter the marks : "))
    s_list[i].set__marks(marks)
    if(s_list[i].check_qualification()):
        print("Admission granted !\nStudent Details")
        print("Student Id : ",s_list[i].get__student_id(),"\nAge : ",s_list[i].get__age(),"\nMarks : ",s_list[i].get__marks())
    else:
        print("Admision Denied !")
            
