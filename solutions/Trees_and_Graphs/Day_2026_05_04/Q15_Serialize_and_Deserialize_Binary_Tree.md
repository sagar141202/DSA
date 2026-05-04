# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root node of a binary tree, write a function to serialize it into a string, and another function to deserialize the string back into the original binary tree. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), NULL); }. The string should be encoded as a level-order traversal of the tree, where each node's value is followed by a comma, and "X" is used to denote an empty node. For example, the binary tree `1,2,3,X,X,4,5` should be serialized into `"1,2,3,X,X,4,5"`. The deserialized binary tree should be the same as the original binary tree.

## Approach
We use a level-order traversal to serialize the binary tree into a string. To deserialize the string back into a binary tree, we use a queue to keep track of the nodes at each level. The algorithm iterates through the string, creating nodes and adding them to the queue as necessary.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "X,";
        string res = to_string(root->val) + ",";
        res += serialize(root->left);
        res += serialize(root->right);
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        string val;
        queue<string> q;
        while (getline(iss, val, ',')) {
            q.push(val);
        }
        return buildTree(q);
    }

    TreeNode* buildTree(queue<string>& q) {
        string val = q.front();
        q.pop();
        if (val == "X") return NULL;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = buildTree(q);
        node->right = buildTree(q);
        return node;
    }
};
```

## Test Cases
```
Input: root = [1,2,3,X,X,4,5]
Output: "1,2,3,X,X,4,5"
Serialization of the binary tree:
     1
   /   \
  2     3
     /   \
    4     5
```

## Key Takeaways
- Use a level-order traversal to serialize the binary tree into a string.
- Use a queue to keep track of the nodes at each level when deserializing the string back into a binary tree.
- Handle the case where a node is empty ("X") when serializing and deserializing the binary tree.