#include <iostream>
#include <vector>
using namespace std;
 
void solve() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (min(a, c) >= min(b, d)) cout << "Gellyfish" << endl;
    else cout << "Flower" << endl;
}

int main() {
    int n; cin >> n;
    while (n--) {
        solve();
    }
    return 0;
}