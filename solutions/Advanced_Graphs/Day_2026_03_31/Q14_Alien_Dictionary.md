# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in lowercase English letters. The list of words is sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. If there are multiple valid orders, return any of them. If the input is invalid (i.e., it is not possible to have a valid order), return an empty string. For example, if the input is ["wrt", "wrf", "er", "ett", "rftt"], the output should be "wertf".

## Approach
The problem can be solved by building a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien alphabet. We can then use a topological sort to find the order of the letters.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is fixed (26 nodes)

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
        int j = 0;
        while (j < word1.size() && j < word2.size() && word1[j] == word2[j]) {
            j++;
        }
        if (j < word1.size() && j < word2.size()) {
            graph[word1[j]].insert(word2[j]);
            indegree[word2[j]]++;
        } else if (j == word2.size() && word1.size() > word2.size()) {
            // Invalid input
            return {};
        }
    }

    // Topological sort
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
    if (result.size() != indegree.size()) {
        // Invalid input
        return {};
    }
    return result;
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
- Use a graph to represent the order of the letters in the alien alphabet
- Use a topological sort to find the order of the letters
- Check for invalid input by verifying that the resulting order has the same number of letters as the input words.