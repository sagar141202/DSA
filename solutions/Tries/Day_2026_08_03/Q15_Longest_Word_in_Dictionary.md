# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If there are multiple longest words, return the lexicographically smallest one. The list does not contain duplicates and all words are lowercase. For example, given `words = ["w","wo","wor","word"]`, the output should be `"word"`. If no such word can be formed, return an empty string.

## Approach
We can solve this problem by using a Trie data structure to store all the words. Then we iterate through each word and check if all its prefixes are in the Trie. We keep track of the longest word that can be formed from other words.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) where N is the number of words and M is the maximum length of a word

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
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }

        // Initialize variables to store the longest word
        string longestWord = "";
        int maxLength = 0;

        // Iterate through each word and check if it can be formed from other words
        for (const string& word : words) {
            TrieNode* node = root;
            bool canBeFormed = true;
            string prefix = "";
            for (char c : word) {
                if (node->children.find(c) == node->children.end() || !node->children[c]->isEndOfWord) {
                    canBeFormed = false;
                    break;
                }
                prefix += c;
                node = node->children[c];
            }

            // Update the longest word if the current word is longer or lexicographically smaller
            if (canBeFormed && (word.length() > maxLength || (word.length() == maxLength && word < longestWord))) {
                longestWord = word;
                maxLength = word.length();
            }
        }

        return longestWord;
    }
};
```

## Test Cases
```
Input: words = ["w","wo","wor","word"]
Output: "word"
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- We use a Trie to store all the words, which allows us to efficiently check if a word's prefix is in the Trie.
- We iterate through each word and check if all its prefixes are in the Trie, which allows us to determine if a word can be formed from other words.
- We keep track of the longest word that can be formed from other words and update it if we find a longer or lexicographically smaller word.