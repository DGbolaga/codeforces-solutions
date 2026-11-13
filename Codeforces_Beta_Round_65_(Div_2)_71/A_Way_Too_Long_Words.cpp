#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--) {

        string x;
        cin >> x;

        if (x.size() <= 10) cout << x << endl;
        else cout << x[0] << to_string(x.size() - 2) << x[x.size() - 1] << endl;
    }

    return 0;
}