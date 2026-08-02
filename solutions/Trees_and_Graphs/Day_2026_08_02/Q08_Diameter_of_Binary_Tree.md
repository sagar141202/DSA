# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. For example, the diameter of the tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5    
The diameter of this tree is 3, which is the path between node 4 and node 5.

## Approach
To find the diameter of a binary tree, we can use a depth-first search (DFS) approach, calculating the height of the left and right subtrees for each node. The diameter is then the maximum sum of these heights plus one for the edge between the two subtrees. 

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

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
Input: [1,2,3,4,5]
Output: 3
```

## Key Takeaways
- The diameter of a binary tree can be found by calculating the maximum sum of the heights of the left and right subtrees for each node.
- A depth-first search (DFS) approach is suitable for this problem, allowing us to efficiently calculate the heights of the subtrees.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, since we visit each node once. The space complexity is O(H), where H is the height of the tree, due to the recursive call stack.