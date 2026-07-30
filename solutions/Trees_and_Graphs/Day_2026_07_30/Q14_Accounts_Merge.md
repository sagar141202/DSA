# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all accounts that have at least one common email. The input is a list of lists of strings, where each inner list represents an account and contains the account name and a list of emails. The output should be a list of lists of strings, where each inner list represents a merged account and contains the account name and a list of unique emails. The account name for each merged account should be the same as the account name of the first account in the merge group. For example, if we have two accounts ["John", "john.smith@email.com", "john_newyork@email.com"] and ["John", "john.smith@email.com", "john00@email.com"], they should be merged into one account ["John", "john00@email.com", "john_newyork@email.com", "john.smith@email.com"]. The emails in the merged account should be sorted in alphabetical order.

## Approach
We can use a union-find data structure to group the accounts based on common emails. We will iterate over each account and its emails, and for each email, we will find its parent and union it with the current account. After unioning all accounts, we will group the emails by their parent and create the merged accounts.

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
        for (int j = 1; j < accounts[i].size(); j++) {
            if (emailToIndex.find(accounts[i][j]) != emailToIndex.end()) {
                uf.union_(emailToIndex[accounts[i][j]], i);
            } else {
                emailToIndex[accounts[i][j]] = i;
            }
        }
    }
    unordered_map<int, vector<string>> groups;
    for (const auto& emailIndex : emailToIndex) {
        int group = uf.find(emailIndex.second);
        groups[group].push_back(emailIndex.first);
    }
    vector<vector<string>> result;
    for (const auto& group : groups) {
        vector<string> mergedAccount;
        mergedAccount.push_back(accounts[group.first][0]);
        sort(group.second.begin(), group.second.end());
        mergedAccount.insert(mergedAccount.end(), group.second.begin(), group.second.end());
        result.push_back(mergedAccount);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "john.smith@email.com", "john_newyork@email.com"}, 
                                        {"John", "john.smith@email.com", "john00@email.com"}, 
                                        {"Mary", "mary@email.com"}};
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
Input: [["John", "john.smith@email.com", "john_newyork@email.com"], 
        ["John", "john.smith@email.com", "john00@email.com"], 
        ["Mary", "mary@email.com"]]
Output: [["John", "john00@email.com", "john_newyork@email.com", "john.smith@email.com"], 
         ["Mary", "mary@email.com"]]
```

## Key Takeaways
- Use a union-find data structure to group accounts based on common emails.
- Iterate over each account and its emails to find the parent and union it with the current account.
- Group the emails by their parent and create the merged accounts.