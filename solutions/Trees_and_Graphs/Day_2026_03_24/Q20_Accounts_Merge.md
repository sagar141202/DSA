# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all accounts that have at least one common email. The input is a list of lists of strings, where each inner list represents an account and each string represents an email. The output should be a list of lists of strings, where each inner list represents a merged account. For example, if we have two accounts `["account1@email.com", "account2@email.com"]` and `["account2@email.com", "account3@email.com"]`, they should be merged into one account `["account1@email.com", "account2@email.com", "account3@email.com"]`. The order of the emails in the output does not matter.

## Approach
We will use a union-find algorithm to group the accounts based on common emails. Each email will be a node in the union-find data structure, and two nodes will be connected if they are in the same account. Then, we will iterate over the accounts again to merge the accounts that are connected.

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

    string find(string email) {
        if (parent[email] != email) {
            parent[email] = find(parent[email]);
        }
        return parent[email];
    }

    void union Emails(string email1, string email2) {
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
        string name = account[0];
        for (int i = 1; i < account.size(); i++) {
            emailToName[account[i]] = name;
            if (i > 1) {
                uf.unionEmails(account[i], account[i - 1]);
            }
            if (uf.parent.find(account[i]) == uf.parent.end()) {
                uf.parent[account[i]] = account[i];
                uf.rank[account[i]] = 0;
            }
        }
    }

    unordered_map<string, vector<string>> mergedAccounts;
    for (auto email : emailToName) {
        string root = uf.find(email.first);
        mergedAccounts[root].push_back(email.first);
    }

    vector<vector<string>> result;
    for (auto account : mergedAccounts) {
        sort(account.second.begin(), account.second.end());
        account.second.insert(account.second.begin(), emailToName[account.second[0]]);
        result.push_back(account.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                       {"John", "johnnybravo@mail.com"}, 
                                       {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
                                       {"Mary", "mary@mail.com"}};
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
Input: [["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["John", "johnnybravo@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use union-find algorithm to group accounts based on common emails
- Use an unordered_map to store the parent and rank of each email for efficient lookup and update
- Use another unordered_map to store the merged accounts for efficient construction of the final result