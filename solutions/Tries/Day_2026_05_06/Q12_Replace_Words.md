# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of the words in the sentence with a specified string. The replacement should be case-sensitive and should only replace whole words. For example, if we want to replace "cat" with "dog", the sentence "I have a cat and a catalog" should become "I have a dog and a catalog".

## Approach
We can use a Trie data structure to store the words to replace, and then iterate over the sentence to find and replace the words. The Trie will allow us to efficiently check if a word is in the list of words to replace. We will also use a set to store the words to replace for efficient lookup.

## Complexity
- Time: O(n + m) where n is the length of the sentence and m is the total length of the words to replace
- Space: O(m) where m is the total length of the words to replace

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

    string replace(string sentence) {
        istringstream iss(sentence);
        string word, result;
        while (iss >> word) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    break;
                }
                node = node->children[c];
            }
            if (node->isEndOfWord) {
                result += node->replacement + " ";
            } else {
                result += word + " ";
            }
        }
        return result.substr(0, result.size() - 1); // remove trailing space
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word, "#");
    }
    return trie.replace(sentence);
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cat sat on the mat with a bat and a rat";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cat sat on the mat with a bat and a rat"
Output: "the # sat on the mat with a # and a #"
```

## Key Takeaways
- Use a Trie data structure to store the words to replace for efficient lookup
- Use a set to store the words to replace for efficient lookup
- Iterate over the sentence to find and replace the words using the Trie