# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order among the letters is unknown to you. You receive a list of words in the alien language, where words are sorted lexicographically. Determine the order of the letters in this alien language. The input is a list of strings, and the output should be a string representing the order of the letters. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf". If the input is ["z", "x"], the correct order is "zx". If the input is ["z", "x", "z"], the output should be an empty string, indicating that the input is invalid.

## Approach
We will use a topological sorting algorithm to solve this problem. The idea is to build a graph where each letter is a node, and there is a directed edge from one letter to another if the first letter comes before the second letter in the alien language. We will then use Kahn's algorithm to perform the topological sorting.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited by the size of the alphabet

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph where each letter is a node
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> inDegree;
    
    // Initialize the graph and in-degree map
    for (const string& word : words) {
        for (char c : word) {
            graph[c] = {};
            inDegree[c] = 0;
        }
    }
    
    // Build the graph by comparing adjacent words
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        int len = min(word1.length(), word2.length());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                // Add a directed edge from word1[j] to word2[j]
                graph[word1[j]].insert(word2[j]);
                inDegree[word2[j]]++;
                break;
            }
        }
        // If word1 is a prefix of word2, the input is invalid
        if (word1.length() > word2.length() && word1.substr(0, word2.length()) == word2) {
            return {};
        }
    }
    
    // Perform topological sorting using Kahn's algorithm
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
    
    // If the result does not contain all letters, the input is invalid
    if (result.size() != inDegree.size()) {
        return {};
    }
    
    return result;
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> result = alienOrder(words);
    for (char c : result) {
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
- Topological sorting can be used to solve problems that involve ordering nodes in a directed acyclic graph (DAG).
- Kahn's algorithm is a popular method for performing topological sorting.
- The alien dictionary problem requires careful handling of invalid inputs, such as words that are prefixes of other words.