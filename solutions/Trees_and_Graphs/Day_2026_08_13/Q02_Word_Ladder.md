# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the word list.
- The transformation sequence must start with `beginWord` and end with `endWord`.
- If there is no such transformation sequence, return 0.
- Example: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`, the output is `5` because one of the shortest transformation sequences is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
Use a Breadth-First Search (BFS) algorithm to explore all possible transformations from the `beginWord`.
Generate all possible words by changing one character at a time and check if they exist in the word list.
Keep track of the transformation sequence length and return the shortest one.

## Complexity
- Time: O(N * M^2) where N is the number of words in the word list and M is the length of each word
- Space: O(N * M) for storing the word list and the transformation sequence

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
            string word = q.front().first;
            int length = q.front().second;
            q.pop();
            
            if (word == endWord) {
                return length;
            }
            
            for (int i = 0; i < word.size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    string nextWord = word;
                    nextWord[i] = c;
                    
                    if (wordSet.find(nextWord) != wordSet.end()) {
                        wordSet.erase(nextWord);
                        q.push({nextWord, length + 1});
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
```

## Key Takeaways
- Use BFS to explore all possible transformations from the `beginWord`.
- Generate all possible words by changing one character at a time and check if they exist in the word list.
- Keep track of the transformation sequence length and return the shortest one.