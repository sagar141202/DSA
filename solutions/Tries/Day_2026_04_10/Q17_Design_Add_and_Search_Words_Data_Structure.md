# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `addWord(word)` and `search(word)`. The `search(word)` method can search a literal word or a regular expression containing only dots (`.`) as wildcards. For example, `"."` matches any single character, and `"a"` matches only "a". You may assume that all words are composed of lowercase letters `a-z`. The data structure should be case-sensitive and should support up to `10^4` operations. For example, `addWord("bad")` and `addWord("dad")`, then `search("pad")` returns `false`, while `search("bad")` returns `true` and `search(".ad")` returns `true`.

## Approach
The problem can be solved by using a Trie data structure. Each node in the Trie will have 26 children (one for each lowercase letter) and a boolean flag to indicate whether a word ends at that node. The `addWord` method will iterate over the characters in the word, creating new nodes as necessary, and setting the flag at the final node. The `search` method will also iterate over the characters in the word, but will use a recursive approach to handle the dot (`.`) wildcard.

## Complexity
- Time: O(M) for `addWord` and `search`, where M is the length of the word
- Space: O(N*M) for storing all words, where N is the number of words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isWord;
    };

    TrieNode* root;

    void addWordHelper(TrieNode* node, string word) {
        if (word.empty()) {
            node->isWord = true;
            return;
        }
        char c = word[0];
        if (node->children.find(c) == node->children.end()) {
            node->children[c] = new TrieNode();
        }
        addWordHelper(node->children[c], word.substr(1));
    }

    bool searchHelper(TrieNode* node, string word) {
        if (word.empty()) {
            return node->isWord;
        }
        char c = word[0];
        if (c == '.') {
            for (auto child : node->children) {
                if (searchHelper(child.second, word.substr(1))) {
                    return true;
                }
            }
            return false;
        } else {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            return searchHelper(node->children[c], word.substr(1));
        }
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        addWordHelper(root, word);
    }

    bool search(string word) {
        return searchHelper(root, word);
    }
};

int main() {
    WordDictionary wordDictionary;
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    cout << wordDictionary.search("pad") << endl; // false
    cout << wordDictionary.search("bad") << endl; // true
    cout << wordDictionary.search(".ad") << endl; // true
    return 0;
}
```

## Test Cases
```
Input: 
addWord("bad")
addWord("dad")
search("pad")
search("bad")
search(".ad")
Output: 
false
true
true
```

## Key Takeaways
- The Trie data structure is well-suited for problems that involve string matching with wildcards.
- Recursive approaches can be effective for handling complex string patterns.
- The time complexity of the `addWord` and `search` methods is O(M), where M is the length of the word.