# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace each word in the sentence with the shortest prefix from the list of words that is a prefix of the word. If no such prefix exists, the word remains unchanged. The sentence is a string of words separated by spaces, and the list of words is an array of strings. We need to return the modified sentence after replacing all the words.

## Approach
We will use a Trie data structure to store the list of words for efficient prefix matching. Then, we will iterate over each word in the sentence and find the shortest prefix in the Trie that matches the word.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(N * M) for storing the Trie and the modified sentence

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

    string search(string word) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            prefix += c;
            node = node->children[c];
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
        string replacedWord = trie.search(word);
        result += replacedWord + " ";
    }
    return result.substr(0, result.size() - 1);
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
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- Using a Trie data structure allows for efficient prefix matching.
- The `insert` method in the Trie class is used to add words to the Trie.
- The `search` method in the Trie class is used to find the shortest prefix that matches a word.