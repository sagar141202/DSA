# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` is the greed factor of the `i`-th child and `s[j]` is the size of the `j`-th cookie. Assign cookies to children such that the number of children who get a cookie is maximized and the child with a higher greed factor gets a larger cookie. Assume that there are `m` children and `n` cookies, and that `1 <= m <= n <= 20000`.

## Approach
The greedy approach is used to solve this problem, where we first sort both arrays and then assign cookies to children based on their greed factor. We iterate over the sorted arrays, assigning the smallest possible cookie to each child.

## Complexity
- Time: O(m log m + n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort both arrays in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0;  // Index for the child array
        int cookie = 0;  // Index for the cookie array
        
        // Iterate over the sorted arrays
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child's greed
            if (s[cookie] >= g[child]) {
                // Assign the cookie to the child and move to the next child
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // Return the number of children who got a cookie
        return child;
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
- Sort both arrays before assigning cookies to ensure that the smallest possible cookie is assigned to each child.
- Use a two-pointer technique to iterate over the sorted arrays.
- The time complexity is dominated by the sorting operation, which takes O(m log m + n log n) time.