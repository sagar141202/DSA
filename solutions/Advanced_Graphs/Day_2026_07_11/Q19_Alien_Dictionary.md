# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. If there are multiple valid orders, return any of them. If the input is invalid (i.e., it is not possible to order the letters), return an empty string. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf".

## Approach
The problem can be solved by using a topological sorting algorithm on a directed graph, where each letter is a node and there is a directed edge from one letter to another if the first letter appears before the second letter in the alien dictionary. The algorithm checks for cycles in the graph to ensure a valid order exists.

## Complexity
- Time: O(N * M)
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph and in-degree map
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> inDegree;
    
    // Initialize the graph and in-degree map
    for (const string& word : words) {
        for (char c : word) {
            if (inDegree.find(c) == inDegree.end()) {
                inDegree[c] = 0;
            }
        }
    }
    
    // Build the graph
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        
        int minLen = min(word1.size(), word2.size());
        for (int j = 0; j < minLen; j++) {
            if (word1[j] != word2[j]) {
                graph[word1[j]].insert(word2[j]);
                inDegree[word2[j]]++;
                break;
            }
        }
        
        // If word1 is a prefix of word2, the input is invalid
        if (word1.size() > word2.size() && word1.substr(0, minLen) == word2.substr(0, minLen)) {
            return {};
        }
    }
    
    // Perform topological sorting
    queue<char> q;
    for (const auto& pair : inDegree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }
    
    vector<char> order;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        order.push_back(c);
        
        for (char neighbor : graph[c]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // If there are remaining nodes with non-zero in-degree, the input is invalid
    if (order.size() != inDegree.size()) {
        return {};
    }
    
    return order;
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> order = alienOrder(words);
    for (char c : order) {
        cout << c;
    }
    return 0;
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
- The alien dictionary problem can be solved using a topological sorting algorithm on a directed graph.
- The graph is built by comparing adjacent words in the input list and adding directed edges between letters that appear in the correct order.
- The algorithm checks for cycles in the graph to ensure a valid order exists, and returns an empty string if the input is invalid.