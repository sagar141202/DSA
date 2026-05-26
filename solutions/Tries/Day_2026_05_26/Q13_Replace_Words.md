# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of these words in the sentence with a specified string. The replacement should be done in a way that if a word in the sentence is a prefix of another word, the longer word should be replaced first. For example, if we want to replace "cat" and "catnip" with "dog", the sentence "I love catnip" should become "I love dog" and not "I love dognip".

## Approach
We can use a Trie data structure to store the words to replace, and then iterate over the sentence to replace the words. The Trie will allow us to efficiently check if a word is a prefix of another word. We will use a depth-first search approach to replace the words.

## Complexity
- Time: O(n + m) where n is the length of the sentence and m is the total length of all words to replace
- Space: O(m) where m is the total length of all words to replace

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string replacement;

    TrieNode() {
        isEndOfWord = false;
        replacement = "";
    }
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        // Create a Trie and insert all words to replace
        TrieNode* root = new TrieNode();
        for (string word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->replacement = word;
        }

        // Replace words in the sentence
        stringstream ss(sentence);
        string word;
        string result = "";
        while (ss >> word) {
            TrieNode* node = root;
            string replacedWord = "";
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    break;
                }
                node = node->children[c];
                replacedWord += c;
                if (node->isEndOfWord) {
                    result += node->replacement + " ";
                    break;
                }
            }
            if (!node->isEndOfWord) {
                result += word + " ";
            }
        }
        result.pop_back(); // Remove the last space
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cat sat on the mat";
    cout << solution.replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cat sat on the mat"
Output: "the cat sat on the mat"
Input: dictionary = ["cat"], sentence = "the cat sat on the mat"
Output: "the cat sat on the mat"
```

## Key Takeaways
- We can use a Trie data structure to efficiently store and replace words in a sentence.
- The Trie allows us to check if a word is a prefix of another word, which is important for replacing words correctly.
- We can use a depth-first search approach to replace the words in the sentence.