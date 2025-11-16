import json
import csv

# 1. Загружаем данные о покупках в словарь user_id -> category
purchase_categories = {}

with open('resources/purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        user_id = data.get("user_id")
        category = data.get("category")
        if user_id and category:
            purchase_categories[user_id] = category

# 2. Построчная обработка visit_log.csv и запись funnel.csv
with open('resources/visit_log__1_.csv', encoding='utf-8') as visits, \
     open('resources/funnel.csv', 'w', encoding='utf-8', newline='') as out:

    writer = csv.writer(out)
    writer.writerow(['user_id', 'source', 'category'])  # заголовок

    reader = csv.reader(visits)
    header = next(reader)  # пропускаем заголовок visit_log.csv

    for user_id, source in reader:    # ожидаемый формат: user_id,source
        if user_id in purchase_categories:
            writer.writerow([user_id, source, purchase_categories[user_id]])