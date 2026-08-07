# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is `-1`. The input array `nums1` is a subset of `nums2`. The function should return an array of the same length as `nums1` where each element at index `i` is the next greater element of `nums1[i]` in `nums2`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a greater element to their right yet. We iterate over `nums2` and for each element, we pop all elements from the stack that are smaller than the current element and update the next greater element for these elements. We then push the current element to the stack.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a hashmap to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> stk;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // While the stack is not empty and the top element is smaller than the current element
        while (!stk.empty() && stk.top() < num) {
            // Update the next greater element for the top element
            nextGreater[stk.top()] = num;
            // Pop the top element from the stack
            stk.pop();
        }
        // Push the current element to the stack
        stk.push(num);
    }
    
    // Create a result array to store the next greater element for each element in nums1
    vector<int> result(nums1.size(), -1);
    
    // Iterate over nums1 to find the next greater element for each element
    for (int i = 0; i < nums1.size(); i++) {
        // If the next greater element for the current element exists, update the result array
        if (nextGreater.find(nums1[i]) != nextGreater.end()) {
            result[i] = nextGreater[nums1[i]];
        }
    }
    
    return result;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements that do not have a greater element to their right yet.
- Use a hashmap to store the next greater element for each element in `nums2`.
- Iterate over `nums2` to find the next greater element for each element and update the hashmap.
- Iterate over `nums1` to find the next greater element for each element using the hashmap.