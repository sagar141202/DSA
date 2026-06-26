# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge the accounts that have the same email. The emails in each account are unique, and the emails in different accounts may be the same. The task is to group all the accounts that have at least one common email. For example, if we have two accounts ["account1", "email1", "email2"] and ["account2", "email2", "email3"], these two accounts should be merged because they have "email2" in common. The output should be a list of merged accounts where each account is a list of emails.

## Approach
The algorithm uses a graph to model the accounts and their connections. Each email is a node in the graph, and two nodes are connected if they appear in the same account. Then, it uses depth-first search (DFS) to find all connected components in the graph, which represent the merged accounts.

## Complexity
- Time: O(N * M) where N is the number of accounts and M is the average number of emails per account
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // Create a graph where each email is a node
        unordered_map<string, string> emailToName;
        unordered_map<string, vector<string>> graph;
        
        for (auto& account : accounts) {
            string name = account[0];
            for (int i = 1; i < account.size(); i++) {
                emailToName[account[i]] = name;
                if (i > 1) {
                    string prevEmail = account[i - 1];
                    string currEmail = account[i];
                    graph[prevEmail].push_back(currEmail);
                    graph[currEmail].push_back(prevEmail);
                }
            }
        }
        
        // Use DFS to find all connected components
        unordered_set<string> visited;
        vector<vector<string>> result;
        for (auto& account : accounts) {
            string email = account[1];
            if (!visited.count(email)) {
                vector<string> component;
                dfs(graph, email, visited, component);
                // Sort the emails in the component
                sort(component.begin(), component.end());
                component.insert(component.begin(), emailToName[email]);
                result.push_back(component);
            }
        }
        
        return result;
    }
    
    void dfs(unordered_map<string, vector<string>>& graph, string email, unordered_set<string>& visited, vector<string>& component) {
        visited.insert(email);
        component.push_back(email);
        for (auto& neighbor : graph[email]) {
            if (!visited.count(neighbor)) {
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
- We use an unordered_map to store the graph where each email is a node and its corresponding value is a vector of neighboring emails.
- We use DFS to traverse the graph and find all connected components, which represent the merged accounts.
- The time complexity is O(N * M) because we iterate over each account and each email in the account. The space complexity is also O(N * M) because in the worst case, we may need to store all emails in the graph.