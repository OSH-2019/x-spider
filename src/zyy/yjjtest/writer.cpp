#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include "yijinjing/journal/JournalWriter.h"
#include "yijinjing/journal/FrameHeader.h"
#include "yijinjing/journal/Timer.h"
#include "yijinjing/journal/PageProvider.h"

using yijinjing::JournalWriterPtr;
using namespace yijinjing;


#define KUNGFU_JOURNAL_FOLDER "/tmp/yijinjing-lite/journal/"  /**< where we put journal files */



int main(int argc, char *argv[]){

    getNanoTime();
    JournalWriterPtr writer_ = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test", "Client");


    int len = 20;
    if(argc > 1){
    	len = atoi(argv[1]);
    }
    if(len <= 0) len = 10;
    std::cout<<"DataLength:"<<len<<std::endl;

    char * data = new char[len];
    data[len-1]=0;
    //strncpy(data, "This is a test", len - 1);

	int k = 0;
    srand(time(NULL));
    while(k <= 15){
        itoa(rand(),data,10);
        writer_->write_frame(data, len, 11, 0);
        ++k;
        //usleep(yijinjing::MICROSECONDS_PER_SECOND);
    }

}
