# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The merge rule is that if two accounts have at least one common email, they are considered as the same account. The task is to group all the accounts that are considered the same and return the merged accounts. Each account should have a unique name. The input is a list of accounts where each account is a list of strings, and the output is a list of merged accounts.

## Approach
We can use a disjoint-set data structure to solve this problem, where each account is a set and two sets are merged if they have at least one common email. We also use a map to store the parent of each email and a map to store the emails for each account.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the average number of emails per account
- Space: O(N * M) for storing the parent and rank of each email

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    unordered_map<string, string> parent;
    unordered_map<string, string> emailToName;

    string find(string email) {
        if (parent[email] != email) {
            parent[email] = find(parent[email]);
        }
        return parent[email];
    }

    void unionEmails(string email1, string email2, string name) {
        string root1 = find(email1);
        string root2 = find(email2);
        if (root1 != root2) {
            parent[root1] = root2;
            emailToName[root2] = name;
        }
    }
};

vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    UnionFind uf;
    unordered_map<string, string> emailToName;
    for (int i = 0; i < accounts.size(); i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            uf.parent[accounts[i][j]] = accounts[i][j];
            emailToName[accounts[i][j]] = accounts[i][0];
        }
    }

    for (int i = 0; i < accounts.size(); i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            uf.unionEmails(accounts[i][1], accounts[i][j], accounts[i][0]);
        }
    }

    unordered_map<string, vector<string>> mergedAccounts;
    for (int i = 0; i < accounts.size(); i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            string root = uf.find(accounts[i][j]);
            mergedAccounts[root].push_back(accounts[i][j]);
        }
    }

    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        sort(pair.second.begin(), pair.second.end());
        vector<string> account = {emailToName[pair.first]};
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
- Use a disjoint-set data structure to group accounts with common emails
- Use a map to store the parent of each email and a map to store the emails for each account
- Sort the emails in each merged account for a consistent output