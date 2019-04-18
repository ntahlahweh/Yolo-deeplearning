import os

path = 'C:/Users/Hafiz_Araken/PycharmProjects/darkflow/hippocampal/test/new test/ha'
files = os.listdir(path)
i = 177
for file in files:
    os.rename(os.path.join(path,file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
print("Done renaming files")