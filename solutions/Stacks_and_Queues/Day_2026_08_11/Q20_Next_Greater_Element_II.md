# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (in a circular manner) that is greater than `x`. If no such element exists, return `-1`. The input array `nums` will contain unique integers, and the length of `nums` will be between 1 and 1000.

## Approach
We will utilize a stack to keep track of the elements we have seen so far and their indices. We iterate over the array twice to consider the circular nature of the array, and for each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

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
    
    // iterate over the array twice to consider the circular nature
    for (int i = 0; i < 2 * n; i++) {
        // use the modulus operator to wrap around to the start of the array
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
- Use a stack to efficiently keep track of the elements and their indices.
- Iterate over the array twice to consider the circular nature of the array.
- Utilize the modulus operator to wrap around to the start of the array when necessary.