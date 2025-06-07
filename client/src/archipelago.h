#pragma once

#include <string>

void setup_apclient(std::string URI, std::string slot_name, std::string password);
void apclient_poll();
bool is_apclient_connected();
void apclient_say(std::string message);
bool check_location(int32_t location);