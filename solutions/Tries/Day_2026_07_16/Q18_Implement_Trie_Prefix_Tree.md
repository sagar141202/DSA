# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The constraints are: 1 <= word.length <= 10, word consists of lowercase English letters, and at most 3 * 10^4 calls will be made to insert, search, and startsWith.

## Approach
We will use a TrieNode data structure to represent each node in the Trie, containing a boolean flag to mark the end of a word and a map to store the child nodes. The Trie will be initialized with a root node, and the operations will be performed recursively.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n * m) where n is the number of words and m is the average length of the words

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
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
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
Input: Trie trie; trie.insert("apple"); trie.insert("app"); trie.insert("banana");
Output: trie.search("apple") -> true, trie.search("app") -> true, trie.search("banana") -> true, trie.search("ban") -> false
trie.startsWith("app") -> true, trie.startsWith("ban") -> true, trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is suitable for storing a collection of strings and performing prefix-based operations efficiently.
- The use of a TrieNode data structure with a boolean flag and a map to store child nodes allows for efficient insertion, search, and startsWith operations.
- The time complexity of the operations is linear with respect to the length of the word, and the space complexity is linear with respect to the number of words and their average length.