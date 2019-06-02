
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


extern "C" void writer(int sum, int *dat);
void writer(int sum, int *dat){
    
        int cpu_id_ = 1;
        cpu_set_affinity(cpu_id_);

    //getNanoTime();
    JournalWriterPtr writer_ = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test", "Client");
    int len = 10;
    /*
    
    if(argc > 1){
    	len = atoi(argv[1]);
    }
    if(len <= 0) len = 10;
    
    std::cout<<"DataLength:"<<len<<std::endl;
*/
    char * data = new char[len];
    data[len-1]=0;

	//Calculator::print_header();
	int k = 0;
    while(k < sum){
        
        ///data += 2;
        //Calculator cal;
        sprintf(data,"%d", dat[k]*1000);
        writer_->write_frame(data, len, 11, 0);
        ++k;
    }
    
    //Calculator::print_footer();

}
