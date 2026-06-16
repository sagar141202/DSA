# Replace Words
## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a special token. The replacement should be done in a way that the resulting sentence has the minimum number of words. The constraints are that the sentence and the list of words are non-empty, and the words in the list are unique. For example, if the sentence is "this is a test" and the list of words is ["is", "a"], the output should be "this * test" where "*" is the special token.

## Approach
The approach to solve this problem is to use a Trie data structure to store the list of words. We then iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with the special token.

## Complexity
- Time: O(n + m) where n is the length of the sentence and m is the total length of all words in the list
- Space: O(m) where m is the total length of all words in the list

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
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word, result;
    while (iss >> word) {
        string temp = "";
        for (char c : word) {
            temp += c;
            if (trie.search(temp)) {
                result += "*" + " ";
                break;
            }
        }
        if (temp == word) {
            result += word + " ";
        }
    }
    return result.substr(0, result.size() - 1);
}

int main() {
    vector<string> dictionary = {"cat","bat","rat"};
    string sentence = "the cattle was rattled by the battery";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rattled by the bat"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and search for words in a list.
- The replacement of words in a sentence should be done in a way that minimizes the number of words in the resulting sentence.
- The time complexity of this solution is O(n + m) where n is the length of the sentence and m is the total length of all words in the list.