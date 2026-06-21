# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the word list.
- There is no limit on how many times a word can be used as an intermediate.
If there is no such transformation sequence, return 0.
For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, the output should be 5, because one of the shortest transformation sequences is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The algorithm uses Breadth-First Search (BFS) to explore all possible transformations of the `beginWord`. It generates all possible words that can be formed by changing one letter of the current word and checks if the new word is in the `wordList`. If it is, the new word is added to the queue for further transformations.

## Complexity
- Time: O(N * M^2), where N is the number of words in the `wordList` and M is the length of each word.
- Space: O(N * M), for storing the words in the queue and the `wordList`.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Check if endWord is in the wordList
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord
        queue<string> q;
        q.push(beginWord);
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the endWord, return the level
                if (word == endWord) {
                    return level;
                }
                
                // Generate all possible words by changing one letter
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        if (wordSet.find(temp) != wordSet.end()) {
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            level++;
        }
        
        // If there is no transformation sequence, return 0
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
- Use BFS to explore all possible transformations of the `beginWord`.
- Use a set for O(1) lookup of words in the `wordList`.
- Generate all possible words by changing one letter of the current word and check if the new word is in the `wordList`.