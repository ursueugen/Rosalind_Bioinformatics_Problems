// Solved by implementing recurrence Fn = Fn-1 + k*Fn-2
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

const int n=36;

int k=5;

//string myText;
//vector<string> numbers;

int main() {

    //ifstream MyFile("problem_data.txt");
    //getline(MyFile, myText, ' ');
    //numbers = atoi( myText.c_str() );
    //cout << numbers;
    
    //int n = numbers[0];
    //int k = numbers[1];
    int F[n];

    for (int i=0; i<=n-1; i++) {
        if ((i == 0) or (i == 1)) {
            F[i] = 1;
        }
        else {
            F[i] = F[i-1] + F[i-2]*k;
        };
    };
    cout << F[n-1] << "\n";
};