if((BUILD_CONVERT OR BUILD_IFCPYTHON) AND WITH_OPENCASCADE)
    add_subdirectory(schema)
    get_property(geometry_serializer_libraries GLOBAL PROPERTY geometry_serializer_libraries)
    message(STATUS "geometry_serializer_libraries: ${geometry_serializer_librarie}")
    add_library(geometry_serializer OBJECT Serialization.cpp)
    target_link_libraries(geometry_serializer ${geometry_serializer_libraries})
    set(IFCOPENSHELL_LIBRARIES ${IFCOPENSHELL_LIBRARIES} geometry_serializer ${geometry_serializer_libraries})


    file(GLOB IFCGEOM_SERIALIZATION_H_FILE *.h)
    install(FILES ${IFCGEOM_SERIALIZATION_H_FILE}
        DESTINATION ${INCLUDEDIR}/ifcgeom/Serialization
    )

    # install(TARGETS geometry_serializer ${geometry_serializer_libraries}
    #     ARCHIVE DESTINATION ${LIBDIR}
    #     LIBRARY DESTINATION ${LIBDIR}
    #     RUNTIME DESTINATION ${BINDIR}
    # )
endif()
