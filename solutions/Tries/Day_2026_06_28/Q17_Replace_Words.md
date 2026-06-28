# Replace Words

## Problem Statement
In this problem, we are given a list of words in a dictionary and a sentence. The task is to replace words in the sentence with their prefixes from the dictionary if they exist. For example, if we have a dictionary with words ["cat", "bat", "rat"] and a sentence "the cattle is batting", the output should be "the cat is bat". The constraints are that the dictionary can have at most 1000 words and the sentence can have at most 1000 characters. The goal is to write an efficient algorithm that can solve this problem.

## Approach
We can solve this problem using a Trie data structure to store the dictionary words. We will then iterate through each word in the sentence and check if it has a prefix in the Trie. If it does, we replace the word with its prefix. This approach allows us to efficiently find prefixes in the dictionary.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(D) where D is the total number of characters in the dictionary

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
    string getPrefix(string word) {
        TrieNode* node = root;
        string prefix;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return word;
            }
            prefix += c;
            node = node->children[c];
            if (node->isEndOfWord) {
                return prefix;
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
    string result;
    while (iss >> word) {
        string prefix = trie.getPrefix(word);
        result += prefix + " ";
    }
    result.pop_back(); // remove the last space
    return result;
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cattle is batting";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cattle is batting"
Output: "the cat is bat"
```

## Key Takeaways
- Using a Trie data structure can efficiently solve this problem by allowing us to quickly find prefixes in the dictionary.
- The TrieNode class and Trie class encapsulate the Trie data structure and its operations, making the code more organized and readable.
- The replaceWords function integrates the Trie with the input sentence and dictionary to produce the desired output.