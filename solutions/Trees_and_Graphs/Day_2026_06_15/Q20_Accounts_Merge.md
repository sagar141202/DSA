# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The result should be a list of merged accounts, where each merged account is a list of emails in sorted order. The input is a list of accounts, where each account is a list of strings representing the account name and the emails associated with it. The output should be a list of merged accounts. For example, if the input is `[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]`.

## Approach
The approach is to use a graph to model the relationships between the emails, where each email is a node and two nodes are connected if they appear in the same account. Then, we can use a depth-first search (DFS) to traverse the graph and merge the accounts.

## Complexity
- Time: O(N * M * log(M))
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // Create a graph to model the relationships between the emails
        unordered_map<string, vector<string>> graph;
        unordered_map<string, string> emailToName;
        
        // Build the graph
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                graph[account[i]].clear();
                emailToName[account[i]] = name;
            }
            for (int i = 1; i < account.size(); i++) {
                for (int j = i + 1; j < account.size(); j++) {
                    graph[account[i]].push_back(account[j]);
                    graph[account[j]].push_back(account[i]);
                }
            }
        }
        
        // Use a DFS to traverse the graph and merge the accounts
        vector<vector<string>> result;
        unordered_set<string> visited;
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                if (visited.find(account[i]) == visited.end()) {
                    vector<string> emails;
                    dfs(graph, account[i], visited, emails);
                    sort(emails.begin(), emails.end());
                    emails.insert(emails.begin(), name);
                    result.push_back(emails);
                }
            }
        }
        
        return result;
    }
    
    void dfs(unordered_map<string, vector<string>>& graph, string email, unordered_set<string>& visited, vector<string>& emails) {
        visited.insert(email);
        emails.push_back(email);
        for (auto& neighbor : graph[email]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(graph, neighbor, visited, emails);
            }
        }
    }
};
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use a graph to model the relationships between the emails.
- Use a DFS to traverse the graph and merge the accounts.
- Use an unordered_set to keep track of the visited emails.