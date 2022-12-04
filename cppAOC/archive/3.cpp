/*
 * Created by Sabrina on 12/2/22.
*/
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

set<char> strToSet (string str) {
    set<char> ans;
    for (int i = 0; i < str.length(); i++) {
        ans.insert(str[i]);
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    ifstream cin("/Users/sabrina/projects_local/AdventOfCode/cppAOC/inputs/3.txt");

    ll N = 300;

    ll ans = 0;

    string bagStr;
    for (int i = 0; i < N/3; i++) {
        map<char, int> counts;
        cin >> bagStr;
        // bag 1
        set<char> bag = strToSet(bagStr);
        for (auto c : bag) {
            counts.insert({c, 1});
        }

        cin >> bagStr;
        // bag 2
        bag = strToSet(bagStr);
        for (auto c : bag) {
            if (counts.count(c) > 0) {
                counts[c] = 2;
            }
            else {
                counts.insert({c, 1});
            }
        }

        cin >> bagStr;
        // bag 2
        bag = strToSet(bagStr);
        for (auto c : bag) {
            if (counts.count(c) > 0) {
                counts[c] ++;
            }
            else {
                counts.insert({c, 1});
            }
        }

        for (auto const& [key, val] : counts) {
            if (val == 3) {
                if (isupper(key)) {
                    ans += key - 38;
                }
                else {
                    ans += key - 96;
                }
//                cout << "\n" << key << "\n";
                break;
            }
        }
    }

    cout << ans;
}