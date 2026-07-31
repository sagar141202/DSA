# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of lists where the ith list contains the values of the nodes at the ith level of the tree. The traversal should be from left to right, and nodes at the same level should be in the same list. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`.

## Approach
We can use a queue to perform a level order traversal of the binary tree, where we enqueue each node's children and dequeue the current node at each step. This approach ensures that we visit all nodes at a given level before moving on to the next level.

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* currentNode = q.front();
                q.pop();
                level.push_back(currentNode->val);
                
                if (currentNode->left) q.push(currentNode->left);
                if (currentNode->right) q.push(currentNode->right);
            }
            
            result.push_back(level);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a queue to store nodes at each level and dequeue them to process their children.
- Keep track of the number of nodes at each level to separate them into different lists.
- Use a vector of vectors to store the result, where each inner vector represents a level in the tree.