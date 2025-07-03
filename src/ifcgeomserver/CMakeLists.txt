find_package(Boost COMPONENTS chrono REQUIRED)

file(GLOB CPP_FILES *.cpp)
file(GLOB H_FILES *.h)
set(SOURCE_FILES ${CPP_FILES} ${H_FILES})
add_executable(IfcGeomServer ${SOURCE_FILES})
target_link_libraries(IfcGeomServer IfcGeom)

# if((NOT WIN32) AND BUILD_SHARED_LIBS)
#     SET_INSTALL_RPATHS(IfcGeomServer "${IFCOPENSHELL_LIBRARY_DIR};${OCC_LIBRARY_DIR};${Boost_LIBRARY_DIRS}")
# endif()

install(TARGETS IfcGeomServer
    ARCHIVE DESTINATION ${LIBDIR}
    LIBRARY DESTINATION ${LIBDIR}
    RUNTIME DESTINATION ${BINDIR}
)
