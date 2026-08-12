# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts, where each account is a list of emails in sorted order. Two accounts are considered the same if they have at least one common email. For example, if we have two accounts `["johnsmith@mail.com"]` and `["john_newyork@mail.com", "johnsmith@mail.com"]`, they should be merged into one account `["john_newyork@mail.com", "johnsmith@mail.com"]`. The input is a list of accounts where each account is a list of strings representing the emails. The output should be a list of lists of strings, where each sublist contains the merged emails.

## Approach
We can solve this problem by using a union-find algorithm to group the accounts that have the same email. We create a parent array to store the parent of each email and a rank array to optimize the union operation. Then, we iterate over each account and each email in the account to union the emails.

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
    vector<int> rank;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
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
                uf.unionSet(i, emailToIndex[email]);
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        int root = uf.find(i);
        mergedAccounts[root].insert(mergedAccounts[root].end(), accounts[i].begin(), accounts[i].end());
    }

    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        vector<string> emails = pair.second;
        sort(emails.begin(), emails.end());
        result.push_back(emails);
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
- Use a union-find algorithm to group the accounts that have the same email.
- Use a `UnionFind` class to encapsulate the union-find logic.
- Use an `unordered_map` to store the index of each email in the `accounts` vector.