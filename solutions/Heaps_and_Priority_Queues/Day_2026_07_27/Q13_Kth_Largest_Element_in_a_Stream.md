# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream is represented as a sequence of integers, and we need to maintain a data structure to efficiently find the kth largest element. The value of k is given, and we can assume that k is less than or equal to the number of elements seen so far. For example, if the stream is [4, 5, 8, 2] and k = 2, the kth largest element is 5.

## Approach
We can use a min-heap to store the k largest elements seen so far. When a new element is added to the stream, we check if the heap has less than k elements. If it does, we add the new element to the heap. If the heap already has k elements, we compare the new element with the smallest element in the heap (the root). If the new element is larger, we remove the root and add the new element to the heap.

## Complexity
- Time: O(log k) for adding a new element to the stream
- Space: O(k) for storing the k largest elements in the heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k) : k(k) {}

    void add(int val) {
        // If the heap has less than k elements, add the new element
        if (minHeap.size() < k) {
            minHeap.push(val);
        } 
        // If the new element is larger than the smallest element in the heap, replace it
        else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
    }

    int getKthLargest() {
        // The kth largest element is the smallest element in the heap
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: KthLargest kthLargest(3); 
       kthLargest.add(4); 
       kthLargest.add(5); 
       kthLargest.add(8); 
       kthLargest.add(2);
Output: kthLargest.getKthLargest() -> 4
```

## Key Takeaways
- Use a min-heap to efficiently maintain the k largest elements in a stream.
- The time complexity of adding a new element to the stream is O(log k) due to the heap operations.
- The space complexity is O(k) for storing the k largest elements in the heap.