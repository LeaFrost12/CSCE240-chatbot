#Lea Frost
#Chatbot back end
#CSCE 240H - S24

import src.wordmatcher as wm
import src.sessionlogger as sl
import re

'''
returns the contents of an item using a start and end pattern

Parameters:
    start (string): Regex pattern to find the start of the part
    end (string): Regex pattern to find the end of the part
    file (string): Path to the company's 10-k file
Returns:
    text (string): the system's response to the user
'''
def findItem(start, end, file):
    #initialize a text string to store the text
    text = ""

    #initialize the regex start and end
    start = re.compile(start)
    end = re.compile(end)

    #iterate through each line in the file to find start pattern
    #open 10k file
    try:
        with open(file, 'r', encoding="utf8") as f:
            #iterate through each line
            for line in f:

                #when the start expression is found, add each line until the end expression is reached
                if(re.search(start, line)):

                    #continue until end is reached
                    while(not re.search(end, line)):
                        #add line to the text string
                        text += line
                        #move to next line
                        line = f.readline()
                    #break once end is reached
                    break

    except IOError as error:
        print("\nERROR - Could not open company 10-k file\n")
        return
    
     #notify that the output has been printed to a file
    print("\nThe answer has been written in an output file.\n")

    #return the text
    return text
    
'''
Determines the company of interest and what part the user wants and then finds that part using findsItem()
Answers questions about supported companies and questions, usage stats
Informs user if query isn't supported

Parameters:
    str (string): The user's input
Returns:
    text (string): the system's response to the user
'''
def mapToPart(str):
    text = ""

    #If the user chooses to quit, print goodbye
    if ((str == "QUIT") | (str == "Q") | ("QUIT" in str)):
        text = "You have terminated the chat. Goodbye."
        print("\n" + text + "\n")
        return text

    else:
        #User might be asking about what questions they can ask
        if (wm.isMatch(str, "WHAT INFO") or wm.isMatch(str, "WHAT QUESTIONS")):
            text = "Ask about business, risk factors, properties, legal proceedings, market, directors,\ndisclosures, executive compensation, statements, all information about a company, \nor usage stats"
            print("\n"+text+"\n")
            return text

        #determine what business they question is asking about and set the path to that file
        #apple
        if wm.isMatch(str, "APPLE") or wm.isMatch(str, "APPLE'S"):
            file = "data/input/Apple-2023.txt"

        #amazon
        elif wm.isMatch(str, "AMAZON") or wm.isMatch(str, "AMAZON'S"):
            file = "data/input/Amazon-2022.txt"

        #No company name, user asking about supported companies
        elif (wm.isMatch(str, "SUPPORT") or wm.isMatch(str, "COMPANIES")):
            text = "Supported companies are Apple and Amazon"
            print("\n" + text + "\n")
            return text
        
        #No company name, user might be asking about usage stats
        elif (wm.isMatch(str, "STATISTICS") or wm.isMatch(str, "USAGE")):
            text = sl.summary()
            return text

        #if company name is not included, ask them to try again
        else:
            text = f"{str} - I do not know this information.\nPlease include the business name and try again. You can ask about Apple or Amazon.\nFor information on what questions you can ask, ask me \"What questions can I ask?\""
            print("\n"+text+"\n")
            return text
        #business name was found, now decide what question they are asking and print the item contents
        #Item 1: Business
        if wm.isMatch(str, "BUSINESS"):
            text = findItem(r"(?i)ITEM 1.\s*BUSINESS", r"(?i)ITEM 1A.\s*RISK FACTORS", file)

        #Item 1A: Risk factors
        elif wm.isMatch(str, "RISK FACTORS"):
            text =  findItem(r"(?i)ITEM 1A.\s*RISK FACTORS", r"(?i)ITEM 1B.\s*UNRESOLVED STAFF COMMENTS", file)

        #Item 2: Properties
        elif wm.isMatch(str, "PROPERTY"):
            text =  findItem(r"(?i)ITEM 2.\s*PROPERTIES", r"(?i)ITEM 3.\s*LEGAL PROCEEDINGS", file)

        #Item 3: Legal Proceedings
        elif wm.isMatch(str, "LEGAL PROCEEDINGS"):
            text =  findItem(r"(?i)ITEM 3.\s*LEGAL PROCEEDINGS", r"(?i)ITEM 4.\s*MINE SAFETY DISCLOSURES", file)

        #Item 5: Market
        elif wm.isMatch(str, "MARKET"):
            text = findItem(r"(?i)ITEM 5.\s*MARKET", r"(?i)ITEM 6.", file)

        #Item 7A: Disclosures
        elif wm.isMatch(str, "DISCLOSURE"):
            text = findItem(r"(?i)ITEM 7A.\s*Quantitative and Qualitative Disclosures About Market Risk", r"(?i)ITEM 8.\s*Financial Statements and Supplementary Data", file)

        #Item 10: Directors
        elif wm.isMatch(str, "DIRECTOR"):
            text = findItem(r"(?i)ITEM 10.\s*Directors, Executive Officers, and Corporate Governance", r"(?i)ITEM 11.\s*Executive Compensation", file)

        #Item 11: #Compensation
        elif wm.isMatch(str, "COMPENSATION") | wm.isMatch(str, "EXECUTIVE"):
            text = findItem(r"(?i)ITEM 11.\s*Executive Compensation", r"(?i)ITEM 12.", file)

        #Item 15: Statements
        elif wm.isMatch(str, "STATEMENT"):
            text = findItem(r"(?i)ITEM 15.\s*Exhibit and Financial Statement Schedules", r"(?i)ITEM 16.", file)

        #all information
        elif wm.isMatch(str, "ALL INFORMATION") or wm.isMatch(str, "EVERYTHING"):
            text = findItem(r"(?i)ITEM 1.\s*BUSINESS", r"(?i)ITEM 16.", file)

        #The question wasn't recognized, ask them to try again
        else:
            text = f"\"{str}\" - I do not know this information.\nFor information on what questions you can ask, ask me \"What questions can I ask?\""
            print("\n"+text+"\n")
            
        return text
         
'''
Prints a string to a file

Parameters:
    str (string): String to be printed
    file_name (string): path to the output file
    mode (char): mode to open the file
Returns:
    text (string): the system's response to the user
'''
def printToFile(str, file_name, mode):
    
    #open file for writing
    try:
        with open(file_name, mode, encoding = "utf8") as file:
            #write to file
            file.write(str + "\n")
    except IOError as error:
        print(f"ERROR - Could not open file - {file_name}")
        return