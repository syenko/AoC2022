/*
 * Created on 12/1/22
*/
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    ifstream cin("/Users/sabrina/projects_local/AdventOfCode/cppAOC/inputs/2.txt");

    string a, b;
//    cin >> a >> b;

    map<string, int> yours;
    yours.insert({"X", 1});
    yours.insert({"Y", 2});
    yours.insert({"Z", 3});

    map<string, string> wins;
    wins.insert({"X", "C"});
    wins.insert({"Y", "A"});
    wins.insert({"Z", "B"});

    map<string, string> ties;
    ties.insert({"X", "A"});
    ties.insert({"Y", "B"});
    ties.insert({"Z", "C"});

    ll ans = 0;
    for (int i = 0; i < 2500; i++) {
        cin >> b >> a;
//        cout << b << ", " << a << endl;
        if (wins[a] == b) {
            ans += 6;
        }
        else if (ties[a] == b) {
            ans += 3;
        }
        ans += yours[a];
//        cout << ans << " - " << b << "\n";
    }

    cout << ans;
}