print("Starting OOP practice")

print()


class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old, "
            f"and I major in {self.major}.\n"
        )

    def __str__(self):
        return f"Student(name:{self.name}, age:{self.age}, major:{self.major})\n"


student1 = Student("Christian", 21, "Information Technology")
student2 = Student("Maya", 22, "Psychology")
student3 = Student("Jordan", 19, "Biology")


print(student1)
print(student2)
print(student3)


student1.introduce()
student2.introduce()
student3.introduce()


print("Updated version with GPA")


class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def introduce(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old, "
            f"and I major in {self.major}. My GPA is {self.gpa}.\n"
        )

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def __str__(self):
        return (
            f"Student(name:{self.name}, age:{self.age}, "
            f"major:{self.major}, gpa:{self.gpa})\n"
        )


student1 = Student("Christian", 21, "Information Technology", 3.6)
student2 = Student("Maya", 22, "Psychology", 3.8)
student3 = Student("Jordan", 19, "Biology", 3.4)


print(student1)
print(student2)
print(student3)


student1.introduce()
student2.introduce()
student3.introduce()


student1.update_gpa(3.7)
print(student1)
