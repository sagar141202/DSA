# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in the array are in the range `[1, 10^5]`.

## Approach
We will use a stack-based approach to solve this problem, iterating through the array twice to handle the circular nature of the array. The stack will store indices of elements that do not have a greater element to their right yet.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> s;
    
    // iterate through the array twice to handle circular nature
    for (int i = 0; i < 2 * n; i++) {
        while (!s.empty() && nums[s.top()] < nums[i % n]) {
            result[s.top()] = nums[i % n];
            s.pop();
        }
        s.push(i % n);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1, 2, 1]
Output: [2, -1, 2]
Input: nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

## Key Takeaways
- Use a stack to store indices of elements that do not have a greater element to their right yet.
- Iterate through the array twice to handle the circular nature of the array.
- Use the modulo operator to handle the circular indexing.