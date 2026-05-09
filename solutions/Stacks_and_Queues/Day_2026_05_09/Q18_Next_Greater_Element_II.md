# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1` for that element. The input array `nums` contains distinct integers and has a length of `n`, where `n` is in the range `[1, 10^4]`. The elements of `nums` are in the range `[1, 10^5]`.

## Approach
We can use a stack to keep track of the elements we've seen so far and their indices. We iterate over the array twice to handle the circular case, popping elements from the stack and updating the result when we find a greater element.

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
    stack<int> stack;
    
    // Iterate over the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulus operator to handle the circular case
        int idx = i % n;
        
        // While the stack is not empty and the current element is greater than the top of the stack
        while (!stack.empty() && nums[idx] > nums[stack.top()]) {
            // Pop the top element from the stack and update the result
            result[stack.top()] = nums[idx];
            stack.pop();
        }
        
        // Push the current index onto the stack
        stack.push(idx);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1, 2, 1]
Output: [2, -1, 2]
```

## Key Takeaways
- Use a stack to keep track of the elements we've seen so far and their indices.
- Iterate over the array twice to handle the circular case.
- Use the modulus operator to handle the circular case when indexing the array.