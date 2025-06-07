#pragma once
#include <cstdint>

typedef enum {
    CATEGORY_NONE = -1,
    CATEGORY_WEAPON = 0x0000,
    CATEGORY_ARMOR = 0x1000,
    CATEGORY_GOODS = 0x4000
} ItemCategory;

typedef struct {
    int16_t id;
    int16_t category;
    int32_t quantity;
    int32_t durability;
    int8_t padding[4];
} GiveItemEntry;

typedef struct {
    int32_t amount;
    GiveItemEntry items[6];
} GiveItemList;

typedef struct {
    int8_t idk[0x10];
    GiveItemList item_list;
} GiveItemStruct; // no idea what this actually is

void give_item(GiveItemList item_list);
void init_hooks();
