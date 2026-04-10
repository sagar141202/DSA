# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The accounts are represented as a list of lists, where each inner list contains the account name and a list of emails. The task is to merge the accounts and return the merged accounts. The order of the emails in the merged account does not matter, but the emails should be sorted. The account name should be the same as the original account name. For example, if we have two accounts ["John", ["john1@mail.com", "john2@mail.com"]] and ["John", ["john2@mail.com", "john3@mail.com"]], the merged account should be ["John", ["john1@mail.com", "john2@mail.com", "john3@mail.com"]]. The input is a list of accounts and the output should be a list of merged accounts.

## Approach
The approach to solve this problem is to use a graph to represent the accounts and their corresponding emails. We can use a depth-first search (DFS) to traverse the graph and merge the accounts. We will use a union-find data structure to keep track of the connected components in the graph.

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
        for (int j = 1; j < accounts[i].size(); j++) {
            if (emailToIndex.find(accounts[i][j]) != emailToIndex.end()) {
                uf.union_(i, emailToIndex[accounts[i][j]]);
            } else {
                emailToIndex[accounts[i][j]] = i;
            }
        }
    }
    unordered_map<int, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        int root = uf.find(i);
        if (mergedAccounts.find(root) == mergedAccounts.end()) {
            mergedAccounts[root] = {accounts[i][0]};
        }
        for (int j = 1; j < accounts[i].size(); j++) {
            mergedAccounts[root].push_back(accounts[i][j]);
        }
    }
    vector<vector<string>> result;
    for (auto& account : mergedAccounts) {
        sort(account.second.begin() + 1, account.second.end());
        result.push_back(account.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {
        {"John", "johnsmith@mail.com", "john_newyork@mail.com"},
        {"John", "johnsmith@mail.com", "john00@mail.com"},
        {"Mary", "mary@mail.com"},
        {"John", "johnnybravo@mail.com"}
    };
    vector<vector<string>> mergedAccounts = accountsMerge(accounts);
    for (auto& account : mergedAccounts) {
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
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"], 
        ["John", "johnnybravo@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"], 
         ["John", "johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a union-find data structure to keep track of the connected components in the graph.
- Use a depth-first search (DFS) to traverse the graph and merge the accounts.
- Sort the emails in the merged account to ensure they are in the correct order.