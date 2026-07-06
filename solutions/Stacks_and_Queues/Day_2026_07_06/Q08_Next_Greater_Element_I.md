# Next Greater Element I

## Problem Statement
Given two arrays, find the next greater element for each element in the first array. The next greater element of an element `x` is the first element to its right in the second array that is greater than `x`. If no such element exists, return `-1`. The first array contains distinct integers, and the second array contains distinct integers as well. The length of the first array is `nums1.length` and the length of the second array is `nums2.length`. For example, given `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, the next greater element for each element in `nums1` is `[2,-1,3]` and `[-1,3,-1]` respectively for the two possible orders of `nums2`.

## Approach
The approach is to use a stack to keep track of the elements in `nums2` and iterate over `nums1` to find the next greater element for each element. We will use a hashmap to store the next greater element for each element in `nums2`.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a hashmap to store the next greater element for each element in nums2
    unordered_map<int, int> hashmap;
    stack<int> st;
    
    // Iterate over nums2 to populate the hashmap
    for (int num : nums2) {
        // While the stack is not empty and the top of the stack is less than the current number
        while (!st.empty() && st.top() < num) {
            // Pop the top of the stack and update the hashmap
            hashmap[st.top()] = num;
            st.pop();
        }
        // Push the current number onto the stack
        st.push(num);
    }
    
    // Iterate over nums1 to find the next greater element for each element
    vector<int> result;
    for (int num : nums1) {
        // If the hashmap contains the current number, add the next greater element to the result
        if (hashmap.find(num) != hashmap.end()) {
            result.push_back(hashmap[num]);
        } else {
            // Otherwise, add -1 to the result
            result.push_back(-1);
        }
    }
    return result;
}
```

## Test Cases
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [2,-1,3]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to keep track of the elements in `nums2` and iterate over `nums1` to find the next greater element for each element.
- Use a hashmap to store the next greater element for each element in `nums2` to avoid redundant calculations.
- The time complexity is O(n + m) where n is the length of `nums1` and m is the length of `nums2`.