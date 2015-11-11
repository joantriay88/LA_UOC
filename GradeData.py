import sys    
reload(sys)    
sys.setdefaultencoding('utf-8')
import json
import datetime


class GradeData:

	def __init__(self):
		pass

	def calculate_modules(self, jsonfile):
		modules=[]

		for line in jsonfile:
			if len(line)>0:	
				#remove example "juliacarrion", last and.
				if line['event_type']== "problem_check" and line['event_source']=="server" and line['username']=="juliacarrion":
					typee=line['event']
					context = line['context']
					module = context['module']
					display=module['display_name']

					if display not in modules:
						modules.append(display)

		return modules



	def calculate_grades(self, jsonfile, li_names_stud, attempts):
		
		modules = self.calculate_modules(jsonfile)

		dict_grades_students_modules={}
		for stud in li_names_stud:
			dict_grades_modules={}
			for module in modules:
				dic_grades_attempt_module={}
				for counter in range(1,attempts+1):
					dic_grades_attempt_module[counter] = -1

				dict_grades_modules[str(module)]=dic_grades_attempt_module

			dict_grades_students_modules[str(stud)]=dict_grades_modules


		for line in jsonfile:

			if line['event_type']== "problem_check" and line['event_source']=="server":

				student = line ['username']

				if student not in li_names_stud:
					pass
				else:
					context = line['context']
					module = context['module']
					display=module['display_name']
					typee=line['event']
					grade = typee['grade']
					attempts = typee['attempts']
	
					dict_grades_students_modules[str(student)][str(display)][int(attempts)]= int(grade)

		return dict_grades_students_modules, modules
