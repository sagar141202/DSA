# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The constraints are `1 <= k <= arr.length` and `arr` is a sorted array.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It calculates the absolute difference between each element and the target value, then uses a priority queue or a custom sorting function to find the `k` smallest differences. The elements corresponding to these smallest differences are the `k` closest elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    // Create a priority queue to store the differences and corresponding indices
    priority_queue<pair<int, int>> pq;
    for (int i = 0; i < arr.size(); i++) {
        // Calculate the absolute difference between each element and the target value
        int diff = abs(arr[i] - x);
        // Push the difference and index into the priority queue
        pq.push({diff, i});
        // If the queue size exceeds k, pop the largest difference
        if (pq.size() > k) {
            pq.pop();
        }
    }
    // Create a vector to store the k closest elements
    vector<int> result;
    // Pop the elements from the priority queue and push them into the result vector
    while (!pq.empty()) {
        result.push_back(arr[pq.top().second]);
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
- Use a priority queue to efficiently find the k smallest differences.
- The two-pointer technique can be used to find the closest elements in a sorted array.
- The algorithm has a time complexity of O(n log k) due to the use of the priority queue.