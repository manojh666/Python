class Student:
    def __init__(self, name, usn, m1,m2,m3,avg):
        self.name = name
        self.usn = usn
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.avg = avg


    def __str__(self):
        return f"Name: {self.name}, USN: {self.usn}, Mark1: {self.m1},Mark2: {self.m2},Mark3: {self.m3}"
class Student_delt:
    def __init__(self):
        self.stds = []

    def addstd(self,name, usn, m1,m2,m3,avg):
        self.stds.append(Student(name, usn, m1,m2,m3,avg))
    def print_min_max(self):
        min_avg = min(self.stds, key=lambda x: x.avg)
        max_avg = max(self.stds, key=lambda x: x.avg)
        print("Student with min avg: ", min_avg.name, "with avg: ", min_avg.avg)
        print("Student with max avg: ", max_avg.name, "with avg: ", max_avg.avg)
    def ranklist(self):
        self.stds.sort(key = lambda x:x.avg, reverse=True)
        for i, student in enumerate(self.stds, start=1):
            print("Rank: ", i, "Student: ", student.name, "with avg: ", student.avg)

st_dict = {}
stdlt=[]
num = int(input("Enter the number of student"))
student_details = Student_delt()
for i in range(num):
    name = input(f"Enter name for student {i+1}: ")
    usn = int(input(f"Enter usn for student {i+1}: "))
    m1 = int(input(f"Enter marks of student subject 1: "))
    m2 = int(input(f"Enter marks of student subject 2: "))
    m3 = int(input(f"Enter marks of student subject 3: "))
    avg = (m1+m2+m3) /3

    student = Student(name, usn, m1,m2,m3,avg)
    st_dict[usn] = student
    student_details.addstd(name, usn, m1,m2,m3,avg)


print("\nStudents are :")

for key, student in st_dict.items():
    print(f"{key}: {student}")
student_details.print_min_max()
student_details.ranklist()
