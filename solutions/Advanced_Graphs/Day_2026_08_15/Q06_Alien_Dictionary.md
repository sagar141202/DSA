# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is composed of lowercase English letters. Within each word, letters that appear later in the word must appear later in the alien dictionary's order. For example, if the word "abc" is in the list, then 'a' must come before 'b' and 'b' must come before 'c' in the alien dictionary. Additionally, if two words are the same length and one is a prefix of the other, the shorter word must come first in the sorted order. Return the lexicographically smallest ordering of the letters in the alien dictionary. If there is no valid ordering, return an empty string. The input is a list of strings, where each string is a word in the alien language. The output is a string representing the lexicographically smallest ordering of the letters in the alien dictionary.

## Approach
The problem can be solved using a topological sorting algorithm with a directed graph, where each node represents a letter in the alphabet and each edge represents the ordering constraint between two letters. The algorithm works by first building the graph based on the given words, then performing a topological sort on the graph to obtain the ordering of the letters.

## Complexity
- Time: O(N * M + 26 * log(26))
- Space: O(26 + N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        // Create a graph with 26 nodes, each representing a letter in the alphabet
        vector<unordered_set<char>> graph(26);
        vector<int> indegree(26, 0);
        
        // Initialize the graph with all possible edges
        for (char c = 'a'; c <= 'z'; c++) {
            for (char d = 'a'; d <= 'z'; d++) {
                if (c != d) {
                    // graph[c - 'a'].insert(d - 'a');
                }
            }
        }
        
        // Build the graph based on the given words
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            int len1 = word1.length();
            int len2 = word2.length();
            
            // Check if word1 is a prefix of word2
            int j = 0;
            while (j < len1 && j < len2 && word1[j] == word2[j]) {
                j++;
            }
            
            // If word1 is a prefix of word2, add an edge from the last character of word1 to the next character in word2
            if (j == len1 && j < len2) {
                graph[word1[j - 1] - 'a'].insert(word2[j] - 'a');
                indegree[word2[j] - 'a']++;
            }
            // If word1 is not a prefix of word2, add an edge from the character in word1 that is different from the character in word2 to the character in word2
            else if (j < len1 && j < len2 && word1[j] != word2[j]) {
                graph[word1[j] - 'a'].insert(word2[j] - 'a');
                indegree[word2[j] - 'a']++;
            }
            // If word1 is not a prefix of word2 and they have the same length, the input is invalid
            else if (len1 > len2) {
                return "";
            }
        }
        
        // Perform a topological sort on the graph to obtain the ordering of the letters
        queue<int> q;
        for (int i = 0; i < 26; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        string result = "";
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            result += (char) (node + 'a');
            
            for (char neighbor : graph[node]) {
                indegree[neighbor - 'a']--;
                if (indegree[neighbor - 'a'] == 0) {
                    q.push(neighbor - 'a');
                }
            }
        }
        
        // If there is a cycle in the graph, the input is invalid
        if (result.length() != 26) {
            return "";
        }
        
        return result;
    }
};

## Test Cases
```
Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

## Key Takeaways
- The problem can be solved using a topological sorting algorithm with a directed graph.
- The graph is built based on the given words, where each edge represents the ordering constraint between two letters.
- The algorithm works by first building the graph, then performing a topological sort on the graph to obtain the ordering of the letters.