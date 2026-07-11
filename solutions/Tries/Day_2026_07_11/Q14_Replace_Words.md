# Replace Words

## Problem Statement
In this problem, we are given a list of words and a sentence. Our task is to replace words in the sentence with their prefixes from the given list if a prefix match is found. The replacement should be done in a way that the resulting sentence has the minimum number of words. For example, given the list of words ["cat", "bat", "rat"] and the sentence "the cattle is cattle", the output should be "the cat is cat". The constraints are: 1 <= sentence.length <= 10^5, 1 <= dictionary.length <= 10^4, 1 <= dictionary[i].length <= 10^3.

## Approach
We will use a Trie data structure to store the given list of words. Then, we will iterate over the sentence and check for each word if it has a prefix in the Trie. If a prefix match is found, we replace the word with its prefix.

## Complexity
- Time: O(n * m) where n is the length of the sentence and m is the maximum length of a word in the dictionary
- Space: O(n) for storing the Trie

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
            if (!node->children.count(c)) {
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
            if (!node->children.count(c)) {
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
    ostringstream oss;
    string word;
    while (iss >> word) {
        oss << trie.getPrefix(word) << " ";
    }
    return oss.str().substr(0, oss.str().size() - 1);
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
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cattle is cattle"
Output: "the cat is cat"
```

## Key Takeaways
- Using a Trie data structure can efficiently solve the problem by storing the given list of words and checking for prefix matches.
- The time complexity is O(n * m) due to the iteration over the sentence and the dictionary.
- The space complexity is O(n) for storing the Trie, where n is the total number of characters in the dictionary.