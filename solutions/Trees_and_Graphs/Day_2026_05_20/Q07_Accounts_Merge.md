# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The accounts should be merged in a way that the resulting accounts are still lists of emails. For example, if we have two accounts `["name1","email1","email2"]` and `["name2","email2","email3"]`, they should be merged into one account `["name1","email1","email2","email3"]`. However, if we have two accounts `["name1","email1","email2"]` and `["name2","email3","email4"]`, they should not be merged. We can assume that the input list of accounts will not be empty and that the emails in each account will not be empty. The names of the accounts will be the same if the accounts are merged.

## Approach
We can solve this problem using a Union-Find algorithm to group the accounts that have the same email. Then, we can merge the accounts in each group. The Union-Find algorithm will help us to find the connected components in the graph where the nodes are the emails and the edges are the accounts. We will use a map to store the parent of each email and a map to store the rank of each email.

## Complexity
- Time: O(N * M * alpha(N * M)) where N is the number of accounts and M is the maximum number of emails in an account, and alpha is the inverse Ackermann function which grows very slowly.
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    unordered_map<string, string> parent;
    unordered_map<string, int> rank;

    string find(string email) {
        if (parent[email] != email) {
            parent[email] = find(parent[email]);
        }
        return parent[email];
    }

    void unionEmails(string email1, string email2) {
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
    for (auto account : accounts) {
        for (int i = 1; i < account.size(); i++) {
            uf.parent[account[i]] = account[i];
            uf.rank[account[i]] = 1;
            emailToName[account[i]] = account[0];
        }
    }
    for (auto account : accounts) {
        for (int i = 1; i < account.size() - 1; i++) {
            uf.unionEmails(account[i], account[i + 1]);
        }
    }
    unordered_map<string, vector<string>> groups;
    for (auto account : accounts) {
        for (int i = 1; i < account.size(); i++) {
            string root = uf.find(account[i]);
            groups[root].push_back(account[i]);
        }
    }
    vector<vector<string>> result;
    for (auto group : groups) {
        vector<string> emails = group.second;
        sort(emails.begin(), emails.end());
        vector<string> mergedAccount = {emailToName[emails[0]]};
        mergedAccount.insert(mergedAccount.end(), emails.begin(), emails.end());
        result.push_back(mergedAccount);
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
    for (auto account : result) {
        for (auto email : account) {
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
- Using a Union-Find algorithm to group the accounts that have the same email.
- Merging the accounts in each group by finding the root of each email.
- Using a map to store the parent of each email and a map to store the rank of each email.