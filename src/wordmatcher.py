#Lea Frost
#PA 4 - user 2 intent query mapper
#CSCE 240H - S24

THRESHOLD = 0.7
LENGTH = 8

'''
Calculates the percent match of the user input compared to the mapped sentence

Parameters:
    user_sent (string): The user's input
    map_sent (string): The mapped sentence
Returns:
    double: The match percent of user_sent
'''
def matchSentence(user_sent, map_sent):
    matches = 0
    match_percent = 0   

    #split sentences into an array for comparison
    user_arr = user_sent.split()
    map_arr = map_sent.split()


    #for each user word, count the matches for each word in the mapped sentence
    for i in range (len(map_arr)):
        j = 0
        match = False
        #if a match is found, stop the loop so less comparisons are done
        while(not match and j<len(user_arr)):
            #if the match percent is greater than the threshold, count the match
            if(matchWord(user_arr[j].upper(),map_arr[i].upper())>=THRESHOLD):
                matches += 1
                match = True

            j += 1

    #calculate percentage match
    match_percent = matches / len(map_arr)

    #return percentage match
    return match_percent

'''
Calculates the percent match of the user word compared to the mapped word

Parameters:
    user_word (string): A word from the user's input
    keyword (string): A word from the mapped words
Returns:
    double: The match percent of the user_word
'''
def matchWord(user_word, keyword):
    user_len = len(user_word)
    key_len = len(keyword)

    match_percent = 0
    if(user_len<LENGTH and key_len<LENGTH):
        min_len = min(user_len, key_len)
        distance = editDistance(keyword, user_word[0:min_len], key_len, min_len)
    #If the user word is short, calculate edit distance on the entire user word
    elif(user_len<LENGTH):
        distance = editDistance(keyword, user_word, key_len, user_len)
    #If the map word is short
    elif(key_len<LENGTH):
        distance = editDistance(keyword, user_word[0:key_len], key_len, key_len)
    #If the word is long, calculate edit distance on just the first 8 letters
    else:
        distance = editDistance(keyword[0:LENGTH], user_word[0:LENGTH], LENGTH, LENGTH)

    #calculate match percentage by dividing edit distance by map word length
    match_percent = 1 - (distance / key_len)

    #return match percent
    return match_percent

'''
Calculates how many operations needed to convert one word to another

Parameters:
    str1 (string): A word from the user's input
    str2 (string): A word from the mapped sentences
    len1 (int): Length of the user word
    len2 (int): Length of the mapped word
Returns:
    int: The edit distance between str1 and str2
'''
def editDistance(str1, str2, len1, len2):
    #base cases
    if len1 == 0:
        return len2

    if len2 == 0:
        return len1
    
    #if characters match
    if str1[len1-1] == str2[len2-1]:
        return editDistance(str1, str2, len1-1, len2-1)
    
    #if characters dont match
    return 1 + min(editDistance(str1, str2, len1, len2-1),    # Insert
                   editDistance(str1, str2, len1-1, len2),    # Remove
                   editDistance(str1, str2, len1-1, len2-1)    # Replace
                   )

#determines if the user utterance matches a keyword
def isMatch(user_input, keyword):
    if (matchSentence(user_input, keyword)>THRESHOLD):
        return True
    return False
