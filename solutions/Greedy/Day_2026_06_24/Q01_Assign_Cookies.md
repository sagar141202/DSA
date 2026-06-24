# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if they receive a cookie that is greater than or equal to their greed factor. The goal is to find the maximum number of children that can be satisfied with the given cookies.

## Approach
The approach to solve this problem is to sort both arrays in ascending order and then use two pointers to assign cookies to children. We start by assigning the smallest cookie to the child with the smallest greed factor and continue this process until we have assigned all possible cookies.

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
        
        int child = 0; // Pointer for the children array
        int cookie = 0; // Pointer for the cookies array
        
        // Assign cookies to children
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++; // Assign cookie to child and move to the next child
            }
            cookie++; // Move to the next cookie
        }
        
        return child; // Return the maximum number of children that can be satisfied
    }
};

int main() {
    Solution solution;
    vector<int> g = {1, 2, 3};
    vector<int> s = {1, 2};
    cout << solution.findContentChildren(g, s) << endl;
    return 0;
}
```

## Test Cases
```
Input: g = [1, 2, 3], s = [1, 2]
Output: 2
Input: g = [1, 2], s = [1, 2, 3]
Output: 2
```

## Key Takeaways
- Sort both arrays in ascending order to efficiently assign cookies to children.
- Use two pointers to keep track of the current child and cookie being considered.
- Assign cookies to children based on their greed factor, starting with the smallest cookie and the child with the smallest greed factor.