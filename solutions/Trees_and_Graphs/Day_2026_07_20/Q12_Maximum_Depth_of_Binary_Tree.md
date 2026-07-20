# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. For example, the maximum depth of the binary tree in the figure below is 3. The constraints for this problem are that the number of nodes in the tree will be in the range [0, 10^4] and the value of each node will be in the range [-2^31, 2^31 - 1]. 

## Approach
The algorithm to find the maximum depth of a binary tree involves using a recursive or iterative approach to traverse the tree and keep track of the maximum depth encountered. We can use a depth-first search (DFS) to solve this problem. The idea is to recursively calculate the maximum depth of the left and right subtrees and return the maximum of the two plus one for the current node.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum of the two depths plus one for the current node
        return max(leftDepth, rightDepth) + 1;
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
- The maximum depth of a binary tree can be found using a recursive DFS approach.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, since we visit each node once.
- The space complexity of this solution is O(H), where H is the height of the tree, since that's the maximum depth of the recursive call stack.