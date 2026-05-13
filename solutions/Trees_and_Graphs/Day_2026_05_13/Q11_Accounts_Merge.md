# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The input is a list of lists of strings, where each inner list represents an account and each string represents an email. The output should be a list of lists of strings, where each inner list represents a merged account. For example, if we have two accounts ["account1@example.com", "account2@example.com"] and ["account2@example.com", "account3@example.com"], they should be merged into one account ["account1@example.com", "account2@example.com", "account3@example.com"]. The order of the emails in the output does not matter.

## Approach
We will use a union-find algorithm to solve this problem, where each account is a node and two nodes are connected if they have the same email. The algorithm will then group all connected nodes into the same account. We will use a parent array to keep track of the parent of each node and a rank array to optimize the union operation.

## Complexity
- Time: O(N * M * L) where N is the number of accounts, M is the maximum number of emails in an account, and L is the maximum length of an email.
- Space: O(N * M) for storing the parent and rank arrays.

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

    void unionNodes(int x, int y) {
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
        for (const string& email : accounts[i]) {
            if (emailToIndex.find(email) == emailToIndex.end()) {
                emailToIndex[email] = i;
            } else {
                uf.unionNodes(i, emailToIndex[email]);
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        int root = uf.find(i);
        mergedAccounts[root].insert(mergedAccounts[root].end(), accounts[i].begin(), accounts[i].end());
    }

    vector<vector<string>> result;
    for (const auto& account : mergedAccounts) {
        sort(account.second.begin(), account.second.end());
        result.push_back(account.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"}, 
                                        {"johnsmith@mail.com", "john_newyork@mail.com"}, 
                                        {"johnnewyork@mail.com", "johnsmith@mail.com"}};
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
Input: [["johnsmith@mail.com","john_newyork@mail.com"],["johnsmith@mail.com","john00@mail.com"],["john_newyork@mail.com","johnsmith@mail.com"],["john00@mail.com","john_newyork@mail.com"]]
Output: [["john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]]
```

## Key Takeaways
- Use a union-find algorithm to group connected accounts.
- Use a parent array to keep track of the parent of each node and a rank array to optimize the union operation.
- Sort the emails in each merged account to ensure the output is in a consistent order.