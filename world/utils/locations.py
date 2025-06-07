import csv
from enum import IntEnum
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class ItemCategory(IntEnum):
    NONE = -1
    WEAPON = 0
    ARMOR = 268435456
    GOODS = 1073741824

id_to_name = {}

def remove_weird_symbols(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s.,;:!?\'"()\[\]{}<>/@&+\-_\u4e00-\u9fff]', '', text)

with open("data/TitleGoods.fmgmerge.txt", encoding="utf-8") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.startswith("###"):
        ids = [int(match) for match in re.findall(r"###(\d+)", line)]
        if i + 1 < len(lines):
            raw_name = lines[i + 1].strip()
            clean_name = remove_weird_symbols(raw_name)

            # Assign unique names for each ID on this line
            for idx, skill_id in enumerate(ids):
                if idx == 0:
                    unique_name = clean_name
                else:
                    unique_name = f"{clean_name} ({idx + 1})"
                id_to_name[skill_id] = unique_name
        i += 2
    else:
        i += 1

# Collect matching entries
location_data_entries = []

with open("data/ItemLotParam.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        code = int(row["getItemFlagId"])
        if code == -1: continue
        name = row["Name"]
        
        item_name = None
        for i in range(1, 9):
            item_id = int(row["lotItemId0" + str(i)])
            drop_chance = int(row["lotItemBasePoint0" + str(i)])
            category = int(row["lotItemCategory0" + str(i)])
            if drop_chance != 1000 or item_id == 0 or category != ItemCategory.GOODS or item_id not in id_to_name:
                continue
            item_name = id_to_name[item_id]
            break
        
        if item_name:
            location_data_entries.append((code, name, item_name))

def remove_weird_symbols(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s.,;:!?\'"()\[\]{}<>/@&+-_]', '', text)

# Sort and print
for code, name, item_name in sorted(location_data_entries, key=lambda x: x[0]):
    print(f'        LocationData({code}, "{remove_weird_symbols(name.split("--")[0]).strip()}", "{item_name}"),')
