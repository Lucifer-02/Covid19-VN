from datetime import datetime

date = datetime.now()

# Import data from csv file
file = open('data_clean.csv', 'r', encoding='UTF8')

data = file.read()

data = data.split('\n')


Patient_Num = 0;

for i in range(len(data)):
	if 'Bắc Giang' in data[i]:
		Patient_Num+=1

file = open('Bac_Giang.csv', 'a', encoding='UTF8')

file.write(str(date.hour) + ',' + str(date.day)+ ',' + str(date.month)+ ',' + str(date.year) + ',' + str(Patient_Num) + '\n')



