# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left and right child nodes of each internal node are swapped. Given the root of a binary tree, return the root of the inverted binary tree. For example, given the binary tree:
```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```
The inverted binary tree will be:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```
The binary tree node has a value and two child nodes, left and right. The input tree is not empty, and the number of nodes in the tree is in the range [1, 100].

## Approach
To invert a binary tree, we can use a recursive approach by swapping the left and right child nodes of each internal node. We start from the root node and recursively call the function for the left and right subtrees. This approach ensures that all nodes in the tree are visited and their child nodes are swapped.

## Complexity
- Time: O(N), where N is the number of nodes in the tree, since we visit each node once.
- Space: O(H), where H is the height of the tree, due to the recursive call stack.

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
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
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
- Use recursive approach to invert the binary tree by swapping the left and right child nodes of each internal node.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.
- The solution can be implemented using a simple and efficient recursive function.