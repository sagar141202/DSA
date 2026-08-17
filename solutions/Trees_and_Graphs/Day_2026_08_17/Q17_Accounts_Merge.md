# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The output should be a list of merged accounts, where each merged account is a list of emails. The order of the emails in the merged account does not matter. If two accounts have the same email, they are owned by the same person. The input is a list of accounts, where each account is a list of strings representing the emails of the account. The output should be a list of lists of strings, where each inner list represents a merged account.

## Approach
We can use a union-find algorithm to group the accounts that have the same email. We will iterate over each account and each email in the account, and union the emails that are in the same account. Then, we will group the emails by their root email.

## Complexity
- Time: O(N * M * alpha(N * M)) where N is the number of accounts, M is the maximum number of emails in an account, and alpha is the inverse Ackermann function
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
    unordered_map<string, int> emailToIndex;
    for (int i = 0; i < accounts.size(); i++) {
        for (string email : accounts[i]) {
            if (emailToIndex.find(email) == emailToIndex.end()) {
                emailToIndex[email] = i;
            } else {
                uf.union_(emailToIndex[email], i);
            }
        }
    }
    unordered_map<int, vector<string>> ans;
    for (int i = 0; i < accounts.size(); i++) {
        int root = uf.find(i);
        ans[root].insert(ans[root].end(), accounts[i].begin(), accounts[i].end());
    }
    vector<vector<string>> result;
    for (auto& pair : ans) {
        vector<string> emails = pair.second;
        sort(emails.begin(), emails.end());
        result.push_back(emails);
    }
    return result;
}
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use union-find algorithm to group the accounts that have the same email.
- Use an unordered_map to store the email to index mapping for efficient lookup.
- Use an unordered_map to store the root email to emails mapping for efficient grouping.