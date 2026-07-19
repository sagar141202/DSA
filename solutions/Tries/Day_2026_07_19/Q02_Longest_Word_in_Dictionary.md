# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed using other words in the list. If there are multiple longest words, return the lexicographically smallest one. The list does not contain duplicates and all words are lowercase. For example, if the input is `["w","wo","wor","word"]`, the output should be `"word"`. If the input is `["a","banana","app","appl","ap","apply","apple"]`, the output should be `"apple"`.

## Approach
The approach to solve this problem is to use a Trie data structure to store all the words in the dictionary. Then, for each word in the dictionary, check if it can be formed using other words in the dictionary by searching for its prefixes in the Trie.

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
        if (word.length() < longest.length() || (word.length() == longest.length() && word > longest)) {
            continue;
        }
        bool canBeFormed = true;
        for (int i = 1; i < word.length(); i++) {
            string prefix = word.substr(0, i);
            if (!trie.search(prefix)) {
                canBeFormed = false;
                break;
            }
        }
        if (canBeFormed && (word.length() > longest.length() || (word.length() == longest.length() && word < longest))) {
            longest = word;
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
- Use a Trie data structure to store all the words in the dictionary for efficient prefix searching.
- Check if each word can be formed using other words in the dictionary by searching for its prefixes in the Trie.
- Keep track of the longest word that can be formed and update it if a longer word is found.