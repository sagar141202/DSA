# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree, which is the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of the path is the number of edges between the two nodes. The diameter of a tree is the maximum length of a path between any two nodes. For example, in the tree with nodes 1, 2, 3, 4, 5, the diameter is 3, which is the path between nodes 4 and 5. The constraints are that the number of nodes in the tree will be in the range [1, 1000], and the values of nodes will be in the range [0, 1000].

## Approach
The algorithm to find the diameter of a binary tree involves performing a depth-first search (DFS) to find the height of the left and right subtrees for each node. The diameter is then calculated as the maximum of the current diameter and the sum of the heights of the left and right subtrees plus one. This approach ensures that all possible paths between nodes are considered.

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
        int diameter = 0;
        dfs(root, diameter);
        return diameter;
    }
    
    int dfs(TreeNode* node, int& diameter) {
        if (!node) return 0;
        
        int leftHeight = dfs(node->left, diameter);
        int rightHeight = dfs(node->right, diameter);
        
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
- The diameter of a binary tree can be found using a depth-first search (DFS) approach.
- For each node, calculate the height of the left and right subtrees and update the diameter accordingly.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.