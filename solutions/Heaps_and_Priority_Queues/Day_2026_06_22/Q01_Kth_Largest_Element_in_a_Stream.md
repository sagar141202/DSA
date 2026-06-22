# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream. The stream can contain duplicate integers, and `k` is a positive integer. The data structure should support two operations: `add(int num)` to add an integer to the stream and `kthLargest()` to return the `k`th largest element in the stream. The `k`th largest element is the `k`th largest element in sorted order, not the `k`th distinct element. For example, if the stream is `[4, 5, 8, 2]` and `k = 3`, the `k`th largest element is `4`.

## Approach
We can use a min-heap data structure to store the `k` largest elements seen so far. When a new integer is added to the stream, we check if the heap has less than `k` elements. If it does, we add the integer to the heap. If the heap already has `k` elements and the new integer is larger than the smallest element in the heap, we remove the smallest element and add the new integer.

## Complexity
- Time: O(log k) for `add` operation and O(1) for `kthLargest` operation
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

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
Input: KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

## Key Takeaways
- Use a min-heap to efficiently store the `k` largest elements.
- The `add` operation has a time complexity of O(log k) due to the heap operations.
- The `kthLargest` operation has a time complexity of O(1) since we can directly access the top element of the min-heap.