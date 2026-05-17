cmake_minimum_required(VERSION 3.17)
project(proj)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(external)

find_package(OpenGL REQUIRED)

set(libs
        ${OPENGL_LIBRARY}
        glfw
        glad
        glm
)
add_executable(${PROJECT_NAME} src/main.cpp
        src/utils/shader_utils.cpp
        src/utils/shader_utils.h
        src/utils/texture.cpp
        src/utils/texture.h)

add_executable(task3_2 src/task3_2.cpp
        src/utils/shader_utils.cpp
        src/utils/shader_utils.h
        src/utils/texture.cpp
        src/utils/texture.h)

target_link_libraries(task3_2 ${libs})

target_include_directories(task3_2 PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/src/utils
        ${CMAKE_CURRENT_SOURCE_DIR}/src/res
)

target_include_directories(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/src/utils
        ${CMAKE_CURRENT_SOURCE_DIR}/src/res
)

target_link_libraries(${PROJECT_NAME} ${libs})

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_SOURCE_DIR}/src/res
        $<TARGET_FILE_DIR:${PROJECT_NAME}>/res
)
