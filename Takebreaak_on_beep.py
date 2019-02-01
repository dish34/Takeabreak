import time
import winsound

Total_hrs=int(input("Total number of hours you want to study:\n "))
Take_break=0
while (Take_break<Total_hrs):
                   time.sleep(3600)
                   winsound.Beep(3475,1000)
                   Take_break+=1
 
#ctrl-c for exit
