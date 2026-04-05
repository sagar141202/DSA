# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in the array are in the range `[-10^5, 10^5]`. For example, given `nums = [1, 2, 1]`, the next greater element for each element would be `[2, -1, 2]`.

## Approach
We can use a stack to solve this problem by iterating through the array twice to handle the circular nature. The stack will store the indices of the elements. We will iterate through the array, popping elements from the stack if the current element is greater than the element at the top of the stack.

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
    stack<int> st;
    
    // Iterate through the array twice to handle the circular nature
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[i % n] > nums[st.top()]) {
            // If the current element is greater than the element at the top of the stack, update the result
            result[st.top()] = nums[i % n];
            st.pop();
        }
        st.push(i % n);
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
- Use a stack to store the indices of the elements to efficiently find the next greater element.
- Iterate through the array twice to handle the circular nature of the problem.
- Update the result array whenever a greater element is found for an element at the top of the stack.