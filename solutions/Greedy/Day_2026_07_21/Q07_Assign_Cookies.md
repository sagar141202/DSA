# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with different levels of hunger and a list of cookies with different sizes. We need to assign cookies to the children such that each child gets at most one cookie and the hunger of the child is satisfied. The goal is to find the maximum number of children that can be satisfied. The hunger level of a child is satisfied if the size of the cookie is greater than or equal to the hunger level of the child.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting both the hunger levels of the children and the sizes of the cookies in ascending order. Then, we iterate over the sorted lists and assign the smallest possible cookie to each child.

## Complexity
- Time: O(n log n + m log m)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort the hunger levels of the children in ascending order
        sort(g.begin(), g.end());
        // Sort the sizes of the cookies in ascending order
        sort(s.begin(), s.end());
        
        int child = 0; // Index of the current child
        int cookie = 0; // Index of the current cookie
        
        // Iterate over the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child's hunger
            if (s[cookie] >= g[child]) {
                // Move to the next child
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // The number of children that can be satisfied is the index of the last child
        return child;
    }
};
```

## Test Cases
```
Input: g = [1,2,3], s = [1,2]
Output: 2
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort the input lists to apply the greedy algorithm efficiently.
- Use two pointers to iterate over the sorted lists and assign cookies to children.
- The greedy algorithm ensures that the maximum number of children can be satisfied.