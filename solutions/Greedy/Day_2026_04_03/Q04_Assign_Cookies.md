# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children and a list of cookies. Each child has a greed factor, which is the minimum size of cookie that the child will be satisfied with. We want to assign cookies to children such that the maximum number of children are satisfied. The problem has the following constraints: 1 <= g.length <= 3 * 10^4, 1 <= s.length <= 3 * 10^4, 1 <= g[i] <= 2^31 - 1, 1 <= s[i] <= 2^31 - 1. For example, if we have g = [1,2,3] and s = [1,1], the output will be 1 because we can only satisfy one child.

## Approach
The approach to solve this problem is to use a greedy algorithm. We first sort both the children's greed factors and the cookies in ascending order. Then, we iterate over the sorted lists and assign the smallest possible cookie to each child.

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
        // Sort the children's greed factors and the cookies in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Index of the current child
        int cookie = 0; // Index of the current cookie
        
        // Iterate over the sorted lists and assign the smallest possible cookie to each child
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++; // The current child is satisfied, move to the next child
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
- Sort the input lists to apply the greedy algorithm.
- Use two pointers to iterate over the sorted lists and assign cookies to children.
- The time complexity is dominated by the sorting operation.