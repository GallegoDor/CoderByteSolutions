#Task 3
#Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
#If there are two or more words that are the same length, return the first word from the string with that length. 
#Ignore punctuation and assume sen will not be empty. 

def LongestWord(sen):
  longest = ' '
  punctuation = "!@#$%^&*()_-+=|\"']}[{:;?/><.,"
  for i in sen:
    if i in punctuation:
      sen = sen.replace(i, ' ')
  for substring in sen.split(' '):
    if len(substring) > len(longest): longest = substring
  return longest  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           

