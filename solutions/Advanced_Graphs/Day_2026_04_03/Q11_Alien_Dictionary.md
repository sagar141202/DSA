# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order of the letters is unknown. We are given a list of words in this alien language, and we need to determine the order of the letters. The words are sorted lexicographically in the alien language. For example, if we are given the words ["wrt", "wrf", "er", "ett", "rftt"], we can determine that 'w' comes before 'e', 'e' comes before 'r', 'r' comes before 't', and so on. The constraints are that the input list of words is non-empty, and each word is non-empty. The output should be a string representing the order of the letters in the alien language.

## Approach
We can use a topological sorting algorithm to solve this problem. The idea is to create a graph where each node represents a letter, and there is a directed edge from node A to node B if A comes before B in the alien language. We can then use a topological sorting algorithm to order the nodes in the graph, which will give us the order of the letters in the alien language.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited to 26 nodes (one for each letter of the alphabet)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> alienOrder(vector<string>& words) {
    // Create a graph where each node represents a letter
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;
    
    // Initialize the graph and indegree map
    for (const string& word : words) {
        for (char c : word) {
            if (indegree.find(c) == indegree.end()) {
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
        // If word1 is a prefix of word2, then word1 must come before word2
        if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
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
    
    string result;
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
    
    // If there is a cycle in the graph, then we cannot determine the order of the letters
    if (result.size() != indegree.size()) {
        return {};
    }
    
    return {result};
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<string> result = alienOrder(words);
    for (const string& word : result) {
        cout << word << endl;
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
Output: "" (invalid input)
```

## Key Takeaways
- We can use a topological sorting algorithm to solve this problem.
- We need to handle the case where the input list of words is invalid (e.g. a word is a prefix of another word).
- We need to check for cycles in the graph to ensure that the order of the letters is unique.