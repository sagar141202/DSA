# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words from this language, where the words are sorted lexicographically in this alien language. Determine the order of the letters in this alien language. The list of words is given as an array of strings, and there may be multiple possible orders. The input array will contain at least one word, and all words will contain only lowercase English letters. For example, given the following array of words ["wrt", "wrf", "er", "ett", "rftt"], the alien dictionary order is "wertf".

## Approach
The approach to solve this problem is to use a topological sorting algorithm with a directed graph. We create a graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien dictionary. We then perform a topological sort on this graph to find the order of the letters.

## Complexity
- Time: O(N * M + 26 * 26) where N is the number of words and M is the maximum length of a word
- Space: O(26 * 26 + 26) where 26 is the number of letters in the alphabet

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph where each node represents a letter
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> inDegree;
    
    // Initialize the graph and in-degree map
    for (const auto& word : words) {
        for (char c : word) {
            if (graph.find(c) == graph.end()) {
                graph[c] = {};
                inDegree[c] = 0;
            }
        }
    }
    
    // Build the graph and update in-degrees
    for (int i = 0; i < words.size() - 1; i++) {
        const auto& word1 = words[i];
        const auto& word2 = words[i + 1];
        
        // Find the first different character
        int j = 0;
        while (j < word1.size() && j < word2.size() && word1[j] == word2[j]) {
            j++;
        }
        
        // If word1 is a prefix of word2, the graph should be empty
        if (j == word1.size() && j < word2.size()) {
            return {};
        }
        
        // Add an edge from the character in word1 to the character in word2
        if (j < word1.size() && j < word2.size()) {
            graph[word1[j]].insert(word2[j]);
            inDegree[word2[j]]++;
        }
    }
    
    // Perform a topological sort on the graph
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
    
    // If the graph has a cycle, return an empty vector
    if (order.size() != graph.size()) {
        return {};
    }
    
    return order;
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> order = alienOrder(words);
    
    if (order.empty()) {
        cout << "No valid order" << endl;
    } else {
        for (char c : order) {
            cout << c;
        }
        cout << endl;
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
Output: "" (no valid order)
```

## Key Takeaways
- Use a topological sorting algorithm to find the order of the letters in the alien dictionary
- The graph should be a directed acyclic graph (DAG) for a valid order to exist
- If the graph has a cycle, there is no valid order for the letters in the alien dictionary