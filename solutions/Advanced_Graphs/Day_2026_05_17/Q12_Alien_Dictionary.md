# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written using the English alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. If there are multiple possible orders, return any of them. If the given words do not form a valid order, return an empty string. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the order of the letters in the alien alphabet is "wertf".

## Approach
The problem can be solved by building a graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien alphabet. We can then perform a topological sort on the graph to find the order of the letters. If a cycle is detected in the graph, we return an empty string.

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
        // Build the graph
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> indegree;
        
        for (const string& word : words) {
            for (char c : word) {
                if (graph.find(c) == graph.end()) {
                    graph[c] = {};
                    indegree[c] = 0;
                }
            }
        }
        
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
            
            // If word1 is a prefix of word2, return an empty string
            if (word1.size() > word2.size() && word1.substr(0, len) == word2.substr(0, len)) {
                return "";
            }
        }
        
        // Perform a topological sort
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
        
        // If the length of the order is not equal to the number of unique characters, return an empty string
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
- The problem can be solved by building a graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien alphabet.
- We can perform a topological sort on the graph to find the order of the letters.
- If a cycle is detected in the graph, we return an empty string.