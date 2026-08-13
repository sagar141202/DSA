# Next Greater Element I

## Problem Statement
The problem requires finding the next greater element for each element in the given array. Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`. If no such element exists, return -1. The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`. The input arrays `nums1` and `nums2` contain only unique elements, and the length of `nums1` is less than or equal to the length of `nums2`.

## Approach
We use a stack to store the indices of elements from `nums2` and iterate over `nums2` to find the next greater element for each element. We then use a hashmap to store the next greater element for each element in `nums2` and finally find the next greater element for each element in `nums1`.

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
    stack<int> s;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // While the stack is not empty and the top element is less than the current element
        while (!s.empty() && s.top() < num) {
            // Pop the top element from the stack and update the next greater element
            nextGreater[s.top()] = num;
            s.pop();
        }
        // Push the current element to the stack
        s.push(num);
    }
    
    // Create a result vector to store the next greater element for each element in nums1
    vector<int> result;
    for (int num : nums1) {
        // If the next greater element exists, add it to the result vector
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        } else {
            // If no next greater element exists, add -1 to the result vector
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
- Use a stack to efficiently find the next greater element for each element in the array.
- Utilize a hashmap to store the next greater element for each element and reduce the time complexity.
- Handle edge cases where no next greater element exists for an element.