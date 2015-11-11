# -*- coding: utf-8 -*-
import sys
import json
import datetime



class WriteData:

	def __init__(self):
		pass

	def writeInFile(self, dict_data, name, li_names_stud, li_ids_video):
		fileToWrite = open ("files/"+name,'a')

		for stud in li_names_stud:
			line=str(stud)+","
			counter_last_element=1
			for video in li_ids_video:
				if counter_last_element==len(li_ids_video):
					line=line+str(dict_data[stud][video])
				else:
					line=line+str(dict_data[stud][video])+","
					counter_last_element=counter_last_element+1
			line = line+"\n"
			fileToWrite.write(line)
		fileToWrite.close()

		return

	def writeInFileSampleData(self, dict_data, name, li_ids_video):
		fileToWrite = open ("files/"+name,'a')


		for video in li_ids_video:
			line = str(video)+","+str(dict_data[video])+"\n"
			fileToWrite.write(line)

		fileToWrite.close()

		return

	def writeGradesData(self, dict_data, modules, li_names_stud, attempts):
		for module in modules:
			fileToWrite = open ("files/"+str(module)+"Grades.txt",'a')
			for student in li_names_stud:
				line = str(student)+","
				for attempt in range (1, attempts+1):

					if attempt == attempts:
						line = line + str(dict_data[str(student)][str(module)][attempt])+"\n"
					else:
						line = line + str(dict_data[str(student)][str(module)][attempt]) + ","

				fileToWrite.write(line)
			fileToWrite.close()

		return

	def writeGradesDataMax(self, dict_data, modules, li_names_stud):
		for module in modules:
			fileToWrite = open ("files/"+str(module)+"GradesMaxAttempt.txt",'a')
			for student in li_names_stud:
				line = str(student)+","+str(max(dict_data[str(student)][str(module)].values()))+"\n"
				fileToWrite.write(line)
			fileToWrite.close()

		return

	def writeNameStudents(self, names):
		fileToWrite = open('files/NameStudents.txt', 'a')
		for name in names:
			fileToWrite.write(str(name)+"\n")
		fileToWrite.close()
		return


	def split_data(slef, line):
		div=line.split(",")
		div=div[1].split("\n")
		return str(div[0])

	def split_first_data(self, line):
		div=line.split(",")
		data=div[1].split("\n")
		return str(div[0]),str(data[0]) 


	def join_video_data(self):
		f=open("files/replayed_time_accumulated_videos.txt", "r")
		replayed_accumulated= f.readlines()
		f.close()

		f=open("files/replayed_time_average_videos.txt", "r")
		replayed_average= f.readlines()
		f.close()

		f=open("files/skipped_time_accumulated_videos.txt", "r")
		skipped_accumulated= f.readlines()
		f.close()

		f=open("files/skipped_time_average_videos.txt", "r")
		skipped_average= f.readlines()
		f.close()

		f=open("files/speedUp_average_videos.txt", "r")
		speedUp= f.readlines()
		f.close()

		f=open("files/speedDown_average_videos.txt", "r")
		speedDown= f.readlines()
		f.close()

		f=open("files/times_seek_back_videos.txt", "r")
		seek_back= f.readlines()
		f.close()

		f=open("files/times_seek_for_videos.txt", "r")
		seek_for= f.readlines()
		f.close()

		
		fileData = open("files/AllVariablesVideo.txt", "a")

		fileData.write("Name,SeekForTimes,SeekBackTimes,SkippedTimeAv,SkippedTimeAc,ReplayedTimeAv,ReplayedTimeAc,SpeedUpAv,SpeedDownAv\n")

		for i in range(len(seek_for)):
			name_video, seek_for_data = self.split_first_data(seek_for[i])
			seek_back_data = self.split_data(seek_back[i])
			skipped_average_data = self.split_data(skipped_average[i])
			skipped_accumulated_data = self.split_data(skipped_accumulated[i])
			replayed_average_data = self.split_data(replayed_average[i])
			replayed_accumulated_data = self.split_data(replayed_accumulated[i])
			speedUp_data = self.split_data(speedUp[i])
			speedDown_data = self.split_data(speedDown[i])
			line=name_video+","+seek_for_data+","+seek_back_data+","+skipped_average_data+","+skipped_accumulated_data+","+replayed_average_data+","+replayed_accumulated_data+","+speedUp_data+","+speedDown_data+"\n"
			fileData.write(line)

		fileData.close()
		return

	def join_all_stud_data(self):
		f=open("files/AllVariablesStud.txt", "r")
		studData= f.readlines()
		f.close()

		f=open("files/time_viewed_videos_stud2.txt", "r")
		studTimeVideo = f.readlines()
		f.close

		f=open("files/AllVariablesStudent.txt", "a")

		for i in range(len(studData)):
			line=""
			data_stud=studData[i].split("\n")
			data_time_video=studTimeVideo[i].split("\n")

			line=data_stud[0]+","+data_time_video[0]+"\n"

			f.write(line)

		f.close()

		print len(studData)
		print len(studTimeVideo)





