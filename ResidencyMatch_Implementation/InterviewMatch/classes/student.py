import random
import string

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