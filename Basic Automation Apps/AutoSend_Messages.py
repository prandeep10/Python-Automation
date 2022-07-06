#THIS PROGRAM TAKES INPUT MESSAGES AND AUTOMATICALLY TYPE IT WHILE PRESSING ENTER.
#THIS CAN BE USED TO AUTOTYPE SOME PARTICULAR MESSAGES IN ANY CHAT-APPLICATION OR SPAM THOSE MESSAGES
#IF THE INPUT MESSAGE IS DONE, THEN IT STOPS TAKING INPUTS AND THE AUTOMATION PROGRAM STARTS.


import pyautogui as pg
import time
import random

msg_list = []

while True :
    msg = str(input("Enter Message :"))
    msg_list.append(msg)

    if msg.upper() == "SPAM":
        msg_list.pop()
        no = int(input("Enter The Number of Times You Wanna Spam :"))

        time.sleep(10)
        for i in range(no):
            a = random.choice(msg_list)
            pg.write(a)
            pg.press("Enter")
        break
    
    

    if msg.upper() == "DONE":
        msg_list.pop()
        
        time.sleep(5)
        for item in msg_list:
            pg.write(item)
            pg.press("Enter")
        break
    
    




    
    
    


