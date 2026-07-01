# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are ordered such that for each pair of adjacent words, the first word must be lexicographically smaller than the second word. Determine the order of the letters in the alien alphabet.

## Approach
The problem can be solved using a topological sorting algorithm. We create a graph where each node represents a letter, and a directed edge from node A to node B means that A must come before B in the alien alphabet. We then perform a topological sort on the graph to find the order of the letters.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited to 26 nodes (one for each letter)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph where each node represents a letter
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
        
        // Build the graph and update indegrees
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
            // If word1 is a prefix of word2, the input is invalid
            if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
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
        
        string result;
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
        
        // If there are remaining nodes with non-zero indegree, the graph has a cycle
        if (result.size() != indegree.size()) {
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
```

## Key Takeaways
- The alien dictionary problem can be solved using a topological sorting algorithm.
- We need to handle the case where the input is invalid (e.g., a word is a prefix of another word).
- The time complexity is O(N*M) and the space complexity is O(1), where N is the number of words and M is the maximum length of a word.