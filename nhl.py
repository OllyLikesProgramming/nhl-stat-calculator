import webbrowser
from sportsreference.nhl.roster import Player
import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from sportsreference.nhl.teams import Teams



#Called once the first dropdown is changed
def change_dropdown(*args):
    statcode0 = (tkvar1.get())
    print ("Stat dropdown has been changed to " + statcode0)
    #Called once the second dropdown is changed
def changedropdown(*args):
    seasoncode0 = (tkvar2.get())
    print ("Season dropdown has been changed to " + seasoncode0)
    
#The function that runs once the "Generate Button" Is pressed
def delete():
    input2 = str(input1.get())
    if input2 == "":
        messagebox.showinfo("Error", "You did not choose a player \n Please type a player")
    playerid1 = input2.lower()
    playerid2 = str(playerid1)
    playerid3 = (playerid2.split(" "))
    playercode =  ((playerid3[1][:5]) + (playerid3[0][:2]) + "01")
    realcode = Player((playerid3[1][:5]) + (playerid3[0][:2]) + "01")
    
    statcode0 = (tkvar1.get())
    statcode1 = statcode0.replace(" ", "_")
    statcode = statcode1.lower()
    
    seasoncode0 = (tkvar2.get())
    
    
    if statcode == "stat":
        messagebox.showinfo("Error", "The stat dropdown is empty.  \n Please select a stat")
    if seasoncode0 == "Season":
        messagebox.showinfo("Error", "Error code: The season dropdown is empty. \n Please select a season")
        


    
    if seasoncode0 == "2015-16":
        realstatcode = getattr(realcode('2015-16'), statcode)
        ofile = open("nhlsite.html", "w")
        ofile.write (str(input2) + " had " + str(realstatcode) + " " + str(statcode0) + " in the 2015-2016 season")
        ofile.close()
        
    elif seasoncode0 == "2016-17":
        realstatcode = getattr(realcode('2016-17'), statcode)
        ofile = open("nhlsite.html", "w")
        ofile.write (str(input2) + " had " + str(realstatcode) + " " + str(statcode0) + " in the 2016-2017 season")
        ofile.close()
        
        
    elif seasoncode0 == "2017-18":
        realstatcode = getattr(realcode('2017-18'), statcode)
        ofile = open("nhlsite.html", "w")
        ofile.write (str(input2) + " had " + str(realstatcode) + " " + str(statcode0) + " in the 2017-2018 season")
        ofile.close()
    
    elif seasoncode0 == "2018-19":
        realstatcode = getattr(realcode('2018-2019'), statcode)
        ofile = open("nhlsite.html", "w")
        ofile.write (str(input2) + " had " + str(realstatcode) + " " + str(statcode0) + " in the 2018-2019 season")
        ofile.close()
        
    elif seasoncode0 == "Career":
        realstatcode = getattr(realcode('Career'), statcode)
        ofile = open("nhlsite.html", "w")
        ofile.write (str(input2) + " had " + str(realstatcode) + " " + str(statcode0) + " in his career")
        ofile.close()

   
    playerage = str(realcode.age)
    playerid = str(realcode.player_id)
    playerweight = str(realcode.weight)
    playerheight = str(realcode.height)
    playerteam = str(realcode.team_abbreviation)
    ofile = open("nhlsite.html", "w")
    ofile.write ("""<html>
    
    <head>
    <style>
    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 100%;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {
      background-color: #dddddd;
    }
    </style>
    </head>
    <body>

    <h2>""" +str(input2) + """'s Stats</h2>

    <table>
      <tr>
        <th>Stat</th>
        <th>Info</th>
      </tr>
      <tr>
        <td>"""+ str(seasoncode0) + """ """ + str(statcode0) + """</td>
        <td>"""+ str(realstatcode) + """ """ + str(statcode0) +"""</td>
      </tr>
      <tr>
        <td>Age in """ + str(seasoncode0)+"""</td>
        <td>"""+ (playerage) + """</td>
      </tr>
      <tr>
        <td>Sports Reference ID</td>
        <td>"""+ (playerid) + """</td>
      </tr>
      <tr>
        <td>Weight</td>
        <td>"""+ (playerweight) + """lbs</td>
      </tr>
      <tr>
        <td>Height</td>
        <td>"""+ (playerheight) +""" (in feet-inches) </td>
      </tr>
      <tr>
        <td>Current Team</td>
        <td>"""+ (playerteam) +"""</td>
      </tr>
    </table>

    </body>
    </html>
    """)
    ofile.close()
    #except NoneType:
    #     messagebox.showinfo("The player you chose does not exist")
        
 
    messagebox.showinfo("Data Generated!", "Congratulations, your stat has been generated. Please doubleclick your nhlsite.html file for your generated results! Thanks for using: Stat Generator by Oliver He.")
    
   # ofile.write (str(input2) + " had " + str(realcode('2018-19').statcode) + " points in the 2018-2019 season and " + str(realcode('Career').statcode) + " Career points")
   # ofile = open("nhlsite.html", "w")
   #ofile.write(str(input2) + " had " + str(realcode('2018-19').statcode) + " points in the 2018-2019 season and " + str(realcode('Career').statcode) + " Career points")
   #ofile.close()


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
choices = ( 'Goals','Assists','Blocks at even strength','Even strength assists','Even strength goals', 'Game winning goals', 'Goals Against','Hits at even strength','Penalty minutes','+/-','Points', 'Power play goals', 'Power play assists', 'Shooting percentage', 'Save percentage','Short handed assists', 'Short handed goals', 'Shutouts', "Shots on goal")
tkvar1.set('Stat')
popupMenuStat = OptionMenu(mainframe, tkvar1, *choices)
Label(mainframe, text="Choose a stat").grid(row = 30, column = 0)
popupMenuStat.grid(row = 32, column =0)
tkvar1.trace('w', change_dropdown)

#Dropdown for seasons

tkvar2 = StringVar(root)

choices2 = ('2015-16','2016-17', '2017-18', '2018-19' , 'Career')
tkvar2.set('Season')

popupMenuSeason = OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text="Choose a season").grid(row = 30, column = 2)
popupMenuSeason.grid(row = 32, column =2)


tkvar2.trace('w', changedropdown)
#
tk.Label(mainframe, text="Type an NHL player with format, First name Last name.").grid(row = 0, column = 1)

input1 = tk.Entry(mainframe)
input1.grid(row=3, column=1)
tk.Button(mainframe, text= "Generate Data!",command = delete).grid(row=10, column=1, sticky=tk.W, pady=4)
tk.Button(mainframe, text= "Quit application",command = quit ).grid(row=3, column=2, sticky=tk.W, pady=4)



tk.mainloop()
#The ID for the players are the 5 letters of last name plus first 2 letters of first name and 01
#https://sportsreference.readthedocs.io/en/stable/index.html

