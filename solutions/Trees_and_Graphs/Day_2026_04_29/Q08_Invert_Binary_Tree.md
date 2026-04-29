# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left and right child nodes of each internal node are swapped. Given the root of a binary tree, invert the tree and return its root. The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100. 

## Approach
The algorithm involves recursively traversing the tree and swapping the left and right child nodes of each internal node. This approach ensures that the entire tree is inverted. The base case for the recursion is when a node is null, in which case the function returns null. 

## Complexity
- Time: O(n)
- Space: O(h)

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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return null
        if (root == nullptr) {
            return nullptr;
        }
        
        // Swap the left and right subtrees
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        // Return the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

## Key Takeaways
- Recursive approach can be used to invert a binary tree by swapping the left and right child nodes of each internal node.
- The base case for the recursion is when a node is null, in which case the function returns null.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.