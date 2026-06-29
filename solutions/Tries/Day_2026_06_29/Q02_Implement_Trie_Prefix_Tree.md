# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should be able to store a collection of strings and provide efficient lookup, insertion, and prefix matching. The constraints are: 1 <= word.length <= 10, word consists of lowercase English letters, and the maximum number of operations is 10^4. Examples include inserting words like "apple" and "app", then searching for "apple" and checking if "app" is a prefix of any word.

## Approach
The Trie data structure is a tree-like data structure where each node represents a string. We will use a nested unordered_map to store the children of each node and a boolean flag to mark the end of a word. The algorithm involves iterating over each character in the input string and creating new nodes if necessary.

## Complexity
- Time: O(m) where m is the length of the input string for insert and search operations, and O(m) for startsWith operation
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <unordered_map>
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
trie.search("apple");     // returns True
trie.search("app");       // returns True
trie.search("ap");        // returns False
trie.startsWith("app"); // returns True
trie.startsWith("ap");  // returns True
trie.startsWith("a");   // returns True
```

## Key Takeaways
- Tries are useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The time complexity of Trie operations is O(m) where m is the length of the input string.
- The space complexity of a Trie is O(n*m) where n is the number of words and m is the average length of the words.