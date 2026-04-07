# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s` where `g[i]` is the greed factor of the `i`-th child and `s[j]` is the size of the `j`-th cookie, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if the size of the cookie assigned to them is greater than or equal to their greed factor. The goal is to find the maximum number of children that can be satisfied.

## Approach
The algorithm sorts both the greed factors and cookie sizes in ascending order, then iterates through the sorted arrays, assigning the smallest possible cookie to each child. This approach ensures that the maximum number of children are satisfied.

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
        
        int child = 0;  // Index of the current child
        int cookie = 0;  // Index of the current cookie
        
        // Iterate through the sorted arrays
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, assign it
            if (s[cookie] >= g[child]) {
                child++;  // Move to the next child
            }
            cookie++;  // Move to the next cookie
        }
        
        // The number of satisfied children is the index of the last satisfied child
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
- Sort the input arrays to simplify the assignment process
- Use a two-pointer technique to iterate through the sorted arrays
- Assign the smallest possible cookie to each child to maximize the number of satisfied children