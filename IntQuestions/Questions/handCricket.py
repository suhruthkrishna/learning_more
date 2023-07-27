import random
import math
n=int(input('Enter number of deliveries to be bowled'))
balls=0
score=0
cpu_score=0
while(balls<n):
    run=int(input("Enter your choice of runs you want to make between 1,6"))
    cpu=random.randint(1,6)
    if(run==cpu):
        #print("The batsman chose",run)
        #print("The bowler bowled",cpu)
        #print("Brilliant delivery and the bastman has to walk back")
        print("The total score of the batsman is ",score)
        break
    else:
        #print("The batsman chose", run)
        #print("The bowler bowled", cpu)
        #print("Good shot and the batsman adds more runs to his kitty")
        score=score+run
        print("The score of the batsman now is ",score)
    balls+=1

print("After that exciting display of batting from the batting squad the opposition will come out to bat now")
balls2=0
#print("The bowler(you) chose", bowl)
            #print("The batsman shot", cpu_run)
            #print("Brilliant delivery and the bastman has to walk back")
while (balls2 < n):
    bowl = int(input("Enter your choice of length 1,6"))
    cpu_run = random.randint(1, 6)
    if (bowl == cpu_run):
        print("The total score of the batsman is ", cpu_score)
        break
    else:
            #print("The bowler(you) chose", bowl)
            #print("The batsman shot", cpu_run)
            #print("Good shot and the batsman adds more runs to his kitty")
        cpu_score = cpu_score + bowl
        print("The score of the batsman now is ", cpu_score)
    balls2 += 1
if(score>cpu_score):
    print("Congractulations you won!")
elif(score==cpu_score):
    print("Can you believe it we have a rare tie!")
else:
    print("This was a tough loss but sure to jump back")