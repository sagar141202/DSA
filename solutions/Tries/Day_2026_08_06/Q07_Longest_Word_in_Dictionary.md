# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If there are multiple words of the same length that can be formed, return the lexicographically smallest one. The length of each word is between 1 and 1000. The number of words is between 1 and 1000. The words are all in lowercase.

## Approach
The approach is to use a Trie data structure to store all the words in the dictionary. Then, for each word in the dictionary, check if it can be formed from other words in the dictionary by searching for its prefixes in the Trie.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing all the words in the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool endOfWord;
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
            node->endOfWord = true;
        }

        // Initialize result
        string result = "";
        for (string word : words) {
            // Check if the word can be formed from other words
            if (canBeFormed(word, root)) {
                if (word.length() > result.length() || (word.length() == result.length() && word < result)) {
                    result = word;
                }
            }
        }
        return result;
    }

    bool canBeFormed(string word, TrieNode* root) {
        TrieNode* node = root;
        for (int i = 0; i < word.length(); i++) {
            if (node->children.find(word[i]) == node->children.end()) {
                return false;
            }
            node = node->children[word[i]];
            if (i < word.length() - 1 && !node->endOfWord) {
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
- Use a Trie data structure to efficiently store and search for words
- Check if a word can be formed from other words by searching for its prefixes in the Trie
- Use a recursive or iterative approach to check if a word can be formed from other words