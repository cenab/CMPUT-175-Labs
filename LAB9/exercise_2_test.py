import unittest
from exercise_2 import *
import random

class TestEx2(unittest.TestCase):

	def test_print_student(self):
		student = Student("ID_1", "Name_1", 100)
		self.assertEqual(str(student)," - ID_1, Name_1, 100")

	def test_is_greater_than(self):
		student_1 = Student("ID_1", "Name_1", 80)
		student_2 = Student("ID_2", "Name_2", 90)
		self.assertEqual(student_1.is_greater_than(student_2),False)
		self.assertEqual(student_2.is_greater_than(student_1),True)

	def test_sort_students_in_and_out_of_order(self):
		student_1 = Student("ID_1", "Name_1", 60)
		student_2 = Student("ID_2", "Name_2", 80)
		student_3 = Student("ID_3", "Name_3", 50)

		students_input_list=[(student_1),(student_2),(student_3)]
		output = [ str(student) for student in Student.sort_students(students_input_list)]

		students_sorted_list = [str(student_3),str(student_1),str(student_2)]
		self.assertEqual(output, students_sorted_list)

	def test_sort_students_repeated_marks(self):
		# TODO
		return

	# Optional
	def test_sort_students_random_marks(self):
		return


if  __name__== "__main__":
    unittest.main()
