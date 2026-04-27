# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The goal is to group all the emails that belong to the same person. The input is a list of accounts where each account is a list of strings representing the emails in that account. The output should be a list of merged accounts where each account is a list of strings representing the merged emails. For example, if the input is `[["johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"], ["johnsmith@mail.com", "johnnybravo@mail.com"]]`, the output should be `[["johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com", "johnnybravo@mail.com"]]`. The constraints are that each account has at least one email and the total number of accounts is at most 1000.

## Approach
The approach to solve this problem is to use a union-find data structure to group the emails that belong to the same person. We can iterate over the accounts and for each email in the account, we check if it is already in the union-find data structure. If it is, we union the current account with the account that the email belongs to. If not, we add the email to the union-find data structure and mark it as the representative of the current account.

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
    unordered_map<string, int> emailToAccount;
    for (int i = 0; i < accounts.size(); i++) {
        for (string email : accounts[i]) {
            if (emailToAccount.count(email)) {
                uf.unionSet(i, emailToAccount[email]);
            } else {
                emailToAccount[email] = i;
            }
        }
    }

    unordered_map<int, vector<string>> mergedAccounts;
    for (auto& pair : emailToAccount) {
        int account = uf.find(pair.second);
        mergedAccounts[account].push_back(pair.first);
    }

    vector<vector<string>> result;
    for (auto& pair : mergedAccounts) {
        sort(pair.second.begin(), pair.second.end());
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"}, 
                                        {"johnsmith@mail.com", "johnnybravo@mail.com"}};
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
Input: [["johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com"], 
        ["johnsmith@mail.com", "johnnybravo@mail.com"]]
Output: [["johnsmith@mail.com", "john00@mail.com", "john_newyork@mail.com", "johnnybravo@mail.com"]]
```

## Key Takeaways
- Use a union-find data structure to group the emails that belong to the same person.
- Iterate over the accounts and for each email in the account, check if it is already in the union-find data structure.
- The time complexity is O(N * M * L) where N is the number of accounts, M is the maximum number of emails in an account, and L is the maximum length of an email.