''' 
Problem : Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet (either lowercase or uppercase or both). For example, we say the letter A is present in the string if either 'a' is present or 'A' is present.
'''
''' 
link : https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1
'''

def checkPangram(self,s):
        # Hashmap for storing char
        words = {} 

        
        # looping through the string 
        for char in s: 

            # if char is English alphabet then add to dict   
             if char.isalpha() : 

                # we are not increasing char value 
                words[char.lower()] = 1 
     
        # If all 26 alphabet are in dict then return True else False
        if len(words) == 26 : 
            return True 
        else : 
            return False
