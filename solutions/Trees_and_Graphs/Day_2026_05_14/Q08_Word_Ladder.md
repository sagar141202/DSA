# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the word list.
- There is no limit on how many times a word can be used in the sequence.
If there is no such transformation sequence, return 0. 
Example: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`, output: `5` because one of the shortest transformations is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The problem can be solved using a Breadth-First Search (BFS) algorithm, where each word in the dictionary is a node, and two nodes are connected if the corresponding words differ by only one character. We start from `beginWord` and explore all possible transformations level by level until we reach `endWord` or exhaust all possibilities.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the length of each word, because for each word, we generate all possible transformations.
- Space: O(N * M) for storing the words and the transformation queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for efficient look-up
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the word list, return 0
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        // Initialize the queue with the beginWord
        queue<string> q;
        q.push(beginWord);
        int level = 1; // The level of the current word
        
        // Perform BFS
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the endWord, return the level
                if (word == endWord) return level;
                
                // Generate all possible transformations of the current word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        // If the transformation is in the word set, add it to the queue and remove it from the set
                        if (wordSet.find(temp) != wordSet.end()) {
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            // Move to the next level
            level++;
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
- Use BFS to explore all possible transformations level by level.
- Use a set to store the words for efficient look-up and avoid revisiting the same word.
- Generate all possible transformations of each word by changing one character at a time.