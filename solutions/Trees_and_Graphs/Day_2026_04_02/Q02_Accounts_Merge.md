# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The accounts should be merged in a way that the emails in the merged account are unique and sorted. The problem statement can be formalized as follows: 
- There are n accounts.
- Each account is a list of m emails.
- Two accounts are considered the same if they have at least one common email.
- The task is to merge the accounts and return a list of merged accounts.
- The constraint is that the emails in the merged account should be unique and sorted.

## Approach
The approach to solve this problem is to use a Union-Find data structure to group the accounts that have the same email. Then, for each group, merge the emails and sort them. The Union-Find data structure will help us to efficiently find the group of an account and merge two groups.

## Complexity
- Time: O(N * M * logM) where N is the number of accounts and M is the maximum number of emails in an account.
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
        parent[find(x)] = find(y);
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
    unordered_map<int, set<string>> groups;
    for (const auto& pair : emailToIndex) {
        int group = uf.find(pair.second);
        groups[group].insert(pair.first);
    }
    vector<vector<string>> result;
    for (const auto& pair : groups) {
        vector<string> emails(pair.second.begin(), pair.second.end());
        sort(emails.begin(), emails.end());
        emails.insert(emails.begin(), "dummy");
        result.push_back(emails);
    }
    return result;
}

int main() {
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                       {"John", "johnnybravo@mail.com"}, 
                                       {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
                                       {"Mary", "mary@mail.com"}};
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
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["John", "johnnybravo@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- We use a Union-Find data structure to group the accounts that have the same email.
- We use an unordered_map to store the email to index mapping for efficient lookup.
- We use a set to store the emails in each group to ensure uniqueness and efficient insertion.
- The time complexity is O(N * M * logM) due to the sorting of emails in each group.