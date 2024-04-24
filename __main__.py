#Lea Frost
#main
#CSCE 240H - S24

import src.sessionlogger as sl
import src.chatbotBE as be
import src.WebScraper as ws
import time
import sys

#main class
def main():

    user_input = ""
    user_utterances = 0
    system_utterances = 0

    #Create session file name
    current_time = sl.getTime()
    session_file = f"data/chat_sessions/chatsession_{current_time}.txt"

    #out file name
    output_file = "data/output/output.txt"

    #If 10-k files are empty/missing, scrape content from web
    ws.scrape10ks()

    #regular chat mode, no debug
    if len(sys.argv)==1:

        #record start time
        start = time.perf_counter()
        
        #while loop that continues until the user enters quit
        print("\nEnter the question you would like to ask or enter \"quit\" or \"q\" to exit.\nFor information on what questions you can ask, ask me \"What questions can I ask?\"\n")
        while (not user_input == "QUIT") & (not user_input == "Q") & (not "QUIT" in user_input):
            
            #save question as a string
            user_input = input(">")

            #print user utterance to session file
            be.printToFile(f"<USER INPUT>:\n\n{user_input}\n", session_file, 'a')
            user_utterances += 1

            #convert user input to upper case
            user_input = user_input.upper()
            #find the part based on user input
            output = be.mapToPart(user_input)

            #print to output file
            be.printToFile(output, output_file, 'w')

            #print to session file
            be.printToFile(f"<SYSTEM OUTPUT>:\n{output}\n", session_file, 'a')
            system_utterances += 1

        #calculate elapsed time
        elapsed_time = time.perf_counter() - start

        #log the session
        sl.logSession("chatsession_" + current_time + ".txt", user_utterances, system_utterances, int(elapsed_time))

    #debug mode

    #summary
    elif sys.argv[1] == "-summary":
        sl.summary()

    #show chat contents
    elif sys.argv[1] == "-showchat":
        sl.showchat()

    #showchat summary
    elif sys.argv[1] == "-showchat-summary":
        sl.showchatSummary()

    else:
        print("ERROR- Unrecognized command")
        
        
if __name__ == "__main__":
    main()
    