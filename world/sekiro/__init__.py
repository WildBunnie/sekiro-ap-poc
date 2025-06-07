from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification, Location, Region, LocationProgressType, Tutorial
from .Items import item_list, ItemData
from .Locations import location_table, LocationData

class SekiroLocation(Location):
    game: str = "Sekiro"
    data: LocationData

    def __init__(self, player, name, code, parent_region, data):
        self.data = data
        super(SekiroLocation, self).__init__(
            player, name, code, parent_region
        )

class SekiroItem(Item):
    game: str = "Sekiro"
    data: ItemData

    def __init__(self, name, classification, code, player, data):
        self.data = data
        super(SekiroItem, self).__init__(
            name, classification, code, player
        )

class DS2World(World):
    game = "Sekiro"

    item_name_to_id = {item_data.name: item_data.code for item_data in item_list }
    location_name_to_id = { location_data.name: location_data.code for locations in location_table.values() for location_data in locations }

    def create_regions(self):

        regions = {}

        menu_region = self.create_region("Menu")
        self.multiworld.regions.append(menu_region)
        regions["Menu"] = menu_region
    
        for region_name in location_table:
            region = self.create_region(region_name)

            for location_data in location_table[region_name]:
                location = self.create_location(location_data, region)
                region.locations.append(location)

            regions[region_name] = region
            self.multiworld.regions.append(region)
            
        regions["Menu"].connect(regions["Sekiro"])
            

    def create_region(self, name) -> Region:
        return Region(name, self.player, self.multiworld)

    def create_location(self, location_data: LocationData, region) -> SekiroLocation:
        name =  location_data.name
        code = self.location_name_to_id[name]
        location = SekiroLocation(self.player, name, code, region, location_data)
        return location

    def create_items(self):
        pool : list[SekiroItem] = []
        max_pool_size = len(self.multiworld.get_unfilled_locations(self.player))

        for location in self.multiworld.get_unfilled_locations(self.player):
            location_data: LocationData = location.data
            item_data = next((item for item in item_list if item.name == location_data.default_item), None)
            assert item_data, f"location's default item not in item list '{location_data.default_item}'"

            item = self.create_item(item_data)
            pool.append(item)

        self.multiworld.itempool += pool

    def create_item(self, item_data: ItemData) -> SekiroItem:
        name = item_data.name
        code = self.item_name_to_id[name]
        classification = ItemClassification.filler
        return SekiroItem(name, classification, code, self.player, item_data)