# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie. Assign cookies to children such that the number of children who get a cookie is maximized. A child can be assigned a cookie if the size of the cookie is greater than or equal to the child's greed factor. Assume that the cookies are assigned in the order they appear in the array.

## Approach
The idea is to sort both the children's greed factors and the cookie sizes in ascending order. Then, iterate over the sorted arrays and assign the smallest possible cookie to each child.

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
        // Sort the children's greed factors and the cookie sizes
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child's greed, assign it
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // The number of children who get a cookie is the answer
        return child;
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
Input: g = [1,2,3], s = [1,2]
Output: 2
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort the input arrays to simplify the assignment process.
- Use two pointers to iterate over the sorted arrays.
- Assign the smallest possible cookie to each child to maximize the number of children who get a cookie.