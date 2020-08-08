import csv
import shutil
import os, os.path

f = open('hemorrhage_diagnosis.csv')

reader = csv.reader(f)

PatientNumber = []
No_Hemmorhage = []
SliceNumber = []

for row in reader:
    PatientNumber.append(row[0])
    No_Hemmorhage.append(row[7])
PatientNumber.remove(PatientNumber[0])
No_Hemmorhage.remove(No_Hemmorhage[0])

start = 49
index = []
counter = 1

for pt in PatientNumber:
    if pt==str(start):
        index.append(pt+str(counter))
        counter += 1 
    else: 
        index.append(pt+str(1))
        counter = 1 
        counter += 1
        start += 1
       
print(len(index))
print(len(PatientNumber))
print(len(No_Hemmorhage))  


temp = 0
dest = '/Users/Hakkar/Desktop/Brain/Positiv'
dest2 = '/Users/Hakkar/Desktop/Brain/Negativ'

for nh in No_Hemmorhage:
    if nh == str(1):
        try:
            print("test")
            src = '/Users/Hakkar/Desktop/Brain/'+ index[temp]+ '.jpg'
            print(src)
            temp +=1
            moveFromTo = shutil.move(src, dest)
        except:
            pass
    else:
        src = '/Users/Hakkar/Desktop/Brain/'+ index[temp]+ '.jpg'
        moveFromTo = shutil.move(src,dest2) 
        temp +=1

    
print("Completed.......")