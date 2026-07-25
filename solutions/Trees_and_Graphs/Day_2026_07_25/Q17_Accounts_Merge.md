# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts, where each account is a list of emails in sorted order. The emails in each account should be in sorted order, and the accounts should be in the order they were given in the input. For example, if the input is `[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "johnsmith@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]]`. The length of the accounts will not exceed 1000, and the length of the name will not exceed 10, and the length of the email will not exceed 30.

## Approach
The algorithm uses a union-find data structure to group the accounts that have the same email. The emails in each account are used as the nodes in the union-find data structure, and two nodes are connected if they are in the same account. After that, the algorithm groups the connected components and constructs the merged accounts.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

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
    void unionNodes(int x, int y) {
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
            string email = accounts[i][j];
            if (emailToIndex.find(email) != emailToIndex.end()) {
                uf.unionNodes(emailToIndex[email], i);
            } else {
                emailToIndex[email] = i;
            }
        }
    }
    unordered_map<int, vector<string>> groups;
    for (const auto& pair : emailToIndex) {
        int group = uf.find(pair.second);
        groups[group].push_back(pair.first);
    }
    vector<vector<string>> result;
    for (const auto& pair : groups) {
        vector<string> group = pair.second;
        sort(group.begin(), group.end());
        group.insert(group.begin(), accounts[pair.first][0]);
        result.push_back(group);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                        {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
                                        {"John", "johnsmith@mail.com", "johnsmith@mail.com"}};
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
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "johnsmith@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]]
```

## Key Takeaways
- Use a union-find data structure to group the accounts that have the same email.
- Use an unordered map to store the index of each email in the accounts.
- Use an unordered map to store the groups of emails.
- Sort the emails in each group before constructing the merged accounts.