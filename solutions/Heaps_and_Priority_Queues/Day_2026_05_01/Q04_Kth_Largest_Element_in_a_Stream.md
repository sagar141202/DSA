# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream can be thought of as an infinite array of integers, and we need to find the kth largest element in the subarray from the beginning to the current position. The value of k is fixed and given beforehand. For example, if the stream is [4, 5, 8, 2] and k = 2, the kth largest element is 5.

## Approach
We can use a min-heap to keep track of the k largest elements seen so far. The heap will store the k largest elements, and its size will always be k. When a new element is added to the stream, we check if the heap is not full. If it's not full, we add the new element to the heap. If the heap is full and the new element is larger than the smallest element in the heap, we remove the smallest element and add the new element.

## Complexity
- Time: O(log k) for each element in the stream, where k is the given value
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
       5
       5
       8
       8
```

## Key Takeaways
- Using a min-heap is an efficient way to keep track of the k largest elements in a stream.
- The time complexity of adding an element to the min-heap is O(log k), where k is the given value.
- The space complexity of storing the min-heap is O(k), where k is the given value.