# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- No word is used more than once in the sequence.
If there is no possible transformation, the function should return 0. For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, the output should be 5, because one of the shortest transformation sequences is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The Word Ladder problem can be solved using a Breadth-First Search (BFS) algorithm, where each word in the dictionary is a node, and two nodes are connected if their corresponding words differ by only one character. We start from the `beginWord` and explore all possible transformations level by level until we reach the `endWord`.

## Complexity
- Time: O(N * M^2), where N is the number of words and M is the length of each word
- Space: O(N), for storing the words in the queue and the set

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
        
        // If there is no possible transformation, return 0
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
- Use a set to store the words for efficient lookup and removal.
- Perform BFS to explore all possible transformations level by level.
- Generate all possible transformations of each word by changing one character at a time.