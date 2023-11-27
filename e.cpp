#include <bits/stdc++.h>

using namespace std;
vector<pair<int, int>> adj[52];

int main() {
    int n; cin >> n;

    string trash; getline(cin, trash);
    for (int i = 0; i < n; i++){
        string cur; getline(cin, cur);
        // split by space into a vector

        vector<string> split;
        istringstream iss(cur);
        for(string s; iss >> s; ) split.push_back(s);

        if (split.size() == 3) {
            int a = split[0][0] > 'Z' ? split[0][0] - 'a' + 26 : split[0][0] - 'A';
            int b = split[2][0] > 'Z' ? split[2][0] - 'a' + 26 : split[2][0] - 'A';

            adj[a].push_back(b);
            adj[b].push_back(a);
        }
    }
}