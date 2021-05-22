#include <iostream>
#include <climits>
using namespace std;
 
int coinsExchange(int amt, int *deno, int n, int *dp) {
    // base case
    if (amt == 0) {
        return dp[amt] = 0;
    }
    if (dp[amt] != -1) {
        return dp[amt];
    }
 
    // recursive case
    int ans = INT_MAX;
    for (int i = 0 ; i < n ; i++) {
        if (amt >= deno[i]) {
            int sa = coinsExchange(amt - deno[i], deno, n, dp);
            if (sa != INT_MAX) {
                ans = min(sa + 1, ans);
            }
        }
    }
 
    return dp[amt] = ans;
}
 
int main() {
 
    int deno[4] = {1, 2, 5, 10};
    int amt = 50;
    int *dp = new int[amt + 1];
    for (int i = 0 ; i <= amt ; i++) {
        dp[i] = -1;
    }
    cout << coinsExchange(amt, deno, 4, dp) << endl;
 
    return 0;
}