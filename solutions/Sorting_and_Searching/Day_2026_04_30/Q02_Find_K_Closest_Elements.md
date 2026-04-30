# Find K Closest Elements

## Problem Statement
Given a sorted array, find the K closest elements to a target value. The array is sorted in ascending order, and the target value can be any integer. The K closest elements are the K elements in the array that have the smallest absolute difference with the target value. If there are multiple elements with the same absolute difference, the elements with the smaller value should be considered closer. For example, given the array [1, 2, 3, 4, 5] and the target value 3, the 2 closest elements are [2, 3] or [3, 4]. The input array will have at least K elements.

## Approach
The problem can be solved by using a two-pointer technique to find the K closest elements. We can use the lower_bound function to find the first element that is greater than or equal to the target value. Then, we can expand outwards from this element to find the K closest elements.

## Complexity
- Time: O(logN + K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Find the first element that is greater than or equal to the target value
    auto it = lower_bound(arr.begin(), arr.end(), x);
    
    // Initialize two pointers, one at the found element and one before it
    int left = it - arr.begin() - 1;
    int right = it - arr.begin();
    
    // Initialize the result vector
    vector<int> result;
    
    // Expand outwards from the found element to find the K closest elements
    while (k > 0) {
        // If the left pointer is out of bounds or the right pointer is closer to the target value
        if (left < 0 || (right < arr.size() && x - arr[left] > arr[right] - x)) {
            result.push_back(arr[right]);
            right++;
        } 
        // If the right pointer is out of bounds or the left pointer is closer to the target value
        else {
            result.push_back(arr[left]);
            left--;
        }
        k--;
    }
    
    // Sort the result vector
    sort(result.begin(), result.end());
    
    return result;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 2, x = 3
Output: [2, 3] or [3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- The lower_bound function can be used to find the first element that is greater than or equal to the target value.
- A two-pointer technique can be used to expand outwards from the found element to find the K closest elements.
- The result vector should be sorted before returning it.