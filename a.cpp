// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c; cin >> a >> b >> c;
	if(a + b == c){
		cout << "Try again, Bob" << endl;
	} else {
		cout << "Good job, Bob!" << endl;
	}
}
