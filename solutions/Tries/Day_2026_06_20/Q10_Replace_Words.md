# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. We need to replace all occurrences of these words in the sentence with a specified replacement string. The replacement should be case-insensitive and should only replace whole words. For example, if we want to replace "is" with "is not", the sentence "This is a test" should become "This is not a test", but "isis" should remain "isis". We will use a Trie data structure to efficiently store and match the words to replace.

## Approach
We will use a Trie to store the words to replace, then iterate over each word in the sentence to check if it matches any word in the Trie. If a match is found, we replace the word with the specified replacement string.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(n) for storing the Trie and the sentence

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool is_end_of_word;
    string replacement;

    TrieNode() : is_end_of_word(false) {}
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
        node->is_end_of_word = true;
        node->replacement = replacement;
    }

    string get_replacement(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return "";
            }
            node = node->children[c];
        }
        if (node->is_end_of_word) {
            return node->replacement;
        }
        return "";
    }
};

string replace_words(string sentence, vector<string> words, string replacement) {
    Trie trie;
    for (string word : words) {
        trie.insert(word, replacement);
    }

    istringstream iss(sentence);
    string word;
    string result;

    while (iss >> word) {
        string lower_word = word;
        transform(lower_word.begin(), lower_word.end(), lower_word.begin(), ::tolower);
        string rep = trie.get_replacement(lower_word);
        if (!rep.empty()) {
            result += rep + " ";
        } else {
            result += word + " ";
        }
    }

    // remove trailing space
    if (!result.empty()) {
        result.pop_back();
    }

    return result;
}

int main() {
    string sentence = "This is a test";
    vector<string> words = {"is"};
    string replacement = "is not";

    cout << replace_words(sentence, words, replacement) << endl;

    return 0;
}
```

## Test Cases
```
Input: sentence = "This is a test", words = ["is"], replacement = "is not"
Output: "This is not a test"
```

## Key Takeaways
- Use a Trie to efficiently store and match words to replace
- Iterate over each word in the sentence to check for matches in the Trie
- Use a case-insensitive comparison to match words in the sentence with words in the Trie