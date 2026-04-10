# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. Constraints: The number of nodes in the tree is in the range [1, 104]. The values of the nodes in the tree are in the range [-231, 231 - 1].

## Approach
We can solve this problem by using a recursive approach and checking if each node's value falls within a valid range. The range for the root node is negative infinity to positive infinity, and for each subsequent node, the range is updated based on the parent node's value.

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
        // Base case: an empty tree is a valid BST
        if (node == NULL) {
            return true;
        }

        // If the current node's value is not within the valid range, return false
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }

        // Recursively check the left and right subtrees with updated ranges
        return isValidBSTHelper(node->left, minVal, node->val) &&
               isValidBSTHelper(node->right, node->val, maxVal);
    }
};
```

## Test Cases
```
Input: [2,1,3]
Output: true
Input: [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- A valid BST must satisfy the property that all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- The recursive approach with range updates is an efficient way to solve this problem.
- The time complexity is O(N) because we visit each node exactly once, and the space complexity is O(H) due to the recursive call stack.