# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. Each account is represented by a list of strings (the emails of the account), and two accounts are merged if they share a common email. The result should be a list of merged accounts.

## Approach
The approach is to use a Union-Find algorithm to group the accounts that have the same email. We iterate over each account, and for each email in the account, we find the parent of the email and union it with the parent of the account. Finally, we group the emails by their parent and return the result.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the maximum number of emails in an account
- Space: O(N * M) for storing the parent and rank of each email

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    unordered_map<string, string> parent;
    unordered_map<string, int> rank;

    string find(const string& email) {
        if (parent[email] != email) {
            parent[email] = find(parent[email]);
        }
        return parent[email];
    }

    void unionEmails(const string& email1, const string& email2) {
        string root1 = find(email1);
        string root2 = find(email2);

        if (root1 != root2) {
            if (rank[root1] > rank[root2]) {
                parent[root2] = root1;
            } else if (rank[root1] < rank[root2]) {
                parent[root1] = root2;
            } else {
                parent[root2] = root1;
                rank[root1]++;
            }
        }
    }
};

vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    UnionFind uf;
    unordered_map<string, string> emailToName;

    for (const auto& account : accounts) {
        string name = account[0];
        for (int i = 1; i < account.size(); i++) {
            if (uf.parent.find(account[i]) == uf.parent.end()) {
                uf.parent[account[i]] = account[i];
                uf.rank[account[i]] = 0;
                emailToName[account[i]] = name;
            }
            if (i > 1) {
                uf.unionEmails(account[i], account[i - 1]);
            }
        }
    }

    unordered_map<string, vector<string>> groups;
    for (const auto& account : accounts) {
        for (int i = 1; i < account.size(); i++) {
            string root = uf.find(account[i]);
            groups[root].push_back(account[i]);
        }
    }

    vector<vector<string>> result;
    for (const auto& group : groups) {
        vector<string> mergedAccount;
        string name = emailToName[group.first];
        mergedAccount.push_back(name);
        sort(group.second.begin(), group.second.end());
        mergedAccount.insert(mergedAccount.end(), group.second.begin(), group.second.end());
        result.push_back(mergedAccount);
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
- Use Union-Find algorithm to group accounts with common emails
- Use an unordered_map to store the parent and rank of each email
- Use another unordered_map to store the email to name mapping for easy lookup
- Finally, group the emails by their parent and return the result