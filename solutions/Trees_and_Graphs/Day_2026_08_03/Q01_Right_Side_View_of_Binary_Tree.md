# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node you would visit as you traverse the tree level by level from left to right. The number of nodes in the tree is in the range [1, 100]. The input tree is guaranteed to be a non-empty binary tree. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
We can solve this problem using a level order traversal (BFS) approach, where we iterate through each level of the tree and append the last node value to our result. This way, we ensure that we capture the rightmost node at each level. We use a queue to keep track of nodes at each level.

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
        // Initialize result vector and queue
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);

        // Perform level order traversal
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                // Get the current node
                TreeNode* currentNode = q.front();
                q.pop();

                // If this is the last node at the current level, add its value to the result
                if (i == levelSize - 1) {
                    result.push_back(currentNode->val);
                }

                // Add child nodes to the queue for the next level
                if (currentNode->left) q.push(currentNode->left);
                if (currentNode->right) q.push(currentNode->right);
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
- Use level order traversal (BFS) to capture the rightmost node at each level.
- Utilize a queue to efficiently manage nodes at each level.
- Append the last node value at each level to the result vector to obtain the right side view of the binary tree.