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
jsonfile=open("/Users/LearningAnalytics/Dropbox/tot_arr.json")
print "LOADING .JSON FILE..."
json_file=json.load(jsonfile)
print ".JSON FILE LOADED"

'''
#************SYSTEM VARIABLES****************************#
li_names_stud=students.calculateNameStudents(json_file)
fileData.writeName("NameStudents.txt", li_names_stud)
print "NAME STUDENTS CALCULATED"

li_ids_video = videos.calculate_video_ids(json_file)
fileData.writeName("CodeVideos.txt", li_ids_video)
print "IDS VIDEOS CALCULATED"
'''
videos.calculate_duration_videos(json_file)

'''

#*******************************************SYSTEM****************************************************# 
dict_video_times_plays, dict_video_times_stops, dict_video_times_pauses = videos.calculate_number_plays_stops_pauses(json_file,li_ids_video)
fileData.writeInFileSampleData(dict_video_times_plays, "times_play_for_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_times_stops, "times_stop_for_video.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_times_pauses, "times_pauses_for_video.txt", li_ids_video)
print "STOP, PAUSE AND PLAY TIME FOR VIDEO CALCULATED "


dict_video_seek_for_time_accumulated, dict_video_seek_back_time_accumulated=videos.calculate_accumulated_time_kind_seeks(json_file, li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_time_accumulated, "replayed_time_accumulated_videos.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_time_accumulated, "skipped_time_accumulated_videos.txt",li_ids_video)
print "ACCUMULATED TIMES SEEK BACKWARD AND FORWARD CALCULATED"


dict_video_seek_for_time, dict_video_seek_back_time, dict_video_seek_back_num, dict_video_seek_for_num=videos.calculate_average_time_kind_seeks(json_file, li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_time, "replayed_time_average_videos.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_time, "skipped_time_average_videos.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_back_num, "times_seek_back_videos.txt",li_ids_video)
fileData.writeInFileSampleData(dict_video_seek_for_num, "times_seek_for_videos.txt",li_ids_video)
print "AVERAGE TIMES SEEK BACKWARD AND FORWARD CALCULATED"


dict_videos_students_lasts_stops = videos.calculate_duration_play(json_file, li_names_stud, li_ids_video)
fileData.writeInFile(dict_videos_students_lasts_stops,"time_viewed_videos_stud.txt", li_names_stud,li_ids_video)
print "LAST STOP PLAY CALCULATED"


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
fileData.writeInFileSampleData(dict_video_change_speed_up_average,"speedUp_average_videos.txt", li_ids_video)
fileData.writeInFileSampleData(dict_video_change_speed_down_average,"speedDown_average_videos.txt", li_ids_video)
print "AVERAGE SPEED UP AND DOWN CALCULATED"


dict_grades_students_modules, modules = grades.calculate_grades(json_file, li_names_stud, 3)
fileData.writeGradesData(dict_grades_students_modules, modules, li_names_stud, 3)
fileData.writeGradesDataMax(dict_grades_students_modules, modules, li_names_stud)
print "GRADES ATTEMPT FOR MODULE AND MAX GRADE FOR MODULE CALCULATED"


'''

'''
#******************************************TESTING TRACKING LOGS**********************************#
readedData.read_modify_pre_jsons(li_names_stud)
print "JSON FOR EACH STUDENT GENERATED (DATA TEST)"
videos.calculate_number_video_events(li_names_stud)
print "NUMBER EVENTS CALCULATED (TEST)"
'''



#fileData.join_video_data()
#fileData.join_all_stud_data()

