# Kth Largest Element in Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the kth largest element in the array. The kth largest element is the element that would be at index `k-1` if the array were sorted in descending order. The input array will contain at least `k` elements. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5`, which is the 2nd largest element in the array.

## Approach
We can use the `std::sort` function in C++ to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to find the kth largest element efficiently. The intuition behind this approach is to maintain a min-heap of size `k` and iterate through the array, pushing elements into the heap and popping the smallest element when the heap size exceeds `k`.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min-heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Iterate through the array and push elements into the heap
        for (int num : nums) {
            // Push the element into the heap
            minHeap.push(num);
            
            // If the heap size exceeds k, pop the smallest element
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // The top of the heap will be the kth largest element
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1,2,3,4,5], k = 1
Output: 5
```

## Key Takeaways
- Use a min-heap to efficiently find the kth largest element in an array.
- The time complexity of this approach is O(n log k), where n is the size of the array.
- The space complexity is O(k), where k is the number of largest elements to find.