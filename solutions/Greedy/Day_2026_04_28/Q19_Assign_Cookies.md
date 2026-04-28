# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children and a list of cookies, each with a certain size. We want to assign a cookie to each child such that the child's greed factor is satisfied. The greed factor of a child is the minimum size of cookie that the child will accept. We need to find the maximum number of children that can be satisfied with the given cookies. The constraints are: 1 <= g.length <= 3 * 10^4, 1 <= s.length <= 3 * 10^4, 1 <= g[i] <= 2^31 - 1, 1 <= s[i] <= 2^31 - 1.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting both the children's greed factors and the cookie sizes in ascending order. We then iterate through the sorted lists, assigning the smallest possible cookie to each child.

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
        // Sort the children's greed factors and the cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Pointer for the children
        int cookie = 0; // Pointer for the cookies
        
        // Iterate through the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, move to the next child
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // Return the number of satisfied children
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
- Use two pointers to iterate through the sorted lists and assign cookies to children.
- The time complexity is dominated by the sorting operations.