#include <bits/stdc++.h>

using namespace std;

int main() {
    int x, y, r;
    cin >> x >> y >> r;

    int dx, dy;
    cin >> dx >> dy;

    double d = sqrt((dx - x) * (dx - x) + (dy - y) * (dy - y));

    if (d < r) {
        cout << 0 << endl;
        return 0;
    }
    
    
    double cx = x + r * (dx - x) / d, cy = y + r * (dy - y) / d;
    cout << cx << " " << cy << endl;
    cout << (abs(dx - cx) + abs(dy - cy)) << endl;
}