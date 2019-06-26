
add_executable(writer writer.cpp)
TARGET_LINK_LIBRARIES(writer paged journal)

add_executable(reader reader.cpp)
TARGET_LINK_LIBRARIES(reader paged journal)

add_executable(yjj_page_service page_service.cpp)
TARGET_LINK_LIBRARIES(yjj_page_service paged journal)

INSTALL(TARGETS yjj_page_service  DESTINATION "bin/")

ADD_SUBDIRECTORY(../include/yijinjing/journal)
ADD_SUBDIRECTORY(../include/yijinjing/paged)
ADD_SUBDIRECTORY(../include/yijinjing/utils)