# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The output should be a list of merged accounts. Each merged account should contain all the emails from the original accounts. The order of the emails in the merged account does not matter. For example, if we have two accounts ["account1@example.com", "account2@example.com"] and ["account2@example.com", "account3@example.com"], they should be merged into one account ["account1@example.com", "account2@example.com", "account3@example.com"]. The input is a 2D vector of strings where each inner vector represents an account and each string represents an email.

## Approach
We will use a graph to model the problem, where each email is a node and two nodes are connected if they are in the same account. Then we will use depth-first search (DFS) to find all the connected components in the graph, which represent the merged accounts.

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
        
        // Perform DFS
        vector<vector<string>> result;
        unordered_set<string> visited;
        for (auto& account : accounts) {
            string email = account[1];
            if (visited.find(email) == visited.end()) {
                vector<string> mergedAccount;
                dfs(graph, email, visited, mergedAccount);
                // Add the name to the merged account
                mergedAccount.insert(mergedAccount.begin(), emailToName[email]);
                result.push_back(mergedAccount);
            }
        }
        
        return result;
    }
    
    void dfs(unordered_map<string, set<string>>& graph, string email, unordered_set<string>& visited, vector<string>& mergedAccount) {
        visited.insert(email);
        mergedAccount.push_back(email);
        for (auto& neighbor : graph[email]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(graph, neighbor, visited, mergedAccount);
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
- Use a graph to model the problem where each email is a node and two nodes are connected if they are in the same account.
- Use DFS to find all the connected components in the graph, which represent the merged accounts.
- Use an unordered_map to store the email to name mapping and another unordered_map to store the graph.