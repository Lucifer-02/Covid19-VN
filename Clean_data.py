raw_file = open("raw_data.txt", "r")

data = raw_file.read()

# split line into elements
data = data.split("\\n")

# remove "\r" and "\t"
for i in range(len(data)):
    data[i] = data[i].replace("\\r", "")
    data[i] = data[i].replace("\\t", "")


# # remove tag
# for i in range(len(data)):
#     tags = []
#     for j in range(len(data[i])):
#         if data[i][j] == "<":
#             begin = j
#         if data[i][j] == ">":
#             end = j
#             tags.append(data[i][begin:end + 1])
#     for tag in tags:
#         data[i] = data[i].replace(tag, "")

# # remove space
# for i in range(len(data)):
#     data[i] = data[i].strip()

# data_without_space = []

# for i in range(len(data)):
#     if data[i] != "":
#         data_without_space.append(data[i])
# data = data_without_space


# # convert special char
# file = open("unicode.txt", "r", encoding="utf8")

# char_table = file.read().split("\n")

# for i in range(len(char_table)):
#     char_table[i] = char_table[i].replace("\\", "")
#     char_table[i] = char_table[i].split("\t")

#     # remove "\" in data

# for i in range(len(data)):
#     data[i] = data[i].replace("\\", "")

# for i in range(len(data)):
#     for j in range(len(char_table)):
#         data[i] = data[i].replace(char_table[j][1], char_table[j][0])


# remove unused line

# start_line = data.index("Bệnh nhân")


# for i in range(len(data)):
#     if data[i] == "BN1" and len(data[i]) == 3:
#         end_line = i
#         print("the end_line is: " + str(end_line) + '\n')

# data = data[start_line:end_line + 5]


# # remove "(BN"
# for i in range(len(data)):
#     data[i] = data[i].replace("(BN", "BN")

# # make a list of lines which content Bệnh nhân's informations
# string = []

# string.append("Bệnh nhân,Tuổi,Địa điểm,Tình trạng,Quốc tịch")

# for i in range(len(data)):
#     if data[i] == "BN1":
#         string.append(data[i] + "," + data[i + 1] + "," +
#                       data[i + 2] + "," + data[i + 3] + "," + data[i + 4])
#         break

#     if data[i][0:2] == "BN" and data[i + 5][0:2] == "BN":
#         string.append(data[i] + "," + data[i + 1] + "," +
#                       data[i + 2] + "," + data[i + 3] + "," + data[i + 4])
#         i += 4
#     if data[i][0:2] == "BN" and data[i + 4][0:2] == "BN":
#         string.append(data[i] + "," + data[i + 1] + "," +
#                       "-1" + "," + data[i + 2] + "," + data[i + 3])
#         i += 3

# data = string


# write data is clean to data_test.txt file
file_txt = open("data_clean.txt", encoding="utf8", mode="w")

for i in range(len(data)):
    file_txt.write(data[i] + "\n")


# write data is clean to data_clean.csv file
file_csv = open("data_clean.csv", encoding="utf8", mode="w")

for i in range(len(data)):
    file_csv.write(data[i] + "\n")
