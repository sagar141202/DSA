# Word Ladder

## Problem Statement
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- beginWord is not the same as endWord.
- If there is no such transformation sequence, return 0.
Example: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations of the beginWord. It checks each neighboring word by changing one character at a time and verifies if the resulting word is in the dictionary.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the words in the queue and the set

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set for O(1) lookups
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the dictionary, return 0
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        // Initialize the queue with the beginWord and its level (1)
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        while (!q.empty()) {
            // Get the current word and its level
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
                    // If the transformed word is in the dictionary, add it to the queue and remove it from the dictionary
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
```

## Key Takeaways
- Use BFS to explore all possible transformations of the beginWord.
- Use a set to store the words in the dictionary for O(1) lookups.
- Generate all possible transformations of the current word by changing one character at a time.