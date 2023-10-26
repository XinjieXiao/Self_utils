import os
file_road = r"F:\All_DataSet\Data\NHC-D\valid_NH\input"
output_road = r'F:\All_DataSet\Data\NHC-D\valid_NH\val_list.txt'
files = os.listdir(file_road)
with open(output_road,'w') as f:
    f.write('\n'.join(files))
print('Finish')
