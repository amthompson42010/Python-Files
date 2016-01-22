######################################################################
#
#    Alexander M. Thompson
#    CS 150, Project 2
#
#    File to read files with tweets in them and then list the five
#    earliest tweeters and tweets.
#
#####################################################################

import datetime
from scanner import *
import sys
import os

def main():
   table1 = readTable(sys.argv[1])
   table2 = readTable(sys.argv[2])
   print("Reading files...")
   compareFiles(table1, table2)
   print("Merging files...")
   last = mergeFiles(table1, table2, CompareDates)
   print("Writing files...")
   WriteOutput(last)
   print("Files written. Displaying five earliest tweeters and tweets.")
   DisplayEarly(last)   

def readRecord(s):
   name = s.readtoken()
   if(name == ""):
     return ""
   name = name[1:]
   title = s.readstring()
   years = s.readint()
   months = s.readint()
   days = s.readint()
   hour = s.readtoken()
   return [name, title, years, months, days, hour]

def readTable(filename):
   s = Scanner(filename)
   table = []
   record = readRecord(s)
   while(record != ""):
      table.append(record)
      record = readRecord(s)
   s.close()
   return table

def compareFiles(table1, table2):
   if(len(table1) > len(table2)):
     print(sys.argv[1],"contained the most tweets with", len(table1))
   else:
     print(sys.argv[2],"contained the most tweets with", len(table2))

def CompareDates(ary1, ary2):
   first_year = ary1[2]
   second_year = ary2[2]
   first_month = ary1[3]
   second_month = ary2[3]
   first_day = ary1[4]
   second_day = ary2[4]
   first_time = ary1[5]
   first_time = first_time.split(":")
   second_time = ary2[5]
   second_time = second_time.split(":")
   first_hour = int(first_time[0])
   second_hour = int(second_time[0])
   first_minute = int(first_time[1])
   second_minute = int(second_time[1])
   first_second = int(first_time[2])
   second_second = int(second_time[2])
   first_date = datetime.datetime(first_year, first_month, first_day, first_hour, first_minute, first_second)
   second_date = datetime.datetime(second_year, second_month, second_day, second_hour, second_minute, second_second)
   if(first_date > second_date):
     return True
   else:
     return False

def mergeFiles(table1, table2, f):
   last = []
   i = 0
   j = 0
   while(i < len(table1) and j < len(table2)):
      records1 = table1[i]
      records2 = table2[j]
      if(f(records1, records2) == True):
        last += [table1[i]]
        i += 1
      else:
        last += [table2[j]]
        j += 1
   return last + table1[i:] + table2[j:]

def DisplayEarly(table):
   for i in range(0, 5, 1):
      print(table[i][0] + " " + table[i][1])

def WriteOutput(table):
   fp = open("output", 'w')
   for i in range(0, len(table), 1):
      fp.write(str(table[i][0]) + "\t"  + str(table[i][1]) + " " + str(table[i][2]) + " " +str(table[i][3]) + " " +  str(table[i][4]) + "\t" + str(table[i][5]) + " ")
      fp.write("\n")
   fp.close()


main()
