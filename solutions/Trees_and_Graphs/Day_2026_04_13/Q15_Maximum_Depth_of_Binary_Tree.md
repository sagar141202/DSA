# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree is not limited, and each node has at most two children (i.e., left child and right child). For example, the maximum depth of the binary tree in the figure is 3. Constraints: The number of nodes in the tree is in the range [0, 104]. The depth of the tree is in the range [0, 104]. -100 <= Node.val <= 100.

## Approach
The algorithm involves performing a depth-first search (DFS) or breadth-first search (BFS) traversal of the binary tree. We can use recursion to calculate the maximum depth of the left and right subtrees. The maximum depth of the tree is then the maximum of the depths of the left and right subtrees plus one.

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
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // The maximum depth of the tree is the maximum of the depths of the left and right subtrees plus one
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
- The maximum depth of a binary tree can be calculated using DFS or BFS traversal.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.
- The space complexity of the solution is O(h), where h is the height of the tree.