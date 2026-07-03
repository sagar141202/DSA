# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the order of the letters is "w-e-r-t-f" (because "wrt" comes before "wrf" which means 't' comes before 'f' in the alien language). If the order is invalid (i.e., the given words do not satisfy the lexicographical order), return an empty string. The length of each word is between 1 and 10, and there are at most 26 letters in the alien alphabet.

## Approach
The problem can be solved using a topological sorting algorithm with a directed acyclic graph (DAG). We create a graph where each node represents a letter in the alphabet, and a directed edge from node A to node B means A comes before B in the alien language. We then perform a topological sort on the graph to determine the order of the letters.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the space complexity is constant (at most 26 nodes in the graph)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph where each node represents a letter in the alphabet
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
        
        // Build the graph and update the indegree map
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
            if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
                return "";
            }
        }
        
        // Perform a topological sort on the graph
        queue<char> q;
        for (const auto& pair : indegree) {
            if (pair.second == 0) {
                q.push(pair.first);
            }
        }
        
        string order;
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            order += c;
            for (char neighbor : graph[c]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If there are remaining nodes with non-zero indegree, the order is invalid
        if (order.size() != graph.size()) {
            return "";
        }
        
        return order;
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
Output: "" (invalid order)
```

## Key Takeaways
- Topological sorting can be used to solve problems involving ordering or sequencing.
- A directed acyclic graph (DAG) can be used to model the relationships between nodes in a problem.
- The indegree of a node in a graph can be used to determine the order of the nodes in a topological sort.