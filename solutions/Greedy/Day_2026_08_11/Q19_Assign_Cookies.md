# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with different levels of greed factor and a list of cookies with different sizes. The goal is to assign cookies to the children in such a way that the maximum number of children are satisfied. A child is satisfied if they are assigned a cookie that is greater than or equal to their greed factor. The input consists of two lists: `g` representing the greed factors of the children and `s` representing the sizes of the cookies. The output is the maximum number of children that can be satisfied.

## Approach
The approach to this problem is to use a greedy algorithm, sorting both the children's greed factors and the cookie sizes in ascending order. Then, we iterate over the sorted lists, assigning the smallest possible cookie to each child.

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
        // Sort the greed factors and cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Index of the current child
        int cookie = 0; // Index of the current cookie
        
        // Iterate over the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, move to the next child
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // The number of satisfied children is the index of the last child
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
- The number of satisfied children is the index of the last child that was assigned a cookie.