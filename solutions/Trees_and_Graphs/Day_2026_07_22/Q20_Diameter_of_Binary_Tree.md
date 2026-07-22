# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a tree is defined as the number of nodes along the longest path between any two nodes, which may or may not pass through the root. For example, in the tree with nodes 1, 2, 3, 4, 5, the diameter is 3 (path: 4 -> 2 -> 1 -> 3 or 4 -> 2 -> 5).

## Approach
To solve this problem, we can use a depth-first search (DFS) approach to find the height of each node in the tree. The diameter of the tree will be the maximum sum of the heights of two child nodes of any node. We can maintain a variable to store the maximum diameter found so far.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

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
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (node == NULL) return 0;
        int leftHeight = dfs(node->left, maxDiameter);
        int rightHeight = dfs(node->right, maxDiameter);
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
- Use DFS to find the height of each node in the tree.
- Maintain a variable to store the maximum diameter found so far.
- The diameter of the tree is the maximum sum of the heights of two child nodes of any node.