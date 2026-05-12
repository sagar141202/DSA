# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream. The stream can contain duplicate integers, and the data structure should be able to handle a large number of integers. The `k`th largest element is the `k`th largest unique integer in the stream. For example, if `k` is 3 and the stream is `[4, 5, 8, 2]`, the `k`th largest element is `4`.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. When a new integer is added to the stream, we check if the heap has less than `k` elements or if the new integer is larger than the smallest element in the heap. If either condition is true, we add the new integer to the heap and remove the smallest element if the heap has more than `k` elements.

## Complexity
- Time: O(log k) for each integer in the stream
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
#include <vector>

class KthLargest {
public:
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    KthLargest(int k, std::vector<int>& nums) {
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
Input: k = 3, stream = [4, 5, 8, 2]
Output: 4
Input: k = 1, stream = [1, 2, 3]
Output: 3
```

## Key Takeaways
- Use a min-heap to efficiently store and retrieve the `k` largest elements.
- The time complexity of adding an integer to the stream is O(log k) due to the heap operations.
- The space complexity is O(k) for storing the min-heap.