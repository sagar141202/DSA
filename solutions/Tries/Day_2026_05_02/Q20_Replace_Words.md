# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of each word in the list with a specified replacement string. The replacement string is the same for all words. The words to replace are stored in a Trie data structure. The input sentence is a string of words separated by spaces, and the list of words to replace is stored in the Trie. We need to write a function that takes the sentence and the Trie as input and returns the modified sentence with all occurrences of the words replaced.

## Approach
We will use a Trie data structure to store the words to replace. We will then iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with the replacement string.

## Complexity
- Time: O(n*m) where n is the number of words in the sentence and m is the average length of a word
- Space: O(n) for storing the Trie and the modified sentence

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
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word, result;
    while (iss >> word) {
        TrieNode* node = trie.root;
        string prefix;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            prefix += c;
            node = node->children[c];
            if (node->isEndOfWord) {
                result += prefix + " ";
                break;
            }
        }
        if (node->isEndOfWord == false) {
            result += word + " ";
        }
    }
    result.pop_back(); // remove the last space
    return result;
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cattle was rattled by the battery";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rattled by the bat"
```

## Key Takeaways
- We use a Trie data structure to store the words to replace for efficient lookup.
- We iterate over each word in the sentence and check if it is present in the Trie.
- If a word is present in the Trie, we replace it with the replacement string.