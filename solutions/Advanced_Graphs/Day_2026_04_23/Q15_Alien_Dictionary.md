# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the alien alphabet is "wertf". If the order cannot be determined, return an empty string. The input is a list of strings, and each string consists of lowercase English letters. The length of the input list is in the range [1, 100], and the length of each string is in the range [1, 100].

## Approach
We can use topological sorting to solve this problem. We create a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet. We then perform a topological sort on the graph to get the order of the letters.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the size of the graph is limited by the size of the alphabet (26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
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
    
    // Build the graph
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
        // If word1 is a prefix of word2, the order is invalid
        if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
            return {};
        }
    }
    
    // Perform topological sorting
    queue<char> q;
    for (const auto& pair : indegree) {
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
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // If the order is not complete, the input is invalid
    if (order.size() != graph.size()) {
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
Output: ""
```

## Key Takeaways
- Use topological sorting to solve the problem.
- The graph should be built carefully to reflect the order of the letters in the alien alphabet.
- The input is invalid if the order cannot be determined.