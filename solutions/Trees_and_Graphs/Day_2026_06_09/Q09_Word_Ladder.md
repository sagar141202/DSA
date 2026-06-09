# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each intermediate word is in the dictionary and differs from the previous word by exactly one character. If no such sequence exists, return 0. For example, given `beginWord = "hit"`, `endWord = "cog"`, and a dictionary `["hot","dot","dog","lot","log","cog"]`, one possible transformation sequence is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations from the `beginWord`. It generates all possible words that differ by one character from the current word and checks if they are in the dictionary.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the dictionary and the transformation sequence

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
            int len = q.front().second;
            q.pop();
            if (word == endWord) return len;
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    if (dict.count(temp)) {
                        q.push({temp, len + 1});
                        dict.erase(temp);
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
- Generate all possible words that differ by one character from the current word and check if they are in the dictionary.
- Remove the word from the dictionary after it is used to avoid revisiting the same word.