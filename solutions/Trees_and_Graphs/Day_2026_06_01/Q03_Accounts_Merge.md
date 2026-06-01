# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The result should be a list of merged accounts, where each account is a list of sorted emails. If two accounts have the same email, they are owned by the same person. The emails in each account should be sorted, and the merged accounts should be returned in the order they were first encountered in the input. For example, if the input is `[["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"]]`, the output should be `[["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"]]`.

## Approach
We can solve this problem using a graph data structure, where each email is a node and two nodes are connected if they are in the same account. Then we can use depth-first search (DFS) to find all connected components in the graph, which represent the merged accounts.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // Create a graph where each email is a node and two nodes are connected if they are in the same account
        unordered_map<string, string> emailToName;
        unordered_map<string, unordered_set<string>> graph;
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                emailToName[account[i]] = name;
                graph[account[1]].insert(account[i]);
                graph[account[i]].insert(account[1]);
            }
        }

        // Use DFS to find all connected components in the graph
        vector<vector<string>> result;
        unordered_set<string> visited;
        for (auto& account : accounts) {
            string email = account[1];
            if (!visited.count(email)) {
                visited.insert(email);
                vector<string> component;
                dfs(graph, email, visited, component);
                // Sort the emails in the component
                sort(component.begin(), component.end());
                // Add the name to the component
                component.insert(component.begin(), emailToName[email]);
                result.push_back(component);
            }
        }

        return result;
    }

    void dfs(unordered_map<string, unordered_set<string>>& graph, string email, unordered_set<string>& visited, vector<string>& component) {
        component.push_back(email);
        for (auto& neighbor : graph[email]) {
            if (!visited.count(neighbor)) {
                visited.insert(neighbor);
                dfs(graph, neighbor, visited, component);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<vector<string>> accounts = {{"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
                                      {"John", "johnsmith@mail.com", "john00@mail.com"}, 
                                      {"Mary", "mary@mail.com"}};
    vector<vector<string>> result = solution.accountsMerge(accounts);
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
Input: [["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["Mary", "mary@mail.com"]]
```

## Key Takeaways
- Use a graph data structure to model the relationships between emails.
- Use depth-first search (DFS) to find all connected components in the graph, which represent the merged accounts.
- Sort the emails in each merged account and add the name to the account.