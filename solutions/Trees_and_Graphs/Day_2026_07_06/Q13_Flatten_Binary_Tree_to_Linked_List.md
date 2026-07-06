# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointers to connect the nodes at the next level in the tree. Also, the left child of each node should be set to nullptr. The root of the tree is given as the input, and the output is the root of the modified tree. For example, given the following binary tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The output should be:
1 -> 2 -> 3 -> 4 -> 5 -> 6

## Approach
The approach to solving this problem is to use a recursive function that traverses the tree in a pre-order manner (root, left, right) and appends the right child of each node to the right of its left child. This process continues until all nodes have been visited and the tree has been flattened.

## Complexity
- Time: O(n)
- Space: O(n)

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
        if (root == nullptr) {
            return;
        }

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left child is not nullptr, append its right child to the right of the root
        if (root->left != nullptr) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }

            // Append the right child of the root to the right of the rightmost node in the left subtree
            rightmost->right = root->right;

            // Set the right child of the root to its left child
            root->right = root->left;

            // Set the left child of the root to nullptr
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input: 
        1
       / \
      2   5
     / \   \
    3   4   6

Output: 
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

## Key Takeaways
- The key to solving this problem is to use a recursive function that traverses the tree in a pre-order manner.
- The function should append the right child of each node to the right of its left child.
- The left child of each node should be set to nullptr after the right child has been appended.