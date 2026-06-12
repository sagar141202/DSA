# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the first `k` elements. The array is sorted in ascending order. The closest elements are defined as the elements with the smallest absolute difference to the target value `x`.

## Approach
The approach involves using a two-pointer technique to find the closest elements. We maintain two pointers, one at the start and one at the end of the array, and move them based on the comparison with the target value. We use a priority queue to store the closest elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // Create a priority queue to store the closest elements
        priority_queue<pair<int, int>> pq;
        
        // Push all elements into the priority queue
        for (int num : arr) {
            pq.push({abs(num - x), num});
        }
        
        // Create a result vector to store the k closest elements
        vector<int> result;
        
        // Pop the k closest elements from the priority queue
        for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        
        // Sort the result vector
        sort(result.begin(), result.end());
        
        return result;
    }
};
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [5, 10, 15]
```

## Key Takeaways
- The two-pointer technique is useful for finding the closest elements in a sorted array.
- A priority queue can be used to efficiently store and retrieve the closest elements.
- The result vector needs to be sorted after popping the k closest elements from the priority queue.