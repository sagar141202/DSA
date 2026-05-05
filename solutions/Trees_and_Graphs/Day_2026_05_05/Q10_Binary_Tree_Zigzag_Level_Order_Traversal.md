# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should handle trees of any size and structure, with nodes having a value and at most two children (left and right). For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`.

## Approach
The algorithm uses a level order traversal (BFS) approach with a queue to traverse the tree level by level. It utilizes a flag to track the current level's order (normal or reverse) and reverses the level's nodes when necessary.

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        bool isReverse = false;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
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
- Use a queue to perform level order traversal of the binary tree.
- Utilize a flag to track the current level's order and reverse the level's nodes when necessary.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.