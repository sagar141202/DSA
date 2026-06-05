# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty strings of the alien language, where each string is sorted lexicographically. Determine the order of the letters in the alien language's alphabet.

## Approach
The approach to solve this problem is to use a topological sorting algorithm on a directed graph, where each node represents a letter in the alphabet, and each edge represents the lexicographical order between two letters. The algorithm will find a valid ordering of the letters that satisfies the given constraints.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the space complexity is constant with respect to the input size, considering the size of the alphabet is fixed (26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph
        unordered_map<char, unordered_set<char>> graph;
        // Initialize the indegree of each node
        unordered_map<char, int> indegree;
        
        // Populate the graph and indegree
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            int len = min(word1.size(), word2.size());
            for (int j = 0; j < len; j++) {
                if (word1[j] != word2[j]) {
                    // Add an edge from word1[j] to word2[j]
                    graph[word1[j]].insert(word2[j]);
                    // Increase the indegree of word2[j]
                    indegree[word2[j]]++;
                    break;
                }
            }
            // If word2 is a prefix of word1, return an empty string
            if (word1.size() > word2.size() && word1.substr(0, len) == word2.substr(0, len)) {
                return "";
            }
        }
        
        // Add all unique characters to the graph
        for (const string& word : words) {
            for (char c : word) {
                if (graph.find(c) == graph.end()) {
                    graph[c] = {};
                }
                if (indegree.find(c) == indegree.end()) {
                    indegree[c] = 0;
                }
            }
        }
        
        // Perform topological sorting
        string result;
        queue<char> q;
        for (const auto& pair : indegree) {
            if (pair.second == 0) {
                q.push(pair.first);
            }
        }
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            result += c;
            for (char neighbor : graph[c]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If the result length is not equal to the number of unique characters, return an empty string
        if (result.size() != graph.size()) {
            return "";
        }
        
        return result;
    }
};

```

## Test Cases
```
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Input: ["z","x"]
Output: "zx"
Input: ["z","x","z"]
Output: "" (invalid input)
```

## Key Takeaways
- The problem requires a topological sorting of the graph, which can be achieved using a queue to keep track of nodes with an indegree of 0.
- The graph is represented as an adjacency list, where each node is a character in the alien language, and each edge represents the lexicographical order between two characters.
- The algorithm returns an empty string if the input is invalid (i.e., there is a cycle in the graph or a word is a prefix of another word).