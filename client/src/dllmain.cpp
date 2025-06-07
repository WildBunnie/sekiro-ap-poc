#include "archipelago.h"
#include "game.h"

#include "modengine/extension.h"
#include "spdlog/sinks/stdout_color_sinks.h"

#include <string>
#include <iostream>
#include <cstdint>

#pragma comment(lib, "Crypt32.lib")

void handle_input()
{
    spdlog::info("Archipelago client\n"
        "Type '/connect {SERVER_IP}:{SERVER_PORT} {SLOT_NAME} [password:{PASSWORD}]' to connect to the room\n"
        "Type '/help' for more information\n"
        "-----------------------------------------------------");

	while (true) {
		std::string line;
		std::getline(std::cin, line);

		if (line == "/help") {
			spdlog::info(
				"List of available commands : \n"
				"/help : Prints this help message.\n"
				"!help : Prints the help message related to Archipelago.\n"
				"/connect {SERVER_IP}:{SERVER_PORT} {SLOT_NAME} [password:{PASSWORD}] : Connect to the specified server.\n"
				"/debug on|off : Prints additional debug info");
		}
		else if (line.find("/connect ") == 0) {
			std::string param = line.substr(9);
			int spaceIndex = param.find(" ");
			if (spaceIndex == std::string::npos) {
				spdlog::warn("Missing parameter: make sure to type '/connect {SERVER_IP}:{SERVER_PORT} {SLOT_NAME} [password:{PASSWORD}]'");
			}
			else {
				int passwordIndex = param.find("password:");
				std::string address = param.substr(0, spaceIndex);
				std::string slotName = param.substr(spaceIndex + 1, passwordIndex - spaceIndex - 2);
				std::string password = "";
				if (passwordIndex != std::string::npos)
				{
					password = param.substr(passwordIndex + 9);
				}
                setup_apclient(address, slotName, password);
			}
		}
		else if (line.find("!") == 0) {
			apclient_say(line);
		}
	}
};


void run()
{
    AllocConsole();
    freopen_s((FILE**)stdout, "CONOUT$", "w", stdout);
    freopen_s((FILE**)stdin, "CONIN$", "r", stdin);

    // setup spdlog to print to stdout
	auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
    auto logger = std::make_shared<spdlog::logger>("console", console_sink);
    spdlog::set_default_logger(logger);
    spdlog::set_pattern("[%Y-%m-%d %H:%M:%S.%e] [%^%l%$] %v");
    spdlog::set_level(spdlog::level::debug);

    CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)handle_input, NULL, 0, NULL);

    Sleep(5000);

	init_hooks();

    while (true) {
        apclient_poll();
        Sleep(1000 / 60);
    }
}

class CCore : public modengine::ModEngineExtension {
public:
    CCore(modengine::ModEngineExtensionConnector* connector) : modengine::ModEngineExtension(connector) {};
private:
    void on_attach() override {};
    void on_detach() override {};
    const char* id() override
    {
        return "archipelago";
    }
};

bool modengine_ext_init(modengine::ModEngineExtensionConnector* connector, modengine::ModEngineExtension** extension)
{   
    *extension = new CCore(connector);
    CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)run, NULL, NULL, NULL);
    return true;
}