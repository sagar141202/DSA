# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, however, the order of the letters is unknown to us. The alien language has a dictionary where each word is a valid word in the alien language. Given a list of words in the alien dictionary, determine the order of the letters in the alien alphabet. The order of the letters can be determined by comparing adjacent words in the dictionary. If a word is a prefix of another word, then the word should come before the other word in the dictionary. For example, if the dictionary contains the words "apple" and "app", then "app" should come before "apple". The dictionary is sorted in ascending order. The input is a list of strings, where each string is a word in the alien dictionary. The output should be a string representing the order of the letters in the alien alphabet. If the input is invalid, return an empty string. The constraints are: 1 <= words.length <= 100, 1 <= words[i].length <= 100, words[i] consists of only lowercase English letters.

## Approach
The approach to solve this problem is to use a topological sorting algorithm with a directed graph. We create a graph where each node represents a letter in the alphabet, and a directed edge from node A to node B means that A comes before B in the alien alphabet. We then perform a topological sort on the graph to get the order of the letters.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is fixed (26 nodes for 26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph where each node represents a letter in the alphabet
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
            }
            // If word1 is a prefix of word2, then the input is invalid
            if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
                return "";
            }
        }
        
        // Perform a topological sort on the graph
        queue<char> q;
        for (const auto& pair : inDegree) {
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
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If the result length is not equal to the number of unique letters, then the input is invalid
        if (result.size() != graph.size()) {
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
Input: ["z","x"]
Output: "zx"
Input: ["z","x","z"]
Output: ""
```

## Key Takeaways
- Use a topological sorting algorithm to solve this problem.
- The graph should be a directed graph where each node represents a letter in the alphabet.
- The in-degree map is used to keep track of the number of incoming edges for each node.