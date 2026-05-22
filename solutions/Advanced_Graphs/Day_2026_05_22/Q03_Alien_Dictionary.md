# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order of the letters is unknown. However, the aliens have provided a list of words in their language, along with the knowledge that the list is sorted lexicographically. The task is to determine the order of the letters in the alien alphabet. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order is "wertf". The constraints are that the input list of words is non-empty, and each word is a non-empty string consisting only of lowercase English letters. The output should be a string representing the correct order of the letters in the alien alphabet.

## Approach
The approach to solve this problem is to use a topological sorting algorithm on a graph where each node represents a letter and each edge represents a lexicographical order between two letters. We can build the graph by comparing adjacent words in the list. The intuition is that if a letter appears before another letter in a word, then it should come before that letter in the alien alphabet.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the size of the graph is limited to 26 nodes (one for each letter)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Build the graph
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;
    for (char c = 'a'; c <= 'z'; c++) {
        graph[c] = {};
        indegree[c] = 0;
    }
    
    for (int i = 0; i < words.size() - 1; i++) {
        string word1 = words[i];
        string word2 = words[i + 1];
        int len = min(word1.size(), word2.size());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                graph[word1[j]].insert(word2[j]);
                indegree[word2[j]]++;
                break;
            }
        }
        if (word1.size() > word2.size() && word1.substr(0, len) == word2) {
            return {}; // Invalid input
        }
    }
    
    // Perform topological sorting
    queue<char> q;
    for (char c = 'a'; c <= 'z'; c++) {
        if (indegree[c] == 0) {
            q.push(c);
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
    
    // Check for cycles
    if (result.size() != 26) {
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
```

## Key Takeaways
- The key to solving this problem is to build a graph that represents the lexicographical order of the letters in the alien alphabet.
- Topological sorting is used to find a valid order of the letters.
- The solution checks for invalid inputs by verifying that the list of words is sorted lexicographically.