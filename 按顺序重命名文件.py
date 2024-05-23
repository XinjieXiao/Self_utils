import os

path = r'F:\DownLoad_Storage\UIEB'
os.chdir(path)
count = 1
for i in os.listdir(path):
    _ , file_format = i.split('.')
    new_name = str(count)+ '.' + file_format
    os.rename(i,new_name)
    print(f'-----------------{count}/{len(os.listdir(path))}-----------------')
    count += 1

print(f'Finish Renamed!')