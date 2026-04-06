# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word from the list that can be formed by other words in the list. If there are multiple longest words, return the lexicographically smallest one. If no such word exists, return an empty string. The length of the word will not exceed 1000 and the number of words will not exceed 1000.

## Approach
The approach is to use a Trie data structure to store all the words and then check each word to see if it can be formed by other words in the Trie. We will use depth-first search to check if a word can be formed by other words.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) where N is the number of words and M is the maximum length of a word

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string word) {
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

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }
    string longest = "";
    for (string word : words) {
        if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
            bool canBeFormed = true;
            for (int i = 1; i < word.length(); i++) {
                string prefix = word.substr(0, i);
                if (!trie.search(prefix)) {
                    canBeFormed = false;
                    break;
                }
            }
            if (canBeFormed) {
                longest = word;
            }
        }
    }
    return longest;
}
```

## Test Cases
```
Input: ["w","wo","wor","word"]
Output: "word"
Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- Use a Trie to store all the words for efficient lookup
- Check each word to see if it can be formed by other words in the Trie using depth-first search
- Keep track of the longest word that can be formed by other words and return it at the end