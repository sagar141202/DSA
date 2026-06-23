# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root of a binary tree, serialize it into a string, and then deserialize the string back into a binary tree. The serialization of a binary tree should follow the pre-order traversal (root, left, subtree, right subtree) where an empty node is represented as 'X'. For example, the serialization of the binary tree below is "1,2,X,X,3,X,X".

## Approach
To solve this problem, we can use a recursive approach to serialize the binary tree into a string and then deserialize it back into a binary tree. We will utilize a pre-order traversal to serialize the tree and a recursive function to deserialize the string.

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
        ostringstream os;
        serializeHelper(root, os);
        return os.str();
    }
    
    void serializeHelper(TreeNode* node, ostringstream& os) {
        if (node == NULL) {
            os << "X,";
        } else {
            os << node->val << ",";
            serializeHelper(node->left, os);
            serializeHelper(node->right, os);
        }
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream is(data);
        return deserializeHelper(is);
    }
    
    TreeNode* deserializeHelper(istringstream& is) {
        string val;
        getline(is, val, ',');
        if (val == "X") {
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(is);
        node->right = deserializeHelper(is);
        return node;
    }
};
```

## Test Cases
```
Input: root = [1,2,3]
Output: "1,2,X,X,3,X,X"
```

## Key Takeaways
- Use pre-order traversal to serialize the binary tree into a string.
- Use a recursive approach to deserialize the string back into a binary tree.
- Utilize ostringstream and istringstream to handle string operations efficiently.