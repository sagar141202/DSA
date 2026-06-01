# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the dictionary.
- If there is no such transformation sequence, return 0.
For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, one possible transformation sequence is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`, so the output should be 5.

## Approach
The algorithm uses a breadth-first search (BFS) to explore all possible transformations of the `beginWord`. It generates all possible words that can be formed by changing one character of the current word and checks if the new word exists in the dictionary. If it does, the new word is added to the queue for further exploration.

## Complexity
- Time: O(N * M^2), where N is the number of words in the dictionary and M is the length of each word.
- Space: O(N * M), for storing the queue and the set of visited words.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        queue<string> q;
        q.push(beginWord);
        int len = 1;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                if (curr == endWord) return len;
                for (int j = 0; j < curr.size(); j++) {
                    string temp = curr;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        if (dict.count(temp)) {
                            q.push(temp);
                            dict.erase(temp);
                        }
                    }
                }
            }
            len++;
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
- Use BFS to explore all possible transformations of the `beginWord`.
- Use a set to store the visited words to avoid revisiting the same word.
- Generate all possible words that can be formed by changing one character of the current word and check if the new word exists in the dictionary.