# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each word in the sequence is in the dictionary and each word is one edit distance away from the previous word. If no such sequence exists, return 0. The edit distance between two words is the number of positions at which the corresponding characters are different. For example, `INT -> LNT` is one edit distance away.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations from the `beginWord`. It constructs a queue with the `beginWord` and then iteratively generates all possible words that are one edit distance away from the current word, checking if they exist in the dictionary.

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
        // Create a set from the word list for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        // Initialize the queue with the beginWord and its level (1)
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Perform BFS
        while (!q.empty()) {
            string word = q.front().first;
            int level = q.front().second;
            q.pop();
            
            // If the current word is the endWord, return the level
            if (word == endWord) return level;
            
            // Generate all possible words that are one edit distance away
            for (int i = 0; i < word.size(); ++i) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; ++c) {
                    temp[i] = c;
                    // If the new word is in the wordSet, add it to the queue and remove it from the wordSet
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
```

## Key Takeaways
- Use a set to store the word list for efficient lookup.
- Utilize a queue for BFS to explore all possible transformations level by level.
- Generate all possible words that are one edit distance away from the current word by replacing each character with all lowercase letters.