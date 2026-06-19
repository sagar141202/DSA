# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s` where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie. Assign cookies to children such that the maximum number of children are satisfied, and each child can only be assigned one cookie. A child can be satisfied if the size of the cookie is greater than or equal to their greed factor. The arrays are non-empty and have lengths of at most 1000. The values in the arrays are all positive integers.

## Approach
The approach is to sort both the greed factors and the cookie sizes in ascending order. Then, use two pointers to assign the smallest possible cookie to each child. This greedy strategy ensures the maximum number of children are satisfied.

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
        
        int child = 0; // Pointer for the children
        int cookie = 0; // Pointer for the cookies
        
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
Input: g = [1,2,3], s = [1,1]
Output: 1
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort the input arrays to apply the greedy strategy effectively.
- Use two pointers to keep track of the current child and cookie being considered.
- The time complexity is dominated by the sorting operations.