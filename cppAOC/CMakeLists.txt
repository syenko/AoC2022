cmake_minimum_required(VERSION 3.23)
project(AdventOfCode)

set(CMAKE_CXX_STANDARD 14)

include_directories(/usr/local/include)

add_executable(Day2 archive/2.cpp)
add_executable(day22 archive/2p2.cpp)
add_executable(3 archive/3.cpp)