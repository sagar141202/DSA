# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. The tree is represented by a TreeNode class, where each node has a value, a left child, and a right child. The function should return the diameter of the binary tree. For example, given the binary tree with the following structure:
       1
      / \
     2   3
    / \     
   4   5    
The diameter of this tree is 3, which is the path between node 4 and node 5.

## Approach
To find the diameter of a binary tree, we can calculate the height of the left and right subtrees for each node and keep track of the maximum diameter found. We will use a recursive approach to calculate the height of each subtree and update the diameter accordingly. The key idea is to consider each node as a potential starting point for the diameter.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree.

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        height(root, diameter);
        return diameter;
    }
    
    int height(TreeNode* node, int& diameter) {
        if (node == nullptr) {
            return 0;
        }
        
        int leftHeight = height(node->left, diameter);
        int rightHeight = height(node->right, diameter);
        
        diameter = max(diameter, leftHeight + rightHeight);
        
        return 1 + max(leftHeight, rightHeight);
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5]
Output: 3
```

## Key Takeaways
- The diameter of a binary tree can be calculated by considering each node as a potential starting point for the diameter.
- We use a recursive approach to calculate the height of each subtree and update the diameter accordingly.
- The time complexity is O(N), where N is the number of nodes in the tree, because we visit each node once.