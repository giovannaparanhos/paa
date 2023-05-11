#include <iostream>
using namespace std;

class Calculate{

    //Access modifiers
    public: 
        //data member
        int num1 =  50;
        int num2 = 30;

        // member function
        int addition() {
            int result = num1 + num2;
            cout << result << endl;
        }
};

int main() {

    //object declaration
    Calculate add;
    //member function calling
    add.addition();

    return 0;
}