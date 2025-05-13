import csv

def validate_row(row, row_number):
    # Проверка, что в строке ровно 7 значений
    if len(row) != 7:
        print(f"Строка {row_number}: Несоответствие структуре. Ожидалось 7 значений, получено {len(row)}.")
        return False

    # Проверка на пустые значения
    for i, value in enumerate(row):
        if not value.strip():
            print(f"Строка {row_number}: Пустое значение в столбце {i + 1}.")
            return False

    # Проверка допустимости значений для каждого столбца
    buying = row[0].strip()
    maint = row[1].strip()
    doors = row[2].strip()
    persons = row[3].strip()
    lug_boot = row[4].strip()
    safety = row[5].strip()
    class_val = row[6].strip()

    # Проверка допустимых значений для каждого атрибута
    valid_buying = ['vhigh', 'high', 'med', 'low']
    valid_maint = ['vhigh', 'high', 'med', 'low']
    valid_doors = ['2', '3', '4', '5more']
    valid_persons = ['2', '4', 'more']
    valid_lug_boot = ['small', 'med', 'big']
    valid_safety = ['low', 'med', 'high']
    valid_class = ['unacc', 'acc', 'good', 'vgood']

    errors = []

    if buying not in valid_buying:
        errors.append(f"Недопустимое значение '{buying}' в столбце 'buying'. Допустимые значения: {valid_buying}.")
    if maint not in valid_maint:
        errors.append(f"Недопустимое значение '{maint}' в столбце 'maint'. Допустимые значения: {valid_maint}.")
    if doors not in valid_doors:
        errors.append(f"Недопустимое значение '{doors}' в столбце 'doors'. Допустимые значения: {valid_doors}.")
    if persons not in valid_persons:
        errors.append(f"Недопустимое значение '{persons}' в столбце 'persons'. Допустимые значения: {valid_persons}.")
    if lug_boot not in valid_lug_boot:
        errors.append(
            f"Недопустимое значение '{lug_boot}' в столбце 'lug_boot'. Допустимые значения: {valid_lug_boot}.")
    if safety not in valid_safety:
        errors.append(f"Недопустимое значение '{safety}' в столбце 'safety'. Допустимые значения: {valid_safety}.")
    if class_val not in valid_class:
        errors.append(f"Недопустимое значение '{class_val}' в столбце 'class'. Допустимые значения: {valid_class}.")

    if errors:
        print(f"Строка {row_number}: Обнаружены ошибки:")
        for error in errors:
            print(f"  - {error}")
        return False

    return True


def clean_data(input_file, output_file):
    cleaned_rows = []
    total_rows = 0
    invalid_rows = 0

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row_number, row in enumerate(reader, start=1):
            total_rows += 1
            # Удаление лишних символов и пробелов
            cleaned_row = [value.strip() for value in row]

            # Проверка строки на валидность
            if validate_row(cleaned_row, row_number):
                cleaned_rows.append(cleaned_row)
            else:
                invalid_rows += 1

    # Запись очищенных данных в новый файл
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_rows)

    # Отчет о проделанной работе
    print("\nОтчет о проверке данных:")
    print(f"Всего строк: {total_rows}")
    print(f"Корректных строк: {len(cleaned_rows)}")
    print(f"Некорректных строк: {invalid_rows}")
    print(f"Очищенные данные сохранены в файл: {output_file}")


# Пример использования
input_file = 'data/raw/raw_data.csv'
output_file = 'data/prepared/clean_data.csv'
clean_data(input_file, output_file)