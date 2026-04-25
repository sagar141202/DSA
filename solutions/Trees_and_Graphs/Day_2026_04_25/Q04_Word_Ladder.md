# Word Ladder

## Problem Statement
Given two words (begin_word and end_word), and a dictionary of words, find the length of the shortest transformation sequence from begin_word to end_word, such that each word in the sequence is in the dictionary and each word is formed by changing one letter from the previous word. If no such sequence exists, return 0. The constraints are that the length of begin_word and end_word is the same, and all words in the dictionary have the same length as begin_word.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to find the shortest transformation sequence. It starts with the begin_word and explores all possible words that can be formed by changing one letter. The BFS continues until it finds the end_word or exhausts all possible words.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the dictionary and the BFS queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        while (!q.empty()) {
            auto [word, length] = q.front();
            q.pop();
            
            if (word == endWord) {
                return length;
            }
            
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    if (wordSet.find(temp) != wordSet.end()) {
                        q.push({temp, length + 1});
                        wordSet.erase(temp);
                    }
                }
            }
        }
        
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
- Use an unordered_set to store the dictionary words for efficient lookup.
- Use a queue to implement the BFS approach.
- Use a temporary string to explore all possible words that can be formed by changing one letter from the current word.