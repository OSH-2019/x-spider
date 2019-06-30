
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
#include <fstream>
#include <sstream>


using yijinjing::JournalReaderPtr;
using namespace yijinjing;

#define KUNGFU_JOURNAL_FOLDER "/tmp/yijinjing-lite/journal/"  /**< where we put journal files */

extern "C" char* spdReadSingleData(long rtime,int a);
extern "C" short spdReadSingleMsgType(long rtime,int a);
extern "C" void spdPrintAllData(long startTime,int a);
extern "C" int spdConvertAllToCSV(long startTime,char* fileName);


char* spdReadSingleData(long rtime,int a){
        //  printf("readdata.cpp:%lu\n",rtime);
        //  printf("nowTime:%lu\n",getNanoTime());
        int cpu_id_ = 0;
        cpu_set_affinity(cpu_id_);

    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", -1, "Client_R");
    // JournalReaderPtr reader2 = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER,"test2",-1,"Client_R2");

    bool flag = reader->seekTimeJournalByName("test1", rtime);
    yijinjing::FramePtr frame;

    frame = reader->getNextFrame();
    // data length max = 100;
    char * data = new char[100];
    
    if(frame.get()!=nullptr)
    {
        data = (char*)frame->getData();
    }
    else{
        printf("Data Not Found");
    }   
   
    return data;
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

short spdReadSingleMsgType(long rtime, int a){
    int cpu_id_ = 0;
        cpu_set_affinity(cpu_id_);

    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", -1, "Client_R");
    // JournalReaderPtr reader2 = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER,"test2",-1,"Client_R2");

    bool flag = reader->seekTimeJournalByName("test1", rtime);
    yijinjing::FramePtr frame;

    frame = reader->getNextFrame();
    short msgType = 0;
    
    if(frame.get()!=nullptr)
    {
        msgType = frame->getMsgType();
    }
    else{
        printf("MsgType Not Found");
    }   
    return msgType;
}

long spdGetNextFrame(long time){
    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", time, "Client_R");
    
    yijinjing::FramePtr frame;
    frame = reader->getNextFrame();
}

void spdPrintAllData(long startTime, int a){
    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", startTime, "Client_R");
    yijinjing::FramePtr frame;
    frame = reader->getNextFrame();

    char* data = new char[100];
    short msgType = 0;
    while(frame.get()!=nullptr)
        {
            data = (char*)frame->getData();
            msgType = frame->getMsgType();
            printf("data:%s    msgType:%d\n",data,msgType);
            frame = reader->getNextFrame();
        }
    
    printf("End of Print Data\n");
}

int spdConvertAllToCSV(long startTime,char* fileName){
    JournalReaderPtr reader = yijinjing::JournalReader::create(KUNGFU_JOURNAL_FOLDER, "test1", startTime, "Client_R");
    yijinjing::FramePtr frame;
    frame = reader->getNextFrame();
    
    char* data = new char[100];
    short msgType = 0;

    std::ofstream outFile;
    outFile.open(fileName,std::ios::out);
    
    while(frame.get()!=nullptr)
        {
            data = (char*)frame->getData();
            msgType = frame->getMsgType();
            outFile<<data<<", "<<msgType<<std::endl;
            frame = reader->getNextFrame();
        }
    
    outFile.close();
    printf("End of Convert To CSV\n");
    return 0;
}