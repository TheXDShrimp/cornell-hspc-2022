#include <bits/stdc++.h>

using namespace std;

int main(){
    string input; cin >> input;
    string digits = "0123456789";
    int plus = 0, equals = 0;
    for(int i = 0; i < input.length(); i++){
        if(input[i] == '+') plus = i;
        if(input[i] == '=') equals = i;
    }
    int cnt = 0;
    do {
        string num1 = "", num2 = "", num3 = "";
        for(int j = 0; j < plus; j++) num1 += digits[input[j] - '0'];
        for(int j = plus + 1; j < equals; j++) num2 += digits[input[j] - '0'];
        for(int j = equals + 1; j < input.length(); j++) num3 += digits[input[j] - '0'];
        int n1 = stoi(num1), n2 = stoi(num2), n3 = stoi(num3);
        if(n1 + n2 == n3){
            string ans = "0000000000";
            for(int j = 0; j < ans.length(); j++){
                ans[digits[j] - '0'] = char(j + '0');
            }
            cout << ans << endl;
            break;
        }
    } while(next_permutation(digits.begin(), digits.end()));
}