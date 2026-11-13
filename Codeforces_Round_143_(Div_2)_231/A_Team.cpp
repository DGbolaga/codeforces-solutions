#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    // keep count of strings that have only 1 '0';
    int c = 0;
    while (n--) {
        
        string x;
        getline(cin, x);

        int n0 = 0;
        for (char y: x) {
            if (y == '0') n0++;
            if (n0 > 1) break;
        }
        
        if (n0 <= 1) c++;
    }

    cout << c << endl;

    return 0;
}