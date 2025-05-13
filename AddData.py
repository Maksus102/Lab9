import csv

with open("data/prepared/clean_data.csv", 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

new_row = ["vhigh",'vhigh','3','3','small','med','unacc']

data.append(new_row)
print("Добавление через csv:")
print(f"Новая строчка : {data[1725]}")

with open("data/prepared/clean_data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)