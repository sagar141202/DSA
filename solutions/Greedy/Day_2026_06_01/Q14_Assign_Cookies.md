# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with their greed factors and a list of cookies with their sizes. The goal is to assign cookies to the children in such a way that the maximum number of children are satisfied. A child is satisfied if the size of the cookie assigned to them is greater than or equal to their greed factor. We need to find the maximum number of children that can be satisfied.

## Approach
The algorithm uses a greedy approach by sorting the children's greed factors and the cookie sizes in ascending order. Then, it iterates over the sorted lists and assigns the smallest possible cookie to each child.

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
        
        int child = 0; // Index of the current child
        int cookie = 0; // Index of the current cookie
        
        // Iterate over the sorted lists and assign the smallest possible cookie to each child
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++; // The current child is satisfied, move to the next one
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
- Sort the input lists to apply the greedy approach.
- Use two pointers to iterate over the sorted lists and assign cookies to children.
- The time complexity is dominated by the sorting operations.