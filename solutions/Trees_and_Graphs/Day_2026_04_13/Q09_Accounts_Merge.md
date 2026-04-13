# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have at least one common email. The goal is to group all the emails that belong to the same person. Each email should only appear once in the result, and the emails within each account should be sorted. The accounts should also be sorted in a lexicographical order. For example, if we have two accounts `["johnsmith@mail.com", "john_newyork@mail.com"]` and `["johnsmith@mail.com", "john00@mail.com"]`, we should merge them into one account `["john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]`. The input is a list of lists of strings, where each inner list represents an account, and the output should be a list of lists of strings, where each inner list represents a merged account.

## Approach
We will use a Union-Find algorithm to solve this problem, where each email is a node, and two nodes are connected if they appear in the same account. We then use depth-first search to traverse all the connected components and merge the accounts. The Union-Find algorithm allows us to efficiently manage the connections between the emails.

## Complexity
- Time: O(NMlogM) where N is the number of accounts and M is the maximum number of emails in an account
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
    void union_(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            parent[rootx] = rooty;
        }
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        UnionFind uf(n);
        unordered_map<string, int> emailToIndex;
        for (int i = 0; i < n; i++) {
            for (const string& email : accounts[i]) {
                if (emailToIndex.find(email) == emailToIndex.end()) {
                    emailToIndex[email] = i;
                } else {
                    uf.union_(i, emailToIndex[email]);
                }
            }
        }
        unordered_map<int, vector<string>> ans;
        for (int i = 0; i < n; i++) {
            int root = uf.find(i);
            ans[root].insert(ans[root].end(), accounts[i].begin(), accounts[i].end());
        }
        vector<vector<string>> result;
        for (auto& pair : ans) {
            vector<string> emails = pair.second;
            sort(emails.begin(), emails.end());
            emails.erase(unique(emails.begin(), emails.end()), emails.end());
            result.push_back(emails);
        }
        sort(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution solution;
    vector<vector<string>> accounts = {{"johnsmith@mail.com", "john_newyork@mail.com"}, 
                                        {"johnsmith@mail.com", "john00@mail.com"}, 
                                        {"john_newyork@mail.com", "johnsmith@mail.com"}, 
                                        {"john00@mail.com", "johnsmith@mail.com"}};
    vector<vector<string>> result = solution.accountsMerge(accounts);
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
Input: [["johnsmith@mail.com","john_newyork@mail.com"],["johnsmith@mail.com","john00@mail.com"],["john_newyork@mail.com","johnsmith@mail.com"],["john00@mail.com","johnsmith@mail.com"]]
Output: [["john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]]
```

## Key Takeaways
- Use Union-Find algorithm to manage connections between emails.
- Use depth-first search to traverse all the connected components and merge the accounts.
- Sort the emails within each account and the accounts themselves in lexicographical order.