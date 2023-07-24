# Your program should
#
# Create a generic 'job' class.
class Job:
    # class attributes
    name = None
    salary = None
    hours_worked = None

    #     initialise the class
    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_job(self):
        print(f"Job Title: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hours_worked}")


# The init method will store the details for name, salary and hours worked. 'job' will have another method that
# prints those details nicely. Create two sub-classes from job: 'doctor' and 'teacher' The 'doctor' subclass should
# also include 'speciality' and 'years of experience'. The 'teacher' subclass should also include 'subject' and
# 'position'. The print functions for each sub-class should print this extra data. Instantiate a lawyer, a computer
# science teacher, and a pediatric doctor (this is a doctor for children) with 7 years of experience. Output the
# information for each job.
class Doctor(Job):
    #     class attributes
    speciality = None
    experience = None

    # initialise the class
    def __init__(self, speciality, experience, name, salary, hours_worked):
        super().__init__(name, salary, hours_worked)
        self.speciality = speciality
        self.experience = experience

    def print_doctor(self):
        print(
            f"Job Title: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hours_worked}\nSpeciality: {self.speciality}\nExperience: {self.experience}")


class Teacher(Job):
    # class attributes
    subject = None
    position = None

    # initialise the class
    def __init__(self, subject, position, name, salary, hours_worked):
        super().__init__(name, salary, hours_worked)
        self.subject = subject
        self.position = position

    def print_teacher(self):
        print(
            f"Job Title: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hours_worked}\nSubject: {self.subject}\nPosition: {self.position}")


lawyer = Job("Lawyer", "50,000", "60")
print(lawyer.print_job())
doctor = Doctor("Pediatrics", "7 years", "Doctor", "70,000", "80")
print(doctor.print_doctor())
teacher = Teacher("Computer Science", "Teacher", "Teacher", "40,000", "All of them")
print(teacher.print_teacher())
