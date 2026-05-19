# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The left child of a node should become the right child, and the original right child should become the left child of the left child's rightmost node. The problem can be visualized as follows: 
- For a tree node with value x and left child L, and right child R, we want to transform it into a linked list with the following structure: x -> L' -> R', where L' is the transformed left subtree and R' is the transformed right subtree.

## Approach
The solution involves a recursive approach where we first flatten the left and right subtrees and then rearrange the nodes to form a linked list. We will use a helper function to recursively flatten the subtrees and then connect them. 

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
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
    void flatten(TreeNode* root) {
        // Base case: if tree is empty, return
        if (!root) return;

        // Recursively flatten left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If left child exists, rearrange the nodes
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) {
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
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- Recursively flattening the left and right subtrees is essential for this problem.
- The key insight is to find the rightmost node in the left subtree and connect it to the right subtree.
- The time complexity is O(n) because we visit each node once, and the space complexity is O(n) due to the recursive call stack.