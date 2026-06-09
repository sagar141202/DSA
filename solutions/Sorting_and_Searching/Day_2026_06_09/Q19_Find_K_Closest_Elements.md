# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the first `k` elements. The array is 1-indexed, and the closest elements are defined as the elements with the smallest absolute difference to the target value. For example, given the array `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`.

## Approach
The approach is to use a two-pointer technique to find the closest elements. We will maintain two pointers, one at the start and one at the end of the subarray, and move them based on the comparison of the elements with the target value. We will use a priority queue to store the elements and their distances from the target value.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Create a priority queue to store the elements and their distances
    priority_queue<pair<int, int>> pq;
    
    // Iterate over the array and push the elements and their distances into the priority queue
    for (int num : arr) {
        pq.push({abs(num - x), num});
        
        // If the priority queue size exceeds k, pop the element with the largest distance
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    // Create a vector to store the k closest elements
    vector<int> result;
    
    // Pop the elements from the priority queue and push them into the result vector
    while (!pq.empty()) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    
    // Sort the result vector
    sort(result.begin(), result.end());
    
    return result;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- Use a priority queue to store the elements and their distances from the target value.
- Maintain a size limit for the priority queue to ensure it only stores the k closest elements.
- Sort the result vector to ensure the elements are in ascending order.