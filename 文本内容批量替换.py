import os


txtfilepath = r"F:\DownLoad_Storage\test" #原始txt文件所存文件夹，文件夹可以有一个或多个txt文件
savefilepath = r"F:\DownLoad_Storage\after" #更改后txt文件存放的文件夹
total_txt = os.listdir(txtfilepath) # 返回指定的文件夹包含的文件或文件夹的名字的列表
num = len(total_txt)
list = range(num) #创建从0到num的整数列表
files = os.listdir(savefilepath)

for i in list: #遍历每一个文件
    name = total_txt[i]
    readfile = open(txtfilepath+"/"+name, 'r') #读取文件
    fline = readfile.readlines() #读取txt文件中每一行
    savetxt = open(savefilepath+"/"+name,'w')

    for j in fline:
        if "10" in j:
            b = j.replace('10', '6', 1) #替换固定行内容
        savetxt.write(b) #写入新的文件中

    readfile.close()
    savetxt.close()

print('文件替换完成')