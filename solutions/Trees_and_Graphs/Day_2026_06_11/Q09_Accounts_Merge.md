# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts, where each merged account is a list of all emails that appear in at least one of the original accounts that were merged. The order of the emails in the merged account does not matter. If two accounts have the same email, they are owned by the same person, and we should merge them. The input will be a list of accounts, where each account is a list of strings representing emails. The output should be a list of merged accounts.

## Approach
We can use a Union-Find data structure to solve this problem. Each email will be a node in the Union-Find, and if two emails appear in the same account, we will union them. Then, we can iterate over all the emails and find their parent to group them into merged accounts.

## Complexity
- Time: O(N * M * alpha) where N is the number of accounts, M is the maximum number of emails in an account, and alpha is the inverse Ackermann function.
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

    void unionSet(int x, int y) {
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
            if (emailToIndex.find(accounts[i][j]) == emailToIndex.end()) {
                emailToIndex[accounts[i][j]] = i;
            } else {
                uf.unionSet(i, emailToIndex[accounts[i][j]]);
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        int root = uf.find(i);
        if (mergedAccounts.find(root) == mergedAccounts.end()) {
            mergedAccounts[root] = {};
        }
        for (int j = 1; j < accounts[i].size(); j++) {
            mergedAccounts[root].push_back(accounts[i][j]);
        }
    }

    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        vector<string> account;
        account.push_back(accounts[pair.first][0]);
        sort(pair.second.begin(), pair.second.end());
        account.insert(account.end(), pair.second.begin(), pair.second.end());
        result.push_back(account);
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
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"], 
        ["John", "johnnybravo@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"], 
         ["John", "johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a Union-Find data structure to group emails that appear in the same account.
- Use a map to store the index of each email in the Union-Find.
- Use another map to store the merged accounts.
- Sort the emails in each merged account before returning the result.