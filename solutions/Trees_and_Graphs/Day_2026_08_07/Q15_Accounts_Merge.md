# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The accounts are merged by taking the union of all the emails in the accounts and sorting them. The task is to return a list of the merged accounts. For example, if we have the following accounts: `[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]`. The number of accounts is at most 1000, and the length of each account is at most 1000.

## Approach
We can use a graph to model the problem where each email is a node and two nodes are connected if they are in the same account. Then we can use depth-first search (DFS) to find all the connected components in the graph, which represent the merged accounts.

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
        // Create a graph where each email is a node and two nodes are connected if they are in the same account
        unordered_map<string, vector<string>> graph;
        unordered_map<string, string> emailToName;
        for (const auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                graph[account[i]].push_back(account[i - 1]);
                graph[account[i - 1]].push_back(account[i]);
                emailToName[account[i]] = name;
            }
        }

        // Use DFS to find all the connected components in the graph
        unordered_set<string> visited;
        vector<vector<string>> result;
        for (const auto& account : accounts) {
            string email = account[1];
            if (!visited.count(email)) {
                vector<string> mergedAccount;
                dfs(graph, emailToName, visited, mergedAccount, email);
                // Sort the merged account and add it to the result
                sort(mergedAccount.begin(), mergedAccount.end());
                mergedAccount.insert(mergedAccount.begin(), emailToName[email]);
                result.push_back(mergedAccount);
            }
        }

        return result;
    }

    void dfs(unordered_map<string, vector<string>>& graph, unordered_map<string, string>& emailToName, unordered_set<string>& visited, vector<string>& mergedAccount, string email) {
        visited.insert(email);
        mergedAccount.push_back(email);
        for (const auto& neighbor : graph[email]) {
            if (!visited.count(neighbor)) {
                dfs(graph, emailToName, visited, mergedAccount, neighbor);
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
- Use a graph to model the problem where each email is a node and two nodes are connected if they are in the same account.
- Use DFS to find all the connected components in the graph, which represent the merged accounts.
- Sort the merged account and add it to the result.