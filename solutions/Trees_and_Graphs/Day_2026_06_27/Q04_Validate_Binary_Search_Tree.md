# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. Constraints: The number of nodes in the tree is in the range [1, 104]. The values of the nodes in the tree are unique. The values of the nodes in the tree are in the range [231, 231 - 1].

## Approach
The algorithm checks each node's value against a valid range, ensuring all left subtree values are less than the node and all right subtree values are greater. This is achieved through a recursive depth-first search (DFS) approach, updating the valid range for each subtree.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

## C++ Solution
```cpp
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidBSTHelper(TreeNode* node, long minVal, long maxVal) {
        if (!node) return true;
        
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        return isValidBSTHelper(node->left, minVal, node->val) &&
               isValidBSTHelper(node->right, node->val, maxVal);
    }
};
```

## Test Cases
```
Input: root = [2,1,3]
Output: true
Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- Use a recursive DFS approach to validate the BST.
- Update the valid range for each subtree to ensure all values are within the correct bounds.
- Handle edge cases, such as an empty tree or a tree with a single node, which are inherently valid BSTs.