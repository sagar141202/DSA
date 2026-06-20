# Next Greater Element I

## Problem Statement
The problem "Next Greater Element I" involves finding the next greater element for each element in an array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element `x` is the first element to its right that is greater than `x`. The constraint is that `1 <= nums1.length <= 100` and `1 <= nums2.length <= 100`. For example, if `nums1 = [4,1,2]` and `nums2 = [1,3,4,2]`, then the output should be `[3,-1,3]`.

## Approach
We will use a stack-based approach to solve this problem, iterating over `nums2` and using a stack to keep track of the elements we've seen so far. We will also use a map to store the next greater element for each element in `nums2`. The algorithm iterates over `nums2`, updating the stack and map as it finds greater elements.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element in nums2
    unordered_map<int, int> next_greater;
    stack<int> s;
    
    // Iterate over nums2 to populate the next_greater map
    for (int num : nums2) {
        // While the stack is not empty and the current number is greater than the top of the stack
        while (!s.empty() && num > s.top()) {
            // Update the next greater element for the top of the stack
            next_greater[s.top()] = num;
            // Pop the top element from the stack
            s.pop();
        }
        // Push the current number onto the stack
        s.push(num);
    }
    
    // Create a result vector to store the next greater element for each element in nums1
    vector<int> result;
    for (int num : nums1) {
        // If the next greater element for num exists in the map, add it to the result
        if (next_greater.find(num) != next_greater.end()) {
            result.push_back(next_greater[num]);
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
Output: [3,-1,3]
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

## Key Takeaways
- Use a stack to efficiently find the next greater element for each element in an array.
- Utilize a map to store the next greater element for each element, allowing for constant-time lookups.
- The algorithm has a time complexity of O(n + m), where n and m are the lengths of the input arrays.