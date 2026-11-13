#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;
    
    if (x < 4) cout << "NO" << endl;
    else if ((x - 2) % 2 == 0) cout << "YES" << endl;
    else cout << "NO" << endl;

    return 0;
}