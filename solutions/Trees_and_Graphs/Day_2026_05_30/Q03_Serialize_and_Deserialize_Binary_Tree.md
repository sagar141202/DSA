# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root of a binary tree, implement serialize and deserialize functions. The serialization of a binary tree is a string representation of the binary tree where the null nodes are represented by 'X' and the non-null nodes are represented by their values. The nodes are separated by commas. The deserialize function takes this string and returns the root of the binary tree. For example, the binary tree `1,2,3,X,X,4,5` represents the following binary tree:
       1
     /   \
    2     3
       /   \
      4     5
The constraints are: 
- The number of nodes in the tree is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4.

## Approach
We use a recursive approach to traverse the binary tree and serialize it into a string. For deserialization, we use a queue to store the nodes and recursively construct the binary tree.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <iostream>
#include <queue>
#include <sstream>
#include <vector>
#include <string>

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

    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node) {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        } else {
            oss << "X,";
        }
    }

    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "X") {
            return nullptr;
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
Input: root = [1,2,3,X,X,4,5]
Output: 1,2,X,X,3,4,X,X,5,X,X
```

## Key Takeaways
- Use recursive approach to serialize and deserialize binary tree.
- Use ostringstream to efficiently construct the serialized string.
- Use istringstream to efficiently parse the deserialized string.