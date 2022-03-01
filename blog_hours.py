# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 22:34:19 2022

@author: oleks
"""

#C:\Folders\Uni\Year 2 Sem 2\SoftEngi\gp3\GroupProject-master\config\blogs

import os
from collections import defaultdict
from collections import Counter
from sys import exit
import re
import csv

blog_dir = input("enter blog folder directory ")
dir_list = []
user_hours = []
blog_num = []

print("getting all blog files...")
if (os.path.isdir(blog_dir)):
    for user in os.listdir(blog_dir):
        if (user == ".gitkeep"):
            continue
        dir_list.append(user)
        user_folder = blog_dir+"\\"+user
        global max_blog_num
        index = 0
        for blog in os.listdir(user_folder):
            index += 1
            blog_num.append(index)
            max_blog_num = max(blog_num)
            try:
                with open(user_folder+"\\"+blog, "r") as f:
                    lines = f.readlines()
                    f.close()
                    hours = int(re.search(r'\d+', lines[-1].rstrip()).group())
                    user_hours.append(tuple((user, hours)))
            except IOError:
                print("File not accessible")
            finally:
                f.close()
else:
    print("Directory doesn't exist, exiting...")
    os.system('pause')
    exit()
print("done")
sums = defaultdict(int)
for k, i in user_hours:
    sums[k] += i

##save to text file
# with open("hours.txt", "w") as fp:
#     for user, i in sums.items():
#         all_hours = []
#         #for hours in sums[i]:
#         for mem, j in user_hours:
#             if (mem == user):
#                 all_hours.append(j)
#         fp.write("%s " % user)
#         for hrs in all_hours:
#             fp.write("%d " % hrs)
#         fp.write("%d\n" % i)
#     fp.close
    
with open("hours.csv", "w", newline='') as fp:
    writer = csv.writer(fp)
    print("writing header...")
    header = ["Member"] 
    for i in range(max_blog_num):
        header.append("Blog "+str(i+1)+" Hours")
    header.append("Total Hours")
    writer.writerow(header)
    print("done")

    name = []
    for tup in user_hours:
        name.append(tup[0])
    counter = Counter(e for e in name)
    print("writing hours...")
    for user, i in sums.items():
        row = [user]
        for mem, j in user_hours:
            if (mem == user):
                row.append(j)
        if (counter.get(user) < max_blog_num):
            row.append("N/A")
        row.append(i)
        header.append("Total Hours")
        writer.writerow(row)
    print("done")
os.system('pause')