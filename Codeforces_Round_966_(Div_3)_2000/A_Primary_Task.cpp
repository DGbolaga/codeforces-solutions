#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int arg;
    cin >> arg;

    while(arg--) {
        int x;
        cin >> x;

        if ((x >= 102 && x <= 109) || (x >= 1010 && x <= 1099) || (x >= 10100 && x <= 10999)){
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}