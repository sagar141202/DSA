# Word Ladder

## Problem Statement
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.
3. beginWord is not the same as endWord.
4. If there is no transformation sequence, return 0.
Example: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]. The output is 5, and one possible transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog".

## Approach
The solution uses a Breadth-First Search (BFS) algorithm to traverse through all possible transformations of the given word. It checks each neighboring word by changing one character at a time and uses a queue to keep track of the words to be visited.

## Complexity
- Time: O(N * M^2), where N is the number of words and M is the length of each word
- Space: O(N * M), for storing the visited words and the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set for faster lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Check if endWord exists in the word list
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Initialize the visited set
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        // Initialize the level (distance)
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size();
            
            // Process all words at the current level
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the endWord, return the level
                if (word == endWord) {
                    return level;
                }
                
                // Generate all possible transformations of the current word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    
                    // Try all possible characters
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        
                        // If the transformed word is in the word list and not visited
                        if (wordSet.find(temp) != wordSet.end() && visited.find(temp) == visited.end()) {
                            q.push(temp);
                            visited.insert(temp);
                        }
                    }
                }
            }
            
            // Move to the next level
            level++;
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
- Use BFS to traverse through all possible transformations of the given word.
- Use a set to store the word list for faster lookup and a queue to keep track of the words to be visited.
- Generate all possible transformations of the current word by changing one character at a time.