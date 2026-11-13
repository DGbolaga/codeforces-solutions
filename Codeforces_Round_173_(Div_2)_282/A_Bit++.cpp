#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int res = 0;
    while (n--){
        string x;
        cin >> x;

        if (x == "X++" || x == "++X") res++;
        else res--;
    }
    cout << res << endl;

    return 0;
}