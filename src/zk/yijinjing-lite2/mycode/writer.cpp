
#include <iostream>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include "yijinjing/journal/JournalWriter.h"
#include "yijinjing/journal/FrameHeader.h"
#include "yijinjing/journal/Timer.h"
#include "yijinjing/journal/PageProvider.h"

#include "stat.h"

using yijinjing::JournalWriterPtr;
using namespace yijinjing;


#define KUNGFU_JOURNAL_FOLDER "/tmp/yijinjing-lite/journal/"  /**< where we put journal files */


// extern "C"  int mywrite(char* data, int len, short msgType, byte lastFlag)
// int mywrite(char* data, int len, short msgType, byte lastFlag){

// int main (int argc, char* argv[]){



// int createWriter(){
//     int cpu_id_ = 1;
//     cpu_set_affinity(cpu_id_);
      
    
//     JournalWriterPtr writer_ = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test", "Client");
//     return 0;
// }

extern "C" int spdwriter(char* data,int len,short msgType,byte lastFlag);
int spdwriter(char* data,int len,short msgType,byte lastFlag){
    int cpu_id_ = 1;
    cpu_set_affinity(cpu_id_);
      
    
    JournalWriterPtr writer1 = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test1", "Client1");
    // JournalWriterPtr writer2 = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test2", "Client2");
        // int len = 10;
        // char* data = new char[len];
        // strncpy(data,"ss",len-1);

        long wtime = getNanoTime();
        writer1->write_frame(data,len,msgType,lastFlag);
        // long ntime = getNanoTime();
        // printf("%lu\n",ntime);
        return wtime;

//     int len = 10;
//     if(argc > 1){
//     	len = atoi(argv[1]);
//     }
//     if(len <= 0) len = 10;
//     std::cout<<"DataLength:"<<len<<std::endl;

//     char * data = new char[len];
//     data[len-1]=0;
//     strncpy(data, "This is a test", len - 1);

// 	Calculator::print_header();
// 	int k = 0;
//     while(k <= 15){
        
//         ///data += 2;
//         Calculator cal;
        
//         int count = 4000;
//         for(int i = 0; i < count; ++i){
//             int64_t nano = writer_->write_frame(data, len, 11, 0);
//             int64_t cur_time = getNanoTime() - nano;
            
//             cal.update(cur_time);
            
//             usleep(1);
//         }

//         cal.print();
//         ++k;
//         usleep(yijinjing::MICROSECONDS_PER_SECOND);
//     }
    
//     Calculator::print_footer();

}
