# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. The binary tree node has an integer value and two children (left child and right child). The diameter should be calculated considering all possible paths.

## Approach
To solve this problem, we will use a depth-first search (DFS) approach and calculate the height of the left and right subtree for each node. The diameter at each node is the sum of the heights of the left and right subtrees. We keep track of the maximum diameter seen so far.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

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
        int ans = 1;
        depth(root, ans);
        return ans - 1; // subtract 1 because diameter is defined as the number of edges
    }
    
    int depth(TreeNode* node, int& ans) {
        if (!node) return 0;
        int L = depth(node->left, ans);
        int R = depth(node->right, ans);
        ans = max(ans, L + R + 1); // update ans if current diameter is larger
        return max(L, R) + 1; // return the depth of the current node
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
- The key to solving this problem is to use DFS to calculate the height of the left and right subtree for each node.
- Keep track of the maximum diameter seen so far and update it whenever a larger diameter is found.
- The final diameter is the maximum diameter seen minus one, because the diameter is defined as the number of edges between two nodes.