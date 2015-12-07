# -*- coding: utf-8 -*-
import sys
import json
import datetime
import copy
import pafy
import urllib
import isodate

class HeatMap:

  def __init__(self):
    pass

  def calculate_matrix(self, dict_total_duration_video, json_file,  correlation_ids_video_ucatx_ytube, li_names_stud, li_ids_video):

    dict_video_list_seek={}
    
    for video in li_ids_video:
      dict_video_list_seek[str(video)]=[]


    for line in json_file:
      if line['event_type']=="seek_video":
        student = str(line["username"])
        if student in li_names_stud:
          event= line['event']
          elements_events=json.loads(event)           
          code_video=str(elements_events['id'])
          old_time = str(elements_events['old_time'])
          new_time = str(elements_events['new_time'])
          if old_time != "None" and new_time != "None":
            if old_time > new_time: 
              li_seek=["seek",old_time, new_time]
              dict_video_list_seek[code_video].append(li_seek)

    for video in li_ids_video:
      print "PROCESSING HEATMAP "+video
      youtube_id = correlation_ids_video_ucatx_ytube[video]
      seek_list=dict_video_list_seek[video]
      duration = dict_total_duration_video[video]
      duration=int(duration)
      resolution=5
      intervals=(duration/resolution)+1
      print intervals
      print duration

      li_from_to=[]
      i=0
      while i < intervals:
        li_to=[]
        j=0
        while j<intervals:
            li_to.append(0)
            j+=1
        li_from_to.append(li_to)
        i+=1
    
      for event in seek_list:
          if event[0]=="seek":
            row_float=float(event[1])
            col_float=float(event[2])
            
            if row_float > col_float:
              row=int(row_float)/resolution
              col=int(col_float)/resolution
              
              if int(row_float)>duration:
                row=duration/resolution
              if int(col_float)>duration:
                col=duration/resolution
              li_from_to[row][col]=li_from_to[row][col]+1
      
      file_data = open("heatmap/data_heatmap_"+str(youtube_id)+".tsv", "a")
      file_data.write("row_idx\tcol_idx\trepetitions\n")

      i=0
      while i < intervals:
        j=0
        while j<intervals:
          file_data.write(str(i+1)+"\t"+str(j+1)+"\t"+str(li_from_to[i][j])+"\n")
          j+=1
        
        i+=1
      
      file_data.close()
      
      self.create_html(str(youtube_id), intervals)


  def create_html(self, youtube_id, intervals):

      base_html=open("./base.html")
      base_data_html=base_html.readlines()
      base_html.close()

      html_file=open("heatmap/heatmap_"+youtube_id+".html","a")

      html_file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//ENhttp://www.w3.org/TR/html4/strict.dtd">\n')
      html_file.write("<html>\n")
      html_file.write("<meta charset='utf-8'>\n")
      html_file.write("<style>\n")
      html_file.write("svg *::selection {\n")
      html_file.write("background : transparent;\n")
      html_file.write("}\n")
           
      html_file.write("svg *::-moz-selection {\n")
      html_file.write("background:transparent;\n")
      html_file.write("} \n")
           
      html_file.write("svg *::-webkit-selection {\n")
      html_file.write("background:transparent;\n")
      html_file.write("}\n")
      html_file.write("rect.selection {\n")
      html_file.write("stroke          : #333;\n")
      html_file.write("stroke-dasharray: 4px;\n")
      html_file.write("stroke-opacity  : 0.5;\n")
      html_file.write("fill            : transparent;\n")
      html_file.write("}\n")

      html_file.write("rect.cell-border {\n")
      html_file.write("stroke: #eee;\n")
      html_file.write("stroke-width:0.3px;\n")
      html_file.write("      }\n")

      html_file.write("      rect.cell-selected {\n")
      html_file.write("        stroke: rgb(51,102,153);\n")
      html_file.write("        stroke-width:0.5px;\n")
      html_file.write("      }\n")

      html_file.write("      rect.cell-hover {\n")
      html_file.write("        stroke: #F00;\n")
      html_file.write("        stroke-width:0.3px;\n")
      html_file.write("      }\n")

      html_file.write("      text.mono {\n")
      html_file.write("        font-size: 9pt;\n")
      html_file.write("        font-family: Consolas, courier;\n")
      html_file.write("       fill: #aaa;\n")
      html_file.write("      }\n")

      html_file.write("      text.text-selected {\n")
      html_file.write("        fill: #000;\n")
      html_file.write("      }\n")

      html_file.write("      text.text-highlight {\n")
      html_file.write("        fill: #c00;\n")
      html_file.write("      }\n")
      html_file.write("      text.text-hover {\n")
      html_file.write("        fill: #00C;\n")
      html_file.write("      }\n")
      html_file.write("     #video {\n")
      html_file.write("      position: relative;\n")
      html_file.write("      left: 63em;\n")
      html_file.write("      top: -42em;\n")
      html_file.write("      }\n")

      html_file.write("      #tooltip {\n")
      html_file.write("        position: absolute;\n")
      html_file.write("        width: 200px;\n")
      html_file.write("        height: auto;\n")
      html_file.write("        padding: 10px;\n")
      html_file.write("        background-color: white;\n")
      html_file.write("        -webkit-border-radius: 10px;\n")
      html_file.write("        -moz-border-radius: 10px;\n")
      html_file.write("        border-radius: 10px;\n")
      html_file.write("        -webkit-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);\n")
      html_file.write("        -moz-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);\n")
      html_file.write("        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);\n")
      html_file.write("        pointer-events: none;\n")
      html_file.write("      }\n")

      html_file.write("      #tooltip.hidden {\n")
      html_file.write("        display: none;\n")
      html_file.write("     }\n")

      html_file.write("      #tooltip p {\n")
      html_file.write("        margin: 0;\n")
      html_file.write("       font-family: sans-serif;\n")
      html_file.write("        font-size: 12px;\n")
      html_file.write("        line-height: 20px;\n")
      html_file.write("      }\n")
      html_file.write("    </style>\n")

      title="Heat map "+youtube_id

      html_file.write("<title>"+title+"</title>\n")
      html_file.write("</head>\n")

      html_file.write("<body>\n")
      html_file.write("<div id='tooltip' class='hidden'>\n")
      html_file.write("        <p><span id='value'></p>\n")
      html_file.write("</div>\n")
      html_file.write("<script src='http://d3js.org/d3.v3.min.js'></script>\n")
      html_file.write("  </select>\n")
      html_file.write("<div id='chart' style='overflow:auto; width:960px; height:700px;'></div>\n")

      html_file.write("<script type='text/javascript'>\n")
      html_file.write("var margin = { top: 75, right: 10, bottom: 50, left: 100 },\n")
      html_file.write("  cellSize=12;\n")

      html_file.write("  col_number="+str(intervals)+";\n")
      html_file.write("  row_number="+str(intervals)+";\n")
      html_file.write("  width = cellSize*col_number, // - margin.left - margin.right,\n")
      html_file.write("  height = cellSize*row_number , // - margin.top - margin.bottom,\n")
      html_file.write("  gridSize = Math.floor(width / 24),\n")
      html_file.write("  legendElementWidth = cellSize*2.5,\n")
      html_file.write("  colorBuckets = 11,\n")

      i=1
      rows_cols="["
      while i<=intervals:
        if i !=intervals:
          rows_cols=rows_cols+str(i)+","
        else:
          rows_cols=rows_cols+str(i)+"]"
        i+=1 

      html_file.write("  colors = ['#FFFFFF','#F1EEF6','#E6D3E1','#DBB9CD','#D19EB9','#C684A4','#BB6990','#B14F7C','#A63467','#9B1A53','#91003F'];\n")
      html_file.write("  hcrow = "+rows_cols+", // change to gene name or probe id\n")
      html_file.write("  hccol = "+rows_cols+", // change to gene name or probe id\n")

      i=1
      x=0
      y=4
      frome =""
      toe=""
      while i<=intervals:
        if i !=intervals:
          frome=frome+"'From "+str(x)+"-"+str(y)+"', "
          toe=toe+"'To "+str(x)+"-"+str(y)+"', "
          x+=5
          y+=5
        else:
          frome=frome+"'From "+str(x)+"-"+str(y)+"'"
          toe=toe+"'To "+str(x)+"-"+str(y)+"'"
          x+=5
          y+=5
        i+=1 

      html_file.write("  rowLabel = ["+frome+"], // change to gene name or probe id\n")
      html_file.write("  colLabel = ["+toe+"]; // change to contrast name\n")
      html_file.write('d3.tsv("data_heatmap_'+youtube_id+'.tsv",\n')
      html_file.writelines(base_data_html)
      
      html_file.write('<div id=video>\n')
      html_file.write('<embed width="420" height="315"src="http://www.youtube.com/v/'+youtube_id+'">\n')
      html_file.write('</div>\n')
      html_file.write('</body>\n')
      html_file.write('</html>')
      
      html_file.close()
      
      return
