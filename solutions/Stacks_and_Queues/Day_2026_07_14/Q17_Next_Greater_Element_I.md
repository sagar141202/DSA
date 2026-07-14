# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is -1. The input consists of two arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`. The function should return an array of the same length as `nums1`, where each element at index `i` is the next greater element of `nums1[i]` in `nums2`. The constraint is that `1 <= nums1.length <= nums2.length <= 1000`, and `0 <= nums1[i], nums2[i] <= 10^4`.

## Approach
The approach is to use a stack to keep track of the elements in `nums2` that do not have a greater element to their right yet. We iterate through `nums2` and for each element, we pop all elements from the stack that are smaller than the current element and update the next greater element for these elements. We then push the current element onto the stack. Finally, we iterate through `nums1` and find the next greater element for each element using the updated next greater elements for `nums2`.

## Complexity
- Time: O(n + m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> st;
    
    // Iterate through nums2 to find the next greater element for each element
    for (int num : nums2) {
        // Pop all elements from the stack that are smaller than the current element
        while (!st.empty() && st.top() < num) {
            nextGreater[st.top()] = num;
            st.pop();
        }
        // Push the current element onto the stack
        st.push(num);
    }
    
    // Initialize the result array with -1
    vector<int> result(nums1.size(), -1);
    
    // Iterate through nums1 to find the next greater element for each element
    for (int i = 0; i < nums1.size(); i++) {
        // Check if the next greater element for the current element exists
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
- Use a stack to keep track of elements that do not have a greater element to their right yet.
- Iterate through the second array to find the next greater element for each element and store it in a map.
- Iterate through the first array to find the next greater element for each element using the map.