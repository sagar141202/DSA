# Word Ladder

## Problem Statement
Given two words (`begin_word` and `end_word`) and a dictionary's word list, find the length of the shortest transformation sequence from `begin_word` to `end_word`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- No word is used more than once.
If there is no possible transformation, return 0.
Example: `begin_word = "hit", end_word = "cog", word_list = ["hot","dot","dog","lot","log","cog"]`, the output is `5` because one of the shortest transformations is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
We can use a Breadth-First Search (BFS) algorithm to explore all possible transformations of the given word, level by level, until we find the target word or exhaust all possibilities. The BFS will help us find the shortest transformation sequence.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the average length of a word
- Space: O(N) for storing the words in the queue and the set

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string begin_word, string end_word, vector<string>& word_list) {
        unordered_set<string> word_set(word_list.begin(), word_list.end());
        queue<pair<string, int>> q;
        q.push({begin_word, 1});
        
        while (!q.empty()) {
            auto [word, step] = q.front();
            q.pop();
            
            if (word == end_word) return step;
            
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    if (word_set.count(temp)) {
                        word_set.erase(temp);
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
Input: begin_word = "hit", end_word = "cog", word_list = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

## Key Takeaways
- Use BFS to find the shortest transformation sequence.
- Utilize a set to keep track of visited words and avoid revisiting them.
- Iterate through each character in the current word and replace it with all possible letters to generate new words.