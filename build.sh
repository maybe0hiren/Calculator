c++ -O3 -Wall -shared -std=c++11 -fPIC \
    $(python3 -m pybind11 --includes) \
    logic.cpp -o logic$(python3-config --extension-suffix)