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

with open("data/EquipParamGoods.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        code = int(row["ID"])
        if code not in id_to_name: continue
        name = id_to_name[code]

        print(f'    ItemData({code}, "{name}"),')

