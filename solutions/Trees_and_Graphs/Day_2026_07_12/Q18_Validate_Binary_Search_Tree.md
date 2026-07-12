# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. Constraints: The number of nodes in the tree is in the range [1, 104]. The values of the nodes in the tree are unique. The input is guaranteed to be a binary tree.

## Approach
We will use a recursive approach to check each node's value and ensure it falls within the valid range defined by its ancestors. This range will be updated as we traverse the tree. We'll use a helper function to perform the recursive checks.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree.

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
        // Base case: an empty tree is a valid BST
        if (node == NULL) return true;
        
        // Check if the current node's value is within the valid range
        if (node->val <= minVal || node->val >= maxVal) return false;
        
        // Recursively check the left and right subtrees with updated ranges
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
- Use recursion to traverse the tree and validate each node's value.
- Update the valid range for each node based on its ancestors to ensure BST properties are maintained.
- Base cases for recursion include an empty tree (valid BST) and a node with a value outside the valid range (not a valid BST).