# Kth Largest Element in a Stream

## Problem Statement
Given an integer k and a stream of integers, design an algorithm to find the kth largest element in the stream. The stream can be thought of as an array of integers that is being added to dynamically. The algorithm should be able to handle a large number of integers in the stream and find the kth largest element efficiently. For example, if the stream is [4, 5, 8, 2] and k = 3, the output should be 4 because 4 is the 3rd largest element in the stream.

## Approach
We can use a min-heap to store the k largest elements seen so far. When a new element is added to the stream, we push it into the heap if the heap has less than k elements. If the heap has k elements and the new element is larger than the smallest element in the heap, we remove the smallest element and push the new element into the heap.

## Complexity
- Time: O(log k) for each insertion into the stream
- Space: O(k) for storing the k largest elements

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
public:
    int k;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
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
Input: KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
Output: kthLargest.add(3); // returns 4
       kthLargest.add(5); // returns 5
       kthLargest.add(10); // returns 5
       kthLargest.add(9); // returns 8
```

## Key Takeaways
- The min-heap data structure is used to efficiently find the kth largest element in a stream of integers.
- The time complexity of the algorithm is O(log k) for each insertion into the stream, making it suitable for handling large streams.
- The space complexity is O(k), which is the maximum number of elements stored in the min-heap.