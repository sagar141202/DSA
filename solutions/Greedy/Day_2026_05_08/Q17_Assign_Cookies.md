# Assign Cookies

## Problem Statement
Assign Cookies problem is a classic problem in the field of Greedy Algorithms. We are given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie. We need to find the maximum number of children who can be satisfied with the given cookies. A child can be satisfied if the size of the cookie is greater than or equal to the child's greed factor. We need to assign the cookies to the children in such a way that the maximum number of children are satisfied.

## Approach
The algorithm works by first sorting the greed factors of the children and the sizes of the cookies in ascending order. Then, we use two pointers to assign the cookies to the children. The intuition behind this approach is that we want to assign the smallest possible cookie to each child to maximize the number of satisfied children.

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
        
        // Assign cookies to the children
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
- Always sort the input arrays before applying the Greedy Algorithm.
- Use two pointers to keep track of the current position in the input arrays.
- The key to solving this problem is to assign the smallest possible cookie to each child to maximize the number of satisfied children.