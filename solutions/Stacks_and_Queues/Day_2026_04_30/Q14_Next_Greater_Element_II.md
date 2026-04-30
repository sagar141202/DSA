# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will have a length in the range `[1, 104]`, and the elements will be in the range `[-104, 104]`. For example, given `nums = [1, 2, 1]`, the next greater element for each element would be `[2, -1, 2]`.

## Approach
We can use a stack-based approach to solve this problem, iterating through the array twice to simulate the circular behavior. The stack will store the indices of the elements, allowing us to efficiently find the next greater element for each element.

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
    
    // Iterate through the array twice to simulate circular behavior
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i % n]) {
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
- Iterate through the array twice to simulate the circular behavior.
- The time complexity is O(n) because each element is pushed and popped from the stack exactly once.