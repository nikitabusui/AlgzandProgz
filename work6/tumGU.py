import json
import csv

purchase_categories = {}

with open('resources/purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        user_id = data.get("user_id")
        category = data.get("category")
        if user_id and category:
            purchase_categories[user_id] = category

with open('resources/visit_log__1_.csv', encoding='utf-8') as visits, \
     open('resources/funnel.csv', 'w', encoding='utf-8', newline='') as out:

    writer = csv.writer(out)
    writer.writerow(['user_id', 'source', 'category'])

    reader = csv.reader(visits)
    header = next(reader)

    for user_id, source in reader:
        if user_id in purchase_categories:
            writer.writerow([user_id, source, purchase_categories[user_id]])