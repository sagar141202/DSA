# Word Ladder

## Problem Statement
The Word Ladder problem is a classic problem in computer science and graph theory. Given two words (begin_word and end_word) and a dictionary of words, find the length of the shortest transformation sequence from begin_word to end_word. A transformation sequence is a sequence of words where each word is obtained by changing one character from the previous word, and each word is in the dictionary. If no transformation sequence exists, return 0. The constraints are: 1 <= begin_word.length <= 10, 1 <= end_word.length <= 10, 1 <= dictionary.length <= 1000, and dictionary[i].length == begin_word.length.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to traverse the graph of words, where each word is a node and two nodes are connected if they differ by one character. The BFS traversal starts from the begin_word and explores all possible transformations until it reaches the end_word.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the words and their transformations

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If the endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        // Initialize the queue with the beginWord and its level
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Perform BFS
        while (!q.empty()) {
            string word = q.front().first;
            int level = q.front().second;
            q.pop();
            
            // If the current word is the endWord, return the level
            if (word == endWord) return level;
            
            // Generate all possible transformations of the current word
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    // If the transformed word is in the wordSet, add it to the queue and remove it from the wordSet
                    if (wordSet.find(temp) != wordSet.end()) {
                        q.push({temp, level + 1});
                        wordSet.erase(temp);
                    }
                }
            }
        }
        
        // If no transformation sequence is found, return 0
        return 0;
    }
};
```

## Test Cases
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
```

## Key Takeaways
- Use a BFS approach to traverse the graph of words and find the shortest transformation sequence.
- Use a set to store the words for O(1) lookup and avoid duplicates.
- Generate all possible transformations of each word by changing one character at a time.