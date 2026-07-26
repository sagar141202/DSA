# Replace Words
## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified string. The replacement should be done in such a way that the replaced word is the longest possible match. For example, if we have the sentence "the cat is in the cattle" and the list of words to replace is ["cat", "cattle"], the output should be "the *** is in the ***". The words to replace are case-sensitive and the replacement is case-sensitive as well.

## Approach
We will use a Trie data structure to store the words to replace. Then, we will iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with the specified string. We will use a recursive approach to find the longest matching word in the Trie.

## Complexity
- Time: O(n*m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(k) where k is the total number of characters in the words to replace

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
    stringstream ss(sentence);
    string word;
    string result;
    while (ss >> word) {
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
    string sentence = "the cattle started to cat and bat and rat";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle started to cat and bat and rat"
Output: "the cat started to cat and bat and rat"
Input: dictionary = ["cat","bat","rat"], sentence = "the cat sat on the mat and the bat sat on the rat"
Output: "the cat sat on the mat and the bat sat on the rat"
```

## Key Takeaways
- The Trie data structure is useful for storing and retrieving strings with common prefixes.
- The recursive approach is used to find the longest matching word in the Trie.
- The time complexity is O(n*m) where n is the number of words in the sentence and m is the maximum length of a word.