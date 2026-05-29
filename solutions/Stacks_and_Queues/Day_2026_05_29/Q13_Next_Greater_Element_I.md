# Next Greater Element I

## Problem Statement
The problem asks to find the next greater element for each element in the given array. The next greater element of an element x is the first element to the right of x that is greater than x. If no such element exists, the result is -1. The input array contains distinct integers and the length of the array is between 1 and 10^5. The elements in the array are between 1 and 10^5. For example, given the array [2,1,5], the next greater elements are [5,-1,5] because the next greater element of 2 is 5, there is no next greater element for 1, and the next greater element of 5 is -1 (since there is no element to the right of 5).

## Approach
We use a stack to keep track of the elements that do not have a next greater element yet. We iterate through the array and for each element, we pop all the elements from the stack that are smaller than the current element and assign the current element as their next greater element. Then we push the current element onto the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // Create a map to store the next greater element for each element
    unordered_map<int, int> nextGreater;
    stack<int> s;

    // Iterate through nums2 to find the next greater element for each element
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
        // If the next greater element exists, add it to the result array
        if (nextGreater.find(num) != nextGreater.end()) {
            result.push_back(nextGreater[num]);
        }
        // If the next greater element does not exist, add -1 to the result array
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
- Iterate through the array and pop all elements from the stack that are smaller than the current element.
- Assign the current element as the next greater element for the popped elements.
- Push the current element onto the stack.