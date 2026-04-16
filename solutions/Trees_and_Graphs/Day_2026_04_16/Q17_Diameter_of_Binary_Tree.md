# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The length of the path is the number of edges between the two nodes. For example, the diameter of the binary tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
is 3, which is the path between node 4 and node 5.

## Approach
The algorithm involves calculating the height of the left and right subtrees for each node and keeping track of the maximum diameter found. We use a recursive approach to calculate the height and diameter. The diameter of a tree is the maximum of the following: the diameter of the left subtree, the diameter of the right subtree, and the sum of the heights of the left and right subtrees plus one.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

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
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        calculateHeight(root, maxDiameter);
        return maxDiameter;
    }
    
    int calculateHeight(TreeNode* node, int& maxDiameter) {
        if (node == NULL) {
            return 0;
        }
        
        int leftHeight = calculateHeight(node->left, maxDiameter);
        int rightHeight = calculateHeight(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftHeight + rightHeight);
        
        return 1 + max(leftHeight, rightHeight);
    }
};

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    Solution solution;
    int diameter = solution.diameterOfBinaryTree(root);
    
    cout << "Diameter of the binary tree: " << diameter << endl;
    
    return 0;
}
```

## Test Cases
```
Input: 
       1
      / \
     2   3
    / \
   4   5
Output: 3

Input: 
       1
      / \
     2   3
    / \
   4   5
  / \
 6   7
Output: 4
```

## Key Takeaways
- The diameter of a binary tree can be calculated using a recursive approach.
- The height of the left and right subtrees is calculated for each node, and the maximum diameter is updated accordingly.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree.