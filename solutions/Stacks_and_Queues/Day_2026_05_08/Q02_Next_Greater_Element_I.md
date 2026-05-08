# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is -1. The input array `nums1` is a subset of the array `nums2`. The function should return an array where each element at index `i` is the next greater element of the corresponding element in `nums1`. The arrays `nums1` and `nums2` contain distinct elements and the length of `nums1` is less than or equal to the length of `nums2`.

## Approach
The solution uses a stack to keep track of the elements from `nums2` that do not have a greater element to their right yet. We iterate over `nums2` and for each element, we pop all elements from the stack that are smaller than the current element and update the next greater element for these elements. Finally, we iterate over `nums1` and find the next greater element for each element using the updated information.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> st;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // Pop all elements from the stack that are smaller than the current element
        while (!st.empty() && st.top() < num) {
            nextGreater[st.top()] = num;
            st.pop();
        }
        // Push the current element to the stack
        st.push(num);
    }
    
    // Iterate over nums1 to find the next greater element for each element
    vector<int> result;
    for (int num : nums1) {
        // If the next greater element is found, add it to the result
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        } else {
            // If not found, add -1 to the result
            result.push_back(-1);
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
- Use a stack to keep track of elements that do not have a greater element to their right yet.
- Use an unordered map to store the next greater element for each element in `nums2`.
- Iterate over `nums1` to find the next greater element for each element using the updated information.