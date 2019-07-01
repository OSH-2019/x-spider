
#include <iostream>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include "yijinjing/journal/JournalWriter.h"
#include "yijinjing/journal/FrameHeader.h"
#include "yijinjing/journal/Timer.h"
#include "yijinjing/journal/PageProvider.h"

#include "stat.h"
#include <fstream>
#include <sstream>
#include <vector>

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

extern "C" long spdwriter(char* data,int len,short msgType,byte lastFlag,char* jname);
// extern "C" void spdInitJournal(char* dir, char* jname);
extern "C" int spdReadCSV(char* filename, char* jname);

long spdwriter(char* data,int len,short msgType,byte lastFlag,char* jname){
    int cpu_id_ = 1;
    cpu_set_affinity(cpu_id_);
      
    
    JournalWriterPtr writer1 = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, jname, "Client1");
    // JournalWriterPtr writer2 = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test2", "Client2");
        // int len = 10;
        // char* data = new char[len];
        // strncpy(data,"ss",len-1);

        long wtime = getNanoTime();
        writer1->write_frame(data,len+1,msgType,lastFlag);
        // long ntime = getNanoTime();
        // printf("%lu\n",ntime);
        // printf("writer.cpp:%lu\n",wtime);
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

// void spdInitJournal(char* dir, char* jname){
//     JournalWriterPtr writer = yijinjing::JournalWriter::create(KUNGFU_JOURNAL_FOLDER, "test1", "Client1");
//     printf("success\n");
//     return;
//     writer->init(dir,jname);
// }

//一定要保证数据格式为"char*,short\n"
int spdReadCSV(char* filename, char* jname){
    std::ifstream inFile(filename, std::ios::in);
	std::string lineStr;
	std::vector<std::vector<std::string> > strArray;
    char* data = new char[100];
    short msgType = 0;
    long wtime = 0;
    int length = 0;
	while (getline(inFile, lineStr,','))
	{
		// 打印整行字符串
        strcpy(data,lineStr.c_str());
        length = strlen(data);
        getline(inFile,lineStr);
        msgType=(short)std::stoi(lineStr);
        wtime = spdwriter(data,length,msgType,0,jname);
		// 存成二维表结构
		// std::stringstream ss(lineStr);
		// std::string str;
		// std::vector<std::string> lineArray;
		// // 按照逗号分隔
		// while (getline(ss, str, ','))
		// 	lineArray.push_back(str);
		// strArray.push_back(lineArray);
	}
    printf("Write CSV To YJJ Successfully!\n");
	return 0;
}