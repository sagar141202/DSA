# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts, where each merged account is a list of emails in sorted order. For example, if we have two accounts ["johnsmith@mail.com", "john_newyork@mail.com"] and ["johnsmith@mail.com", "john00@mail.com"], they should be merged into one account ["john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]. The input is a list of accounts where each account is a list of strings representing emails.

## Approach
We can use a Union-Find algorithm to solve this problem by treating each email as a node and merging the nodes that belong to the same account. We use a parent array to keep track of the parent of each node and a rank array to optimize the union operation. The find operation is used to find the parent of a node and the union operation is used to merge two nodes.

## Complexity
- Time: O(N * M * log(M)) where N is the number of accounts and M is the maximum number of emails in an account
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
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
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
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
                uf.unionNodes(i, emailToIndex[email]);
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (auto& pair : emailToIndex) {
        int index = uf.find(pair.second);
        mergedAccounts[index].push_back(pair.first);
    }

    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        sort(pair.second.begin(), pair.second.end());
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@mail.com", "john_newyork@mail.com"}, 
                                        {"johnsmith@mail.com", "john00@mail.com"}, 
                                        {"john_newyork@mail.com", "johnsmith@mail.com"}, 
                                        {"john00@mail.com", "johnsmith@mail.com"}};
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
Input: [["johnsmith@mail.com","john_newyork@mail.com"],["johnsmith@mail.com","john00@mail.com"],["john_newyork@mail.com","johnsmith@mail.com"],["john00@mail.com","johnsmith@mail.com"]]
Output: [["john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]]
```

## Key Takeaways
- The Union-Find algorithm is used to merge accounts that have the same email.
- The `find` operation is used to find the parent of a node and the `union` operation is used to merge two nodes.
- The result is a list of merged accounts, where each merged account is a list of emails in sorted order.