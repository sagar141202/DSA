# Word Ladder

## Problem Statement
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the dictionary.
3. beginWord is not the same as endWord.
4. All words have the same length.
5. All words consist of lowercase alphabets.
If there is no such transformation sequence, return 0.
Example: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

## Approach
The problem can be solved using a Breadth-First Search (BFS) algorithm, where we explore all possible transformations of the current word. We use a queue to keep track of the words to be processed and a set to store the visited words. We generate all possible transformations of the current word by changing one character at a time and check if the transformed word exists in the dictionary.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the queue and visited set

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Create a queue for BFS, with the initial word and its length
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Create a set to store visited words
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        while (!q.empty()) {
            // Dequeue the current word and its length
            string word = q.front().first;
            int len = q.front().second;
            q.pop();
            
            // If the current word is the endWord, return its length
            if (word == endWord) {
                return len;
            }
            
            // Generate all possible transformations of the current word
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    // If the transformed word is in the wordSet and not visited, add it to the queue
                    if (wordSet.find(temp) != wordSet.end() && visited.find(temp) == visited.end()) {
                        q.push({temp, len + 1});
                        visited.insert(temp);
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
- Use BFS to explore all possible transformations of the current word.
- Use a set to store visited words to avoid revisiting them.
- Generate all possible transformations of the current word by changing one character at a time.