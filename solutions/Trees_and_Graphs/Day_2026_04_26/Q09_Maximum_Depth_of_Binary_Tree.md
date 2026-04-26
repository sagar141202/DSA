# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The length of the path between two nodes is represented by the number of edges between them. For example, the maximum depth of the binary tree with the following structure:
       3
      / \
     9   20
        /  \
       15   7
is 3.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the binary tree and calculate its maximum depth. The maximum depth is the maximum of the depths of the left and right subtrees plus one for the root node.

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
        // base case: if the tree is empty, return 0
        if (root == NULL) return 0;
        
        // recursively calculate the depth of the left and right subtrees
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        
        // return the maximum depth plus one for the root node
        return max(left_depth, right_depth) + 1;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: 3
Input: [1,null,2]
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the tree.
- The space complexity of the algorithm is O(h), where h is the height of the tree.