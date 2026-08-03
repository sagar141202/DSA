# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty strings of the alien language, where each string is a word in the alien language. Within each word, the letters are in the correct order for the alien language. Also, the order of the words in the list is such that for any two adjacent words, the first word is either a prefix of the second word, or the second word is a prefix of the first word. The task is to determine the order of the letters in the alien alphabet. If there are multiple valid orders, return any one of them. If the input is invalid, return an empty string. The length of each word is at most 10, and the number of words is at most 100.

## Approach
We will use a topological sorting algorithm to solve this problem, where each letter is a node and the edges represent the order of the letters. We will iterate through each pair of adjacent words and compare the letters at the same position. If the letters are different, we will add an edge from the letter in the first word to the letter in the second word. Then, we will perform a topological sort on the graph to get the order of the letters.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the size of the graph is constant (26 letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string alienOrder(vector<string>& words) {
    // Create a graph where each letter is a node
    vector<unordered_set<char>> graph(26);
    vector<int> indegree(26, 0);
    
    // Initialize the graph with all letters
    for (char c = 'a'; c <= 'z'; c++) {
        graph[c - 'a'] = unordered_set<char>();
    }
    
    // Iterate through each pair of adjacent words
    for (int i = 0; i < words.size() - 1; i++) {
        string word1 = words[i];
        string word2 = words[i + 1];
        
        // Compare the letters at the same position
        int minLen = min(word1.length(), word2.length());
        for (int j = 0; j < minLen; j++) {
            if (word1[j] != word2[j]) {
                // Add an edge from the letter in the first word to the letter in the second word
                if (graph[word1[j] - 'a'].find(word2[j]) == graph[word1[j] - 'a'].end()) {
                    graph[word1[j] - 'a'].insert(word2[j]);
                    indegree[word2[j] - 'a']++;
                }
                break;
            }
        }
        
        // If the first word is longer than the second word and the second word is a prefix of the first word, return an empty string
        if (word1.length() > word2.length() && word1.substr(0, minLen) == word2.substr(0, minLen)) {
            return "";
        }
    }
    
    // Perform a topological sort on the graph
    queue<char> q;
    for (char c = 'a'; c <= 'z'; c++) {
        if (indegree[c - 'a'] == 0) {
            q.push(c);
        }
    }
    
    string order;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        order += c;
        
        // Decrease the indegree of all neighbors
        for (char neighbor : graph[c - 'a']) {
            indegree[neighbor - 'a']--;
            if (indegree[neighbor - 'a'] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // If there is a cycle in the graph, return an empty string
    if (order.length() != 26) {
        return "";
    }
    
    return order;
}

```

## Test Cases
```
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

## Key Takeaways
- The Alien Dictionary problem can be solved using a topological sorting algorithm.
- The graph is represented as an adjacency list where each letter is a node and the edges represent the order of the letters.
- The indegree of each node is used to detect cycles in the graph.