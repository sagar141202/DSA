# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the diameter of the tree. The diameter of a binary tree is defined as the number of nodes in the longest path between any two nodes. For example, the diameter of the binary tree with the following structure:
       1
      / \
     2   3
    / \     
   4   5    
The diameter of the above binary tree is 3 (path: 4 -> 2 -> 1 -> 3 or path: 5 -> 2 -> 1 -> 3).

## Approach
To find the diameter, we will calculate the height of the left and right subtrees for each node and keep track of the maximum diameter seen so far. We can use a recursive approach to calculate the height and diameter.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree.

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
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        height(root, diameter);
        return diameter;
    }
    
    int height(TreeNode* node, int& diameter) {
        if (node == NULL) return 0;
        
        int leftHeight = height(node->left, diameter);
        int rightHeight = height(node->right, diameter);
        
        diameter = max(diameter, leftHeight + rightHeight);
        
        return 1 + max(leftHeight, rightHeight);
    }
};
```

## Test Cases
```
Input: 
       1
      / \
     2   3
    / \     
   4   5    
Output: 3
```

## Key Takeaways
- The diameter of a binary tree can be calculated by finding the maximum sum of heights of left and right subtrees for each node.
- The height of a tree can be calculated recursively by finding the maximum height of the left and right subtrees and adding 1.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, since we visit each node once.