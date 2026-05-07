# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. If there are multiple possible orders, return any of them. If the given list of words is invalid (i.e., it is not possible to have a valid order), return an empty string. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf".

## Approach
The problem can be solved using a topological sorting algorithm with a graph data structure. We create a directed graph where each node represents a letter in the alien alphabet, and there is a directed edge from node A to node B if A comes before B in the alien alphabet. We then perform a topological sort on the graph to obtain the order of the letters.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is bounded by the size of the alphabet (26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph where each node is a letter
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
                graph[word1[j]].insert(word2[j]);
                inDegree[word2[j]]++;
                break;
            }
        }
        
        // If word1 is a prefix of word2, the input is invalid
        if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
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
    
    // If there are remaining nodes with non-zero in-degree, the input is invalid
    if (result.size() != graph.size()) {
        return {};
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
Output: "" (invalid input)
```

## Key Takeaways
- Use topological sorting to solve the problem
- Build a graph where each node represents a letter and each edge represents the order between two letters
- Check for invalid inputs by verifying the prefix condition and the existence of a valid topological ordering