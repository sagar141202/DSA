# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts. Each merged account should contain all the emails from the original accounts that were merged. The emails in each merged account should be sorted in alphabetical order. The merged accounts should be returned in the order they were first encountered in the input list. For example, if the input is `[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnsmith@mail.com", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnnybravo@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"]]`.

## Approach
The approach to solve this problem is to use a graph to model the accounts and their corresponding emails. Then, we use a depth-first search (DFS) to traverse the graph and merge the accounts. We use a parent array to keep track of the parent of each email and a rank array to keep track of the rank of each email.

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
    int n = accounts.size();
    UnionFind uf(n);
    unordered_map<string, int> emailToIndex;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            if (emailToIndex.find(accounts[i][j]) != emailToIndex.end()) {
                uf.union_(emailToIndex[accounts[i][j]], i);
            } else {
                emailToIndex[accounts[i][j]] = i;
            }
        }
    }

    unordered_map<int, vector<string>> ans;
    for (const auto& [email, index] : emailToIndex) {
        ans[uf.find(index)].push_back(email);
    }

    vector<vector<string>> result;
    for (const auto& [index, emails] : ans) {
        sort(emails.begin(), emails.end());
        vector<string> mergedAccount = {accounts[index][0]};
        mergedAccount.insert(mergedAccount.end(), emails.begin(), emails.end());
        result.push_back(mergedAccount);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                        {"John", "johnsmith@mail.com", "johnnybravo@mail.com"}, 
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
        ["John", "johnsmith@mail.com", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnnybravo@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use a Union-Find data structure to group the accounts that have the same email.
- Use a hash map to keep track of the index of each email in the accounts list.
- Use a depth-first search (DFS) to traverse the graph and merge the accounts.
- Sort the emails in each merged account in alphabetical order.