
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

extern "C" int spdreader();
int spdreader(){

        int cpu_id_ = 0;
        cpu_set_affinity(cpu_id_);

    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", -1, "Client_R");
    // JournalReaderPtr reader2 = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER,"test2",-1,"Client_R2");

    bool flag = reader->seekTimeJournalByName("test1", 1561603421415942724);
    yijinjing::FramePtr frame;
    for(int i=0;i<100;i++){
        frame = reader->getNextFrame();
        if(frame.get()!=nullptr)
        {
            short msg_type = frame->getMsgType();
            void* data = frame->getData();
            int len = frame->getDataLength();
            printf("%d %s %d",msg_type,data,len);
        }
        else{
            printf("error");
        }
    }

    // bool flag2 = reader2->seekTimeJournalByName("test2", 1561603421415942724);
    // yijinjing::FramePtr frame2;
    // for(int i=0;i<100;i++){
    //     frame2 = reader2->getNextFrame();
    //     if(frame2.get()!=nullptr)
    //     {
    //         short msg_type = frame2->getMsgType();
    //         void* data = frame2->getData();
    //         int len = frame2->getDataLength();
    //         printf("%d %s %d",msg_type,data,len);
    //     }
    //     else{
    //         printf("error");
    //     }
    // }

    return 0;


    // getNanoTime();
    

    // yijinjing::FramePtr frame;
    // Calculator::print_header();
    // int k = 0;
    // while(k <= 10){
    //     Calculator cal;
    //     int count = 0;
    //     while (count < 8000)
    //     {
    //         frame = reader->getNextFrame();
    //         if (frame.get() != nullptr)
    //         {
    //             short msg_type = frame->getMsgType();            
    //             void* data = frame->getData();
    //             int64_t msg_time = frame->getNano();
    //             int len = frame->getDataLength();

    //             if(msg_type == 11){
    //                 int64_t cur_time = getNanoTime();
                    
    //                 cal.update(cur_time - msg_time);
    //                 ++count;
    //             }
    //         }
    //     }
    //     cal.print();
        
    //     ++k;
    // }
    // Calculator::print_footer();
}
