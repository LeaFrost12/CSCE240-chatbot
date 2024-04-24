# CSCE 240H Final Chatbot

Author: Lea Frost

Code reuse from Tarun Ramkumar - WebScraper.py

Demo video: [https://youtu.be/Ggu_6fOzRIg?si=Ey4N_GuQCw8RV9bz](https://youtu.be/Ggu_6fOzRIg?si=Ey4N_GuQCw8RV9bz)

## Description:

This project answers user questions about a business based on

the business's 10k form. The program is built to work for 

Apple and Amazon, but can work for other companies.

It also reports interaction statistics when requested.


## Instructions:

### Running the chatbot:

While in the directory "my-chatbot", run:

    "python ./"
    
### Running debug mode/iteraction stats:

While in the directory "my-chatbot"

For summary of all chat sessions, run:
    
        python ./ -summary

To see the contents of a specific chat, run:
        
        python ./ -showchat [chat number]

To see the summary statistics of a specific chat, run:
        
        python ./ -showchat-summary [chat number]

## Layout:
'''
my-chatbot

    __main__.py
    
    data
    
        chat sessions
        
            Contains saved chat sessions
            
        input
        
            Contains company 10k files
            
        output
        
            output.txt
            
        chat_statistics.csv
        
    doc
    
        report.txt
        
        test_output.txt
        
    src
    
        chatbot.py
        
        sessionlogger.py
        
        wordmatcher.py
            
        test
        
            test.txt
'''
