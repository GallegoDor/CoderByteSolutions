#Task 2 - The instructions that were given are below
#2. Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it 
#(ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18. 

import math
def FirstFactorial(num): 
  return math.factorial(num)

# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstFactorial(raw_input())

#P.S. I cheated a little with this one by importing math and using the factorial method.
#But hey, it's a good programmers job to know the tools that exist out there for him.
#Keeping my code DRY lol, that pun sounds so lame.
