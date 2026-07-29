# Alien Dictionary

## Problem Statement
There is a new alien language which uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words from this language, where the words are sorted lexicographically in this alien language. Determine the order of the letters in this alien language. The words in the input list are all in lowercase and are composed of letters from the English alphabet. If there is no valid order, return an empty string. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf".

## Approach
The approach to solve this problem is to use a topological sorting algorithm on a directed graph, where each node represents a letter and each edge represents the ordering between two letters. We can build this graph by comparing adjacent words in the input list. The resulting order of the letters will be the topological sorting of this graph.

## Complexity
- Time: O(N * M + 26 * log(26))
- Space: O(26 + N * M)

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
        
        for (char c = 'a'; c <= 'z'; c++) {
            indegree[c] = 0;
        }
        
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            
            int len = min(word1.size(), word2.size());
            
            for (int j = 0; j < len; j++) {
                if (word1[j] != word2[j]) {
                    if (graph[word1[j]].find(word2[j]) == graph[word1[j]].end()) {
                        graph[word1[j]].insert(word2[j]);
                        indegree[word2[j]]++;
                    }
                    break;
                }
            }
            
            if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
                return "";
            }
        }
        
        // Topological sorting
        queue<char> q;
        string order;
        
        for (char c = 'a'; c <= 'z'; c++) {
            if (indegree[c] == 0) {
                q.push(c);
            }
        }
        
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
        
        // Check if there is a cycle
        if (order.size() != 26) {
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
```

## Key Takeaways
- The alien dictionary problem can be solved using a topological sorting algorithm on a directed graph.
- We need to build the graph by comparing adjacent words in the input list and then perform topological sorting to get the order of the letters.
- If there is a cycle in the graph, it means there is no valid order and we should return an empty string.