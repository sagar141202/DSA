# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root node of a binary tree, write a function to serialize it into a string, and another function to deserialize the string back into a binary tree. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) };`. For example, the binary tree `1 / \ 2   3 / \ 4   5` can be serialized into the string `"1,2,4,X,X,3,5,X,X,"` where `X` represents a null node.

## Approach
The approach to solve this problem is to use a pre-order traversal to serialize the binary tree into a string, and then use the string to deserialize the binary tree back into its original form. The serialization process involves recursively traversing the tree in pre-order and appending the node values to the string, while the deserialization process involves recursively constructing the tree from the string.

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
        ostringstream oss;
        serializeHelper(root, oss);
        return oss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        return deserializeHelper(iss);
    }

    // Helper function for serialization
    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node == NULL) {
            oss << "X,";
        } else {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        }
    }

    // Helper function for deserialization
    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "X") {
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(iss);
        node->right = deserializeHelper(iss);
        return node;
    }
};
```

## Test Cases
```
Input: root = [1,2,3,null,null,4,5]
Output: "1,2,X,X,3,4,X,X,5,X,X,"
```

## Key Takeaways
- Use pre-order traversal for serialization and deserialization of the binary tree.
- Utilize `ostringstream` and `istringstream` for string manipulation in C++.
- Handle null nodes by using a sentinel value like "X" during serialization.