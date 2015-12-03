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

	def writeName(self, name_file, names):
		fileToWrite = open('files/'+name_file, 'a')
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
		f=open("files/replayed_time_accumulated_video.txt", "r")
		replayed_accumulated= f.readlines()
		f.close()

		f=open("files/replayed_time_average_video.txt", "r")
		replayed_average= f.readlines()
		f.close()

		f=open("files/skipped_time_accumulated_video.txt", "r")
		skipped_accumulated= f.readlines()
		f.close()

		f=open("files/skipped_time_average_video.txt", "r")
		skipped_average= f.readlines()
		f.close()

		f=open("files/speedUp_average_video.txt", "r")
		speedUp= f.readlines()
		f.close()

		f=open("files/speedDown_average_video.txt", "r")
		speedDown= f.readlines()
		f.close()

		f=open("files/times_seek_back_video.txt", "r")
		seek_back= f.readlines()
		f.close()

		f=open("files/times_seek_for_video.txt", "r")
		seek_for= f.readlines()
		f.close()

		f=open("files/times_play_video.txt", "r")
		play_times= f.readlines()
		f.close()

		f=open("files/times_stop_video.txt", "r")
		stop_times= f.readlines()
		f.close()

		f=open("files/times_pauses_video.txt", "r")
		pause_times= f.readlines()
		f.close()
		

		f=open("files/accumulated_viewed_time_video.txt", "r")
		accumulated_time= f.readlines()
		f.close()

		f=open("files/average_viewed_time_video.txt", "r")
		average_time= f.readlines()
		f.close()

		f=open("files/duration_yt_video.txt", "r")
		duration= f.readlines()
		f.close()

		

		fileData = open("files/AllVariablesVideo.txt", "a")

		fileData.write("Name,Duration,SeekForTimes,SeekBackTimes,SkippedTimeAv,SkippedTimeAc,ReplayedTimeAv,ReplayedTimeAc,SpeedUpAv,SpeedDownAv,Plays,Stops,Pauses,AccumulatedTime,AverageTime\n")

		for i in range(len(seek_for)):
			name_video, seek_for_data = self.split_first_data(seek_for[i])
			duration_data=self.split_data(duration[i])
			seek_back_data = self.split_data(seek_back[i])
			skipped_average_data = self.split_data(skipped_average[i])
			skipped_accumulated_data = self.split_data(skipped_accumulated[i])
			replayed_average_data = self.split_data(replayed_average[i])
			replayed_accumulated_data = self.split_data(replayed_accumulated[i])
			speedUp_data = self.split_data(speedUp[i])
			speedDown_data = self.split_data(speedDown[i])
			play_data = self.split_data(play_times[i])
			stop_data = self.split_data(stop_times[i])
			pause_data = self.split_data(pause_times[i])
			accumulated_time_data = self.split_data(accumulated_time[i])
			average_time_data = self.split_data(average_time[i])

			line=name_video+","+duration_data+","+seek_for_data+","+seek_back_data+","+skipped_average_data+","+skipped_accumulated_data+","+replayed_average_data+","+replayed_accumulated_data+","+speedUp_data+","+speedDown_data+","+play_data+","+stop_data+","+pause_data+","+accumulated_time_data+","+average_time_data+"\n"
			fileData.write(line)

		fileData.close()
		return

	def join_video_data_no_redundant(self):
		f=open("files/replayed_time_accumulated_video.txt", "r")
		replayed_accumulated= f.readlines()
		f.close()

		f=open("files/replayed_time_average_video.txt", "r")
		replayed_average= f.readlines()
		f.close()

		f=open("files/skipped_time_accumulated_video.txt", "r")
		skipped_accumulated= f.readlines()
		f.close()

		f=open("files/skipped_time_average_video.txt", "r")
		skipped_average= f.readlines()
		f.close()

		f=open("files/speedUp_average_video.txt", "r")
		speedUp= f.readlines()
		f.close()

		f=open("files/speedDown_average_video.txt", "r")
		speedDown= f.readlines()
		f.close()

		f=open("files/nr_times_seek_back_video.txt", "r")
		seek_back= f.readlines()
		f.close()

		f=open("files/nr_times_seek_for_video.txt", "r")
		seek_for= f.readlines()
		f.close()

		f=open("files/nr_times_plays_video.txt", "r")
		play_times= f.readlines()
		f.close()

		f=open("files/nr_times_stops_video.txt", "r")
		stop_times= f.readlines()
		f.close()

		f=open("files/nr_times_pauses_video.txt", "r")
		pause_times= f.readlines()
		f.close()

		f=open("files/nr_times_speed_up_video.txt", "r")
		speed_up_times= f.readlines()
		f.close()

		f=open("files/nr_times_speed_down_video.txt", "r")
		speed_down_times= f.readlines()
		f.close()
		
		f=open("files/accumulated_viewed_time_video.txt", "r")
		accumulated_time= f.readlines()
		f.close()

		f=open("files/average_viewed_time_video.txt", "r")
		average_time= f.readlines()
		f.close()

		f=open("files/duration_yt_video.txt", "r")
		duration= f.readlines()
		f.close()

		

		fileData = open("files/AllNoRedVariablesVideo.txt", "a")

		fileData.write("Name,Duration,SkippedTimeAv,SkippedTimeAc,ReplayedTimeAv,ReplayedTimeAc,SpeedUpAv,SpeedDownAv,Plays,Stops,Pauses,SeekForTimes,SeekBackTimes,SpeedDownTimes,SpeedUpTimes,AccumulatedTime,AverageTime\n")

		for i in range(len(seek_for)):
			name_video, seek_for_data = self.split_first_data(seek_for[i])
			duration_data=self.split_data(duration[i])
			seek_back_data = self.split_data(seek_back[i])
			skipped_average_data = self.split_data(skipped_average[i])
			skipped_accumulated_data = self.split_data(skipped_accumulated[i])
			replayed_average_data = self.split_data(replayed_average[i])
			replayed_accumulated_data = self.split_data(replayed_accumulated[i])
			speedUp_data = self.split_data(speedUp[i])
			speedDown_data = self.split_data(speedDown[i])
			play_data = self.split_data(play_times[i])
			stop_data = self.split_data(stop_times[i])
			pause_data = self.split_data(pause_times[i])
			accumulated_time_data = self.split_data(accumulated_time[i])
			average_time_data = self.split_data(average_time[i])
			speedup_times_data= self.split_data(speed_up_times[i])
			speeddown_times_data=self.split_data(speed_down_times[i])

			line=name_video+","+duration_data+","+skipped_average_data+","+skipped_accumulated_data+","+replayed_average_data+","+replayed_accumulated_data+","+speedUp_data+","+speedDown_data+","+play_data+","+stop_data+","+pause_data+","+seek_for_data+","+seek_back_data+","+speeddown_times_data+","+speedup_times_data+","+accumulated_time_data+","+average_time_data+"\n"
			fileData.write(line)

		fileData.close()
		return

	def join_all_stud_data(self):
		f=open("files/all_variables_out.txt", "r")
		studData= f.readlines()
		f.close()
		print len(studData)

		f=open("files/times_stop_videos_stud.txt", "r")
		stopsData = f.readlines()
		f.close
		print len(stopsData)

		f=open("files/times_play_videos_stud.txt", "r")
		playsData = f.readlines()
		f.close
		print len(playsData)

		f=open("files/times_pause_videos_stud.txt", "r")
		pausesData = f.readlines()
		f.close
		print len(pausesData)

		f=open("files/time_viewed_video_stud.txt", "r")
		timeData = f.readlines()
		f.close
		print len(timeData)

		f=open("files/seek_backward_times_stud.txt", "r")
		seekBackData = f.readlines()
		f.close
		print len(seekBackData)

		f=open("files/seek_forward_times_stud.txt", "r")
		seekFordwardsData = f.readlines()
		f.close
		print len(seekFordwardsData)

		f=open("files/quotas_viewed_video_stud.txt", "r")
		quotasData = f.readlines()
		f.close
		print len(quotasData)

		f=open("files/AllVariablesStudent.txt", "a")

		
		for i in range(len(studData)):
			line=""
			data_stud=studData[i].split("\n")
			data_stops=stopsData[i].split("\n")
			data_plays=playsData[i].split("\n")
			data_pauses=pausesData[i].split("\n")
			data_seekBackward=seekBackData[i].split("\n")
			data_seekFordward=seekFordwardsData[i].split("\n")
			data_time_viewed=timeData[i].split("\n")
			data_time_quotas=quotasData[i].split("\n")



			line=data_stud[0]+","+data_stops[0]+","+data_plays[0]+","+data_pauses[0]+","+data_seekBackward[0]+","+data_seekFordward[0]+","+data_time_viewed[0]+","+data_time_quotas[0]+"\n"

			f.write(line)

		f.close()

				
		return


