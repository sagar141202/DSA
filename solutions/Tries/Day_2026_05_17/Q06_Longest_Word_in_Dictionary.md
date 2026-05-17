# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed by other words in the list. If there are multiple such words, return the lexicographically largest one. For example, if the input is `["w","wo","wor","word"]`, the output should be `"word"`. If the input is `["a","banana","app","appl","ap","apply","apple"]`, the output should be `"apple"`.

## Approach
The approach is to use a Trie data structure to store all the words in the dictionary. Then, for each word, check if all its prefixes are in the Trie. If they are, it means the word can be formed by other words in the dictionary.

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

    string longest;
    for (string word : words) {
        bool canBeFormed = true;
        for (int i = 1; i < word.size(); i++) {
            string prefix = word.substr(0, i);
            if (!trie.search(prefix)) {
                canBeFormed = false;
                break;
            }
        }
        if (canBeFormed && word.size() > longest.size()) {
            longest = word;
        } else if (canBeFormed && word.size() == longest.size() && word > longest) {
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
- Check all prefixes of a word to determine if it can be formed by other words in the dictionary
- Keep track of the longest word that can be formed by other words in the dictionary