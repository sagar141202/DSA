# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if the size of the cookie is greater than or equal to their greed factor. The goal is to find the maximum number of children that can be satisfied with the given cookies.

## Approach
The problem can be solved by sorting both arrays and then using a two-pointer technique to assign cookies to children. We start by assigning the smallest cookie to the child with the smallest greed factor and continue this process until we run out of cookies or children.

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
        
        int child = 0; // Pointer for children
        int cookie = 0; // Pointer for cookies
        
        // Assign cookies to children
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++; // Child is satisfied, move to the next child
            }
            cookie++; // Move to the next cookie
        }
        
        return child; // Return the number of satisfied children
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
- Sort the input arrays to simplify the assignment process.
- Use a two-pointer technique to assign cookies to children efficiently.
- The time complexity is dominated by the sorting operation.