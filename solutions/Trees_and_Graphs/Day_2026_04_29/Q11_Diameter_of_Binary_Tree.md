# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree, which is the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of the path is the number of edges between the two nodes. The diameter of a tree is the maximum length of a path between any two nodes. For example, in the binary tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
The diameter of this tree is 3, which is the path between nodes 4 and 5.

## Approach
The approach to solve this problem is to calculate the height of the left and right subtrees for each node and keep track of the maximum diameter found so far. We use a recursive depth-first search (DFS) to calculate the height of each subtree. The diameter of a tree is the maximum value of (left_height + right_height + 1) for all nodes.

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
        int max_diameter = 0;
        dfs(root, max_diameter);
        return max_diameter;
    }
    
    int dfs(TreeNode* node, int& max_diameter) {
        if (!node) return 0;
        
        int left_height = dfs(node->left, max_diameter);
        int right_height = dfs(node->right, max_diameter);
        
        max_diameter = max(max_diameter, left_height + right_height);
        
        return 1 + max(left_height, right_height);
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
- The key to solving this problem is to understand that the diameter of a tree is the maximum value of (left_height + right_height + 1) for all nodes.
- We use a recursive DFS to calculate the height of each subtree and keep track of the maximum diameter found so far.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(H) because of the recursive call stack.