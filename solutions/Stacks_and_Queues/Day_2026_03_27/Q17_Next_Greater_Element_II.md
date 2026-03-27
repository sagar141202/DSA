# Next Greater Element II

## Problem Statement
Given a circular array of integers `nums`, find the next greater element for each element. The next greater element of an element `x` is the first element to its right (circularly) that is greater than `x`. If no such element exists, return `-1`. The input array will contain unique integers, and the length of the array will be between 1 and 10^5. For example, given `nums = [1, 2, 1]`, the output should be `[2, -1, 2]`.

## Approach
We can use a stack to keep track of the elements we have seen so far. We iterate over the array twice to handle the circular case. For each element, we pop all elements from the stack that are smaller than the current element and update the result array accordingly.

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
        // Use the modulus operator to handle the circular case
        int j = i % n;
        
        // While the stack is not empty and the top element is smaller than the current element
        while (!s.empty() && nums[s.top()] < nums[j]) {
            // Update the result array and pop the top element from the stack
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
Input: nums = [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

## Key Takeaways
- Use a stack to keep track of the elements we have seen so far.
- Iterate over the array twice to handle the circular case.
- Use the modulus operator to handle the circular case when indexing the array.