# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified replacement string. The replacement should be case-insensitive and the words to replace should be whole words only, not substrings of other words. The input sentence and the list of words to replace will be provided, and the output should be the modified sentence with all replacements made.

## Approach
We can solve this problem by using a Trie data structure to store the words to replace. Then, we iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with the replacement string.

## Complexity
- Time: O(n + m) where n is the number of words in the sentence and m is the total number of characters in the words to replace
- Space: O(m) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
    string word;

    TrieNode() : isWord(false) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(tolower(c))) {
                node->children[tolower(c)] = new TrieNode();
            }
            node = node->children[tolower(c)];
        }
        node->isWord = true;
        node->word = word;
    }

    string search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(tolower(c))) {
                return word;
            }
            node = node->children[tolower(c)];
        }
        return node->isWord ? "" : word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }

    stringstream ss(sentence);
    string word, result;
    while (ss >> word) {
        string replaced = trie.search(word);
        if (replaced.empty()) {
            result += word + " ";
        } else {
            result += replaced + " ";
        }
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
Output: "the cat sat on the mat"
Input: dictionary = ["cat", "bat", "rat"], sentence = "the cat bat rat sat on the mat"
Output: "the cat bat rat sat on the mat"
```

## Key Takeaways
- Using a Trie data structure allows for efficient lookup of words to replace
- The Trie is case-insensitive, so it can handle words with different cases
- The solution has a linear time complexity with respect to the input size, making it efficient for large inputs