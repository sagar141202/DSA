# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed using other words in the list. If there are multiple such words, return the lexicographically largest one. The list does not contain duplicates, and all words are lowercase. For example, given the list `["w","wo","wor","word"]`, the function should return `"word"`. If no such word exists, return an empty string.

## Approach
The solution involves using a Trie data structure to store the given words and then checking each word in the list to see if it can be formed using other words in the Trie. We use a depth-first search (DFS) to check if a word can be formed.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

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
    sort(words.begin(), words.end(), [](string a, string b) {
        if (a.length() == b.length()) {
            return a > b;
        }
        return a.length() < b.length();
    });
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }
    string longest;
    for (string word : words) {
        if (word.length() <= longest.length()) {
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
        if (canBeFormed) {
            longest = word;
        }
    }
    return longest;
}

int main() {
    vector<string> words = {"w","wo","wor","word"};
    cout << longestWord(words) << endl;
    return 0;
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
- Use a Trie data structure to efficiently store and search for words
- Sort the words by length and lexicographical order to ensure the longest word is found first
- Check each word to see if it can be formed using other words in the Trie by searching for prefixes of the word.