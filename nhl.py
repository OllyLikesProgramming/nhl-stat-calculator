import webbrowser
from sportsreference.nhl.boxscore import Boxscores
from sportsreference.nhl.boxscore import Boxscore
from sportsreference.nhl.roster import Player
from sportsreference.nhl.roster import Roster
import requests
from tkinter import *
import tkinter as tk



'''def printstats():
    print (str(playerid1[1][:5]) + str(playerid1[0][:2]) + "01")

    code = Player(playercode)  
    print(input1 + " had " + str(code('2018-19').points) + " points in the 2018-2019 season and " + str(code('Career').points) + " Career points")'''

def change_dropdown(*args):
    print(" tkvar1.get() ")
    
    
def changedropdown(*args):
    print(" tkvar2.get() ")

def delete():
    input2 = str(input1.get())
    playerid1 = input2.lower()
    playerid2 = str(playerid1)
    playerid3 = (playerid2.split(" "))
    playercode =  ((playerid3[1][:5]) + (playerid3[0][:2]) + "01")
    realcode = Player((playerid3[1][:5]) + (playerid3[0][:2]) + "01")
    print (str(input2) + " had " + str(realcode('2018-19').points) + " points in the 2018-2019 season and " + str(realcode('Career').points) + " Career points")
    ofile = open("nhlsite.html", "w")
    ofile.write(str(input2) + " had " + str(realcode('2018-19').points) + " points in the 2018-2019 season and " + str(realcode('Career').points) + " Career points")
    ofile.close()

root = Tk()
root.title("Stats calculator by Oliver He")
root.geometry('1000x375')
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

#Dropdown for stats
tkvar1 = StringVar(root)
choices = ( 'Goals','Assists','Blocks at even strength','Even strength assists','Even strength goals', 'Game winning goals', 'Goals Against','Hits','Penalty minutes','+/-','Points', 'Power play goals', 'Power play assists', 'Shooting percentage', 'Save percentage','Short handed assists', 'Short handed goals,', 'Shutouts', "Shots on goal")
tkvar1.set('Stat')
popupMenuStat = OptionMenu(mainframe, tkvar1, *choices)
Label(mainframe, text="Choose a stat").grid(row = 30, column = 0)
popupMenuStat.grid(row = 32, column =0)
tkvar1.trace('w', change_dropdown)

#Dropdown for seasons

tkvar2 = StringVar(root)
choices = ('2016-17', '2017-18', '2018-19' , 'Career')
tkvar2.set('Season')

popupMenuSeason = OptionMenu(mainframe, tkvar2, *choices)
Label(mainframe, text="Choose a season").grid(row = 30, column = 2)
popupMenuSeason.grid(row = 32, column =2)


tkvar2.trace('w', changedropdown)
#
tk.Label(mainframe, text="Type an NHL player with format, First name Last name.").grid(row = 0, column = 1)

input1 = tk.Entry(mainframe)
input1.grid(row=3, column=1)
tk.Button(mainframe, text= "Generate Data!",command=delete).grid(row=10, column=1, sticky=tk.W, pady=4)

tk.mainloop()
#The ID for the players are the 5 letters of last name plus first 2 letters of first name and 01
#https://sportsreference.readthedocs.io/en/stable/index.html

