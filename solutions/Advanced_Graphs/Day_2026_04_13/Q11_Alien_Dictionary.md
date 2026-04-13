# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words in the alien language, where each word is written in lowercase English letters. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet.

## Approach
The problem can be solved using a topological sorting algorithm. We will create a directed graph where each node represents a letter in the alphabet, and a directed edge from node A to node B means that A comes before B in the alien alphabet. We will then perform a topological sort on the graph to find the order of the letters.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited to 26 nodes (one for each letter in the alphabet)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph where each node represents a letter in the alphabet
        vector<vector<int>> graph(26);
        vector<int> indegree(26, 0);

        // Build the graph by comparing adjacent words
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            int len = min(word1.size(), word2.size());
            for (int j = 0; j < len; j++) {
                if (word1[j] != word2[j]) {
                    int u = word1[j] - 'a';
                    int v = word2[j] - 'a';
                    graph[u].push_back(v);
                    indegree[v]++;
                    break;
                }
            }
            // If word2 is a prefix of word1, the input is invalid
            if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
                return "";
            }
        }

        // Perform a topological sort on the graph
        queue<int> q;
        for (int i = 0; i < 26; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        string result;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result += (char)('a' + u);
            for (int v : graph[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        // If there is a cycle in the graph, the input is invalid
        if (result.size() != 26) {
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
Output: "" (invalid input)
```

## Key Takeaways
- The alien dictionary problem can be solved using a topological sorting algorithm.
- The graph is built by comparing adjacent words in the input list.
- The algorithm checks for invalid input, such as a word being a prefix of another word, or a cycle in the graph.