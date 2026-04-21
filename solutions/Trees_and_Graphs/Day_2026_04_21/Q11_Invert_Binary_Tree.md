# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the binary tree:
```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```
The inverted binary tree would be:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```
The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`.

## Approach
The approach to inverting a binary tree involves recursively swapping the left and right child nodes of each internal node. This can be achieved by traversing the tree in a depth-first manner and swapping the child nodes at each level. The base case for the recursion is when the current node is NULL, in which case the function returns NULL.

## Complexity
- Time: O(n)
- Space: O(h)

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return NULL
        if (root == NULL) {
            return NULL;
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
Input: 
    4
   / \
  2   7
 / \ / \
1  3 6  9

Output: 
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

## Key Takeaways
- Inverting a binary tree involves swapping the left and right child nodes of each internal node.
- The approach can be implemented using a recursive depth-first traversal of the tree.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.