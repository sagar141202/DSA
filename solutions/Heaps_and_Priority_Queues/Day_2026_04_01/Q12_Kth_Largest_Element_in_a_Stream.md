# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream is represented as a sequence of integers, and we need to design a data structure that can efficiently handle the insertion of new elements and query the kth largest element. The data structure should be able to handle a large number of elements and queries. For example, if the stream is [4, 5, 8, 2] and k = 3, the kth largest element is 4.

## Approach
We can use a min-heap data structure to store the k largest elements from the stream. When a new element is inserted, we check if the heap is not full, and if it is, we remove the smallest element from the heap. This approach ensures that the heap always contains the k largest elements from the stream.

## Complexity
- Time: O(log k) for insertion and query operations
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
#include <vector>
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
Output: kthLargest.add(3); // returns 4
        kthLargest.add(5); // returns 5
        kthLargest.add(10); // returns 5
        kthLargest.add(9); // returns 8
        kthLargest.add(4); // returns 8
```

## Key Takeaways
- Use a min-heap data structure to store the k largest elements from the stream.
- The heap size should be limited to k elements to ensure efficient insertion and query operations.
- The time complexity of insertion and query operations is O(log k), making it suitable for handling large streams and queries.