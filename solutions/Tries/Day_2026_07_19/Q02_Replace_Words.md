# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified string. The replacement should be case-insensitive, and the words to replace should be whole words only. For example, if we have a sentence "I am a programmer" and we want to replace "am" with "is", the resulting sentence should be "I is a programmer". The input sentence will contain only lowercase letters and spaces, and the list of words to replace will also contain only lowercase letters.

## Approach
We can use a Trie data structure to store the words to replace, and then iterate over the sentence to find and replace these words. The Trie will allow us to efficiently check if a word is in the list of words to replace. We will split the sentence into words and check each word against the Trie.

## Complexity
- Time: O(n + m) where n is the length of the sentence and m is the total length of all words to replace
- Space: O(m) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord;
    string replacement;

    TrieNode() : endOfWord(false) {}
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
        node->endOfWord = true;
        node->replacement = replacement;
    }

    string getReplacement(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return word;
            }
            node = node->children[c];
        }
        if (node->endOfWord) {
            return node->replacement;
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word, "<" + word + ">");
    }

    stringstream ss(sentence);
    string word, result;
    while (ss >> word) {
        result += trie.getReplacement(word) + " ";
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
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cat sat on the mat"
Output: "the <cat> sat on the mat"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and retrieve words to replace in a sentence.
- The Trie allows for case-insensitive matching and whole word replacement.
- The time complexity of the solution is O(n + m) where n is the length of the sentence and m is the total length of all words to replace.