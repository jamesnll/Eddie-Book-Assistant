# For more information about build system see
# https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
# The following five lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.5)

# Include components folder
set(EXTRA_COMPONENT_DIRS components components/secrets components/wifi components/http components/queue_wrapper components/output components/stream_buf components/minimp3)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(ESP32)