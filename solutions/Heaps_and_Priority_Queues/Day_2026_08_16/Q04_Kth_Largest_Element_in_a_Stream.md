# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream can be thought of as an infinite sequence of integers, and we need to maintain a data structure to keep track of the kth largest element seen so far. The constraints are that the stream is unbounded, and we need to find the kth largest element in O(log n) time complexity. For example, if the stream is 4, 5, 8, 2, and k = 3, the kth largest element is 4.

## Approach
We can use a min-heap data structure to solve this problem. The min-heap will store the k largest elements seen so far, and we will maintain the heap property to ensure that the smallest element in the heap is always at the top. When a new element is added to the stream, we will insert it into the heap if the heap size is less than k, or if the new element is larger than the smallest element in the heap.

## Complexity
- Time: O(log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class KthLargest {
public:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    KthLargest(int k) : k(k) {}

    void add(int val) {
        // if the heap size is less than k, insert the new element into the heap
        if (minHeap.size() < k) {
            minHeap.push(val);
        } 
        // if the new element is larger than the smallest element in the heap, replace the smallest element with the new element
        else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
    }

    int getKthLargest() {
        // the kth largest element is the smallest element in the heap
        return minHeap.top();
    }
};

int main() {
    KthLargest kthLargest(3);
    kthLargest.add(4);
    kthLargest.add(5);
    kthLargest.add(8);
    kthLargest.add(2);
    cout << kthLargest.getKthLargest() << endl;
    return 0;
}
```

## Test Cases
```
Input: [4, 5, 8, 2], k = 3
Output: 4
```

## Key Takeaways
- We use a min-heap data structure to maintain the k largest elements seen so far.
- The time complexity of adding an element to the stream is O(log k) due to the heap operations.
- The space complexity is O(k) as we need to store the k largest elements in the heap.