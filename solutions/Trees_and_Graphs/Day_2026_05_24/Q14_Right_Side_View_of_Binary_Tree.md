# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node you would encounter when traversing the tree level by level from left to right. The input tree is a binary tree where each node has a value and two children (left and right). The number of nodes in the tree is in the range [1, 100]. The values of the nodes are in the range [-231, 231 - 1]. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
We can solve this problem using a level-order traversal (BFS) approach, where we traverse each level from left to right and store the last node value at each level. This can be achieved by using a queue to store the nodes at each level. We start by adding the root node to the queue, then enter a loop where we process all nodes at the current level, adding their children to the queue for the next level.

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
                
                // If this is the last node at the current level, add its value to the result
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
```

## Key Takeaways
- Use level-order traversal to process the tree level by level.
- At each level, the last node processed will be the rightmost node.
- Utilize a queue to efficiently manage nodes at each level.