# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. For example, in the tree with nodes 1, 2, 3, 4, 5, the diameter is 3 (path: 4 -> 2 -> 1 -> 3 or 4 -> 2 -> 5).

## Approach
To find the diameter of a binary tree, we can use a recursive approach where we calculate the height of the left and right subtree for each node. The diameter of the tree is the maximum diameter of the left subtree, right subtree, or the path through the current node.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree.

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
        int diam = 0;
        height(root, diam);
        return diam;
    }
    
    int height(TreeNode* node, int& diam) {
        if (node == NULL) return 0;
        int leftHeight = height(node->left, diam);
        int rightHeight = height(node->right, diam);
        diam = max(diam, leftHeight + rightHeight);
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
- The diameter of a binary tree can be calculated using a recursive approach by finding the height of the left and right subtree for each node.
- The time complexity of this approach is O(N), where N is the number of nodes in the tree.
- The space complexity of this approach is O(H), where H is the height of the tree, due to the recursive call stack.