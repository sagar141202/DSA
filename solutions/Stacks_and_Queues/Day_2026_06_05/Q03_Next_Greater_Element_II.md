# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If there is no such element, return `-1`. The input array `nums` will have a length in the range `[1, 10^4]` and will contain only integers in the range `[-10^4, 10^4]`. For example, given `nums = [1, 2, 1]`, the next greater element for each element would be `[2, -1, 2]`.

## Approach
We use a stack-based approach to solve this problem. We iterate over the array twice to handle the circular nature of the array, and for each element, we pop all elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // iterate over the array twice to handle circular nature
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i % n]) {
            // update next greater element for top of stack
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
- Use a stack to keep track of indices of elements that we have not found the next greater element for yet.
- Iterate over the array twice to handle the circular nature of the array.
- For each element, pop all elements from the stack that are smaller than the current element and update their next greater element.