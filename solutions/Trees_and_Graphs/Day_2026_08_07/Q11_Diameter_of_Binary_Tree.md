# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. The tree is represented by its root node. For example, given the binary tree with the following structure:
       1
      / \
     2   3
    / \     
   4   5    
The diameter of this tree is 3, which is the path between node 4 and node 5.

## Approach
To solve this problem, we can use a depth-first search (DFS) approach to find the height of each node and keep track of the maximum diameter found so far. The diameter of a tree is the maximum value of the sum of the heights of the left and right subtrees for all nodes.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (node == nullptr) return 0;
        
        int leftHeight = dfs(node->left, maxDiameter);
        int rightHeight = dfs(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftHeight + rightHeight);
        
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
- The diameter of a binary tree can be found by calculating the height of the left and right subtrees for each node and keeping track of the maximum sum of these heights.
- A recursive DFS approach can be used to calculate the height of each node and find the diameter of the tree.
- The time complexity of this approach is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.