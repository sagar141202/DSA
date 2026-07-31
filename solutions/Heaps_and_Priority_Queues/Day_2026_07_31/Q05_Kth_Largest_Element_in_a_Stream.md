# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream is represented as a sequence of integers, and we need to maintain a data structure to efficiently find the kth largest element. The constraints are: 1 <= k <= 10^4, and the stream can contain integers in the range [-10^4, 10^4]. For example, if the stream is [4, 5, 8, 2], and k = 3, the kth largest element is 4.

## Approach
We can use a min-heap to store the k largest elements seen so far. The heap will be maintained such that the smallest element is always at the top. When a new element is added to the stream, we push it into the heap if the heap size is less than k, or if the new element is greater than the smallest element in the heap.

## Complexity
- Time: O(log k) for each element in the stream
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k) : k(k) {}

    void add(int num) {
        // If the heap size is less than k, push the new element into the heap
        if (minHeap.size() < k) {
            minHeap.push(num);
        } 
        // If the new element is greater than the smallest element in the heap, replace it
        else if (num > minHeap.top()) {
            minHeap.pop();
            minHeap.push(num);
        }
    }

    int getKthLargest() {
        // The kth largest element is the smallest element in the heap
        return minHeap.top();
    }
};

int main() {
    KthLargest kthLargest(3);
    kthLargest.add(4);
    kthLargest.add(5);
    kthLargest.add(8);
    kthLargest.add(2);
    cout << kthLargest.getKthLargest() << endl;  // Output: 4
    return 0;
}
```

## Test Cases
```
Input: [4, 5, 8, 2], k = 3
Output: 4
Input: [10, 20, 30, 40], k = 2
Output: 30
```

## Key Takeaways
- We use a min-heap to store the k largest elements seen so far.
- The heap size is maintained at k to ensure efficient retrieval of the kth largest element.
- We push new elements into the heap if the heap size is less than k, or if the new element is greater than the smallest element in the heap.