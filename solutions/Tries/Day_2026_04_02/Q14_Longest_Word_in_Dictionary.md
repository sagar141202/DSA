# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed using the other words in the list. The longest word should have the maximum length, and if there are multiple words with the same maximum length, return the lexicographically smallest word. If no such word exists, return an empty string. The list will not contain any duplicates and will contain at least one word. All the strings in the list will only contain lowercase alphabets.

## Approach
The problem can be solved using a Trie data structure to store all the words in the dictionary. Then, we iterate over each word in the dictionary and check if it can be formed using other words in the dictionary by searching for its prefixes in the Trie. We keep track of the longest word that can be formed.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
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

        // Initialize result
        string result = "";

        // Iterate over each word in the dictionary
        for (string word : words) {
            // Check if the word can be formed using other words
            if (canBeFormed(word, root)) {
                // Update the result if the current word is longer or lexicographically smaller
                if (word.length() > result.length() || (word.length() == result.length() && word < result)) {
                    result = word;
                }
            }
        }

        return result;
    }

    // Helper function to check if a word can be formed using other words
    bool canBeFormed(string word, TrieNode* root) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            prefix += c;
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
            if (!node->isEndOfWord) {
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
- Use a Trie data structure to efficiently store and search for words in the dictionary.
- Iterate over each word in the dictionary and check if it can be formed using other words by searching for its prefixes in the Trie.
- Keep track of the longest word that can be formed and update the result accordingly.