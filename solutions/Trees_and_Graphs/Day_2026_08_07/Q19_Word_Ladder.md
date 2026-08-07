# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each word in the sequence is in the dictionary and each word is one edit distance away from the previous word. If no such sequence exists, return 0. The edit distance between two words is the number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. For example, if `beginWord = "hit"`, `endWord = "cog"`, and the dictionary is `["hot","dot","dog","lot","log","cog"]`, then the shortest transformation sequence is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"` with a length of 5.

## Approach
We use a Breadth-First Search (BFS) algorithm to explore all possible transformations from the `beginWord`. We generate all possible words that are one edit distance away from the current word and check if they are in the dictionary. We continue this process until we reach the `endWord` or exhaust all possibilities.

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
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If the end word is not in the dictionary, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the begin word
        queue<string> q;
        q.push(beginWord);
        
        // Initialize the length of the transformation sequence
        int length = 1;
        
        // Perform BFS
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the end word, return the length
                if (word == endWord) {
                    return length;
                }
                
                // Generate all possible words that are one edit distance away
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
            length++;
        }
        
        // If no transformation sequence is found, return 0
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
- Use a BFS algorithm to explore all possible transformations from the `beginWord`.
- Use a set to store the dictionary for O(1) lookup.
- Generate all possible words that are one edit distance away from the current word and check if they are in the dictionary.