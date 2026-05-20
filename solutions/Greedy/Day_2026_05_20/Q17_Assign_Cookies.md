# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` is the greed factor of the `i-th` child and `s[j]` is the size of the `j-th` cookie, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if the size of the cookie is greater than or equal to their greed factor. The arrays are not necessarily sorted, and there are no constraints on the number of cookies each child can have, but each cookie can only be assigned to one child.

## Approach
The algorithm sorts both the greed factors and cookie sizes in ascending order. Then, it iterates over the sorted arrays, assigning cookies to children with the smallest greed factor first. This greedy approach ensures the maximum number of children are satisfied.

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
        
        // Iterate over the sorted arrays
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie satisfies the current child, move to the next child
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // The number of satisfied children is the index of the last satisfied child plus one
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
- Sort the input arrays to simplify the problem and enable a greedy approach.
- Assign cookies to children with the smallest greed factor first to maximize the number of satisfied children.
- The algorithm has a time complexity of O(n log n + m log m) due to the sorting step.