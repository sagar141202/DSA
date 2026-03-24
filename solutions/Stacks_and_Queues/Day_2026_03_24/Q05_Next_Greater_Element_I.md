# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is considered to be `-1`. The input array `nums1` is a subset of the input array `nums2`. The task is to find the next greater element for each element in `nums1` and return the results in the corresponding order. The constraints are: `1 <= nums1.length <= nums2.length <= 1000`, `1 <= nums1[i], nums2[i] <= 1000`, and `nums1` is a subset of `nums2`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a next greater element yet. It iterates over `nums2` and for each element, it pops all the elements from the stack that are smaller than the current element and updates the next greater element for these elements. The next greater element for each element in `nums1` is stored in a map for efficient lookup.

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
    // Create a stack to keep track of the elements in nums2 that do not have a next greater element yet
    stack<int> stk;
    
    // Iterate over nums2
    for (int num : nums2) {
        // While the stack is not empty and the top element of the stack is smaller than the current element
        while (!stk.empty() && stk.top() < num) {
            // Update the next greater element for the top element of the stack
            nextGreater[stk.top()] = num;
            // Pop the top element from the stack
            stk.pop();
        }
        // Push the current element onto the stack
        stk.push(num);
    }
    
    // Create a vector to store the next greater element for each element in nums1
    vector<int> result;
    // Iterate over nums1
    for (int num : nums1) {
        // If the next greater element for the current element is found in the map, add it to the result
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        } else {
            // If the next greater element is not found, add -1 to the result
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
- Use a stack to efficiently find the next greater element for each element in the array.
- Use a map to store the next greater element for each element in the array for efficient lookup.
- The algorithm has a time complexity of O(n + m) and a space complexity of O(n + m), where n and m are the lengths of the input arrays.