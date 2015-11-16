# -*- coding: utf-8 -*-
import sys
import json
import datetime
import copy
import pafy
import urllib
import isodate


class VideoData:

	def __init__(self):
		pass


	def calculate_video_ids(self, json_file):
		li_ids_video=[]
		for line in json_file:
			if line['event_type']== "stop_video" or line['event_type']=="play_video" or line['event_type']== "pause_video":
				event= line['event']
				elements_events=json.loads(event)
				code_video=elements_events['id']
				if code_video not in li_ids_video:
					li_ids_video.append(code_video)

		return li_ids_video

	def calculate_times_event(self, json_file, eventname, li_names_stud, li_ids_video):
		dict_videos_times={}
		dict_videos_students_times={}
		
		for video in li_ids_video:
			dict_videos_times[str(video)]=0

		for student in li_names_stud:
			dict_videos_students_times[str(student)]=dict_videos_times.copy()
		
		
		for line in json_file:
			if line["event_type"]==eventname:
				stud = str(line["username"])

				if stud not in li_names_stud:
					pass
				else:
					event= line['event']
					elements_events=json.loads(event)						
					code_video=str(elements_events['id'])
					dict_videos_students_times[stud][str(code_video)]=dict_videos_students_times[stud][code_video]+1
		
		
		return dict_videos_students_times


	def calculate_duration_play(self, json_file, li_names_stud, li_ids_video):
		dict_video_last_stop={}
		dict_videos_students_lasts_stops={}
		
		for video in li_ids_video:
			dict_video_last_stop[str(video)]=0

		for student in li_names_stud:
			dict_videos_students_lasts_stops[str(student)]=dict_video_last_stop.copy()
		
		
		for line in json_file:
			if line["event_type"]=="stop_video":
				
				stud = str(line["username"])

				if stud not in li_names_stud:
					pass
				else:

					event= line['event']
					elements_events=json.loads(event)						
					code_video=str(elements_events['id'])
					time = str(elements_events['currentTime'])
				
					if float(dict_videos_students_lasts_stops[stud][str(code_video)]) < float(time):
						dict_videos_students_lasts_stops[stud][str(code_video)] = time	

		return dict_videos_students_lasts_stops


	def calculate_number_kind_seeks (self, json_file, li_names_stud, li_ids_video):
		dict_video_seek_num={}
		dict_videos_students_seek_for={}
		dict_videos_students_seek_back={}
		
		for video in li_ids_video:
			dict_video_seek_num[str(video)]=0

		for student in li_names_stud:
			dict_videos_students_seek_for[str(student)]=dict_video_seek_num.copy()
		
		for student in li_names_stud:
			dict_videos_students_seek_back[str(student)]=dict_video_seek_num.copy()
		
		for line in json_file:
			if line["event_type"]=="seek_video":				
				stud = str(line["username"])

				if stud not in li_names_stud:
					pass
				else:

					event= line['event']
					elements_events=json.loads(event)						
					code_video=str(elements_events['id'])
					old_time = str(elements_events['old_time'])
					new_time = str(elements_events['new_time'])
				

					if old_time!="None" and new_time!="None":
				
					
						if float(old_time) > float(new_time):
							dict_videos_students_seek_back[stud][str(code_video)]=dict_videos_students_seek_back[stud][str(code_video)]+1

						if float(old_time) < float(new_time):
							dict_videos_students_seek_for[stud][str(code_video)]=dict_videos_students_seek_for[stud][str(code_video)]+1
		
		return dict_videos_students_seek_for, dict_videos_students_seek_back

	def calculate_average_time_kind_seeks (self, json_file, li_ids_video):
		dict_video_seek_for_num={}
		dict_video_seek_for_time={}
		dict_video_seek_back_num={}
		dict_video_seek_back_time={}	

		for video in li_ids_video:
			dict_video_seek_for_num[str(video)]=0
			dict_video_seek_for_time[str(video)]=float(0)
			dict_video_seek_back_time[str(video)]=float(0)
			dict_video_seek_back_num[str(video)]=0

		
		for line in json_file:
			if line["event_type"]=="seek_video":	

				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				old_time = str(elements_events['old_time'])
				new_time = str(elements_events['new_time'])
				

				if old_time!="None" and new_time!="None":
	
					if float(old_time) > float(new_time):
						time_replayed = float(old_time)-float(new_time)
						dict_video_seek_back_time[str(code_video)]=dict_video_seek_back_time[str(code_video)] + time_replayed
						dict_video_seek_back_num[str(code_video)]=dict_video_seek_back_num[str(code_video)] + 1


					if float(old_time) < float(new_time):
						time_skipped = float(new_time)-float(old_time)
						dict_video_seek_for_time[str(code_video)]=dict_video_seek_for_time[str(code_video)] + time_skipped
						dict_video_seek_for_num[str(code_video)]=dict_video_seek_for_num[str(code_video)] + 1	


		for video in li_ids_video:
			if dict_video_seek_for_time[str(video)] != float(0):
				dict_video_seek_for_time[str(video)]=dict_video_seek_for_time[str(video)]/dict_video_seek_for_num[str(video)]
			if dict_video_seek_back_time[str(video)] != float(0):
				dict_video_seek_back_time[str(video)]=dict_video_seek_back_time[str(video)]/dict_video_seek_back_num[str(video)]


		return dict_video_seek_for_time, dict_video_seek_back_time, dict_video_seek_back_num, dict_video_seek_for_num


	def calculate_accumulated_time_kind_seeks (self, json_file, li_ids_video):
		dict_video_seek_for_time={}
		dict_video_seek_back_time={}	

		for video in li_ids_video:
			dict_video_seek_for_time[str(video)]=float(0)
			dict_video_seek_back_time[str(video)]=float(0)

		
		for line in json_file:
			if line["event_type"]=="seek_video":	

				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				old_time = str(elements_events['old_time'])
				new_time = str(elements_events['new_time'])
				

				if old_time!="None" and new_time!="None":
	
					if float(old_time) > float(new_time):
						time_replayed = float(old_time)-float(new_time)
						dict_video_seek_back_time[str(code_video)]=dict_video_seek_back_time[str(code_video)] + time_replayed


					if float(old_time) < float(new_time):
						time_skipped = float(new_time)-float(old_time)
						dict_video_seek_for_time[str(code_video)]=dict_video_seek_for_time[str(code_video)] + time_skipped


		return dict_video_seek_for_time, dict_video_seek_back_time


	def calculate_change_speed (self, json_file, li_ids_video):
		dict_video_change_speed_up_average={}
		dict_video_change_speed_up_times={}

		dict_video_change_speed_down_average={}
		dict_video_change_speed_down_times={}

		for video in li_ids_video:
			dict_video_change_speed_up_average[str(video)]=0
			dict_video_change_speed_down_average[str(video)]=0

			dict_video_change_speed_up_times[str(video)]=0
			dict_video_change_speed_down_times[str(video)]=0

		for line in json_file:
			if line["event_type"]=="speed_change_video":				
				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				old_speed = str(elements_events['old_speed'])
				new_speed = str(elements_events['new_speed'])

				if float(old_speed)<float(new_speed):
					dict_video_change_speed_up_average[str(code_video)]= dict_video_change_speed_up_average[str(code_video)] + float(new_speed)
					dict_video_change_speed_up_times[str(code_video)]= dict_video_change_speed_up_times[str(code_video)]+1


				if float(old_speed)>float(new_speed):
					dict_video_change_speed_down_average[str(code_video)]= dict_video_change_speed_down_average[str(code_video)] + float(new_speed)
					dict_video_change_speed_down_times[str(code_video)]=dict_video_change_speed_down_times[str(code_video)]+1


		for video in li_ids_video:
			if dict_video_change_speed_up_times[str(video)] != 0:
				dict_video_change_speed_up_average[str(video)]=	float(dict_video_change_speed_up_average[str(video)])/dict_video_change_speed_up_times[str(video)]
			
			if dict_video_change_speed_down_times[str(video)] != 0:
				dict_video_change_speed_down_average[str(video)]= float(dict_video_change_speed_down_average[str(video)])/dict_video_change_speed_down_times[str(video)]


		return dict_video_change_speed_up_average, dict_video_change_speed_down_average

	def calculate_number_plays_stops_pauses(self, json_file, li_ids_video):
		dict_video_times_plays={}
		dict_video_times_stops={}
		dict_video_times_pauses={}

		for video in li_ids_video:
			dict_video_times_plays[str(video)]=0
			dict_video_times_stops[str(video)]=0
			dict_video_times_pauses[str(video)]=0

		for line in json_file:
			if line['event_type']=="play_video":
				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				dict_video_times_plays[code_video]=dict_video_times_plays[code_video]+1

			if line['event_type']=="stop_video":
				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				dict_video_times_stops[code_video]=dict_video_times_stops[code_video]+1

			if line['event_type']=="pause_video":
				event= line['event']
				elements_events=json.loads(event)						
				code_video=str(elements_events['id'])
				dict_video_times_pauses[code_video]=dict_video_times_pauses[code_video]+1

		return dict_video_times_plays, dict_video_times_stops, dict_video_times_pauses

	def calculate_duration_videos(self,json_file):
		li_ids_video=[]
		for line in json_file:
			if line['event_type']== "stop_video" or line['event_type']=="play_video" or line['event_type']== "pause_video":
				event= line['event']
				elements_events=json.loads(event)
				code_video=elements_events['code']
				code_video_ucatx=elements_events['id']
				if code_video not in li_ids_video:
					li_ids_video.append(code_video)
		
		
		for video in li_ids_video:
			video_id=str(video)
			if video_id!="Dd1iE-NtBho":
				api_key="AIzaSyB1I6cpK4UTwWmkqqiidXncss9Fvmb_CiQ"
				searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails"
				response = urllib.urlopen(searchUrl).read()
				data = json.loads(response)
				all_data=data['items']
				contentDetails=all_data[0]['contentDetails']
				dur=isodate.parse_duration(contentDetails['duration'])
				print video_id+" "+str(dur.total_seconds())
		return
	
	def calculate_time_video_watched_student(self, json_file, li_names_stud, li_ids_video):
		dict_video_list={}
		dict_video_list_students={}
		
		for video in li_ids_video:
			dict_video_list[str(video)]=0

		for student in li_names_stud:
			dict_video_list_students[str(student)]=dict_video_list.copy()

		for student in li_names_stud:
			for video in li_ids_video:
				dict_video_list_students[str(student)][str(video)]=[]

		for line in json_file:

			if line['event_type']=="pause_video":
				student = str(line["username"])
				if student in li_names_stud:
					event= line['event']
					elements_events=json.loads(event)
					code_video=str(elements_events['id'])
					time = str(elements_events['currentTime'])
					li_play=["pause",time]
					dict_video_list_students[student][code_video].append(li_play)

			if line['event_type']=="stop_video":
				student = str(line["username"])
				if student in li_names_stud:
					event= line['event']
					elements_events=json.loads(event)
					code_video=str(elements_events['id'])
					time = str(elements_events['currentTime'])
					li_play=["stop",time]
					dict_video_list_students[student][code_video].append(li_play)

			if line['event_type']=="play_video":
				student = str(line["username"])
				if student in li_names_stud:
					event= line['event']
					elements_events=json.loads(event)
					code_video=str(elements_events['id'])
					time = str(elements_events['currentTime'])
					li_play=["play",time]
					dict_video_list_students[student][code_video].append(li_play)
	

		print dict_video_list_students["juliacarrion"]["i4x-UPF-C01-video-24c2323fb5ec4945a5b1d5cbd837a23b"]
		print len(dict_video_list_students["juliacarrion"]["i4x-UPF-C01-video-24c2323fb5ec4945a5b1d5cbd837a23b"])
		return

	

    #TEST METHOD REMOVE AT FINAL
	def calculate_number_video_events(self,li_names_stud):
		fileNew=open("counted_events.txt", "a")

		for name in li_names_stud:	
			play=0
			stop=0
			pause=0

			jsonfile=open("files/unitStudentsVideoEvents/"+str(name)+".json")
			json_file=json.load(jsonfile)

			for line in json_file:
				if line['event_type']=="pause_video":
					pause=pause+1
				
				if line['event_type']=="play_video":
					play=play+1

				if line['event_type']=="stop_video":
					stop=stop+1

			fileNew.write(str(name)+"; Plays:"+str(play)+" Stops:"+str(stop)+" Pauses:"+str(pause)+" Stops+Pauses:"+str(stop+pause)+"\n")

		fileNew.close()

		return	


