# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each word in the sequence is in the dictionary and each word is one edit distance away from the previous word. If no such sequence exists, return 0. The edit distance between two words is the number of letters that need to be changed to get from one word to the other.

## Approach
The algorithm uses a breadth-first search (BFS) approach to explore all possible transformations from the `beginWord`. It uses a queue to keep track of the words to be processed and a set to store the visited words. The BFS traversal stops when the `endWord` is found or the queue becomes empty.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the length of each word
- Space: O(N * M) for storing the queue and visited set

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
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        while (!q.empty()) {
            string word = q.front().first;
            int len = q.front().second;
            q.pop();
            
            if (word == endWord) return len;
            
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    if (wordSet.count(temp) && !visited.count(temp)) {
                        q.push({temp, len + 1});
                        visited.insert(temp);
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
- Use a set to store the visited words to avoid revisiting them.
- Use a queue to keep track of the words to be processed.