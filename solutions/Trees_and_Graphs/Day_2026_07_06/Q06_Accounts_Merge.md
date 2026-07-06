# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all accounts that have at least one common email. The input is a list of lists of strings, where each inner list represents an account and contains the account name and a list of emails. The output should be a list of lists of strings, where each inner list represents a merged account and contains the account name and a list of unique emails in sorted order. For example, if the input is `[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]`. The account name is the same for all accounts that need to be merged.

## Approach
We can use a union-find data structure to group accounts that have at least one common email. We iterate through each account and its emails, and for each email, we union the current account with the account that the email belongs to. Then, we group the emails by their account and sort the emails.

## Complexity
- Time: O(N * M * logM)
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
    unordered_map<string, int> emailToAccount;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            if (emailToAccount.find(accounts[i][j]) != emailToAccount.end()) {
                uf.union_(i, emailToAccount[accounts[i][j]]);
            } else {
                emailToAccount[accounts[i][j]] = i;
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (const auto& [email, account] : emailToAccount) {
        int root = uf.find(account);
        mergedAccounts[root].push_back(email);
    }

    for (int i = 0; i < n; i++) {
        if (mergedAccounts.find(i) != mergedAccounts.end()) {
            sort(mergedAccounts[i].begin(), mergedAccounts[i].end());
            mergedAccounts[i].insert(mergedAccounts[i].begin(), accounts[i][0]);
        }
    }

    vector<vector<string>> result;
    for (const auto& [_, emails] : mergedAccounts) {
        result.push_back(emails);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                        {"John", "johnnybravo@mail.com"}, 
                                        {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
                                        {"Mary", "mary@mail.com"}};
    vector<vector<string>> result = accountsMerge(accounts);
    for (const auto& account : result) {
        for (const auto& email : account) {
            cout << email << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["John", "johnnybravo@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use union-find data structure to group accounts with common emails.
- Sort the emails in each merged account.
- Use an unordered map to store the email to account mapping.