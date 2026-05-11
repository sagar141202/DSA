# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. We need to replace all occurrences of these words in the sentence with a specified string. The replacement should be case-insensitive and should consider the whole word only, not part of another word. For example, if the sentence is "I am a programmer" and the word to replace is "am", the output should be "I  a programmer" (with a space in place of "am"). We can use a Trie data structure to store the words to replace and then iterate over the sentence to replace the words.

## Approach
We will create a Trie and insert all the words to replace into it. Then, we will iterate over the sentence and check if the current word is in the Trie. If it is, we replace it with the specified string.

## Complexity
- Time: O(n + m) where n is the length of the sentence and m is the total length of all words to replace
- Space: O(m) for storing the Trie

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

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
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

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word, result;
    while (iss >> word) {
        string temp = word;
        for (int i = 1; i < word.size(); i++) {
            string prefix = word.substr(0, i);
            if (trie.search(prefix)) {
                temp = prefix;
                break;
            }
        }
        result += temp + " ";
    }
    result.pop_back(); // remove the last space
    return result;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- We use a Trie data structure to store the words to replace for efficient lookup.
- We iterate over the sentence and check if each word is in the Trie to replace it.
- We use a prefix matching approach to replace the words with the shortest matching prefix in the Trie.