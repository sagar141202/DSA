# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s` where `g[i]` is the greed factor of the ith child and `s[j]` is the size of the jth cookie, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if the size of the cookie is greater than or equal to their greed factor. The arrays `g` and `s` are sorted in ascending order.

## Approach
The problem can be solved using a greedy algorithm by iterating through both arrays and assigning the smallest possible cookie to each child. This approach ensures that the maximum number of children are satisfied.

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
        // Sort both arrays in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, move to the next child
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
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
- The problem can be solved using a greedy algorithm.
- Sorting both arrays in ascending order is necessary to ensure that the smallest possible cookie is assigned to each child.
- The time complexity is dominated by the sorting operation.