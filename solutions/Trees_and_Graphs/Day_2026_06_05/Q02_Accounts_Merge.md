# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all accounts that have at least one common email. The result should be a list of merged accounts, where each account is a list of sorted emails. The input is a list of accounts, where each account is a list of strings representing emails. The output should be a list of lists of strings, where each sublist contains the merged emails of an account. For example, if we have two accounts ["a@example.com", "b@example.com"] and ["b@example.com", "c@example.com"], they should be merged into one account ["a@example.com", "b@example.com", "c@example.com"].

## Approach
We can use a Union-Find algorithm to solve this problem. The idea is to create a graph where each email is a node, and two nodes are connected if they are in the same account. We then use the Union-Find algorithm to find all connected components in the graph, which represent the merged accounts.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

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
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            parent[rootx] = rooty;
        }
    }
};

vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    int n = accounts.size();
    UnionFind uf(n);
    unordered_map<string, int> emailToIndex;
    for (int i = 0; i < n; i++) {
        for (string email : accounts[i]) {
            if (emailToIndex.find(email) == emailToIndex.end()) {
                emailToIndex[email] = i;
            } else {
                uf.union_(i, emailToIndex[email]);
            }
        }
    }
    unordered_map<int, vector<string>> ans;
    for (int i = 0; i < n; i++) {
        int root = uf.find(i);
        for (string email : accounts[i]) {
            ans[root].push_back(email);
        }
    }
    for (auto& emails : ans) {
        sort(emails.second.begin(), emails.second.end());
    }
    vector<vector<string>> result;
    for (auto& emails : ans) {
        result.push_back(emails.second);
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
- The Union-Find algorithm can be used to solve problems that involve merging connected components in a graph.
- The `find` operation in the Union-Find algorithm can be optimized using path compression.
- The `union` operation in the Union-Find algorithm can be optimized using union by rank.