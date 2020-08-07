import shutil
import os, os.path

counter = 1 

# brain 49 --> 99
for i in range(49,99+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/0'+str(i)+'/brain/'
    

    dirs = os.listdir(path)

    for x in range(1, len(dirs)+1):
        try:
            os.rename(r''+path+str(x)+'.jpg', r''+ path + str(counter) +'.jpg')
            counter += 1 
            
        except: 
            pass

print('Erste Iteration' + str(counter))
# bone 49 --> 99
for i in range(49,99+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/0'+str(i)+'/bone/'
    

    dirs = os.listdir(path)

    for x in range(1, len(dirs)+1):
        try:
             os.rename(r''+path+str(x)+'.jpg', r''+ path + str(counter) +'.jpg')
             counter += 1 
        except: 
            pass


print('Zweite Iteration' + str(counter))


# brain 100 --> 130
for i in range(100,130+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/'+str(i)+'/brain/'
    

    dirs = os.listdir(path)
    for x in range(1, len(dirs)+1):
        try:
             os.rename(r''+path+str(x)+'.jpg', r''+ path + str(counter) + '.jpg')
             counter += 1 
        except: 
            pass

# bone 100 --> 130
for i in range(100,130+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/'+str(i)+'/bone/'
    

    dirs = os.listdir(path)
    

    for x in range(1, len(dirs)+1):
        try:
             os.rename(r''+path+str(x)+'.jpg', r''+ path + str(counter) + '.jpg')
             counter += 1 
        except: 
            pass