# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words from this alien language, where the words are sorted lexicographically in the alien language. Determine the order of the letters in this alien language. The order should be represented as a string of letters in the correct order. If the order is invalid (i.e., it is not possible to order the letters such that the given words are sorted lexicographically), return an empty string. For example, if the input is ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf".

## Approach
The problem can be solved by constructing a graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien dictionary. We use topological sorting to find the order of the letters. If a cycle is detected, the order is invalid.

## Complexity
- Time: O(N * M)
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph where each node is a letter
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> indegree;
        
        // Initialize the graph and indegree map
        for (const string& word : words) {
            for (char c : word) {
                if (graph.find(c) == graph.end()) {
                    graph[c] = {};
                    indegree[c] = 0;
                }
            }
        }
        
        // Build the graph
        for (int i = 0; i < words.size() - 1; i++) {
            const string& word1 = words[i];
            const string& word2 = words[i + 1];
            int len = min(word1.size(), word2.size());
            for (int j = 0; j < len; j++) {
                if (word1[j] != word2[j]) {
                    graph[word1[j]].insert(word2[j]);
                    indegree[word2[j]]++;
                    break;
                }
            }
            // If word1 is a prefix of word2, the order is invalid
            if (word1.size() > word2.size() && word1.substr(0, len) == word2.substr(0, len)) {
                return "";
            }
        }
        
        // Perform topological sorting
        queue<char> q;
        for (const auto& pair : indegree) {
            if (pair.second == 0) {
                q.push(pair.first);
            }
        }
        string order;
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            order += c;
            for (char neighbor : graph[c]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If the order is invalid, return an empty string
        if (order.size() != graph.size()) {
            return "";
        }
        return order;
    }
};
```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
Input: ["z", "x"]
Output: "zx"
Input: ["z", "x", "z"]
Output: ""
```

## Key Takeaways
- The problem can be solved using graph theory and topological sorting.
- We need to handle the case where the order is invalid (i.e., it is not possible to order the letters such that the given words are sorted lexicographically).
- The time complexity is O(N * M), where N is the number of words and M is the maximum length of a word.