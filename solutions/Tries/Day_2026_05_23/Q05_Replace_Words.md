# Replace Words

## Problem Statement
In this problem, we are given a list of words and a sentence. We need to replace all occurrences of words from the list in the sentence with a shorter word. If a word has multiple shorter forms, we should use the shortest one. The replacement should be done in a way that the resulting sentence is the shortest possible. For example, if we have a list of words ["cat", "bat", "rat"] and a sentence "the cat sat on the mat", the output should be "the cat". We can use a Trie data structure to solve this problem efficiently.

## Approach
We will use a Trie to store the list of words. Then, we will iterate over each word in the sentence and check if it is present in the Trie. If it is, we will replace it with the shortest possible word.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;

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
        node->word = word;
    }

    string replace(string word) {
        TrieNode* node = root;
        string result = "";
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return word;
            }
            node = node->children[c];
            result += c;
            if (node->isEndOfWord) {
                return node->word;
            }
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }

    istringstream iss(sentence);
    string word;
    string result = "";
    while (iss >> word) {
        result += trie.replace(word) + " ";
    }

    return result.substr(0, result.size() - 1);
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
Output: "the cat"
Input: dictionary = ["cat","bat","rat"], sentence = "the cat sat on the rat"
Output: "the cat on the rat"
```

## Key Takeaways
- Using a Trie data structure can help us to efficiently check if a word is present in a list of words.
- We can use the Trie to replace words in a sentence with their shorter forms.
- The replacement should be done in a way that the resulting sentence is the shortest possible.