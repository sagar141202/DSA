# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. The next greater element of an element is the first element to its right that is greater than it. If no such element exists, the next greater element is -1. The function should return an array containing the next greater elements for all elements in the input array. The input array will contain distinct integers and will have a length between 1 and 10000.

## Approach
The algorithm uses a stack to keep track of the elements that do not have a next greater element yet. We iterate over the input array, popping elements from the stack that have a next greater element and updating the result array accordingly. The time complexity is reduced by using a stack to avoid unnecessary comparisons.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> nextGreater;
    stack<int> s;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // While the stack is not empty and the top element is smaller than the current number
        while (!s.empty() && s.top() < num) {
            // Update the next greater element for the top element
            nextGreater[s.top()] = num;
            // Pop the top element from the stack
            s.pop();
        }
        // Push the current number onto the stack
        s.push(num);
    }
    
    // Create a result array with the same length as nums1
    vector<int> result(nums1.size());
    // Iterate over nums1 to find the next greater element for each element
    for (int i = 0; i < nums1.size(); i++) {
        // If the next greater element exists, update the result array
        if (nextGreater.find(nums1[i]) != nextGreater.end()) {
            result[i] = nextGreater[nums1[i]];
        } else {
            // If the next greater element does not exist, set it to -1
            result[i] = -1;
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
- Create a map to store the next greater element for each element to avoid redundant calculations.
- Iterate over the input array to find the next greater element for each element and update the result array accordingly.