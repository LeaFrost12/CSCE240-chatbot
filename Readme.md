Author: Lea Frost

Code written for CSCE 240H

Code reuse from Tarun Ramkumar - WebScraper.py

Demo video: [https://youtu.be/Ggu_6fOzRIg?si=Ey4N_GuQCw8RV9bz](https://youtu.be/Ggu_6fOzRIg?si=Ey4N_GuQCw8RV9bz)

Description:

    This project answers user questions about a business based on
    
    the business's 10k form. The program is built to work for 
    
    Apple and Amazon, but can work for other companies.
    
    It also reports interaction statistics when requested.


Instructions:

For running the chatbot:

    While in the directory "my-chatbot", run "python ./"
    
For running debug mode/iteraction stats:

    While in the directory "my-chatbot", run:
    
        python ./ -summary
        
        python ./ -showchat [chat number]
        
        python ./ -showchat-summary [chat number]

Layout:

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
