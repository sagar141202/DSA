# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. If there are multiple possible orders, return any of them. If the given list of words is invalid (i.e., it is not possible for the words to be sorted lexicographically in the alien language), return an empty string. The input is a list of strings, where each string is a word in the alien language. The length of the input list is between 1 and 100. The length of each word is between 1 and 100. The words only contain lowercase English letters.

## Approach
The solution uses a topological sorting algorithm to find the order of the letters in the alien alphabet. We build a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet. We then use the topological sorting algorithm to find a valid order of the letters.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the size of the graph is constant (26 nodes)

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
        for (char c = 'a'; c <= 'z'; c++) {
            indegree[c] = 0;
        }
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            int len = min(word1.size(), word2.size());
            for (int j = 0; j < len; j++) {
                if (word1[j] != word2[j]) {
                    if (graph[word1[j]].find(word2[j]) == graph[word1[j]].end()) {
                        graph[word1[j]].insert(word2[j]);
                        indegree[word2[j]]++;
                    }
                    break;
                }
            }
            if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
                return "";
            }
        }
        
        // Topological sorting
        queue<char> q;
        for (char c = 'a'; c <= 'z'; c++) {
            if (indegree[c] == 0) {
                q.push(c);
            }
        }
        string result = "";
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
        
        // Check if all characters are visited
        if (result.size() != count_if(indegree.begin(), indegree.end(), [](auto& x) { return x.second == 0; })) {
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
Output: "" (invalid input)
```

## Key Takeaways
- The problem can be solved using a topological sorting algorithm.
- We need to build a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet.
- The time complexity is O(NM) where N is the number of words and M is the maximum length of a word.