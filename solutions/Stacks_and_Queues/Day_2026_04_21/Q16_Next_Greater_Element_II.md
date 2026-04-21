# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain distinct integers, and the length of the array will be between 1 and 10,000.

## Approach
Use a stack to keep track of the indices of the elements. Iterate over the array twice to handle the circular case, popping elements from the stack when a greater element is found.

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
    
    // Iterate over the array twice to handle the circular case
    for (int i = 0; i < 2 * n; i++) {
        // Use the modulo operator to handle the circular case
        int j = i % n;
        
        // While the stack is not empty and the current element is greater than the top of the stack
        while (!s.empty() && nums[j] > nums[s.top()]) {
            // Pop the top of the stack and update the result
            result[s.top()] = nums[j];
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
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements.
- Iterate over the array twice to handle the circular case.
- Use the modulo operator to handle the circular case when accessing the array elements.