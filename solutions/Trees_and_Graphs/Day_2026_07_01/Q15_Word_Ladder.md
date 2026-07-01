# Word Ladder

## Problem Statement
The Word Ladder problem is a classic problem in graph theory and computer science. Given two words (beginWord and endWord), and a dictionary of words, find the length of the shortest transformation sequence from beginWord to endWord. A transformation sequence is a sequence of words where each word is obtained by changing one character from the previous word, and each word is in the dictionary. If no transformation sequence exists, return 0. The constraints are: 1 <= beginWord.length <= 10, 1 <= endWord.length <= 10, 1 <= wordList.length <= 5000, beginWord, endWord, and wordList[i] consist of lowercase English letters, beginWord != endWord, and wordList contains no duplicates.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations of the beginWord. It checks all possible words that can be formed by changing one character of the current word and adds them to the queue if they exist in the dictionary. The BFS traversal continues until it finds the endWord or exhausts all possible transformations.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the queue and the set of visited words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for efficient lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Create a queue for BFS and add the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Initialize the length of the transformation sequence
        int length = 1;
        
        // Create a set to store visited words
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        while (!q.empty()) {
            // Get the size of the queue
            int size = q.size();
            
            // Process each word at the current level
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the word is the endWord, return the length
                if (word == endWord) {
                    return length;
                }
                
                // Generate all possible transformations of the word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        
                        // If the transformation is in the wordSet and not visited, add it to the queue
                        if (wordSet.count(temp) && !visited.count(temp)) {
                            q.push(temp);
                            visited.insert(temp);
                        }
                    }
                }
            }
            
            // Increment the length of the transformation sequence
            length++;
        }
        
        // If no transformation sequence exists, return 0
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
- The Word Ladder problem can be solved using a BFS approach with a time complexity of O(N * M^2) where N is the number of words in the dictionary and M is the length of each word.
- The space complexity is O(N * M) for storing the queue and the set of visited words.
- The algorithm generates all possible transformations of each word and checks if they exist in the dictionary, making it efficient for finding the shortest transformation sequence.