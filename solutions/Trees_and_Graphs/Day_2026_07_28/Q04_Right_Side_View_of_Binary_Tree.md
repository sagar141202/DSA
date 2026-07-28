# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. Constraints: The number of nodes in the tree is in the range [1, 100]. -100 <= Node.val <= 100.

## Approach
The solution involves using a level-order traversal (BFS) to visit each node level by level, and at each level, the last visited node is the rightmost node. This approach ensures that we can efficiently find the rightmost node at each level.

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
                TreeNode* currentNode = q.front();
                q.pop();
                
                if (i == levelSize - 1) {
                    result.push_back(currentNode->val);
                }
                
                if (currentNode->left) {
                    q.push(currentNode->left);
                }
                if (currentNode->right) {
                    q.push(currentNode->right);
                }
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

## Key Takeaways
- The level-order traversal is suitable for problems that require processing nodes level by level.
- Using a queue data structure is efficient for level-order traversal.
- The key to this problem is to identify the last node at each level, which can be done by checking the current index against the level size.