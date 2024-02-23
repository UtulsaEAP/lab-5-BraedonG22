"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""

def feet_to_steps(user_feet):
   #write your code here
   return(user_feet / 2.5)
if __name__ == '__main__':
    #take input feet steps here
   user_feet = float(input())
    #store it into the function
   steps = int(feet_to_steps(user_feet))
    #print your steps here
   print(steps)