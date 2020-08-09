import shutil
import os, os.path

for i in range(100,130+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/'+str(i)+'/bone/'
    print(path)

    dirs = os.listdir(path)
    print('Anzahl der Dateien:' + str(len(dirs)))

    for x in range(1, len(dirs)+1):
        try:
            source = ''+ path + str(i) + str(x) + '.jpg'
            destination = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/Bone'
            moveFromTo = shutil.move(source, destination)
        except: 
            pass
