# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start from the root node and end at any leaf node. The number of nodes at each level is not limited, and each node has at most two children (i.e., left child and right child). For example, the maximum depth of the binary tree with the following structure:
        3
       / \
      9   20
         /  \
        15   7
is 3, because the path 3 -> 20 -> 15 (or 3 -> 20 -> 7) has the maximum length.

## Approach
The approach to solve this problem is to use a recursive depth-first search (DFS) algorithm, where we traverse the tree and keep track of the maximum depth encountered. We start at the root node and recursively explore the left and right subtrees, updating the maximum depth as we go. The maximum depth is the maximum of the depths of the left and right subtrees plus one (for the current node).

## Complexity
- Time: O(N)
- Space: O(H)

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
        
        // Return the maximum of the depths of the left and right subtrees plus one (for the current node)
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: 3
```

## Key Takeaways
- The maximum depth of a binary tree can be found using a recursive DFS algorithm.
- The time complexity of this algorithm is O(N), where N is the number of nodes in the tree, because we visit each node once.
- The space complexity of this algorithm is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.