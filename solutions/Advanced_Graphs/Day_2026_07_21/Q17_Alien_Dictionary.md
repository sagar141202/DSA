# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words from this language, where the words are sorted lexicographically. Determine the order of the letters in this alien language. The input is a list of strings, and the output should be a string representing the order of the letters. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the output should be "wertf". If the input is invalid (i.e., it is not possible to determine the order of the letters), the function should return an empty string.

## Approach
The approach is to use topological sorting with a graph data structure. We create a directed graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien dictionary. Then, we perform a topological sort on the graph to get the order of the letters.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited by the size of the alphabet (26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string alienOrder(vector<string>& words) {
    // Create a graph where each node represents a letter
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> inDegree;
    
    // Initialize the graph and in-degree map
    for (const string& word : words) {
        for (char c : word) {
            if (graph.find(c) == graph.end()) {
                graph[c] = {};
                inDegree[c] = 0;
            }
        }
    }
    
    // Build the graph and update in-degrees
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        int len = min(word1.size(), word2.size());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                if (graph[word1[j]].find(word2[j]) == graph[word1[j]].end()) {
                    graph[word1[j]].insert(word2[j]);
                    inDegree[word2[j]]++;
                }
                break;
            }
        }
        // Check if word1 is a prefix of word2
        if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
            return "";
        }
    }
    
    // Perform topological sorting
    queue<char> q;
    for (const auto& pair : inDegree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }
    
    string result;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result += c;
        for (char neighbor : graph[c]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // Check if all nodes are visited
    if (result.size() != graph.size()) {
        return "";
    }
    
    return result;
}

```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
Input: ["z", "x"]
Output: "zx"
Input: ["z", "x", "z"]
Output: "" (invalid input)
```

## Key Takeaways
- Topological sorting can be used to solve problems involving ordering or scheduling.
- When building the graph, it's essential to consider the direction of the edges to ensure correct ordering.
- Checking for invalid input is crucial to handle edge cases and provide accurate results.