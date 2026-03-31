# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The left child of a node should become the right child, and the original right child should become the left child of the left child's rightmost node. The resulting linked list should be in the same order as a pre-order traversal of the original tree. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should be:
1 -> 2 -> 3 -> 4 -> 5 -> 6

## Approach
To solve this problem, we can use a recursive approach to flatten the tree in-place. We will recursively flatten the left and right subtrees, then adjust the node's children to match the desired linked list structure. This approach ensures that the tree is flattened in the correct order.

## Complexity
- Time: O(n)
- Space: O(h), where n is the number of nodes and h is the height of the tree

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
    void flatten(TreeNode* root) {
        // Base case: if the tree is empty, return
        if (!root) return;

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left subtree is not empty, move it to the right
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;

            // Move the right subtree to the right of the rightmost node
            rightmost->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input:      1
         / \
        2   5
       / \   \
      3   4   6

Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

## Key Takeaways
- The problem requires a recursive approach to flatten the binary tree in-place.
- The solution involves adjusting the node's children to match the desired linked list structure.
- The time complexity is O(n), where n is the number of nodes, and the space complexity is O(h), where h is the height of the tree.