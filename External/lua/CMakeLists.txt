CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

PROJECT(lua)

IF(WIN32)
	ADD_DEFINITIONS(-D_CRT_SECURE_NO_WARNINGS)
ENDIF()

FILE(GLOB LIBLUA_INC source/*.h)
FILE(GLOB LIBLUA_SRC source/*.c)

ADD_LIBRARY(lua STATIC ${LIBLUA_SRC})

INSTALL(TARGETS lua
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
INSTALL(FILES ${LIBLUA_INC}
	DESTINATION include)
