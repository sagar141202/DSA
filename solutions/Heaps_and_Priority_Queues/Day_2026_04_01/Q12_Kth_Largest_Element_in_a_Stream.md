# Kth Largest Element in a Stream

## Problem Statement
Given an unsorted array of integers `nums` and an integer `k`, find the `k`th largest element in the array. The array can be considered as a stream of integers, and we need to find the `k`th largest element at each step. The `k`th largest element is the `k`th largest element in the sorted array. If `k` is larger than the number of elements in the array, return -1. For example, if `nums` = [4, 5, 8, 2] and `k` = 3, the `k`th largest element is 4.

## Approach
We can use a min-heap to store the `k` largest elements. We iterate through the array, and for each element, we check if the heap has less than `k` elements or if the current element is larger than the smallest element in the heap. If so, we add the current element to the heap and remove the smallest element if the heap has more than `k` elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (minHeap.size() < k) {
            minHeap.push(val);
        } else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: nums = [4, 5, 8, 2], k = 3
Output: 4
Input: nums = [4, 5, 8, 2], k = 4
Output: 2
```

## Key Takeaways
- We use a min-heap to store the `k` largest elements, which allows us to efficiently find the smallest element in the heap.
- We iterate through the array and add each element to the heap if it is larger than the smallest element in the heap or if the heap has less than `k` elements.
- The time complexity is O(n log k) because we perform a heap operation for each element in the array, and each heap operation takes O(log k) time.