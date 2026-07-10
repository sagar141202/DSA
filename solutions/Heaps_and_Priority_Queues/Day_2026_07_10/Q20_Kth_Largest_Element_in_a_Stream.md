# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream. The stream can be very large and we cannot store all the elements in memory. The data structure should support the following operations: `add(int num)` to add a new integer to the stream, and `kthLargest()` to return the `k`th largest element in the stream. The `k`th largest element is the `k`th largest element in the sorted stream in descending order.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. When a new element is added to the stream, we compare it with the smallest element in the heap. If the new element is larger, we remove the smallest element from the heap and add the new element.

## Complexity
- Time: O(log k) for `add` operation and O(1) for `kthLargest` operation
- Space: O(k) for storing the min-heap

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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
       kthLargest.add(3);
       kthLargest.add(5);
       kthLargest.add(10);
       kthLargest.add(9);
       kthLargest.add(4);
Output: 4
```

## Key Takeaways
- We use a min-heap to store the `k` largest elements seen so far.
- The `add` operation takes O(log k) time because we may need to remove and add an element to the heap.
- The `kthLargest` operation takes O(1) time because we simply return the top element of the min-heap.