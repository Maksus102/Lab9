import csv
import random
from sklearn.model_selection import train_test_split

def split_train_test(data, test_size=0.3):
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    return train_data, test_data

def split_train_val_test(data, test_size=0.12, k=8):
    train_val_data, test_data = train_test_split(data, test_size=test_size, random_state=42)

    random.shuffle(train_val_data)
    fold_size = len(train_val_data) // k
    folds = []
    for i in range(k):
        fold = train_val_data[i * fold_size: (i + 1) * fold_size]
        folds.append(fold)

    val_data = folds[0]
    train_data = []
    for fold in folds[1:]:
        train_data.extend(fold)

    return train_data, val_data, test_data

with open("data/prepared/clean_data.csv", 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

train_data_70, test_data_30 = split_train_test(data, test_size=0.3)
print(f"Разделение 70 на 30 - Тренировочная: {len(train_data_70)}, Тестовая: {len(test_data_30)}")

with open("data/prepared/train_data70.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_data_70)

with open("data/prepared/test_data30.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_data_30)

train_data_80, test_data_20 = split_train_test(data, test_size=0.2)
print(f"Разделение 80 на 20 - Тренировочная: {len(train_data_80)}, Тестовая: {len(test_data_20)}")
with open("data/prepared/train_data80.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_data_80)

with open("data/prepared/test_data20.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_data_20)

train_data, val_data, test_data = split_train_val_test(data, test_size=0.12, k=8)
print(f"Разделение с k=8 - Тренировочная: {len(train_data)}, Валидационная: {len(val_data)}, Тестовая: {len(test_data)}")
with open("data/prepared/train_datak8.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_data)

with open("data/prepared/test_datak8.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_data)

with open("data/prepared/vak_datak8.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(val_data)
