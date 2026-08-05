# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` contains distinct integers and has a length of `n`, where `1 <= n <= 10^5`. The elements in the array are in the range `[1, 10^5]`.

## Approach
We will use a stack-based approach to solve this problem. The stack will store the indices of the elements in the array. We will iterate over the array twice to consider the circular nature of the array. For each element, we will pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.

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
    
    // iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // use the modulus operator to wrap around the array
        int idx = i % n;
        
        // pop all the elements from the stack that are smaller than the current element
        while (!st.empty() && nums[st.top()] < nums[idx]) {
            result[st.top()] = nums[idx];
            st.pop();
        }
        
        // push the current index onto the stack
        st.push(idx);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1,2,1]
Output: [2,-1,2]
```

## Key Takeaways
- Use a stack to store the indices of the elements in the array.
- Iterate over the array twice to consider the circular nature of the array.
- Pop all the elements from the stack that are smaller than the current element and update the next greater element for these elements.