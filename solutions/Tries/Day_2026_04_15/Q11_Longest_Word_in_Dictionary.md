# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed by other words from the list. If there are multiple longest words, return the lexicographically smallest one. The words can only be formed by other words in the list if they can be split into a sequence of words where each word is in the list. For example, "cat" and "cats" can be formed by "cat" and "cats" respectively, but "catsdog" cannot be formed by "cat", "dog", and "cats" because "dog" is not in the list.

## Approach
The approach to solve this problem is to use a Trie data structure to store all the words in the list. Then, we iterate through each word in the list and check if it can be formed by other words in the list by splitting it into a sequence of words and checking if each word is in the Trie. We keep track of the longest word that can be formed and return it at the end.

## Complexity
- Time: O(N * M) where N is the number of words in the list and M is the maximum length of a word
- Space: O(N * M) where N is the number of words in the list and M is the maximum length of a word

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

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isWord = true;
    }
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isWord;
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
- Use a Trie data structure to store all the words in the list for efficient lookup.
- Iterate through each word in the list and check if it can be formed by other words in the list by splitting it into a sequence of words and checking if each word is in the Trie.
- Keep track of the longest word that can be formed and return it at the end.