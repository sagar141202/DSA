# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element is the nearest element to its right which is greater than it. If no such element exists, the result is -1. The function should return an array of the same length as the input array, where each element at index i represents the next greater element to the element at index i in the input array. The input array consists of integers and its length is between 1 and 10^5.

## Approach
The algorithm uses a stack to keep track of the elements that do not have a next greater element yet. We iterate over the array from left to right, and for each element, we pop all the elements from the stack that are smaller than the current element and update their next greater element.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> map;
    stack<int> st;
    
    // Iterate over nums2 to fill the map
    for (int num : nums2) {
        // While the stack is not empty and the top of the stack is smaller than the current number
        while (!st.empty() && st.top() < num) {
            // Update the map with the next greater element
            map[st.top()] = num;
            // Pop the top element from the stack
            st.pop();
        }
        // Push the current number onto the stack
        st.push(num);
    }
    
    // Create the result array
    vector<int> result;
    for (int num : nums1) {
        // If the number is in the map, append its next greater element to the result
        if (map.find(num) != map.end()) {
            result.push_back(map[num]);
        } 
        // Otherwise, append -1 to the result
        else {
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
```

## Key Takeaways
- Use a stack to keep track of elements that do not have a next greater element yet.
- Iterate over the array and update the next greater element for each element in the stack that is smaller than the current element.
- Use a map to store the next greater element for each element in the array.