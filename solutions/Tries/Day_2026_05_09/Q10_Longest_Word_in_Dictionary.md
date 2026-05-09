# Longest Word in Dictionary

## Problem Statement
Given a list of strings which contains a list of dictionary words, find the longest word in the dictionary that can be formed by removing characters from another word in the dictionary. If there are multiple such words, return the lexicographically smallest one. For example, given the dictionary `["w","wo","wor","word","wrd"]`, the longest word that can be formed is `"word"` because it can be formed by removing characters from `"word"`.

## Approach
The approach to solve this problem is to use a Trie data structure to store the dictionary words and then perform a depth-first search to find the longest word that can be formed. We will iterate over each word in the dictionary, insert it into the Trie, and then check if it can be formed by removing characters from another word in the Trie.

## Complexity
- Time: O(N * M) where N is the number of words in the dictionary and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        // Create a Trie and insert all words
        TrieNode* root = new TrieNode();
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }
        
        // Perform DFS to find the longest word
        string longest = "";
        for (string word : words) {
            if (canBeFormed(root, word)) {
                if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
                    longest = word;
                }
            }
        }
        return longest;
    }
    
    bool canBeFormed(TrieNode* root, string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};
```

## Test Cases
```
Input: ["w","wo","wor","word","wrd"]
Output: "word"
Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- Use a Trie data structure to store the dictionary words for efficient lookup and insertion.
- Perform a depth-first search to find the longest word that can be formed by removing characters from another word in the Trie.
- Keep track of the longest word found so far and update it if a longer word is found.