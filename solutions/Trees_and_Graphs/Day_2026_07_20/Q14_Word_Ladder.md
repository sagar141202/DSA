# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the word list.
- No word can be reused.
For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, the output should be `5` because one of the shortest transformation sequences is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The problem can be solved using a Breadth-First Search (BFS) algorithm, which explores all possible transformations of the current word. We use a queue to keep track of the words to be processed and a set to keep track of the visited words.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the length of a word
- Space: O(N * M) for storing the queue and the set of visited words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        queue<string> q;
        q.push(beginWord);
        int len = 1;
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                if (word == endWord) {
                    return len;
                }
                
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
```

## Key Takeaways
- Use BFS to explore all possible transformations of the current word.
- Use a set to keep track of the visited words to avoid revisiting them.
- Use a queue to keep track of the words to be processed.