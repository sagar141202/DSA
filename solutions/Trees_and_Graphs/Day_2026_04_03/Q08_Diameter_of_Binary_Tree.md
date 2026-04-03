# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. For example, in the tree shown below, the diameter is 3 (path between nodes 4 and 7). The input tree is represented as a binary tree where each node has a value and two children (left and right). The tree is not guaranteed to be balanced.

## Approach
To find the diameter of a binary tree, we can use a depth-first search (DFS) approach where we calculate the height of the left and right subtrees for each node and keep track of the maximum diameter found so far. The diameter of a tree is the maximum value of the sum of the heights of the left and right subtrees plus one for the current node.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

## C++ Solution
```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (!node) return 0;
        
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

Input: 
    1
   / \
  2   3
Output: 2
```

## Key Takeaways
- The diameter of a binary tree can be calculated using a DFS approach.
- We need to keep track of the maximum diameter found so far and update it whenever we find a longer path.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(H) because of the recursive call stack.