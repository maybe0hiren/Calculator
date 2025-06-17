#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <iostream>

std::vector <float> numbers;
std::vector <char> operations;
float answer = 0;
float returnValue;

void subtraction(int i){
    numbers[i+1] = (-1)*numbers[i+1];
    operations[i] = '+';
}

void division(int i){
    numbers[i+1] = 1/numbers[i+1];
    operations[i] = '*';
}

void multiplication(int i){
    while (operations[i] == '*'){
        numbers[i+1] *= numbers[i];
        numbers[i] = 0;
        operations[i] = '+';
        i++;
    }
}

float fillVectors(std::vector <float> pythonNumbList, std::vector <char> pythonCharList){
    numbers.clear();
    operations.clear();
    for (float x: pythonNumbList){
        numbers.push_back(x);
    }
    for (char x: pythonCharList){
        operations.push_back(x);
    }
    for (int i = 0; i<operations.size(); i++){
        if(operations[i] == '-'){
            subtraction(i);
        }
        else if(operations[i] == '/'){
            division(i);
        }
    }
    for(int i = 0; i<operations.size(); i++){
        if(operations[i] == '*'){
            multiplication(i);
        }
    }
    for(int i = 0; i<numbers.size(); i++){
        answer += numbers[i];
    }
    returnValue = answer;
    answer = 0;
    return returnValue;
}

void mValueTransfer(float mValue){
    answer = mValue;
}



PYBIND11_MODULE(logic, m){
    m.def("fillVectors", &fillVectors, "fillVectors"); 
    m.def("mValueTransfer", &mValueTransfer, "mValueTransfer");
}