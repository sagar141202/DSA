# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal starts from the leftmost node at each level and moves to the right for even levels, and from the rightmost node at each level and moves to the left for odd levels. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be in the range `[0, 100]`.

## Approach
The algorithm uses a level order traversal (BFS) approach to traverse the tree level by level. It utilizes a queue to store nodes at each level and a flag to track whether the current level should be traversed from left to right or right to left.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        bool isReverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (isReverse) {
                    level.insert(level.begin(), node->val);
                } else {
                    level.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
            isReverse = !isReverse;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a queue to store nodes at each level for efficient level order traversal.
- Utilize a flag to determine the traversal direction at each level.
- Insert or push node values into the level vector based on the current traversal direction.