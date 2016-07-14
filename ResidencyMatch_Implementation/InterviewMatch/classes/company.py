import random
import string
from collections import OrderedDict
from student import Student

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
		# Ordered so that we can use it as a stack later
		self.slots = OrderedDict({n:{"student_name":None,
						 "student_rank":None,
						 "student_jitter_rank":float("inf")} for n in xrange(available_slots)})


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
					first_available_slot = self.available_slots[0]
					self.slots[first_available_slot] = student_info
					del self.available_slots[0]

				else:
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
			 self.slots[n]['student_rank']) for n in self.slots if self.slots[n]["student_name"] is not None]) 
		return name_str + "\n" + slot_str + "\n"