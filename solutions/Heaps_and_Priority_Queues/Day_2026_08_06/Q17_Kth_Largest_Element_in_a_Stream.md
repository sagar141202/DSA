# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream can be thought of as an infinite array that is being populated one element at a time. The kth largest element is the kth largest element in the stream so far. For example, if the stream is [4, 5, 8, 2] and k = 2, the kth largest element is 5. If the stream is [4, 5, 8, 2] and k = 3, the kth largest element is 4.

## Approach
We can use a min-heap data structure to solve this problem efficiently. The min-heap will store the k largest elements seen so far in the stream. When a new element is added to the stream, we check if the min-heap has less than k elements or if the new element is larger than the smallest element in the min-heap.

## Complexity
- Time: O(log k) for each element in the stream
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
#include <vector>

class KthLargest {
public:
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    int k;

    KthLargest(int k, std::vector<int>& nums) : k(k) {
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (min_heap.size() < k) {
            min_heap.push(val);
        } else if (val > min_heap.top()) {
            min_heap.pop();
            min_heap.push(val);
        }
        return min_heap.top();
    }
};
```

## Test Cases
```
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
       kthLargest.add(3);
       kthLargest.add(5);
       kthLargest.add(10);
       kthLargest.add(9);
       kthLargest.add(4);
Output: 4, 5, 5, 8, 8
```

## Key Takeaways
- Use a min-heap to store the k largest elements seen so far in the stream.
- When a new element is added to the stream, check if the min-heap has less than k elements or if the new element is larger than the smallest element in the min-heap.
- The time complexity of adding an element to the stream is O(log k) due to the min-heap operations.