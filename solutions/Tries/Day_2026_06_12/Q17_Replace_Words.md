# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified replacement string. The replacement should be done in a way that the replaced words are not part of other words. For example, if we want to replace "cat" with "dog", the word "category" should not be replaced. The input sentence and the list of words are provided, and the output should be the modified sentence with all replacements done.

## Approach
We can use a Trie data structure to store the words to replace, allowing for efficient lookup and replacement. The algorithm involves iterating over each word in the sentence, checking if it is present in the Trie, and replacing it if necessary.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(k) where k is the total number of characters in the words to replace

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string replacement;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    void insert(string word, string replacement) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
        node->replacement = replacement;
    }

    string replace(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return word;
            }
            node = node->children[c];
        }
        if (node->isEndOfWord) {
            return node->replacement;
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word, word);
    }

    istringstream iss(sentence);
    ostringstream oss;
    string word;
    while (iss >> word) {
        string replaced = trie.replace(word);
        oss << replaced << " ";
    }
    return oss.str().substr(0, oss.str().size() - 1);
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cat sat on the mat";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cat sat on the mat"
Output: "the cat sat on the mat"
Input: dictionary = ["cat","bat","rat"], sentence = "the cat bat rat"
Output: "the cat bat rat"
```

## Key Takeaways
- Using a Trie data structure allows for efficient lookup and replacement of words in the sentence.
- The replacement is done in a way that whole words are replaced, not parts of other words.
- The solution has a time complexity of O(n * m) where n is the number of words in the sentence and m is the maximum length of a word.