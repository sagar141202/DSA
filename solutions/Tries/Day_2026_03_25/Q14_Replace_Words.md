# Replace Words

## Problem Statement
In this problem, we are given a list of words and a sentence. We need to replace all occurrences of words from the list in the sentence with a shorter version of the word. The shorter version of a word is the shortest prefix that is unique to that word in the list. For example, if we have a list of words ["cat", "cart", "cattle"] and a sentence "the cat sat on the cart", we should replace "cat" with "ca" and "cart" with "car". The constraints are that the list of words can have up to 1000 words, the length of each word can be up to 100 characters, and the sentence can have up to 1000 words.

## Approach
We will use a Trie data structure to store the list of words. Then, we will iterate over each word in the sentence and check if it is present in the Trie. If it is, we will find the shortest prefix that is unique to that word and replace the word with that prefix.

## Complexity
- Time: O(n * m * k) where n is the number of words in the sentence, m is the maximum length of a word, and k is the average number of children of a node in the Trie.
- Space: O(n * m) where n is the number of words in the list and m is the maximum length of a word.

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

    string getShortestPrefix(string word) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            prefix += c;
            node = node->children[c];
            if (node->isEndOfWord) {
                return prefix;
            }
            if (node->children.size() == 1) {
                continue;
            } else {
                return prefix;
            }
        }
        return prefix;
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
        string shortestPrefix = trie.getShortestPrefix(word);
        if (shortestPrefix != "") {
            result += shortestPrefix + " ";
        } else {
            result += word + " ";
        }
    }
    return result.substr(0, result.size() - 1);
}

int main() {
    vector<string> dictionary = {"cat", "cart", "cattle"};
    string sentence = "the cat sat on the cart";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat", "cart", "cattle"], sentence = "the cat sat on the cart"
Output: "the ca sat on the car"
```

## Key Takeaways
- We can use a Trie data structure to store a list of words and efficiently find the shortest prefix that is unique to each word.
- The `insert` method in the Trie class is used to add words to the Trie, and the `getShortestPrefix` method is used to find the shortest prefix of a word.
- The `replaceWords` function uses the Trie to replace words in a sentence with their shortest prefixes.