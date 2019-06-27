# Install script for directory: /home/hubert/projects/yijinjing-lite2/include/yijinjing/journal

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/yijinjing/journal" TYPE FILE FILES
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/Frame.hpp"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/FrameHeader.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/Journal.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/JournalHandler.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/JournalReader.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/JournalWriter.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/Page.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/PageUtil.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/PageHeader.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/PageProvider.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/IJournalVisitor.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/Timer.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/PageCommStruct.h"
    "/home/hubert/projects/yijinjing-lite2/include/yijinjing/journal/PageSocketStruct.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/hubert/projects/yijinjing-lite2/build/libjournal.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so"
         OLD_RPATH "/home/hubert/tools/boost_1_68_0/stage/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libjournal.so")
    endif()
  endif()
endif()

