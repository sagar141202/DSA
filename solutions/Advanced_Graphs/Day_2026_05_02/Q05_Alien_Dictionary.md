# Alien Dictionary

## Problem Statement
There is a new alien language which uses the Latin alphabet. However, the order among the letters is unknown to you. You receive an array of strings which are words in this new alien language. Each word is compared to its adjacent word and the first different character will indicate the order. For example, if there are two words "wrt" and "wrf", then 't' and 'f' are in the order 't' -> 'f'. If the words are the same length, then the word that comes later in the list will be smaller. The task is to determine the correct order of the letters in the alien alphabet. If there is no valid order, return an empty string. The input will be a list of strings, and the output should be a string representing the correct order of the letters.

## Approach
We can use a topological sorting algorithm to solve this problem, where each letter is a node and the edges represent the order of the letters. We will use a depth-first search (DFS) or breadth-first search (BFS) to perform the topological sorting. The algorithm will iterate over the list of words, compare adjacent words, and build the graph.

## Complexity
- Time: O(N * M + 26 * 26)
- Space: O(26 * 26 + 26)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Build the graph
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;
    for (const string& word : words) {
        for (char c : word) {
            if (indegree.find(c) == indegree.end()) {
                indegree[c] = 0;
            }
        }
    }
    
    for (int i = 0; i < words.size() - 1; i++) {
        const string& word1 = words[i];
        const string& word2 = words[i + 1];
        int len = min(word1.length(), word2.length());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                if (graph[word1[j]].find(word2[j]) == graph[word1[j]].end()) {
                    graph[word1[j]].insert(word2[j]);
                    indegree[word2[j]]++;
                }
                break;
            }
        }
        // If word1 is longer than word2, and word1 is not a prefix of word2, then there is no valid order
        if (word1.length() > word2.length() && word1.substr(0, word2.length()) == word2) {
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
    
    vector<char> result;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result.push_back(c);
        for (char neighbor : graph[c]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // If there is a cycle, then there is no valid order
    if (result.size() != indegree.size()) {
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
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

## Key Takeaways
- We use a topological sorting algorithm to solve this problem.
- We build a graph where each letter is a node and the edges represent the order of the letters.
- We use a queue to perform the topological sorting, where we start with nodes that have no incoming edges.