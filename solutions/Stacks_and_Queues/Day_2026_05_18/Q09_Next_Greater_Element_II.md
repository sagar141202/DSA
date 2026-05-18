# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (circularly) that is greater than `x`. If no such element exists, return `-1`. The array is considered circular, meaning that the last element is considered to be before the first element. For example, given `nums = [1, 2, 3, 4, 5]`, the next greater element for `1` is `2`, for `2` is `3`, for `3` is `4`, for `4` is `5`, and for `5` is `-1`. The function should return an array of the same length as `nums` where each element at index `i` is the next greater element for `nums[i]`. The input array `nums` will contain at least one element and at most 10,000 elements, and all elements will be in the range `[1, 10^5]`.

## Approach
We will use a stack-based approach to keep track of the elements we have seen so far and their corresponding next greater elements. We iterate over the array twice to consider the circular nature of the array. The algorithm will push elements onto the stack and pop them when a greater element is found.

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
    
    // Iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // Use modulo to wrap around to the start of the array
        int j = i % n;
        
        // While the stack is not empty and the current element is greater than the top of the stack
        while (!s.empty() && nums[j] > nums[s.top()]) {
            // Update the result for the top element of the stack
            result[s.top()] = nums[j];
            // Pop the top element from the stack
            s.pop();
        }
        
        // Push the current index onto the stack
        s.push(j);
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
- Use a stack to keep track of the elements and their next greater elements.
- Iterate over the array twice to consider the circular nature.
- Use modulo to wrap around to the start of the array when necessary.