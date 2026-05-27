# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The email can be in any position in the account. The output should be a list of merged accounts. Each merged account should contain all the emails from the original accounts that were merged. The order of the emails in the merged account does not matter. The input is a list of lists of strings, where each inner list represents an account and each string represents an email. The output should be a list of lists of strings, where each inner list represents a merged account.

## Approach
We will use a union-find algorithm to group the accounts that have the same email. We will iterate over each account and each email in the account, and use the union-find algorithm to merge the accounts that have the same email. Then, we will iterate over each account and use the union-find algorithm to get the merged account.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the maximum number of emails in an account
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
    int n = accounts.size();
    UnionFind uf(n);
    unordered_map<string, int> emailToIndex;
    for (int i = 0; i < n; i++) {
        for (const string& email : accounts[i]) {
            if (emailToIndex.find(email) != emailToIndex.end()) {
                uf.union_(i, emailToIndex[email]);
            } else {
                emailToIndex[email] = i;
            }
        }
    }
    unordered_map<int, vector<string>> groups;
    for (int i = 0; i < n; i++) {
        int group = uf.find(i);
        for (const string& email : accounts[i]) {
            groups[group].push_back(email);
        }
    }
    vector<vector<string>> result;
    for (auto& group : groups) {
        sort(group.second.begin(), group.second.end());
        result.push_back(group.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"}, 
                                       {"johnsmith@mail.com", "john00@mail.com"}, 
                                       {"johnnybravo@mail.com"}};
    vector<vector<string>> result = accountsMerge(accounts);
    for (const auto& account : result) {
        for (const string& email : account) {
            cout << email << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [["johnsmith@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["johnsmith@mail.com","john00@mail.com"],["johnnybravo@mail.com"]]
Output: [["john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a union-find algorithm to group the accounts that have the same email.
- Use an unordered_map to store the email to index mapping.
- Use an unordered_map to store the groups of accounts.
- Sort the emails in each group before adding it to the result.