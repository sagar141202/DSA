# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the diameter of the tree. The diameter of a binary tree is the number of nodes in the longest path between any two nodes. For example, in the tree with nodes 1, 2, 3, 4, 5, the diameter is 3 (path: 4 -> 2 -> 1 -> 3 or 4 -> 2 -> 5).

## Approach
To find the diameter, we can calculate the height of the left subtree and the right subtree for each node and keep track of the maximum sum of heights. We use a recursive approach to calculate the height of each subtree.

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
        int maxDiameter = 0;
        height(root, maxDiameter);
        return maxDiameter;
    }
    
    int height(TreeNode* node, int& maxDiameter) {
        if (node == NULL) return 0;
        
        int leftHeight = height(node->left, maxDiameter);
        int rightHeight = height(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftHeight + rightHeight);
        
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
- We use a recursive approach to calculate the height of each subtree and keep track of the maximum diameter found so far.
- The time complexity is O(N) and the space complexity is O(H), where N is the number of nodes and H is the height of the tree.