# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer for the next node in the same level, and the left child pointer should be set to null. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should will look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

## Approach
We use a recursive approach to solve this problem by traversing the tree and rearranging the nodes. The idea is to make the right child of each node the next node in the in-order traversal of the tree, effectively creating a linked list.

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
        // Base case: if tree is empty, return
        if (root == nullptr) return;

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left child is not null, we need to rearrange the nodes
        if (root->left != nullptr) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }

            // Rearrange the nodes
            rightmost->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input: [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- Use recursion to traverse the tree and rearrange the nodes.
- The right child of each node should be the next node in the in-order traversal of the tree.
- We need to find the rightmost node in the left subtree to rearrange the nodes correctly.