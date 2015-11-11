import sys
import json
import datetime

class StudentData:
	def __init__(slef):
		pass

	def calculateNameStudents(self, jsonfile):
		li_names=[]
		for line in jsonfile:
			if len(line)>0:
				if line['username'] not in li_names:
 					li_names.append(line['username']);

 		li_names.remove("staff")
		li_names.remove("")
		li_names.remove("admin")
		li_names.remove("Laia")
		li_names.remove("LaiaA")
		li_names.remove("MiquelOliver")
		li_names.remove("tesa")
		li_names.remove("vdaza")

		return li_names
