"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   v1 = user_val2
   v2 = user_val1
   v3 = user_val4
   v4 = user_val3
   line = (str(v1) + ' ' + str(v2) + ' ' + str(v3) + ' ' + str(v4))
   return line

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   swapped = swap_values(user_input1, user_input2, user_input3, user_input4)
   #print those output
   print(swapped)
 