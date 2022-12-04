/*
 * Created on 12/1/22
*/
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    ifstream cin("/Users/sabrina/projects_local/AdventOfCode/cppAOC/inputs/2.txt");

    string play, res;
//    cin >> a >> b;

    map<string, int> score;
    score.insert({"X", 0});
    score.insert({"Y", 3});
    score.insert({"Z", 6});

    map<string, int> wins;
    wins.insert({"A", 2});
    wins.insert({"B", 3});
    wins.insert({"C", 1});

    map<string, int> lose;
    lose.insert({"A", 3});
    lose.insert({"B", 1});
    lose.insert({"C", 2});

    map<string, int> ties;
    ties.insert({"A", 1});
    ties.insert({"B", 2});
    ties.insert({"C", 3});


    ll ans = 0;
    for (int i = 0; i < 2500; i++) {
        cin >> play >> res;
//        cout << b << ", " << a << endl;
        if (res == "X") {
            ans += lose[play];
        }
        else if (res == "Y") {
            ans += ties[play];
        }
        else if (res == "Z") {
            ans += wins[play];
        }
        ans += score[res];
//        cout << ans << " - " << res << "\n";
    }

    cout << ans;
}