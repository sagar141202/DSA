# Word Ladder

## Problem Statement
The Word Ladder problem is a classic problem in computer science and graph theory. Given two words (beginWord and endWord), and a dictionary of words, find the length of the shortest transformation sequence from beginWord to endWord. A transformation sequence is a sequence of words where each word is a transformation of the previous word by changing one letter to get a new word that is in the dictionary. If no such sequence exists, return 0. For example, given beginWord = "hit", endWord = "cog", and a dictionary = ["hot","dot","dog","lot","log","cog"], the output should be 5, because one of the shortest transformation sequences is "hit" -> "hot" -> "dot" -> "dog" -> "cog".

## Approach
The approach to solve this problem is to use a Breadth-First Search (BFS) algorithm to explore all possible transformations of the given word. We can use a queue data structure to keep track of the words to be processed and a set to keep track of the visited words.

## Complexity
- Time: O(N * M^2), where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M), where N is the number of words in the dictionary and M is the length of each word

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set to store the word list for efficient lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Create a queue for BFS and add the begin word
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        // Create a set to store the visited words
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        while (!q.empty()) {
            string word = q.front().first;
            int len = q.front().second;
            q.pop();
            
            // If the current word is the end word, return the length
            if (word == endWord) {
                return len;
            }
            
            // Generate all possible transformations of the current word
            for (int i = 0; i < word.size(); i++) {
                string temp = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    temp[i] = c;
                    
                    // If the transformed word is in the word set and not visited, add it to the queue
                    if (wordSet.count(temp) && !visited.count(temp)) {
                        q.push({temp, len + 1});
                        visited.insert(temp);
                    }
                }
            }
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
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
```

## Key Takeaways
- The Word Ladder problem can be solved using a BFS algorithm to explore all possible transformations of the given word.
- The use of a set to store the word list and a set to store the visited words can improve the efficiency of the solution.
- The generation of all possible transformations of the current word can be done by changing one letter at a time and checking if the transformed word is in the word set and not visited.