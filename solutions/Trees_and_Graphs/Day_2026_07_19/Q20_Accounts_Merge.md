# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The output should be a list of merged accounts, where each merged account is a list of all emails in the merged accounts. For example, if we have two accounts ["a@example.com", "b@example.com"] and ["b@example.com", "c@example.com"], we should merge them into one account ["a@example.com", "b@example.com", "c@example.com"]. The emails in each account should be sorted and there should be no duplicates.

## Approach
We can use a Union-Find algorithm to solve this problem, where each email is a node and two nodes are connected if they are in the same account. We then use the Union-Find algorithm to find all connected components, which represent the merged accounts.

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
    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    unordered_map<string, int> emailToIndex;
    int emailCount = 0;
    for (auto& account : accounts) {
        for (auto& email : account) {
            if (emailToIndex.find(email) == emailToIndex.end()) {
                emailToIndex[email] = emailCount++;
            }
        }
    }

    UnionFind uf(emailCount);
    for (auto& account : accounts) {
        for (int i = 1; i < account.size(); i++) {
            uf.unionNodes(emailToIndex[account[0]], emailToIndex[account[i]]);
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (auto& emailIndex : emailToIndex) {
        int root = uf.find(emailIndex.second);
        mergedAccounts[root].push_back(emailIndex.first);
    }

    vector<vector<string>> result;
    for (auto& account : mergedAccounts) {
        sort(account.second.begin(), account.second.end());
        result.push_back(account.second);
    }
    return result;
}
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- We use a Union-Find algorithm to group connected emails together.
- We use a hashmap to store the index of each email for efficient lookup.
- We sort the emails in each merged account to ensure they are in the correct order.