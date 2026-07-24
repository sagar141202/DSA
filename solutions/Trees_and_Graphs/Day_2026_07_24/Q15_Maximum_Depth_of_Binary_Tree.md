# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must consist of parent-child connections, and the depth of a node is the number of edges in the path from the root to the node. For example, the maximum depth of the binary tree in the figure below is 3. The constraints are: the number of nodes in the tree is in the range [0, 10^4], and -1000 <= Node.val <= 1000.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate its maximum depth. The maximum depth is calculated by finding the maximum depth of the left subtree and the right subtree and adding 1 to it.

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
        // Base case: if the tree is empty, its depth is 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // The maximum depth of the tree is the maximum depth of its subtrees plus 1
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
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity of the solution is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.