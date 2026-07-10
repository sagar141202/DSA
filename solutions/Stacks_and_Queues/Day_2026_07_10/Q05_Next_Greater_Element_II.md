# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1` for that element. The input array will contain unique integers, and the length of the array will be between 1 and 10,000.

## Approach
We use a stack-based approach to solve this problem. The stack stores the indices of the elements in the array. We iterate through the array, and for each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // iterate through the array twice to handle circular case
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
Input: nums = [1,2,1]
Output: [2,-1,2]
```

## Key Takeaways
- Use a stack to keep track of the indices of the elements that do not have a next greater element yet.
- Iterate through the array twice to handle the circular case.
- Update the next greater element for each element when a greater element is found.