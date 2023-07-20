import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as ny
import pathlib
import xlrd
import pandas as pd
import csv

#I am going to try graphing data from the excel spreadsheet
# from the Hanna from the field work on 6/13/23

#necessary conditions for code to work:
#1) not tampering with downloaded workbook+NOT messing with the
#the order of the worksheets
#2) all parameters that the Hanna can work with must be kept
# will continue finding way to program so that it can always put 
# the necessary data in corresponding lists without specific ordering

#things to work on:
#adjusting code to work with castaway and manta data
#special cases where there is no title for the code; there should just be no entry

#directions for running this code:
#first navigate to the folder with this code stored through the cmd
#then type python [name_of_file.py]
#                       ^^^ of course replace this with the actual name of the file
#you will be prompted to input the name of the file; just paste it in (you can tap with two fingers to do so)

#add r in front of string to make it raw
#make sure file is in same folder as this program
#make sure file is in same folder as this program
file = input("Enter the name of a file to graph. Make sure it ends with an appropriate suffix (e.g. .csv, .xls, or .xlsx): ")

print("Loading graph for: " + file)
#file = r"HANNA_6-13-23_16.32.xls"
#file = MANTA_06-12-2023_17.04.csv
#file = r"CASTAWAY_06-13-2023_15.04.csv"

new_file = r'' #preemptive variable in case original variable won't work

#to convert old file into new .csv file that shows in same folder as this program
#parameters: old file, new file that shows in same directory as this program
def excel_to_csv(oldfile, newfile):
    if "HANNA" in file.upper():
        sheet = pd.read_excel(oldfile, sheet_name=1)
    sheet.to_csv(newfile, encoding = 'utf-8')

if pathlib.Path(file).suffix != '.csv':
    if pathlib.Path(file).suffix == '.xls':
        new_file = file[:-3] + 'csv'
        excel_to_csv(file, new_file)
        file = new_file
    else:
        print("Still need to program for not .xls haha")

mega_list = [] #for putting all the rows in one list; could help with processing data
x = []
y = []

titles_dict = {}
data_dict = {}

titles_list = []
data_list = []

glitchx = []
glitchy = []

#row with data starts at 30 (29 index)

with open(file, 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        mega_list.append(row)


print(mega_list[30])
print(mega_list)
print(len(mega_list))

#sifting through file to find title data in castaway file
if "CASTAWAY" in file.upper():
    new_list = []
    title_found = False
    for i in range (0, len(mega_list)):
        if title_found == True:
            new_list.append(mega_list[i])
        else:
            if isinstance(mega_list[i][0], str):
                if "PRESSURE (DECIBAR)" in mega_list[i][0].upper():
                    title_found = True
                    new_list.append(mega_list[i]) #should contain titles
    mega_list = new_list
print('      \n\n')
print(mega_list)
# #sifting through file to find title data in Manta file
# if "MANTA" in file.upper():
#     new_list = []
#     title_found = False
#     for i in range (0, len(mega_list)):
#         if title_found == True and 'Eureka_Manta_2' not in mega_list[i][0]:
#             if "DATE" not in mega_list[i][0]:
#                 new_list.append(mega_list[i])
#         else:
#             if isinstance(mega_list[i][0], str):
#                 if "DATE" in mega_list[i][0].upper() and 'Eureka_Manta_2' not in mega_list[i+1][0]:
#                     title_found = True
#                     new_list.append(mega_list[i]) #should contain titles
#     mega_list = new_list

#this var is used to set index in which independent variables are held; this axis should be kept on x-axis
# independent_index = 0

# #determining which column contains independent variables; used to reference other ones
# if "CASTAWAY" in file.upper():
#     independent_index = 1
# elif "HANNA" in file.upper():
#     independent_index = 2
# elif "MANTA" in file.upper():
#     independent_index = 1

# for j in range(0, len(mega_list[0])):
#     titles_dict[j] = mega_list[0][j]
#     titles_list.append(mega_list[0][j])
#     for k in range (1, len(mega_list)): #starting at one since title is in first row, which we don't want graphed
#         x.append(mega_list[k][independent_index])
#         y.append(mega_list[k][j])
#     data_dict[j] = [x, y]
#     data_list.append([x, y])
#     x = []
#     y = []

for l in range (1, len(mega_list)):
    x.append(float(mega_list[l][0]))
    y.append(float(mega_list[l][2]))

print(x)
print(y)

plt.plot(x, y)
plt.show()

# #print(titles_dict)

# #stackoverflow: https://stackoverflow.com/questions/33139496/how-to-plot-several-graphs-and-make-use-of-the-navigation-button-in-matplotlib
# toggle = [0, len(data_dict)]
# counter = 1

# def onclick(event):
#     global toggle
#     global counter

#     event.canvas.figure.clear()

#     plt.plot(data_dict[counter][0], data_dict[counter][1], marker=".", markersize=10)
#     plt.title(titles_dict[counter] + " - Plot " + str(counter+1) + " of " + str(len(titles_dict)))
#     plt.ylabel(titles_dict[counter])
#     plt.xlabel(titles_dict[independent_index])
#     plt.yticks (fontsize = 6)
#     plt.xticks(fontsize = 6, rotation = 60)
#     plt.grid()

#     counter += 1

#     if counter >= len(titles_dict):
#         counter = 0

#     event.canvas.draw()

# fig = plt.figure()
# fig.canvas.mpl_connect('button_press_event', onclick)

# plt.plot(data_dict[0][0], data_dict[0][1])
# plt.title(titles_dict[0] + " - Plot 1 of " + str(len(titles_dict)) + " (Click on this window to see other graphs)")
# plt.ylabel(titles_dict[0])
# plt.xlabel(titles_dict[independent_index])
# plt.yticks (fontsize = 6)
# plt.xticks(fontsize = 6, rotation = 60)
# plt.grid()
# plt.legend("yeetus")
# plt.show()