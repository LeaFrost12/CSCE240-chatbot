#Lea Frost
#PA5 - sessionlogger
#CSCE 240H - S24

from datetime import datetime
import csv
from csv import writer
import sys

#path to csv file
csv_file = "data/chat_statistics.csv"

#get the current time
def getTime():
    current_time = datetime.now().strftime("%I_%M_%S_%p")
    return current_time

#counts the number of rows in the csv file
def getRows():
    
    try:
        #open csv
        with open(csv_file,"r",encoding="utf-8") as f:
            #calculate number of rows
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            rows = len(data)

    except FileNotFoundError:
        print("CSV file not found")

    #return number of rows
    return rows

#sums a column of values
def sumCol(col):

    #open csv file
    with open(csv_file) as f:
        #sum the column
        total = sum(int(r[col]) for r in csv.DictReader(f))

    return total

#gets the contents of the specific chat number
def getChat(chat):

    #open csv file and get the chat file name
    with open(csv_file, 'r') as file:

        mycsv = csv.reader(file)
        mycsv = list(mycsv)
        text = mycsv[chat][1]
        
    #generate file name
    file_name = "data/chat_sessions/" + text
    #open chat file and read contents
    with open(file_name, "r", encoding='utf8') as chat_file:

        return chat_file.read()

#gets a csv value using row and column
def getValue(r, c):

    with open(csv_file, 'r') as file:

        mycsv = csv.reader(file)
        mycsv = list(mycsv)
        text = mycsv[r][c]
        return text

#logs the sessions into the csv file 
def logSession(chat_file, user_utterances, system_utterances, time):

    #try to open the csv file
    try:

        with open(csv_file, 'a', newline = '') as file:

            #create writer object
            writer_obj = writer(file)
            #create the list input
            input = [getRows(), chat_file, user_utterances, system_utterances, time]
            #write the list to the file
            writer_obj.writerow(input)

            file.close()

    except FileNotFoundError:
        print("CSV file not found")

#calculate total chats, used later
total_chats = getRows()-1

def summary():
    #calculate values
    user_utterances = sumCol("#user_utterances")
    system_utterances = sumCol("#system_utterances")
    time = sumCol("time")

    #print values
    text = f"There are {total_chats} chats to date with user asking {user_utterances} times and system reponding {system_utterances} times.\nTotal duration is {time} seconds."
    print("\n"+text+"\n")
    return text

def showchat():
    #get chat number
    chat_numb = int(sys.argv[2])

    #check chat validity
    if 0 < chat_numb <= total_chats:
        #print chat contents
        print(f"Chat {chat_numb} is:\n")
        print(getChat(chat_numb))

    #chat number invalid
    else:
        print(f"\nERROR: There are {total_chats} sessions. Please choose a valid number.\n")

def showchatSummary():
    
    #get the chat number
    chat_numb = int(sys.argv[2])
    #check that the chat number is valid

    if 0 < chat_numb <= total_chats:

        #calculate values
        user_utterances = getValue(chat_numb, 2)
        system_utterances = getValue(chat_numb, 3)
        time = getValue(chat_numb, 4)

        #print values
        print(f"\nChat {chat_numb} has user asking {user_utterances} times and system responding {system_utterances} times. Total duration is {time} seconds\n")
