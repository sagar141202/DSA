# Word Ladder

## Problem Statement
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- beginWord is not the same as endWord.
- If there is no such transformation sequence, return 0.
For example, given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return 5.

## Approach
The algorithm uses Breadth-First Search (BFS) to explore all possible transformations of the given word. It checks each word in the dictionary to see if it can be transformed into the target word by changing one character at a time. The BFS traversal stops when the target word is found, and the length of the transformation sequence is returned.

## Complexity
- Time: O(N*M^2) where N is the number of words in the dictionary and M is the maximum length of a word
- Space: O(N) for storing the dictionary and the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        while (!q.empty()) {
            string word = q.front().first;
            int steps = q.front().second;
            q.pop();
            
            if (word == endWord) return steps;
            
            for (int i = 0; i < word.size(); i++) {
                char orig = word[i];
                for (char c = 'a'; c <= 'z'; c++) {
                    word[i] = c;
                    if (dict.find(word) != dict.end()) {
                        dict.erase(word);
                        q.push({word, steps + 1});
                    }
                }
                word[i] = orig;
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
- Use BFS to explore all possible transformations of the given word.
- Keep track of visited words to avoid revisiting them.
- Use a queue to store the words to be visited along with their transformation sequence length.