# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a "linked list": 
- The "linked list" should use the same TreeNode class where each node has two child pointers: left and right.
- Each node's left child should be None.
- Only the right child of each node should be used to form the linked list.
- The tree's nodes should be rearranged such that every node's right child points to the next node in the sequence, with the last node's right child pointing to None.
- The tree should be flattened in an in-order traversal manner.
- Example 1:
  - Input: root = [1,2,3,4,5,6,7]
  - Output: [1,null,2,null,3,null,4,null,5,null,6,null,7]
- Constraints:
  - The number of nodes in the tree is in the range [0, 2000].
  - -100 <= Node.val <= 100

## Approach
We will use a recursive approach to flatten the binary tree into a linked list by rearranging the nodes during an in-order traversal. 
The algorithm will recursively flatten the left and right subtrees and then rearrange the nodes.
This approach ensures the resulting linked list maintains the original in-order traversal sequence.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        // If the tree is empty, return immediately
        if (root == nullptr) return;

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left subtree is not empty, rearrange the nodes
        if (root->left != nullptr) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }

            // Rearrange the nodes
            rightmost->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5,6,7]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7]
```

## Key Takeaways
- To flatten a binary tree into a linked list, we can use a recursive approach with in-order traversal.
- We need to rearrange the nodes after recursively flattening the left and right subtrees.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, because we visit each node once during the in-order traversal.