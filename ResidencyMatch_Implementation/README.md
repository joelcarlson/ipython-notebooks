
## One Sided Implementation of the Residency Match Algorithm

Contained in this repo is an implementation of the residency match algorithm with a simple modification: only the "residents" (students) match the "hospitals" (companies).

This was inspired by a simple problem encountered at the Galvanize bootcamp:

The students wish to interview with a number of companies, and each student has different preferences for the companies they wish to speak with. Thus, each student will rank each company in order of preference. 

The companies do not have access to the students they will interview, which is a departure from the residency match algorithm (in which hospitals and residents both rank each other).

## Code

The code for the algorithm is broken up into 3 separate classes: `Student`, `Company` and `InterviewMatch`.

#### Student Class / [link](https://github.com/joelcarlson/ipython-notebooks/tree/master/ResidencyMatch_Implementation/InterviewMatch/classes/student.py)

The Student class is implemented in `/InterviewMatch/classes/student.py`. It is initialized with a student name, and a list of company names (strings) in rank order. The class stores a dictionary which contains, for each company the student ranked, the students rank for the company, and a jittered value for the rank. The jittering is done as a tie breaker mechanism - in this way if two students have chosen the same rank for a given company, the one with the luckier jitter result wins.

#### Company Class /[link](https://github.com/joelcarlson/ipython-notebooks/tree/master/ResidencyMatch_Implementation/InterviewMatch/classes/company.py)

The Company class is implemented in `/InterviewMatch/classes/company.py`. This class holds the interview slots for each company. Interview slots are modeled as an `OrderedDict()`, and students are placed in slots based on their (jittered) ranks. If a company has empty slots then a student is placed in automatically without regard to their ranking. When a student with a lower (preferred) ranking is attempting to be slotted in, the student who has given the lowest ranking is removed.

#### InterviewMatch Class / [link](https://github.com/joelcarlson/ipython-notebooks/tree/master/ResidencyMatch_Implementation/InterviewMatch/InterviewMatch.py)

The InterviewMatch class is implemented in `/InterviewMatch/InterviewMatch.py`. Initialized with a list of students and a list of companies, it simply places the students in the companies.

## Usage

Usage for the algorithm is simple. First, import the necessary classes (and `random`, so we can randomly create preference lists for the students):

```python
from InterviewMatch import InterviewMatch, Student, Company
import random
```

We then create a sample list of companies, and a list of randomly chosen names. Each of the students randomly chooses the order of the 6 companies, and is convered into an object of class `Student`, and added to a list:


```python
random.seed(1)
company_list = ["Google", "Apple", "Microsoft", "Facebook", "Twitter", "Amazon"]
student_list = ["Joel", "Rhia", "Andy","Dave", "Ryan", "Triston", "Lorin"]
```


```python
students = []
for student in student_list:
    comps = random.sample(company_list, 6)
    students.append(Student(student, ranks=comps))
```

Each `Company` allows 3 possible interview slots:


```python
companies = []
for company in company_list:
    companies.append(Company(company, available_slots=3))
```

Our data is now ready to be put into the algorithm. If we print the `InterviewMatch` object before running a fit, we get to see the preferences of each student:


```python
# Initialize and run matching algorithm
matcher = InterviewMatch(students, companies)
print matcher
```

    Student Preferences
    ============
    Name:  Joel 
    Ranks: ['Google', 'Twitter', 'Facebook', 'Amazon', 'Microsoft', 'Apple']
    
    Name:  Rhia 
    Ranks: ['Twitter', 'Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook']
    
    Name:  Andy 
    Ranks: ['Apple', 'Microsoft', 'Google', 'Facebook', 'Twitter', 'Amazon']
    
    Name:  Dave 
    Ranks: ['Amazon', 'Microsoft', 'Twitter', 'Google', 'Apple', 'Facebook']
    
    Name:  Ryan 
    Ranks: ['Twitter', 'Facebook', 'Apple', 'Amazon', 'Microsoft', 'Google']
    
    Name:  Triston 
    Ranks: ['Apple', 'Microsoft', 'Twitter', 'Facebook', 'Google', 'Amazon']
    
    Name:  Lorin 
    Ranks: ['Google', 'Facebook', 'Twitter', 'Apple', 'Amazon', 'Microsoft']
    
    


The algorithm is run with a simple call to the `fit()` method:


```python
matcher.fit()

# Check results
print matcher
```

    Results
    ============
    Google
    Slot 0: Lorin (0)
    Slot 1: Joel (0)
    Slot 2: Rhia (1)
    
    Apple
    Slot 0: Triston (0)
    Slot 1: Ryan (2)
    Slot 2: Andy (0)
    
    Microsoft
    Slot 0: Triston (1)
    Slot 1: Dave (1)
    Slot 2: Andy (1)
    
    Facebook
    Slot 0: Ryan (1)
    Slot 1: Lorin (1)
    Slot 2: Joel (2)
    
    Twitter
    Slot 0: Ryan (0)
    Slot 1: Rhia (0)
    Slot 2: Joel (1)
    
    Amazon
    Slot 0: Dave (0)
    Slot 1: Joel (3)
    Slot 2: Ryan (3)
    
    


Examining the results we see that there are no situations in which someone who has ranked a company lower than someone else has secured an interview - that is, we have the optimal grouping of students and companies!






