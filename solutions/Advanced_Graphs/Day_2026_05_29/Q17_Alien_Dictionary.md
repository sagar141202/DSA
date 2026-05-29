# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. For example, if the list of words is ["wrt", "wrf", "er", "ett", "rftt"], the order of the letters is "wertf". If the list of words is ["z", "x"], the order of the letters is "zx". If the list of words is ["z", "x", "z"], the order is invalid, so return an empty string. The length of the list of words is in the range [1, 100], and the length of each word is in the range [1, 100].

## Approach
The solution uses a topological sorting algorithm with a directed graph, where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien alphabet. The in-degree of each node is used to keep track of the number of edges entering the node. The algorithm iterates over the list of words, comparing adjacent words and adding edges to the graph as necessary.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited to 26 nodes (one for each letter of the alphabet)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string alienOrder(vector<string>& words) {
    // Create a graph with 26 nodes (one for each letter)
    vector<vector<int>> graph(26);
    vector<int> inDegree(26, 0);

    // Initialize the graph and in-degree array
    for (const string& word : words) {
        for (char c : word) {
            inDegree[c - 'a'] = 0;
        }
    }

    // Build the graph and update the in-degree array
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        int len = min(word1.size(), word2.size());

        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                // Add an edge from the character in word1 to the character in word2
                graph[word1[j] - 'a'].push_back(word2[j] - 'a');
                inDegree[word2[j] - 'a']++;
                break;
            }
        }

        // If word2 is a prefix of word1, the order is invalid
        if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
            return "";
        }
    }

    // Perform topological sorting
    queue<int> q;
    for (int i = 0; i < 26; i++) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    string order;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order += (char)('a' + node);

        for (int neighbor : graph[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // If the order is not complete, the graph has a cycle and the order is invalid
    if (order.size() != count_if(inDegree.begin(), inDegree.end(), [](int x) { return x >= 0; })) {
        return "";
    }

    return order;
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
- The in-degree of each node is used to keep track of the number of edges entering the node.
- The algorithm iterates over the list of words, comparing adjacent words and adding edges to the graph as necessary.