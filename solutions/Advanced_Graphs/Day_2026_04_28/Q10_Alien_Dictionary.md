# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order of the letters is unknown to us. The aliens have provided a list of words in their language, where each word is compared to its adjacent word. The comparison result is either the two words are the same or the first word is lexicographically smaller than the second word. The goal is to determine the order of the letters in the alien language. The input will be a list of words, and the output will be a string representing the order of the letters. For example, if the input is ["wrt", "wrf", "er", "ett", "rftt"], the output will be "wertf".

## Approach
The problem can be solved using a topological sorting algorithm with a directed graph. The graph will have the letters as nodes, and a directed edge will be added from node A to node B if A comes before B in the alien language. The algorithm will then perform a topological sort on the graph to determine the order of the letters.

## Complexity
- Time: O(N * M + 26)
- Space: O(26 + N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph and in-degree map
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> inDegree;
        
        // Initialize the graph and in-degree map
        for (const string& word : words) {
            for (char c : word) {
                if (inDegree.find(c) == inDegree.end()) {
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
                    if (graph[word1[j]].find(word2[j]) == graph[word1[j]].end()) {
                        graph[word1[j]].insert(word2[j]);
                        inDegree[word2[j]]++;
                    }
                    break;
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
        
        // Check for cycle
        if (result.size() != inDegree.size()) {
            return "";
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    cout << solution.alienOrder(words) << endl;
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
- The problem can be solved using a topological sorting algorithm with a directed graph.
- The graph should have the letters as nodes, and a directed edge should be added from node A to node B if A comes before B in the alien language.
- The algorithm should perform a topological sort on the graph to determine the order of the letters.