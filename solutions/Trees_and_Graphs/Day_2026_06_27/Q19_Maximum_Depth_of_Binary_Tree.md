# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree is limited, and each node can have at most two children (i.e., left child and right child). For example, the maximum depth of the binary tree with the following structure:
       3
      / \
     9  20
       /  \
      15   7
is 3, since the longest path from the root node to any leaf node is 3 nodes long (3 -> 20 -> 15 or 3 -> 20 -> 7).

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and find the maximum depth. It checks if the current node is a leaf node and updates the maximum depth accordingly. The maximum depth is calculated by recursively finding the maximum depth of the left and right subtrees and adding 1 to the maximum of these two depths.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum of the left and right depths plus 1
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
Input: root = [1,null,2]
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be found using a recursive DFS approach.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, since each node is visited once.
- The space complexity of the solution is O(h), where h is the height of the tree, since this is the maximum depth of the recursive call stack.