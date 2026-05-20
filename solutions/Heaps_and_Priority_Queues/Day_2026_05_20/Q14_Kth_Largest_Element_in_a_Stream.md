# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure that can find the `k`th largest element in the stream. The stream can be very large and we cannot store all the elements in memory. The data structure should support two operations: `add(int num)` to add a new integer to the stream, and `kthLargest()` to return the `k`th largest element in the stream. For example, if `k = 3` and the stream is `[4, 5, 8, 2]`, the `k`th largest element is `4`.

## Approach
We will use a min-heap to store the `k` largest elements in the stream. When a new element is added, we check if the heap has less than `k` elements, if so, we add the new element to the heap. If the heap already has `k` elements, we compare the new element with the smallest element in the heap (the root), if the new element is larger, we remove the root and add the new element to the heap.

## Complexity
- Time: O(log k) for `add` operation and O(1) for `kthLargest` operation
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
       kthLargest.add(3);
       kthLargest.add(5);
       kthLargest.add(10);
       kthLargest.add(9);
       kthLargest.add(4);
Output: 4
```

## Key Takeaways
- Use a min-heap to store the `k` largest elements in the stream.
- The `add` operation has a time complexity of O(log k) due to the use of a min-heap.
- The `kthLargest` operation has a time complexity of O(1) since we can directly access the root of the min-heap.