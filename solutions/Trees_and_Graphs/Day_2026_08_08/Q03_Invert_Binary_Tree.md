# Invert Binary Tree

## Problem Statement
Invert a binary tree, which means swapping the left and right child nodes of each internal node. Given the root of a binary tree, invert the tree and return its root. The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100. Example: Input: root = [4,2,7,1,3,6,9], Output: [4,7,2,9,6,3,1].

## Approach
The algorithm involves recursively traversing the binary tree and swapping the left and right child nodes of each internal node. This can be achieved through a depth-first search (DFS) approach, where we recursively call the function for the left and right subtrees and then swap them.

## Complexity
- Time: O(n)
- Space: O(h)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }
        
        // Recursively invert the left and right subtrees
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
        // Return the root of the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Input: [2,1,3]
Output: [2,3,1]
Input: []
Output: []
```

## Key Takeaways
- Recursively traverse the binary tree using DFS to invert the tree.
- Swap the left and right child nodes of each internal node to achieve the inversion.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.