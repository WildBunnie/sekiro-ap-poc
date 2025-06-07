#include "game.h"

#include "archipelago.h"

#include "spdlog/spdlog.h"
#include "minhook.h"

#include <cstdint>
#include <windows.h>

uintptr_t base_address;

// credit for ItemGib goes to the people over at the Shared Souls Ghidra Server
typedef void(*item_gib_t)(uintptr_t, GiveItemList*, uintptr_t, uint8_t, uintptr_t, uint8_t);
// credit for flag stuff goes to SoulSplitter by FrankvdStam
typedef uintptr_t(*call_set_flag)(uintptr_t, int32_t, int32_t);

item_gib_t original_item_gib;
call_set_flag original_call_set_flag;

bool give_next_item = true;

void detour_item_gib(uintptr_t map_item_man, GiveItemList* item_list, uintptr_t param_3, uint8_t param_4, uintptr_t param_5, uint8_t param_6)
{
    for (int i = 0; i < item_list->amount; i++) {
        GiveItemEntry* item = &item_list->items[i];
        spdlog::info("just got: {} x{}", item->id, item->quantity);
    }

    if (give_next_item) {
        original_item_gib(map_item_man, item_list, param_3, param_4, param_5, param_6);
    }
    else {
        give_next_item = true;
    }

    return;
}

uintptr_t detour_call_set_flag(uintptr_t param_1, int32_t flag, int32_t area_code_maybe)
{
    spdlog::info("flag was set: {} {}", flag, area_code_maybe);
    if (check_location(flag)) {
        give_next_item = false;
    }
    return original_call_set_flag(param_1, flag, area_code_maybe);
}

void give_item(GiveItemList item_list)
{
    item_gib_t item_gib = (item_gib_t)(base_address + 0x91C970);

    GiveItemStruct item_struct{};
    item_struct.item_list = item_list;

    uint8_t idk[0x200]{}; // its just an empty space in memory :shrug:

    uintptr_t map_item_man = *(uintptr_t*)(base_address + 0x3D6CDC0);

    item_gib(map_item_man, &item_struct.item_list, reinterpret_cast<uintptr_t>(&item_struct), 0, reinterpret_cast<uintptr_t>(idk), 0);
}

void init_hooks()
{
    base_address = (uintptr_t)GetModuleHandleA("sekiro.exe");

    MH_Initialize();

    if (MH_CreateHook((LPVOID)(base_address + 0x91C970), &detour_item_gib, (LPVOID*)&original_item_gib) != MH_OK) {
        spdlog::error("error creating hook");
    }
    if (MH_CreateHook((LPVOID)(base_address + 0x6AAAB0), &detour_call_set_flag, (LPVOID*)&original_call_set_flag) != MH_OK) {
        spdlog::error("error creating hook");
    }

    MH_EnableHook(MH_ALL_HOOKS);
}
