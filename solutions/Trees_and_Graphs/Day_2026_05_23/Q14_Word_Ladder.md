# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the dictionary.
- If there is no possible transformation, return 0.
Example: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`, the output is `5` because one possible transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The solution uses a Breadth-First Search (BFS) algorithm to explore all possible transformations from the `beginWord`. It generates all possible words by changing one character at a time and checks if the new word is in the dictionary.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of a word.
- Space: O(N) for storing the dictionary and the queue.

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
            int steps = q.front().second;
            q.pop();

            if (word == endWord) return steps;

            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    if (wordSet.count(temp)) {
                        wordSet.erase(temp);
                        q.push({temp, steps + 1});
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
- Use a BFS approach to explore all possible transformations.
- Use an unordered set to store the dictionary for efficient lookups.
- Generate all possible words by changing one character at a time and check if the new word is in the dictionary.