# You are given a string s[1 : n] of n characters which is believed to be a corrupted text where all punctuation has been removed.
# For example, the string could be “alltheworldisastage...”. You are also given access to a dictionary in the form of a subroutine
# D(·) which takes as input a string w and D(w) says 0 if w is not a valid word and says 1 if it is. Assume calls to the dictionary
# D(·) take O(1) time. Also assume (it will help you to do so) the empty string is a valid Dictionary word. That is D([ ]) = 1.
# Design an O(n^2) time algorithm that determines whether the input string s[1 : n] can be reconsti-tuted as a sequence of valid words,
# an if it can, your algorithm should also return a corresponding sequence of valid words.

def D(w):
    # Return 1 if w is a valid word, 0 otherwise    
    return 

def removing_spaces(s):
    dp = [0 for i in range(len(s)+1)]
    dp[0] = 1

    for j in range(1, len(s)+1): # Define the start index
        for i in range(j, len(s)+1): # Define the end index
            if D(s[j:i]) and dp[j-1]: # If we have a valid word, and all the chars previous are valid
                dp[i] = 1             # Then we know string s up to end index i is also valid
                break

    return dp[len(s)] # Return if the entire string is valid


