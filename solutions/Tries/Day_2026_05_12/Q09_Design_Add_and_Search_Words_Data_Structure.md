# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the `word` to the data structure.
- `bool search(word)`: returns `true` if the `word` is in the data structure, `false` otherwise.
The `word` may contain dots `.` where dots can be replaced by any letter. The `word` will only consist of lowercase letters and dots.

## Approach
The problem can be solved using a Trie data structure, which is an ordered tree data structure that is often used to store a dynamic set or associative array where the keys are usually strings. We can use a Trie to store all the words and then use depth-first search to check if a word is present in the Trie.

## Complexity
- Time: O(m) for addWord and search operations, where m is the length of the word.
- Space: O(n*m) for storing all the words, where n is the number of words and m is the average length of the words.

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class WordDictionary {
private:
    unordered_map<char, WordDictionary*> children;
    bool isEnd;

public:
    WordDictionary() : isEnd(false) {}

    void addWord(string word) {
        WordDictionary* node = this;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new WordDictionary();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        return search(word, 0, this);
    }

    bool search(string word, int index, WordDictionary* node) {
        if (index == word.size()) {
            return node->isEnd;
        }
        if (word[index] == '.') {
            for (auto& child : node->children) {
                if (search(word, index + 1, child.second)) {
                    return true;
                }
            }
            return false;
        }
        if (node->children.find(word[index]) == node->children.end()) {
            return false;
        }
        return search(word, index + 1, node->children[word[index]]);
    }
};
```

## Test Cases
```
Input: WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
Output: wordDictionary.search("pad") -> false
Output: wordDictionary.search("bad") -> true
Output: wordDictionary.search(".ad") -> true
Output: wordDictionary.search("b..") -> true
```

## Key Takeaways
- Use a Trie data structure to store words for efficient addition and search.
- Use depth-first search to handle the '.' character in the search operation.
- The `addWord` and `search` operations have a time complexity of O(m), where m is the length of the word.