# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The accounts should be merged based on the emails, and the emails in each merged account should be unique and sorted. For example, if we have two accounts ["a@gmail.com", "b@gmail.com"] and ["b@gmail.com", "c@gmail.com"], they should be merged into one account ["a@gmail.com", "b@gmail.com", "c@gmail.com"]. The input is a list of accounts where each account is a list of emails, and the output is a list of merged accounts.

## Approach
We can use a union-find data structure to group the accounts based on the emails. We iterate over each account and each email in the account, and if we have seen the email before, we union the current account with the account that the email belongs to. Finally, we group the emails by their corresponding account and sort the emails in each group.

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
    int n = accounts.size();
    UnionFind uf(n);
    unordered_map<string, int> emailToAccount;
    for (int i = 0; i < n; i++) {
        for (const string& email : accounts[i]) {
            if (emailToAccount.count(email)) {
                uf.union_(i, emailToAccount[email]);
            } else {
                emailToAccount[email] = i;
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (const auto& [email, account] : emailToAccount) {
        int root = uf.find(account);
        mergedAccounts[root].push_back(email);
    }

    vector<vector<string>> result;
    for (const auto& [_, emails] : mergedAccounts) {
        sort(emails.begin(), emails.end());
        result.push_back(emails);
    }
    return result;
}
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"], 
        ["John", "johnnybravo@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"], 
         ["John", "johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a union-find data structure to group the accounts based on the emails.
- Iterate over each account and each email in the account to union the accounts.
- Group the emails by their corresponding account and sort the emails in each group.