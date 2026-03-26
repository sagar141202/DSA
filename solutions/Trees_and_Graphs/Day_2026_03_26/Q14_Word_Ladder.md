# Word Ladder

## Problem Statement
Given two words (`begin_word` and `end_word`) and a dictionary of words, find the length of the shortest transformation sequence from `begin_word` to `end_word` such that each word in the sequence is in the dictionary and each word is one edit distance away from the previous word. If no such sequence exists, return 0. The edit distance between two words is the number of positions at which the corresponding characters are different. For example, the edit distance between "cat" and "bat" is 1.

## Approach
We use a Breadth-First Search (BFS) algorithm to explore all possible transformations of the `begin_word`. We start with the `begin_word` and generate all possible words that are one edit distance away from it. We then add these words to a queue and repeat the process until we find the `end_word` or the queue is empty.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the dictionary and the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set for O(1) lookups
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord and its level (1)
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Perform BFS
        while (!q.empty()) {
            string word = q.front().first;
            int level = q.front().second;
            q.pop();
            
            // If the current word is the endWord, return its level
            if (word == endWord) {
                return level;
            }
            
            // Generate all possible words that are one edit distance away from the current word
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    // If the generated word is in the wordSet, add it to the queue and remove it from the wordSet
                    if (wordSet.find(temp) != wordSet.end()) {
                        q.push({temp, level + 1});
                        wordSet.erase(temp);
                    }
                }
            }
        }
        
        // If no sequence is found, return 0
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
- Use a BFS algorithm to explore all possible transformations of the `begin_word`.
- Use a set to store the dictionary for O(1) lookups.
- Generate all possible words that are one edit distance away from the current word by replacing each character with all possible characters.