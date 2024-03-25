import os
import shutil



my_floders = ['current', 'previous','reference']
target_path = ''
for i in os.listdir(target_path):
    t = os.path.join(target_path,i)

    for j in my_floders:
        k = os.path.join(t,j)
        if not os.path.exists(k):
            os.mkdir(k)
        if j == 'current':
            shutil




