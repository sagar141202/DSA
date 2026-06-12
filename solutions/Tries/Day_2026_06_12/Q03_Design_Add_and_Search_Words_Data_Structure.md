# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `void addWord(word)` and `bool search(word)`. The data structure should be able to store words and search for words that may contain dots (`.`) as wildcards. For example, if you add a word "bad" and search for "b.d", the function should return `true` because "bad" matches the pattern "b.d". The data structure should also support searching for exact words.

## Approach
We will use a Trie data structure to store the words. Each node in the Trie will have a boolean flag to indicate whether a word ends at that node. We will also use a recursive approach to search for words with wildcards.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) where N is the number of words and M is the maximum length of a word

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEnd;
        TrieNode() : isEnd(false) {}
    };

    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        return searchFrom(root, word);
    }

    bool searchFrom(TrieNode* node, string word) {
        for (int i = 0; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (searchFrom(child.second, word.substr(i + 1))) {
                        return true;
                    }
                }
                return false;
            }
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEnd;
    }

private:
    TrieNode* root;
};

int main() {
    WordDictionary wordDictionary;
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    cout << boolalpha << wordDictionary.search("pad") << endl; // returns False
    cout << boolalpha << wordDictionary.search("bad") << endl; // returns True
    cout << boolalpha << wordDictionary.search(".ad") << endl; // returns True
    cout << boolalpha << wordDictionary.search("b..") << endl; // returns True
    return 0;
}
```

## Test Cases
```
Input: 
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad");
wordDictionary.search("bad");
wordDictionary.search(".ad");
wordDictionary.search("b..");
Output: 
False
True
True
True
```

## Key Takeaways
- Use a Trie data structure to store words for efficient prefix matching.
- Use a recursive approach to search for words with wildcards.
- Use an unordered_map to store children of each node in the Trie for efficient lookup.