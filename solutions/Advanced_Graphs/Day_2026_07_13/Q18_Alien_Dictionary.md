# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are not necessarily in alphabetical order in the alien language. Determine the order of the letters in the alien alphabet. For example, if the input is ["wrt", "wrf", "er", "ett", "rftt"], the output should be "wertf". The constraints are that the input list will contain at least one word and at most 100 words, and each word will contain at most 100 letters.

## Approach
The approach to solve this problem is to use a topological sorting algorithm, which is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering. The intuition is to build a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet.

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
        
        // Build the edges
        for (int i = 0; i < words.size() - 1; i++) {
            const string& word1 = words[i];
            const string& word2 = words[i + 1];
            int minLen = min(word1.size(), word2.size());
            for (int j = 0; j < minLen; j++) {
                if (word1[j] != word2[j]) {
                    graph[word1[j]].insert(word2[j]);
                    indegree[word2[j]]++;
                    break;
                }
            }
            if (word1.size() > word2.size() && word1.substr(0, minLen) == word2) {
                return "";
            }
        }
        
        // Topological sorting
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
        
        if (result.size() != graph.size()) {
            return "";
        }
        
        return result;
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
- Use topological sorting to solve the problem.
- Build a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet.
- Check for invalid inputs, such as when a word is a prefix of another word but they are not in the correct order.