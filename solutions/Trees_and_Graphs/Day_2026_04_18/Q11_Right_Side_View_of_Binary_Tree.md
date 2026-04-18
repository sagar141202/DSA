# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node to be visited during a level order traversal of the tree. The number of nodes in the tree is in the range [1, 100]. The input tree is a valid binary tree. For example, given the following binary tree:
```
    1
   / \
  2   3
 / \
4   5
```
The right side view of this tree is [1, 3, 5].

## Approach
The algorithm uses a level order traversal (BFS) approach to traverse the tree level by level, storing the last node value at each level. This is achieved by using a queue to store the nodes at each level and updating the result with the last node value.

## Complexity
- Time: O(N)
- Space: O(N)

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Input: [1,null,3]
Output: [1,3]
Input: [1,2,3,4,5,6,7]
Output: [1,3,7]
```

## Key Takeaways
- Use level order traversal (BFS) to traverse the tree level by level.
- Store the last node value at each level to get the right side view.
- Use a queue to store the nodes at each level and update the result accordingly.