import csv
import os
from typing import Dict, List


def load_csv_data(file_path: str) -> List[Dict[str, str]]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def parse_gender(gender_str: str) -> str:
    gender_map = {
        'female': 'женского пола',
        'male': 'мужского пола'
    }
    return gender_map.get(gender_str.lower(), 'не указан')


def format_device(device_str: str) -> str:
    device_map = {
        'mobile': 'мобильного',
        'desktop': 'настольного',
        'tablet': 'планшетного'
    }
    return device_map.get(device_str.lower(), device_str)


def create_customer_description(row: Dict[str, str]) -> str:
    full_name = row['name']
    gender = parse_gender(row['sex'])
    age = row['age']
    device = format_device(row['device_type'])
    browser = row['browser']
    amount = row['bill']
    region = row['region']

    description = (
        f"Пользователь {full_name} {gender}, {age} лет "
        f"совершил покупку на {amount} у.е. с {device} браузера {browser}. "
        f"Регион, из которого совершалась покупка: {region}."
    )
    return description


def generate_descriptions(data: List[Dict[str, str]]) -> List[str]:
    return [create_customer_description(row) for row in data]


def save_to_txt(descriptions: List[str], output_path: str):
    with open(output_path, mode='w', encoding='utf-8') as file:
        file.write('\n'.join(descriptions))


def main(input_path: str, output_path: str):
    data = load_csv_data(input_path)
    descriptions = generate_descriptions(data)
    save_to_txt(descriptions, output_path)
    print(f"Обработка завершена. Результат сохранён в: {output_path}")


if __name__ == '__main__':
    input_csv = r"C:\Users\kukui\Downloads\web_clients_correct (1).csv"
    output_txt = r"C:\Users\kukui\Downloads\customer_descriptions.txt"
    main(input_csv, output_txt)
