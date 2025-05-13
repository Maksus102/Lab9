import csv

with open("data/prepared/vak_datak8.csv", 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

new_row_1 = ["vhigh",'vhigh','3','3','small','med','unacc']

data.append(new_row_1)

with open("data/prepared/vak_datak8.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data/prepared/train_datak8.csv", 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

new_row_2 = ["vhigh",'vhigh','3','3','small','med','unacc']

data.append(new_row_2)

with open("data/prepared/train_datak8.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)