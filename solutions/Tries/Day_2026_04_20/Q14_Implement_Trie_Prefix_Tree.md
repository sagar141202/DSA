# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The constraints are: 1 <= word.length <= 10, word consists of lowercase English letters, and the maximum number of operations is 10^4. For example, if we insert the words "apple", "app", and "banana" into the Trie, the `search` operation should return `true` for "apple" and `false` for "orange". The `startsWith` operation should return `true` for "app" and `false` for "grape".

## Approach
The algorithm uses a Trie data structure to store the words, where each node represents a character in the word. The `insert` operation iterates through the characters in the word and creates new nodes if necessary. The `search` and `startsWith` operations traverse the Trie based on the input string and check if the corresponding node exists.

## Complexity
- Time: O(m) where m is the length of the word
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
trie.insert("banana");
Output: 
trie.search("apple") -> true
trie.search("app") -> true
trie.search("orange") -> false
trie.startsWith("app") -> true
trie.startsWith("grape") -> false
```

## Key Takeaways
- The Trie data structure is useful for storing and searching collections of strings.
- The `insert`, `search`, and `startsWith` operations have a time complexity of O(m) where m is the length of the word.
- The space complexity of the Trie is O(n*m) where n is the number of words and m is the average length of the words.