# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The goal is to return a list of merged accounts. If two accounts have the same email, they are owned by the same person. Two email addresses are considered the same if they are the same when ignoring the domain name. For example, "user@example.com" and "user@anotherexample.com" are considered the same. The input is a list of accounts where each account is a list of emails, and the output should be a list of merged accounts. For example, if the input is [["johnsmith@email.com", "john_newyork@email.com"], ["johnsmith@email.com", "john00@email.com"]], the output should be [["johnsmith@email.com", "john00@email.com", "john_newyork@email.com"]].

## Approach
The algorithm uses a union-find data structure to group the accounts that have the same email. It iterates over each account and each email in the account, and uses the union-find operations to merge the accounts that have the same email. The algorithm also ignores the domain name of the email addresses.

## Complexity
- Time: O(N * M * L) where N is the number of accounts, M is the maximum number of emails in an account, and L is the maximum length of an email.
- Space: O(N * M) where N is the number of accounts and M is the maximum number of emails in an account.

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
    unordered_map<string, int> emailToIndex;
    for (int i = 0; i < n; i++) {
        for (const string& email : accounts[i]) {
            string localName = email.substr(0, email.find('@'));
            if (emailToIndex.find(localName) == emailToIndex.end()) {
                emailToIndex[localName] = i;
            } else {
                uf.union_(i, emailToIndex[localName]);
            }
        }
    }

    unordered_map<int, vector<string>> ans;
    for (int i = 0; i < n; i++) {
        int root = uf.find(i);
        for (const string& email : accounts[i]) {
            ans[root].push_back(email);
        }
    }

    vector<vector<string>> result;
    for (auto& pair : ans) {
        sort(pair.second.begin(), pair.second.end());
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@email.com", "john_newyork@email.com"}, 
                                         {"johnsmith@email.com", "john00@email.com"}};
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
Input: [["johnsmith@email.com", "john_newyork@email.com"], 
         ["johnsmith@email.com", "john00@email.com"]]
Output: [["john00@email.com", "john_newyork@email.com", "johnsmith@email.com"]]
```

## Key Takeaways
- Use union-find data structure to group the accounts that have the same email.
- Ignore the domain name of the email addresses by taking the local name part of the email.
- Use an unordered map to store the email to index mapping for efficient lookup.