# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that each word in the sequence is in the dictionary and each word is a transformation of the previous word by changing one letter at a time. If no such sequence exists, return 0. The transformation sequence should not contain duplicate words.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to traverse through the possible transformations of the given words. It uses a queue to keep track of the current word and its transformation sequence length. The BFS traversal is performed until the `endWord` is found or all possible transformations are exhausted.

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
        // Create a set of words for O(1) lookups
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord and its sequence length
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Perform BFS traversal
        while (!q.empty()) {
            string currentWord = q.front().first;
            int currentLength = q.front().second;
            q.pop();
            
            // If the current word is the endWord, return its sequence length
            if (currentWord == endWord) {
                return currentLength;
            }
            
            // Generate all possible transformations of the current word
            for (int i = 0; i < currentWord.size(); i++) {
                string temp = currentWord;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    
                    // If the transformed word is in the wordSet, add it to the queue
                    if (wordSet.find(temp) != wordSet.end()) {
                        q.push({temp, currentLength + 1});
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
- Use a BFS approach to traverse through the possible transformations of the given words.
- Use a queue to keep track of the current word and its transformation sequence length.
- Use a set to store the dictionary words for O(1) lookups and to avoid duplicates in the transformation sequence.