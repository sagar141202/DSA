# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in the array are in the range `[1, 10^5]`.

## Approach
We can use a stack to keep track of the indices of the elements we have seen so far. We iterate through the array twice to handle the circular case. For each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> s;
        
        // Iterate through the array twice to handle the circular case
        for (int i = 0; i < 2 * n; i++) {
            while (!s.empty() && nums[s.top()] < nums[i % n]) {
                // Update the next greater element for the top element of the stack
                res[s.top()] = nums[i % n];
                s.pop();
            }
            s.push(i % n);
        }
        return res;
    }
};
```

## Test Cases
```
Input: nums = [1,2,1]
Output: [2,-1,2]
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements we have seen so far.
- Iterate through the array twice to handle the circular case.
- Update the next greater element for each element by popping all the smaller elements from the stack.