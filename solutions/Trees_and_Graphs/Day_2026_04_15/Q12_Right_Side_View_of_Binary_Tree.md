# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node in the level-order traversal of the tree. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`. The constraints are that the number of nodes in the tree is in the range `[0, 100]`, and `-100 <= Node.val <= 100`.

## Approach
We can use a level-order traversal (BFS) approach to solve this problem, where we iterate through each level of the tree and store the last node's value. This approach ensures that we get the rightmost node at each level.

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
                
                // If this is the last node at the current level, add it to the result
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
Input: []
Output: []
```

## Key Takeaways
- Use level-order traversal (BFS) to solve this problem.
- Store the last node's value at each level to get the rightmost node.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is also O(N) due to the queue used for BFS.