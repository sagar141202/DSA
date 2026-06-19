# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order of the letters is unknown. We are given a list of words in this language, where each word is a string of lowercase letters. The task is to determine the order of the letters in the alien alphabet. We can assume that the input is valid and that the order of the letters can be uniquely determined. For example, if we are given the words ["wrt", "wrf", "er", "ett", "rftt"], we can determine that the order of the letters is "w-e-r-t-f".

## Approach
The approach to solve this problem is to use topological sorting on a graph where each node represents a letter and each edge represents the order of the letters. We can build the graph by comparing each pair of words in the input list. The algorithm will then find a valid order of the letters that satisfies all the constraints.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is bounded by the size of the alphabet (26 letters)

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
    }
    // Topological sorting
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
    // Check for cycle
    if (result.size() != indegree.size()) {
        return {};
    }
    return result;
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> order = alienOrder(words);
    for (char c : order) {
        cout << c << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: ["w", "e", "r", "t", "f"]
```

## Key Takeaways
- Use topological sorting to find a valid order of the letters in the alien alphabet.
- Build a graph where each node represents a letter and each edge represents the order of the letters.
- Check for cycle in the graph to ensure a valid order exists.