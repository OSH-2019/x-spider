
#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>
#include <sched.h>
#include <unistd.h>
#include "yijinjing/journal/JournalReader.h"
#include "yijinjing/journal/FrameHeader.h"
#include "yijinjing/journal/Frame.hpp"
#include "yijinjing/journal/Timer.h"

#include "stat.h"

using yijinjing::JournalReaderPtr;
using namespace yijinjing;

#define KUNGFU_JOURNAL_FOLDER "/tmp/yijinjing-lite/journal/"  /**< where we put journal files */

extern "C" int* reader();
int* reader(){

        int cpu_id_ = 0;
        cpu_set_affinity(cpu_id_);


    //std::vector<string> empty;
    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test", -1, "Client_R");
    
    bool flag = reader->seekTimeJournalByName("test", 0);
    //std::cout<< "seekTimeJournalByName Return Flag:" << flag <<std::endl;
    //getNanoTime();
    

    yijinjing::FramePtr frame;
    //Calculator::print_header();
    int k = 0;
    int *num = new int[20];
    while(1){
        
        frame = reader->getNextFrame();
        if (frame.get() != nullptr)
        {           
            void* data = frame->getData();
            int t;
            sscanf((char *)data,"%d",&t);
            num[k]=t;
        }else break;
        
        ++k;
    }
    return num;
}
