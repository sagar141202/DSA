# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `kth` largest element in the stream at any point. The stream can be thought of as a sequence of integers that are generated on the fly. The data structure should support two operations: `add(int num)` to add a new integer to the stream and `kthLargest()` to return the `kth` largest element in the stream. The `kth` largest element is the `kth` largest element in sorted order, not the `kth` distinct element. For example, if the stream is `[4, 5, 8, 2]` and `k = 3`, the `kth` largest element is `4`.

## Approach
We can use a min-heap of size `k` to store the `k` largest elements in the stream. When a new integer is added to the stream, we push it into the heap if the heap is not full. If the heap is full, we check if the new integer is larger than the smallest element in the heap. If it is, we remove the smallest element and push the new integer into the heap.

## Complexity
- Time: O(log k) for `add` and `kthLargest` operations
- Space: O(k) for storing the heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k, vector<int>& nums) : k(k) {
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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
       kthLargest.add(3);
       kthLargest.add(5);
       kthLargest.add(10);
       kthLargest.add(9);
       kthLargest.add(4);
Output: 4
       5
       5
       8
       8
```

## Key Takeaways
- We use a min-heap to store the `k` largest elements in the stream.
- The `add` operation takes O(log k) time complexity.
- The `kthLargest` operation takes O(1) time complexity since we just need to return the top element of the min-heap.