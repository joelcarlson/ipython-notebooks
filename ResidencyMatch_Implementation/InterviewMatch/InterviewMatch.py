import pprint
import random
import string
from classes.company import Company
from classes.student import Student


class InterviewMatch(object):

	"""
	One sided residency match algorithm

	Description
	-----------
	The goal of this algorithm is to match each user to 
	the companies they wish to interview with while 
	considering the preferences of other users.
	This algorithm guarantees that, for a given company, 
	if you failed to secure an interview, no one who 
	secured an interview ranked it lower than you did.

	Usage
	------

	Create a list of students of class Student, and a 
	list of companies of class Company. Initialize the
	matching algorithm with the two lists, and run the 
	fit method.

	"""
	def __init__(self, students, companies):
		self.students = students
		self.companies = companies
		self.fit_complete = False

	def fit(self):
		"""
		Loop through each student and attempt to place
		them in each company. 

		"""

		for student in self.students:
			for company in self.companies:
				print company
				company.try_adding_student(student)
		self.fit_complete = True

	def __str__(self):
		if self.fit_complete:
			company_str = ''.join(["{}".format(company) for company in companies])
			return "Results" + "\n============\n" + company_str



if __name__ == "__main__":
	random.seed(1)
	company_list = ["Oakley", "Reddit", "Burton", "Google", "Apple", "Microsoft"]
	student_list = ["Joel", "Andy", "Ryan", "Triston"]

	# Create list of Student objects
	students = []
	for student in student_list:
		random.shuffle(company_list)
		students.append(Student(student, ranks=company_list))


	# Create list of Company objects
	companies = []
	for company in company_list:
		companies.append(Company(company, available_slots=5))
	companies.append

	# Initialize and run matching algorithm
	matcher = InterviewMatch(students, companies)
	matcher.fit()

	# Check results
	print matcher


