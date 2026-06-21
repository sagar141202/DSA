# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. Each email should only appear once in the merged account. The order of the emails in the merged account does not matter. Two accounts are merged if they share a common email. The input is a list of accounts where each account is a list of strings representing emails. The output is a list of merged accounts.

## Approach
The problem can be solved using a graph where each email is a node and two nodes are connected if they appear in the same account. Then, we can use depth-first search (DFS) to find all connected components in the graph. Each connected component represents a merged account.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the maximum number of emails in an account
- Space: O(N * M) for storing the graph and the visited set

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // Create a graph where each email is a node and two nodes are connected if they appear in the same account
        unordered_map<string, unordered_set<string>> graph;
        unordered_map<string, string> emailToName;
        
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                graph[account[i]].insert(account[i]);
                emailToName[account[i]] = name;
                for (int j = 1; j < account.size(); j++) {
                    if (i != j) {
                        graph[account[i]].insert(account[j]);
                        graph[account[j]].insert(account[i]);
                    }
                }
            }
        }
        
        // Use DFS to find all connected components in the graph
        unordered_set<string> visited;
        vector<vector<string>> result;
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
    
    void dfs(unordered_map<string, unordered_set<string>>& graph, string email, unordered_set<string>& visited, vector<string>& emails) {
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
- Use a graph to model the relationships between emails
- Use DFS to find all connected components in the graph
- Sort the emails in each merged account to ensure consistency