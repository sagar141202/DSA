# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The length of the path between two nodes is represented by the number of edges between them. For example, the maximum depth of the binary tree with the following structure:
       3
      / \
     9   20
        /  \
       15   7
is 3, because the path from the root node (3) to the leaf node (15 or 7) has 3 edges.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum depth. It checks the depth of the left and right subtrees and returns the maximum of the two plus one for the current node. This process is repeated until all nodes are visited.

## Complexity
- Time: O(n)
- Space: O(h)

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
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        
        // Recursively calculate the depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum depth of the two subtrees plus one for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: 
   3
  / \
 9  20
   /  \
  15   7
Output: 3

Input: 
  1
 / \
2   3
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because each node is visited once.
- The space complexity of the solution is O(h), where h is the height of the tree, because of the recursive call stack.