import logging
import time

#Account Creation
print ("Welcome to Data Storage 1.0")
print ("Please enter the following data accordingly:")
#make a change
#Not needed atm:
#Opening the file that contains login data
#text_file = open("Database.txt", "w")
#tf = 'Database.txt'
#f = open(tf)
#f.read()

#Requests a response for the log-in data
line1=["----------------------------------"]             
username = input ('Enter your Username ')
line2= ["Username\n"]     
data = input ("Enter the information you want to be logged in a database: ")
line6= ["Text\n"]
timestr = time.strftime("%Y-%m-%d - %H:%M:%S")
line7= ["timestr\n"]
line8=["----------------------------------"] 

#Informs user that their data is being processed
print ("----------------------------------")
print ("Your have entered the following data: ")
print ("Username: ", username)
print ("Information: ", data)
print ("Time/Date: ", timestr)
print ("----------------------------------")

# Format the text with the time, name, level, and message of the file




#Places the data on a log file, in this case, "Data_Entry.log"
logging.basicConfig(filename='Data_Entry.log',level=logging.WARNING)
logging.debug("----------------------------------")
logging.debug(username)
logging.debug(data)
logging.debug(timestr)
logging.debug("----------------------------------")

# © Michael Kachuk


