# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The `insert` method inserts a word into the trie, the `search` method checks if a word is in the trie, and the `startsWith` method checks if there is any word in the trie that starts with the given prefix. The trie should be able to store a large number of words and provide fast lookup times. For example, given the words "apple", "app", and "banana", the `search` method should return `true` for "apple" and `false` for "apples", and the `startsWith` method should return `true` for "app" and `false` for "ban".

## Approach
The approach is to use a nested map to represent the trie, where each node stores a map of its child nodes and a boolean indicating whether the node represents the end of a word. The `insert` method iterates over the characters in the word, creating new nodes as necessary, and sets the end-of-word flag to `true` for the final node. The `search` method iterates over the characters in the word, following the corresponding child nodes, and returns `true` if the final node has the end-of-word flag set to `true`. The `startsWith` method iterates over the characters in the prefix, following the corresponding child nodes, and returns `true` if it can follow all the characters in the prefix.

## Complexity
- Time: O(m) where m is the length of the word or prefix
- Space: O(n*m) where n is the number of words and m is the average length of the words

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

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
};
```

## Test Cases
```
Input: 
Trie trie;
trie.insert("apple");
trie.insert("app");
trie.insert("banana");
cout << trie.search("apple") << endl;  // Output: 1 (true)
cout << trie.search("app") << endl;     // Output: 1 (true)
cout << trie.search("applees") << endl; // Output: 0 (false)
cout << trie.startsWith("app") << endl;  // Output: 1 (true)
cout << trie.startsWith("ban") << endl;  // Output: 1 (true)
cout << trie.startsWith("ora") << endl; // Output: 0 (false)
```

## Key Takeaways
- The trie data structure is particularly useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The use of a nested map to represent the trie allows for efficient insertion, search, and prefix matching operations.
- The time complexity of the `insert`, `search`, and `startsWith` methods is O(m), where m is the length of the word or prefix, making the trie suitable for large datasets.