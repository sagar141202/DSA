# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The left child of a node should become the right child, and the original right child should become the left child of the left child's rightmost node. The resulting linked list should be in the same order as the original tree's pre-order traversal. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened linked list should be:
1 -> 2 -> 3 -> 4 -> 5 -> 6

## Approach
We can solve this problem by recursively flattening the left and right subtrees, then rearranging the nodes to form a linked list. We'll use a recursive function to flatten the tree in-place.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        // Base case: if the tree is empty, return
        if (root == NULL) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty, rearrange the nodes
        if (root->left != NULL) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != NULL) {
                rightmost = rightmost->right;
            }
            
            // Rearrange the nodes to form a linked list
            rightmost->right = root->right;
            root->right = root->left;
            root->left = NULL;
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
- The key to solving this problem is to recursively flatten the left and right subtrees, then rearrange the nodes to form a linked list.
- We use a recursive function to flatten the tree in-place, which reduces the space complexity to O(n) due to the recursive call stack.
- The time complexity is O(n) because we visit each node exactly once.