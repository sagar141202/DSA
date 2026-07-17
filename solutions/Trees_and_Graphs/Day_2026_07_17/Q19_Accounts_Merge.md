# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The accounts should be merged in a way that the resulting merged account contains all the emails from the original accounts. The order of the emails in the merged account does not matter. For example, if we have two accounts `["account1", "email1", "email2"]` and `["account1", "email2", "email3"]`, the merged account should be `["account1", "email1", "email2", "email3"]`. The input is a list of accounts where each account is a list of strings. The output should be a list of merged accounts.

## Approach
We can use a graph to model the accounts and emails. Each email is a node in the graph, and two nodes are connected if they are in the same account. We can then use a depth-first search (DFS) to find all connected components in the graph, which represent the merged accounts.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the maximum number of emails in an account
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, string> emailToName;
        unordered_map<string, set<string>> graph;
        
        // Build the graph
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                graph[account[1]].insert(account[i]);
                graph[account[i]].insert(account[1]);
                emailToName[account[i]] = name;
            }
        }
        
        vector<vector<string>> result;
        set<string> seen;
        
        // Perform DFS
        for (auto& account : accounts) {
            string email = account[1];
            if (seen.find(email) == seen.end()) {
                seen.insert(email);
                vector<string> component;
                dfs(email, graph, seen, component);
                sort(component.begin(), component.end());
                component.insert(component.begin(), emailToName[email]);
                result.push_back(component);
            }
        }
        
        return result;
    }
    
    void dfs(string email, unordered_map<string, set<string>>& graph, set<string>& seen, vector<string>& component) {
        component.push_back(email);
        for (auto& neighbor : graph[email]) {
            if (seen.find(neighbor) == seen.end()) {
                seen.insert(neighbor);
                dfs(neighbor, graph, seen, component);
            }
        }
    }
};
```

## Test Cases
```
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use a graph to model the accounts and emails
- Perform DFS to find all connected components in the graph
- Use an unordered_map to store the graph and an unordered_set to keep track of visited nodes