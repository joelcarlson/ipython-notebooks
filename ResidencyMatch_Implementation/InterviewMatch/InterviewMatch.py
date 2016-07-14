import pprint
import random
import string


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

class Student(object):
	"""
	Student
	-------

	params
	------
	student_name: string
	  The name of the student, if not given becomes a random string

	ranks: list
	  list of company names in rank order (leftmost = favored)
	"""

	def __init__(self, student_name=None, ranks=[]):

		if student_name is None:
			# Create a random name
		    self.student_name = ''.join([random.choice(string.ascii_letters) for n in xrange(8)])
		else:
			self.student_name = student_name

		# Convert ranks to dict with rank value and jitter
		self.ranks = ranks
		self.rank_dict = {company:{"student_name":self.student_name,
							   "student_rank":rank ,
		                       "student_jitter_rank":rank + random.gauss(0,0.1)}
		              for rank, company in enumerate(ranks)}

	def get_student_info(self, company_name):
		"""
		details
		-------
		return a dictionary including the student_name,
		and the rank and jittered rank of the company given
		"""
		if self.rank_dict.get(company_name) is not None:
			return self.rank_dict.get(company_name)

	def __str__(self):
		return "Name: {} \nRanks: {}".format(self.student_name, self.ranks)


class Company(object):
	"""
	Company 

	params
	------
	company_name: string
	  Name of the company

	available_slots: int
	  The number of slots the company has available

	details
	-------
	Company class which holds information on each
	student assigned to the slots within the company

	"""

	def __init__(self, company_name=None, available_slots=2):
		if company_name is None:
			# Create a random name
		    self.company_name = ''.join([random.choice(string.ascii_letters) for n in xrange(8)])
		else:
			self.company_name = company_name

		# Create list of available slots
		self.available_slots = range(available_slots)
		# Define the slots dictionary
		# Access via slots[slot_number][s]	
		self.slots = {n:{"student_name":None,
						 "student_rank":None,
						 "student_jitter_rank":float("inf")} for n in xrange(available_slots)}


	def _student_already_in(self, student):
		"""
		-- Internal -- 
		Check is a given student is
		already present in a slot

		params
		------
		student: Student
		"""
		students_in = [self.slots[n]["student_name"] for n in self.slots]
		if student.student_name in students_in:
			return True
		return False

	def try_adding_student(self, student):
		"""
		details
		-------
		given a Student object, add them to the company's slot list
		if they have ranked it higher than other students in the list
		"""
		if isinstance(student, Student):
			student_info = student.get_student_info(self.company_name)
			if student_info is not None:
				# What has to happen here: 
				# If there are available slots, just add the student anywhere
				# if there are none, enter the loop
				# if a student is being bumped you need to check the ranks of other
				# students...
				if len(self.available_slots) > 0:
					pass
					#del self.available_slots[slot]
				for slot in self.slots:
					if (student_info["student_jitter_rank"] < self.slots[slot]["student_jitter_rank"])\
					and not self._student_already_in(student):
						self.slots[slot] = student_info
						break

	def __str__(self):
		name_str = self.company_name
		slot_str = ''.join(["Slot {}: {} ({})\n".\
			format(n,
			 self.slots[n]['student_name'],
			 self.slots[n]['student_rank']) for n in self.slots]) 
		return name_str + "\n" + slot_str

class InterviewMatch(object):

	def __init__(self, students, companies):
		self.students = students
		self.companies = companies
		self.fit_complete = False

	def fit(self):
		"""
		Loop through each student and attempt to place
		them in each company. 

		TODO: Better stopping criterion
		"""

		for student in self.students:
			for company in self.companies:
				print company
				company.try_adding_student(student)
		self.fit_complete = True

	def __str__(self):
		if self.fit_complete:
			pass







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
	for company in companies:
		print company



	for student in students:
		print student


