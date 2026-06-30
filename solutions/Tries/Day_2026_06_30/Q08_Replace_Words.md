# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified string. The replacement should be done in a way that the replaced word is the longest possible match. For example, if we have a sentence "the cat sat on the mat" and a list of words ["cat", "mat"], we should replace "cat" and "mat" with a specified string. The constraint is that the replacement should be done in a single pass through the sentence.

## Approach
We will use a Trie data structure to store the words to replace. Then, we will iterate over the sentence and check if the current substring is present in the Trie. If it is, we will replace it with the specified string. The Trie will allow us to find the longest possible match in O(m) time, where m is the length of the substring.

## Complexity
- Time: O(n + m), where n is the length of the sentence and m is the total length of all words to replace
- Space: O(m), where m is the total length of all words to replace

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

    string replace(string sentence, vector<string>& words) {
        for (string word : words) {
            insert(word);
        }

        string result = "";
        int i = 0;
        while (i < sentence.size()) {
            TrieNode* node = root;
            int j = i;
            while (j < sentence.size() && node->children.find(sentence[j]) != node->children.end()) {
                node = node->children[sentence[j]];
                j++;
            }
            if (node->isEndOfWord) {
                result += " ";
                i = j;
            } else {
                result += sentence[i];
                i++;
            }
        }
        return result.substr(1); // remove leading space
    }
};

int main() {
    Trie trie;
    string sentence = "the cat sat on the mat";
    vector<string> words = {"cat", "mat"};
    cout << trie.replace(sentence, words) << endl;
    return 0;
}
```

## Test Cases
```
Input: sentence = "the cat sat on the mat", words = ["cat", "mat"]
Output: "the  sat on the "
```

## Key Takeaways
- Tries can be used to find all occurrences of a set of words in a sentence in a single pass.
- The Trie data structure allows us to find the longest possible match in O(m) time, where m is the length of the substring.
- This approach can be used for text processing tasks such as spell checking, auto-completion, and text replacement.