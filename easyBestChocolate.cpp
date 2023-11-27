#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    pair<int, int> vals[n];
    for (int i = 0; i < n; i++) {
        int f, b;
        cin >> f >> b;
        vals[i] = make_pair(i + 1, f * 4 + b);
    }

    sort(vals, vals + n, [](pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;
    });

    vector<int> ans(k);
    for (int i = 0; i < k; i++) {
        ans[i] = vals[i].first;
    }

    sort(ans.begin(), ans.end());
    for (int i = 0; i < k; i++) {
        cout << ans[i] << " ";
    }
}