#######################################################
######## REGEX : HACKER RANK PROBLEM ##################
#######################################################

########################################################
###### PROBLEM 1: Matching Specific String #############
########################################################

## Link: https://www.hackerrank.com/challenges/matching-specific-string/problem

#########################################################
###################### SOLUTION #########################
#########################################################

import re

Regex_Pattern = r'hackerrank'
Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches : ", len(match))



