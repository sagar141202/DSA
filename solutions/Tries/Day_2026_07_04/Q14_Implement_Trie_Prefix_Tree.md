# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store strings in a way that allows for efficient retrieval of strings that start with a given prefix. The constraints are: 1 <= word.length <= 10, word consists of lowercase English letters, and 1 <= prefix.length <= 10, prefix consists of lowercase English letters. For example, if we insert the words "apple", "app", and "banana", then searching for "apple" should return True, searching for "app" should return True, and searching for "ap" should return False because "ap" is not a word in the Trie.

## Approach
We will use a nested unordered map to represent the Trie, where each node stores a boolean indicating whether a word ends at that node and a map of its child nodes. We will iterate over the input string to insert words into the Trie, and use a similar approach to search for words and prefixes.

## Complexity
- Time: O(m) where m is the length of the input string for insert, search, and startsWith operations
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

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
trie.search("apple"); // returns True
trie.search("app"); // returns True
trie.search("ap"); // returns False
trie.startsWith("app"); // returns True
trie.startsWith("ap"); // returns True
trie.startsWith("ba"); // returns True
```

## Key Takeaways
- Tries are useful data structures for storing and retrieving strings with common prefixes.
- The insert operation in a Trie involves iterating over the input string and creating new nodes as necessary.
- The search and startsWith operations in a Trie involve iterating over the input string and checking if the corresponding nodes exist in the Trie.