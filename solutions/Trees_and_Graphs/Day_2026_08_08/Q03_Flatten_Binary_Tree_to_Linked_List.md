# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer and each node's value should still be the same. The height of the tree does not matter, and we only care about the final structure of the linked list. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like:
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
We will solve this problem by using a recursive approach to flatten the binary tree. The idea is to recursively flatten the left and right subtrees and then append the right subtree to the end of the left subtree.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        // Base case: if the tree is empty
        if (!root) return;

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left subtree is not empty
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;

            // Append the right subtree to the end of the left subtree
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
- Use recursive approach to solve the problem.
- The key idea is to append the right subtree to the end of the left subtree.
- We need to find the rightmost node in the left subtree to append the right subtree.