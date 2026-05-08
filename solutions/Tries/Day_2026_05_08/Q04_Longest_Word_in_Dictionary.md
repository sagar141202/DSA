# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If there are multiple longest words, return the lexicographically smallest one. For example, if the input is `["w","wo","wor","word"]`, the output should be `"word"`. If the input is `["a","banana","app","appl","ap","apply","apple"]`, the output should be `"apple"`. The length of each word is between 1 and 30, and the total number of words is between 1 and 2000.

## Approach
The approach is to use a Trie data structure to store all the words, and then for each word, check if all its prefixes are in the Trie. We use a recursive function to check if a word can be formed from other words in the list. 

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isWord;
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        // Create the Trie and insert all words
        TrieNode* root = new TrieNode();
        for (string word : words) {
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
        for (int i = 0; i < word.length(); i++) {
            if (node->children.find(word[i]) == node->children.end()) {
                return false;
            }
            node = node->children[word[i]];
            if (!node->isWord) {
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
- Use a Trie to store all the words for efficient prefix lookup
- Check if all prefixes of a word are in the Trie to determine if it can be formed from other words
- Use a recursive function to check if a word can be formed from other words in the list