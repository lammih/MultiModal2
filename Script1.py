import shutil
import os, os.path


# brain 49 --> 99
for i in range(49,99+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/0'+str(i)+'/brain/'
    print(path)

    dirs = os.listdir(path)
    print('Anzahl der Dateien:' + str(len(dirs)))

    for x in range(1, len(dirs)+1):
        try:
            os.rename(r''+path+str(x)+'.jpg', r''+ path + str(i) + str(x) + '.jpg')
        except: 
            pass

# bone 49 --> 99
for i in range(49,99+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/0'+str(i)+'/bone/'
    print(path)

    dirs = os.listdir(path)
    print('Anzahl der Dateien:' + str(len(dirs)))

    for x in range(1, len(dirs)+1):
        try:
            os.rename(r''+path+str(x)+'.jpg', r''+ path + str(i) + str(x) + '.jpg')
        except: 
            pass

# brain 100 --> 130
for i in range(100,130+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/'+str(i)+'/brain/'
    print(path)

    dirs = os.listdir(path)
    print('Anzahl der Dateien:' + str(len(dirs)))
    for x in range(1, len(dirs)+1):
        try:
            os.rename(r''+path+str(x)+'.jpg', r''+ path + str(i) + str(x) + '.jpg')
        except: 
            pass

# bone 100 --> 130
for i in range(100,130+1):
    path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/'+str(i)+'/bone/'
    print(path)

    dirs = os.listdir(path)
    print('Anzahl der Dateien:' + str(len(dirs)))

    for x in range(1, len(dirs)+1):
        try:
            os.rename(r''+path+str(x)+'.jpg', r''+ path + str(i) + str(x) + '.jpg')
        except: 
            pass


"""
DestinationBrain = /Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/Brain
DestinationBone = /Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/Bone

"""

"""
path = '/Users/Hakkar/Downloads/computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/Patients_CT/049/bone'

dirs = os.listdir(path)
"""