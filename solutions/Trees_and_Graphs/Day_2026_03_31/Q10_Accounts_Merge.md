# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The emails for each account are unique, and the emails for each account are sorted. The result should be a list of merged accounts, where each merged account is a list of sorted emails. The order of the emails in the merged account does not matter. For example, if we have two accounts ["a","b"] and ["b","c"], they should be merged into ["a","b","c"]. The input is a list of accounts, where each account is a list of strings representing the emails.

## Approach
We can use a Union-Find algorithm to group the accounts that have the same email. We iterate over each account and each email in the account, and union the accounts that have the same email. Then we group the emails by their parent account.

## Complexity
- Time: O(N * M * log(M))
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    UnionFind uf(accounts.size());
    unordered_map<string, int> emailToAccount;
    for (int i = 0; i < accounts.size(); i++) {
        for (string email : accounts[i]) {
            if (emailToAccount.count(email)) {
                uf.union_(i, emailToAccount[email]);
            } else {
                emailToAccount[email] = i;
            }
        }
    }
    unordered_map<int, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        int parent = uf.find(i);
        for (string email : accounts[i]) {
            mergedAccounts[parent].push_back(email);
        }
    }
    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        sort(pair.second.begin(), pair.second.end());
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@mail.com","john00@mail.com","john_smith_1@mail.com"},{"johnsmith@mail.com","john_newyork@mail.com"},{"johnsmith@mail.com","johnsmith@mail.com"}};
    vector<vector<string>> result = accountsMerge(accounts);
    for (auto& account : result) {
        for (auto& email : account) {
            cout << email << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a Union-Find algorithm to group the accounts that have the same email.
- Use a hash map to store the email to account mapping for efficient lookup.
- Sort the emails in each merged account for a consistent output.