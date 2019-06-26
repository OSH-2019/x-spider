
#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>
#include <sched.h>
#include <unistd.h>

#include "yijinjing/journal/JournalReader.h"
#include "yijinjing/journal/Frame.hpp"
#include "yijinjing/journal/Timer.h"

#include "yijinjing/journal/JournalWriter.h"
#include "yijinjing/journal/FrameHeader.h"
#include "yijinjing/journal/PageProvider.h"

int main(int argc, char** argv){

	std::string log_folder, journal_folder;
	int freq = 1;
	{
	    std::string filename = "page_engine.json";
		if (argc > 1){
			filename = argv[1];
		}

		if(!boost::filesystem::exists(filename)){
			fmt::print(">>> Page engine configuration file {} does not exist!\n", filename);
			return -1;
		}

		std::ifstream ifs(filename.c_str());
		nlohmann::json conf_j;
		ifs >> conf_j;
		ifs.close();

		
		try{
			nlohmann::json page_engine_j = conf_j["page_engine"];
			log_folder = page_engine_j["log_folder"].get<std::string>();
			journal_folder = page_engine_j["journal_folder"].get<std::string>();
			
			if (page_engine_j.find("frequency") != page_engine_j.end()) {
				freq = page_engine_j["frequency"].get<int>();
				if(freq <= 0) freq = 1;
			}
		}catch(...) {
			fmt::print(">>> The json file {} must contain {'page_engine': dict(log_folder='', journal_folder='')}.\n");
			return -1;
		}
	}

	fmt::print(">>> PageEngine will run with log_folder {}, journal_folder {}, and frequency {}.\n", log_folder, journal_folder, freq);
	if(log_folder.size() > 0 && journal_folder.size() > 0 
		&& ensure_dir_exists(log_folder) && ensure_dir_exists(journal_folder)){

	    yijinjing::PageEngine engine(journal_folder + "/" + "PAGE_ENGINE_COMM", journal_folder + "/" + "TEMP_PAGE", log_folder);

	    engine.set_freq(1);
	    engine.start();
	}else{
		fmt::print(">>> Failed to create log_folder {} or journal_folder {}, please check.\n", log_folder, journal_folder);
		return -1;
	}

    return 0;
}
