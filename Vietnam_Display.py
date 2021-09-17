from matplotlib.colors import Normalize
import numpy as np
import matplotlib.pyplot as plt
import subprocess

subprocess.check_output('python3 Update_By_Date.py', shell=True)


file = open('data_clean.csv', 'r', encoding='UTF8')

data = file.read().split('\n')

file = open('County.txt', 'r', encoding='UTF8')

counties = file.read().split('\n')

counties_panic = []

for county in counties:
	count = 0
	for i in range(len(data)):
		if(county in data[i] and 'Đang điều trị' in data[i]):
			count +=1
	counties_panic.append(count)

minimum_county = ['Các tỉnh khác']
minimum_number = [0]

for i in range(len(counties_panic)):
	if(counties_panic[i] < 100):
		minimum_number[0] += counties_panic[i]
	else:
		minimum_county.append(counties[i])
		minimum_number.append(counties_panic[i])

print(minimum_number)
print(minimum_county) 




fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(minimum_number, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(minimum_county[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("VietNam is best")

plt.show()