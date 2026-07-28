# Flatten Binary Tree to Linked List

## Problem Statement
Given a binary tree, flatten it to a linked list in-place. The flattened linked list should be in the same order as a pre-order traversal of the original binary tree. For example, given the following binary tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened linked list should be:
1 -> 2 -> 3 -> 4 -> 5 -> 6
You do not need to return anything, but modify the input tree in-place.

## Approach
We will use a recursive approach to solve this problem, where we will first flatten the left and right subtrees, and then append the right subtree to the left subtree. This process will be repeated until the entire tree is flattened.

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
        if (root == nullptr) return;
        flatten(root->left);
        flatten(root->right);
        if (root->left != nullptr) {
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }
            rightmost->right = root->right;
            root->right = root->left;
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
- Recursion can be used to solve tree problems by breaking down the problem into smaller sub-problems.
- In-order, pre-order, and post-order traversals can be used to solve different types of tree problems.
- Tree problems often require modifying the tree in-place, so it's essential to keep track of the nodes and their relationships.