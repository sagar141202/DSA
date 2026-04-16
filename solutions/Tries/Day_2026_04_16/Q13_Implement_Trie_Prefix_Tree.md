# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure with the following methods: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the methods should operate as follows:
- `insert(word)`: Inserts a word into the Trie.
- `search(word)`: Returns `true` if the word is in the Trie, and `false` otherwise.
- `startsWith(prefix)`: Returns `true` if there is any word in the Trie that starts with the given prefix, and `false` otherwise.
The Trie should be able to handle a large number of strings, and the methods should be efficient in terms of time complexity.
For example, given the following operations:
- `insert("apple")`
- `insert("app")`
- `insert("banana")`
- `search("apple")` returns `true`
- `search("app")` returns `true`
- `search("banana")` returns `true`
- `search("ban")` returns `false`
- `startsWith("app")` returns `true`
- `startsWith("ban")` returns `true`
- `startsWith("ora")` returns `false`

## Approach
The Trie data structure is a tree-like structure where each node represents a character in a string. We can use a hashmap to store the child nodes of each node, and a boolean flag to indicate whether a word ends at a node. The `insert`, `search`, and `startsWith` methods can be implemented by traversing the Trie based on the input string.

## Complexity
- Time: O(m) where m is the length of the input string
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

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
private:
    TrieNode* root;

public:
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
cout << trie.search("app") << endl;    // Output: 1 (true)
cout << trie.search("banana") << endl; // Output: 1 (true)
cout << trie.search("ban") << endl;     // Output: 0 (false)
cout << trie.startsWith("app") << endl; // Output: 1 (true)
cout << trie.startsWith("ban") << endl; // Output: 1 (true)
cout << trie.startsWith("ora") << endl; // Output: 0 (false)
```

## Key Takeaways
- The Trie data structure is suitable for storing a large number of strings and performing prefix-based queries.
- The `insert`, `search`, and `startsWith` methods can be implemented efficiently using a Trie, with a time complexity of O(m) where m is the length of the input string.
- The space complexity of the Trie is O(n*m) where n is the number of strings and m is the average length of the strings.