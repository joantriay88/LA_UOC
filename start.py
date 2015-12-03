# -*- coding: utf-8 -*-
from VideoData import *
from StudentData import *
from WriteData import *
from GradeData import *
from ReadData import *

import sys
import json
import datetime

videos = VideoData()
students = StudentData()
fileData = WriteData()
grades = GradeData()
readedData = ReadData()


#************UPLOAD JSON FILE****************************#
jsonfile=open("/Users/LearningAnalytics/Dropbox/14-15/DadesIntroductionMoocOfAlgebra/tot_arr.json")
print "LOADING .JSON FILE..."
json_file=json.load(jsonfile)
print ".JSON FILE LOADED"

#************SYSTEM VARIABLES****************************#
li_names_stud=students.calculateNameStudents(json_file)
fileData.writeName("NameStudents.txt", li_names_stud)
print "NAME STUDENTS CALCULATED, TOTAL STUDENTS: "+str(len(li_names_stud))

li_ids_video = videos.calculate_video_ids(json_file)
fileData.writeName("CodeVideos.txt", li_ids_video)
print "IDS VIDEOS CALCULATED, TOTAL VIDEOS: "+str(len(li_ids_video))


#*******************************************SYSTEM****************************************************# 
dict_video_times_plays, dict_video_times_stops, dict_video_times_pauses = videos.calculate_number_plays_stops_pauses(json_file,li_ids_video)
fileData.writeInFileSampleData(dict_video_times_plays, "times_play_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_times_stops, "times_stop_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_times_pauses, "times_pauses_video.txt", li_ids_video)
print "STOP, PAUSE AND PLAY TIME FOR VIDEO CALCULATED "


dict_video_seek_for_time_accumulated, dict_video_seek_back_time_accumulated=videos.calculate_accumulated_time_kind_seeks(json_file, li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_time_accumulated, "replayed_time_accumulated_video.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_time_accumulated, "skipped_time_accumulated_video.txt",li_ids_video)
print "ACCUMULATED TIMES SEEK BACKWARD AND FORWARD CALCULATED"


dict_video_seek_for_time, dict_video_seek_back_time, dict_video_seek_back_num, dict_video_seek_for_num=videos.calculate_average_time_kind_seeks(json_file, li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_time, "replayed_time_average_video.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_time, "skipped_time_average_video.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_num, "times_seek_back_video.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_num, "times_seek_for_video.txt",li_ids_video)
print "AVERAGE TIMES SEEK BACKWARD AND FORWARD CALCULATED"


#REMOVE THIS METHOD
#dict_videos_students_lasts_stops = videos.calculate_duration_play(json_file, li_names_stud, li_ids_video)
#fileData.writeInFile(dict_videos_students_lasts_stops,"time_viewed_videos_stud.txt", li_names_stud,li_ids_video)
#print "LAST STOP PLAY CALCULATED"


dic_times_event_students = videos.calculate_times_event(json_file, "play_video", li_names_stud, li_ids_video)
fileData.writeInFile(dic_times_event_students,"times_play_videos_stud.txt", li_names_stud,li_ids_video)
print "PLAYS VIDEOS CALCULATED"


dic_times_event_students = videos.calculate_times_event(json_file, "stop_video", li_names_stud, li_ids_video)
fileData.writeInFile(dic_times_event_students,"times_stop_videos_stud.txt", li_names_stud,li_ids_video)
print "STOPS VIDEOS CALCULATED"


dic_times_event_students = videos.calculate_times_event(json_file, "pause_video", li_names_stud, li_ids_video)
fileData.writeInFile(dic_times_event_students,"times_pause_videos_stud.txt", li_names_stud,li_ids_video)
print "PAUSES VIDEOS CALCULATED"


dict_videos_students_seek_for, dict_videos_students_seek_back=videos.calculate_number_kind_seeks(json_file, li_names_stud, li_ids_video)
fileData.writeInFile(dict_videos_students_seek_for,"seek_forward_times_stud.txt", li_names_stud,li_ids_video)
fileData.writeInFile(dict_videos_students_seek_back,"seek_backward_times_stud.txt", li_names_stud,li_ids_video)
print "NUMBER AND KIND SEEKS CALCULATED"


dict_video_change_speed_up_average, dict_video_change_speed_down_average=videos.calculate_change_speed(json_file, li_ids_video)
fileData.writeInFileSampleData(dict_video_change_speed_up_average,"speedUp_average_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_change_speed_down_average,"speedDown_average_video.txt", li_ids_video)
print "AVERAGE SPEED UP AND DOWN CALCULATED"


dict_grades_students_modules, modules = grades.calculate_grades(json_file, li_names_stud, 3)
fileData.writeGradesData(dict_grades_students_modules, modules, li_names_stud, 3)
fileData.writeGradesDataMax(dict_grades_students_modules, modules, li_names_stud)
print "GRADES ATTEMPT FOR MODULE AND MAX GRADE FOR MODULE CALCULATED"

dict_total_times_video=videos.calculate_duration_videos(json_file)
fileData.writeInFileSampleData(dict_total_times_video, "duration_yt_video.txt", li_ids_video)
print "ALL TIMES FOR EVERY VIDEO CALCULATED WITH YOUTUBE API V3"


dict_video_time_viwed_student=videos.calculate_time_video_watched_student(json_file, li_names_stud, li_ids_video)
fileData.writeInFile(dict_video_time_viwed_student,"time_viewed_video_stud.txt", li_names_stud,li_ids_video)
print "TIME WATCHED FOR EVERY VIDEO AND STUDENT CALCULATED"

dict_quotas_video=videos.calculate_quota_video_viwed(li_names_stud, li_ids_video, dict_total_times_video, dict_video_time_viwed_student)
fileData.writeInFile(dict_quotas_video,"quotas_viewed_video_stud.txt", li_names_stud,li_ids_video)
print "QUOTA TIME VIEWED VIDEO CALCULATED"


dict_video_list_accumulated_time, dict_video_list_average_time=videos.calculate_accumulated_and_average_time_viewed_video(li_names_stud, li_ids_video, dict_video_time_viwed_student)
fileData.writeInFileSampleData(dict_video_list_accumulated_time, "accumulated_viewed_time_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_list_average_time, "average_viewed_time_video.txt", li_ids_video)
print "ACCUMULATED AND AVERAGE TIME VIEWED VIDEO CALCULATED "

dict_video_list_events_students=videos.calculate_list_video_events_without_redundant_data(json_file, li_names_stud, li_ids_video)
dict_pauses, dict_stops, dict_plays, dict_seek_back, dict_seek_for, dict_speed_up, dict_speed_down = videos.calculate_times_every_video_events_without_redundant_data(li_names_stud, li_ids_video, dict_video_list_events_students)
fileData.writeInFileSampleData(dict_pauses, "nr_times_pauses_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_stops, "nr_times_stops_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_plays, "nr_times_plays_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_seek_back, "nr_times_seek_back_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_seek_for, "nr_times_seek_for_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_speed_up, "nr_times_speed_up_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_speed_down, "nr_times_speed_down_video.txt", li_ids_video)
print "NO REDUNDANT DATA CALCULATED"


#******************************************TESTING TRACKING LOGS**********************************#
readedData.read_modify_pre_jsons(li_names_stud)
print "JSON FOR EACH STUDENT GENERATED (DATA TEST)"
videos.calculate_number_video_events(li_names_stud)
print "NUMBER EVENTS CALCULATED (TEST)"


#*****************************************JOINING FILES******************************************#

fileData.join_video_data()
print "VIDEO DATA JOINED"
fileData.join_video_data_no_redundant()
print "VIDEO DATA NO REDUNDANT JOINED"
fileData.join_all_stud_data()
print "STUDENT DATA JOINED"

