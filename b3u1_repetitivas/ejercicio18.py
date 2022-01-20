#cronómetro
from time import sleep
from os import system
seconds=00
minutes=00
hours=00
system("clear")

for i in range(0,60-1):
    for j in range(0,60-1):
        for k in range(0,59):
            print(hours,":",minutes,":",seconds)
            sleep(1)
            seconds+=1
            system("clear")
        seconds=0
        minutes+=1
    minutes=0
    seconds=0
    hours+=1