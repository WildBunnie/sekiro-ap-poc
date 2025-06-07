#include "archipelago.h"
#include "game.h"

#include "apclient.hpp"
#include "apuuid.hpp"
#include "spdlog/spdlog.h"

using nlohmann::json;

enum ItemsHandling {
	NO_ITEMS = 0b000,
	OTHER_WORLDS = 0b001,
	OUR_WORLD = 0b010,
	STARTING_INVENTORY = 0b100,
};

APClient* ap;

void setup_apclient(std::string URI, std::string slot_name, std::string password)
{
	std::string uuid = ap_get_uuid("uuid");

	ap = new APClient(uuid, "Sekiro", URI);

	ap->set_room_info_handler([slot_name, password]() {
		int items_handling = ItemsHandling::OTHER_WORLDS | ItemsHandling::OUR_WORLD | ItemsHandling::STARTING_INVENTORY;
		APClient::Version ap_client_version = { 0, 6, 1 };
		ap->ConnectSlot(slot_name, password, items_handling, {}, ap_client_version);
	});

	ap->set_slot_connected_handler([](const json& data) {
		spdlog::debug("received slot data: {}", data.dump());
	});

	ap->set_items_received_handler([](const std::list<APClient::NetworkItem>& received_items) {
		auto it = received_items.begin();
		while (it != received_items.end()) {
			GiveItemList list;
			list.amount = 0;

			for (int i = 0; i < 6 && it != received_items.end(); ++i, ++it) {
				list.items[i].id = it->item;
				list.items[i].category = CATEGORY_GOODS;
				list.items[i].quantity = 1;
				list.items[i].durability = -1;
				list.amount++;
			}

			give_item(list);
		}
	});

	ap->set_print_handler([](const std::string& msg) {
		spdlog::info(msg);
	});

	ap->set_print_json_handler([](const std::list<APClient::TextNode>& msg) {
		auto message = ap->render_json(msg, APClient::RenderFormat::TEXT);
		spdlog::info(message);
	});
}

void apclient_poll()
{
	if (ap) ap->poll();
}

bool is_apclient_connected()
{
	return ap && ap->get_state() == APClient::State::SLOT_CONNECTED;
}

void apclient_say(std::string message)
{
	if (ap && is_apclient_connected()) {
		ap->Say(message);
	}
}

bool check_location(int32_t location)
{
	if (ap && is_apclient_connected()) {
		std::set<int64_t> missing_locations = ap->get_missing_locations();

		if (ap->get_missing_locations().contains(location)) {
			std::list<int64_t> locations = { location };
			return ap->LocationChecks(locations);
		}
	}
	return false;
}