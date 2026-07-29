# Word Ladder
## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words consist of lowercase alphabets.
- You may return any shortest transformation sequence.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations of the given word. It utilizes a queue to keep track of the words to be processed and a set to store the visited words. The BFS traversal continues until it finds the target word or exhausts all possibilities.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the length of each word
- Space: O(N * M) for storing the queue and visited words

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
            int step = q.front().second;
            q.pop();
            if (word == endWord) return step;
            for (int i = 0; i < word.size(); ++i) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; ++c) {
                    temp[i] = c;
                    if (wordSet.count(temp)) {
                        wordSet.erase(temp);
                        q.push({temp, step + 1});
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
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
```

## Key Takeaways
- Utilize BFS to explore all possible transformations of the given word.
- Use a set to store the visited words and avoid revisiting them.
- The time complexity depends on the number of words and the length of each word.