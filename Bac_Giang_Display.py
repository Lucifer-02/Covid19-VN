import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as pltimport 
import subprocess

subprocess.check_output('python.exe Update_By_Date.py', shell=True)
subprocess.check_output('python.exe Bac_Giang_Update.py', shell=True)

file = open('Bac_Giang.csv', 'r', encoding='UTF8')
data = file.read().split('\n')

data.remove(data[len(data)-1])

for i in range(len(data)):
	data[i] = data[i].split(',')

while(data[len(data)-1][0] == data[len(data)-2][0]):
	data[len(data)-2] = data[len(data)-1]
	data.remove(data[len(data)-1])

time = []
number = []
increase = []

for i in range(len(data)):
	time.append(data[i][0]+'h '+data[i][1] +'/'+ data[i][2])
	number.append(int(data[i][4]))


y_pos = np.arange(len(time))
width = 0.4

fig, ax = plt.subplots(figsize=(10,5))

solieu = ax.barh(time,number, width,label='số ca nhiễm')


ax.set_xlabel('Số ca nhiễm')
ax.set_title('Tình hình dịch tại Bắc Giang')
ax.bar_label(solieu, padding=3)
plt.xlim(1300, 4000)
ax.legend()
fig.tight_layout()


plt.show()



