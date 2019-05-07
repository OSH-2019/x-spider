cmake_minimum_required(VERSION 3.1)
project(myexecutor)

add_subdirectory(tasklib)

add_executable(myexecutor
              myexecutor.cpp)

target_include_directories(myexecutor PUBLIC ${CBOR_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_link_libraries (myexecutor tasklib ${CBOR_LIBRARIES} pthread)