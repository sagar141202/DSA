# Replace Words
## Problem Statement
In this problem, we are given a list of strings representing a dictionary and a sentence. The task is to replace words in the sentence with their prefixes from the dictionary. The replacement rule is as follows: if a word in the sentence can be replaced with a prefix from the dictionary, we replace it. If multiple prefixes can replace a word, we use the longest one. For example, given the dictionary ["cat", "bat", "rat"] and the sentence "the cattle is cattle", we should replace "cattle" with "cat" because "cat" is a prefix of "cattle" and it is in the dictionary.

## Approach
We will use a Trie data structure to store the dictionary words. Then, we will iterate over each word in the sentence and check if it can be replaced with a prefix from the Trie. We will use a depth-first search approach to find the longest prefix that can replace a word.

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
    bool isWord;
    TrieNode() : isWord(false) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isWord = true;
    }
    string replace(const string& word) {
        TrieNode* node = root;
        string prefix;
        for (char c : word) {
            if (!node->children.count(c)) {
                return word;
            }
            prefix += c;
            node = node->children[c];
            if (node->isWord) {
                return prefix;
            }
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (const string& word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word, result;
    while (iss >> word) {
        result += trie.replace(word) + " ";
    }
    return result.substr(0, result.size() - 1); // remove trailing space
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cattle is cattle";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle is cattle"
Output: "the cat is cat"
```

## Key Takeaways
- Using a Trie data structure allows us to efficiently store and retrieve dictionary words.
- The replace function in the Trie class uses a depth-first search approach to find the longest prefix that can replace a word.
- The time complexity of the solution is O(N * M) where N is the number of words in the sentence and M is the maximum length of a word.