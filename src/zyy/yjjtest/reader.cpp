
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


using yijinjing::JournalReaderPtr;
using namespace yijinjing;

#define KUNGFU_JOURNAL_FOLDER "/tmp/yijinjing-lite/journal/"  /**< where we put journal files */



int main(){

    std::vector<string> empty;
    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test", -1, "Client_R");
    
    getNanoTime();

    yijinjing::FramePtr frame;
    int k = 0;
    int64_t Time=0;
    while(k <= 10){
        frame = reader->getNextFrame();
        
        if (frame.get() != nullptr)
        {
            short msg_type = frame->getMsgType();            
            void* data = frame->getData();
            int64_t msg_time = frame->getNano();
            int len = frame->getDataLength();
            byte last_flag = frame->getLastFlag();
            
            if(Time==0)
                Time = msg_time;
            if(msg_type == 11){
                
                int64_t cur_time = getNanoTime();
                int num=atoi(data);
                printf("%d\n",num);
            }
        }
        
        ++k;
    }

    reader->jumpStart(Time);
    printf("\n");


    while(k <= 10){
        frame = reader->getNextFrame();
        
        if (frame.get() != nullptr)
        {
            short msg_type = frame->getMsgType();            
            void* data = frame->getData();
            int64_t msg_time = frame->getNano();
            int len = frame->getDataLength();
            byte last_flag = frame->getLastFlag();
            
            if(msg_type == 11){
                
                int64_t cur_time = getNanoTime();
                int num=atoi(data);
                printf("%d\n",num);
            }
        }
        
        ++k;
    }
}
