# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed by other words in the list. If there are multiple longest words, return the lexicographically smallest one. If no such word exists, return an empty string. The input list will have at least one element and all elements will be lowercase.

## Approach
We can use a Trie to store the given words and then check for each word if it can be formed by other words in the Trie. The longest word that can be formed by other words and is lexicographically smallest will be the result.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
    TrieNode() : isWord(false) {}
};
class Solution {
public:
    string longestWord(vector<string>& words) {
        // Create Trie and insert all words
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isWord = true;
        }
        
        string longest;
        for (const string& word : words) {
            if (canBeFormed(root, word)) {
                if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
                    longest = word;
                }
            }
        }
        return longest;
    }
    
    bool canBeFormed(TrieNode* root, const string& word) {
        TrieNode* node = root;
        for (int i = 0; i < word.length(); ++i) {
            if (node->children.find(word[i]) == node->children.end()) {
                return false;
            }
            node = node->children[word[i]];
            if (!node->isWord && i < word.length() - 1) {
                return false;
            }
        }
        return true;
    }
};
```

## Test Cases
```
Input: ["w","wo","wor","word"]
Output: "word"
Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- We use a Trie to store all the given words for efficient lookup.
- We check for each word if it can be formed by other words in the Trie.
- The longest word that can be formed by other words and is lexicographically smallest will be the result.