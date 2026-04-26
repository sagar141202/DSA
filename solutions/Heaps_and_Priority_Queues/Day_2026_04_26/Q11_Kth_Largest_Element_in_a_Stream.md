# Kth Largest Element in a Stream

## Problem Statement
Given an integer array `nums` and an integer `k`, find the kth largest element in the array. The array is a stream of integers, and we need to find the kth largest element after each new integer is added to the stream. The constraint is that we can only use O(k) extra space. For example, if `nums` is `[4, 5, 8, 2]` and `k` is `3`, the output should be `[4, 5, 5, 5]` after each new integer is added to the stream.

## Approach
We can use a min-heap to store the k largest elements. The min-heap will always store the k largest elements seen so far. When a new integer is added to the stream, we check if the heap size is less than k. If it is, we add the new integer to the heap. If the heap size is equal to k and the new integer is larger than the smallest element in the heap, we remove the smallest element and add the new integer.

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
Output: [4, 5, 5, 5]
```

## Key Takeaways
- We use a min-heap to store the k largest elements seen so far.
- The time complexity is O(n log k) because we perform a heap operation for each new integer in the stream.
- The space complexity is O(k) because we store at most k elements in the min-heap.