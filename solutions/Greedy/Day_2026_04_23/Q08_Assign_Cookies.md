# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child satisfaction levels and a list of cookie sizes. We need to assign cookies to children such that each child gets a cookie that is at least as large as their satisfaction level. The goal is to find the maximum number of children that can be satisfied. The input consists of two arrays: `g` representing the child satisfaction levels and `s` representing the cookie sizes. Both arrays are sorted in ascending order.

## Approach
The approach is to use a greedy algorithm, sorting both arrays and then iterating through them. We try to satisfy each child with the smallest possible cookie that meets their satisfaction level. If a child can be satisfied, we move on to the next child and the next cookie.

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
        // Sort both arrays
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
        
        // The number of satisfied children is the index of the last satisfied child
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
- The greedy algorithm works because both arrays are sorted, allowing us to make the optimal choice at each step.
- The time complexity is dominated by the sorting of the input arrays.
- The space complexity is constant because we only use a constant amount of space to store the indices and the input arrays.