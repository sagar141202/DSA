# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream at any point in time. The stream can be thought of as a sequence of integers where each integer is added to the stream one at a time. The `k`th largest element is the `k`th largest integer in the stream so far. If the stream has less than `k` integers, return the largest integer in the stream. For example, if `k = 3` and the stream is `[4, 5, 8, 2]`, the `k`th largest element is `4`. If the stream is `[1, 2, 3, 4, 5]` and `k = 2`, the `k`th largest element is `4`.

## Approach
We can use a min-heap data structure of size `k` to store the `k` largest elements seen so far. When a new integer is added to the stream, we check if the heap is not full or if the new integer is larger than the smallest integer in the heap. If the heap is not full, we add the new integer to the heap. If the heap is full and the new integer is larger than the smallest integer in the heap, we remove the smallest integer from the heap and add the new integer.

## Complexity
- Time: O(log k) for each addition to the stream
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
#include <vector>

class KthLargest {
private:
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

public:
    KthLargest(int k, std::vector<int>& nums) : k(k) {
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
        return minHeap.size() < k ? (minHeap.empty() ? -1 : minHeap.top()) : minHeap.top();
    }
};
```

## Test Cases
```
Input: k = 3, nums = [4, 5, 8, 2]
Output: 4
Input: k = 2, nums = [1, 2, 3, 4, 5]
Output: 4
```

## Key Takeaways
- Using a min-heap data structure allows for efficient retrieval of the `k`th largest element in the stream.
- The min-heap size is limited to `k`, which reduces the space complexity to O(k).
- The time complexity of adding an element to the stream is O(log k) due to the heap operations.