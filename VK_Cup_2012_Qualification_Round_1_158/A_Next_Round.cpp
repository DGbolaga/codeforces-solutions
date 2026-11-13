#include <iostream>
#include <vector>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;

    vector<int> args(x);
    int res = 0;
    int i = 0;
    while (i < x) {
        cin >> args[i];
        i++;
    }
    
    for (int i = 0; i < x; i++) {
        if (args[i] >= args[y-1] && args[i] > 0) res++;
    }
    cout << res << endl;
    return 0;
}