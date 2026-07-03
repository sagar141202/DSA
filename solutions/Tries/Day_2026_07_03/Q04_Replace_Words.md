# Replace Words
## Problem Statement
In this problem, we are given a sentence and a list of words. We need to replace all the words in the sentence that are prefixes of any word in the list with the shortest word that they are a prefix of. For example, if the sentence is "cat catcat meow" and the list of words is ["cat", "catcat"], we should replace "cat" with "catcat" because "cat" is a prefix of "catcat". The constraints are that the sentence will contain only lowercase English letters and spaces, and the list of words will also contain only lowercase English letters.

## Approach
We will use a Trie data structure to store the list of words. Then, we will iterate over each word in the sentence and check if it is a prefix of any word in the Trie. If it is, we will replace it with the shortest word that it is a prefix of.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the average length of a word
- Space: O(k) where k is the total number of characters in the list of words

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

    string getShortestWord(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return "";
            }
            node = node->children[c];
        }
        return getShortestWordHelper(node);
    }

    string getShortestWordHelper(TrieNode* node) {
        if (node->isEndOfWord) {
            return node->word;
        }
        string shortestWord = "";
        for (auto& child : node->children) {
            string word = getShortestWordHelper(child.second);
            if (word != "" && (shortestWord == "" || word.length() < shortestWord.length())) {
                shortestWord = word;
            }
        }
        return shortestWord;
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
        string shortestWord = trie.getShortestWord(word);
        if (shortestWord != "") {
            result += shortestWord + " ";
        } else {
            result += word + " ";
        }
    }
    return result.substr(0, result.length() - 1);
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and retrieve prefixes of words.
- Iterating over each word in the sentence and checking if it is a prefix of any word in the Trie can help replace words with their shortest prefixes.
- Recursively traversing the Trie to find the shortest word that a prefix is a part of can be an efficient approach.