import csv
import numpy as np

def convert_value(value, column):
    if column == 2:
        if value == '5more':
            return 5
        elif value.isdigit():
            return int(value)
        else:
            return 5
    elif column == 3:
        if value == 'more':
            return 5
        elif value.isdigit():
            return int(value)
        else:
            return 5
    else:
        return value


data = []
with open('data/prepared/train_data80.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        converted_row = [convert_value(value, idx) for idx, value in enumerate(row)]
        data.append(converted_row)

column_2 = [row[2] for row in data]

# Нормализация без sklearn
min_val = min(column_2)
max_val = max(column_2)
normalized_row = []
for idx, x in enumerate(column_2):
    normalized_row.append((column_2[idx] - min_val) / (max_val - min_val))

# Масштабирование без sklearn
mean_val = sum(column_2)/len(column_2)
stand_div = np.std(column_2)
scaled_row = []
for idx, x in enumerate(column_2):
    scaled_row.append((column_2[idx] - mean_val) / stand_div)

print("Ручн. норм.")
print("-----------------")
for a, b in zip(column_2,normalized_row):
    print(f"{a:^7} | {b:^7}")

print("Ручн. масш.")
print("-----------------")
for a, b in zip(column_2,scaled_row):
    print(f"{a:^7} | {b:^7}")

with open("data/prepared/norm.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(normalized_row)

with open("data/prepared/scaled.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(scaled_row)

