# -*- coding: utf-8 -*-
import sys
import json
import datetime
import os



class ReadData:

	def __init__(self):
		pass

	def read_modify_pre_jsons(self, li_names_stud):
		
		for name in li_names_stud:
			print name
			fileModify=open("files/unitStudentsVideoEvents/"+str(name)+".json")
			lines = fileModify.readlines()
			fileModify.close()

			if len(lines)>0:
				os.remove("files/unitStudentsVideoEvents/"+str(name)+".json")
				fileNew=open("files/unitStudentsVideoEvents/"+str(name)+".json", "a")
				fileNew.write("[\n")
				i=1
				for line in lines:
					if i==len(lines):
						fileNew.write(line[0:len(line)-2])
						fileNew.write("]")
						

					else:			
						i=i+1
						fileNew.write(line)

				fileNew.close()

			else:
				os.remove("files/unitStudentsVideoEvents/"+str(name)+".json")
				fileNew=open("files/unitStudentsVideoEvents/"+str(name)+".json", "a")
				fileNew.write("[]")
				fileNew.close()
				pass


		
		return

		