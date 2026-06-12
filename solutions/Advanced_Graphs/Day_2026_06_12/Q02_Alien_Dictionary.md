# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order among the letters is unknown to you. You receive a list of non-empty words from this language, where the words are sorted lexicographically in this alien language. Determine the order of the letters in this alien language. For example, if the input is ["wrt", "wrf", "er", "ett", "rftt"], the correct order of the letters is "wertf". The input list will not contain any duplicate words, and all words will only contain lowercase letters.

## Approach
The approach is to use a topological sorting algorithm with a directed graph, where each node represents a letter and a directed edge represents the order of the letters. We will first build the graph based on the given words, and then perform a topological sort to get the order of the letters.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the space complexity is dependent on the size of the alphabet which is constant

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
            if (graph.find(c) == graph.end()) {
                graph[c] = {};
                inDegree[c] = 0;
            }
        }
    }
    
    // Build the graph and update the in-degree map
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        int len = min(word1.size(), word2.size());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                graph[word1[j]].insert(word2[j]);
                inDegree[word2[j]]++;
                break;
            }
            if (j == len - 1 && word1.size() > word2.size()) {
                return {}; // Invalid input
            }
        }
    }
    
    // Perform topological sorting
    queue<char> q;
    for (const auto& pair : inDegree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }
    
    vector<char> result;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result.push_back(c);
        for (char neighbor : graph[c]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // Check if the result is valid
    if (result.size() != graph.size()) {
        return {}; // Invalid input
    }
    
    return result;
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
Output: ""
```

## Key Takeaways
- The alien dictionary problem can be solved using a topological sorting algorithm with a directed graph.
- The graph is built based on the given words, and the in-degree map is used to keep track of the in-degree of each node.
- The result is valid if and only if the size of the result is equal to the number of unique letters in the input words.