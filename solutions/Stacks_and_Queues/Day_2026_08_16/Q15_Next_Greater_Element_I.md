# Next Greater Element I

## Problem Statement
The problem asks to find the next greater element for each element in the given array. The next greater element of an element `x` is the first element to its right that is greater than `x`. If no such element exists, the next greater element is `-1`. The input array `nums1` is a subset of `nums2`. The function should return an array of the same length as `nums1`, where each element is the next greater element of the corresponding element in `nums1`. The constraints are `1 <= nums1.length <= nums2.length <= 1000`, and `0 <= nums1[i], nums2[i] <= 10^4`.

## Approach
The algorithm uses a stack to keep track of the elements in `nums2` that do not have a next greater element yet. We iterate over `nums2` and for each element, we pop all elements from the stack that are smaller than the current element and update their next greater element. We then push the current element onto the stack.

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
    stack<int> s;
    
    // Iterate over nums2 to find the next greater element for each element
    for (int num : nums2) {
        // Pop all elements from the stack that are smaller than the current element
        while (!s.empty() && s.top() < num) {
            nextGreater[s.top()] = num;
            s.pop();
        }
        // Push the current element onto the stack
        s.push(num);
    }
    
    // Create the result array
    vector<int> result;
    for (int num : nums1) {
        // If the next greater element is found, add it to the result array
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        } else {
            // If no next greater element is found, add -1 to the result array
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
- Use a stack to keep track of the elements that do not have a next greater element yet.
- Iterate over the second array to find the next greater element for each element.
- Use a map to store the next greater element for each element in the second array.