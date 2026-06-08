# Kth Largest Element in a Stream

## Problem Statement
Design a class to find the kth largest element in a stream of numbers. The class should have a constructor that takes an integer k as input and a method add that takes an integer num as input and returns the kth largest element in the stream so far. If the stream has less than k elements, return the largest element in the stream. For example, if k = 3, the stream is [4, 5, 8, 2], the output should be 4. If the stream is [4, 5, 8, 2, 10, 1, 3], the output should be 5.

## Approach
We can use a min-heap to store the k largest elements in the stream. When a new number is added to the stream, we check if the heap has less than k elements. If it does, we add the number to the heap. If the heap already has k elements, we check if the new number is larger than the smallest element in the heap. If it is, we remove the smallest element from the heap and add the new number.

## Complexity
- Time: O(log k) for the add method
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
    KthLargest(int k) : k(k) {}

    int add(int num) {
        // If the heap has less than k elements, add the number to the heap
        if (minHeap.size() < k) {
            minHeap.push(num);
        } 
        // If the heap already has k elements and the new number is larger than the smallest element in the heap
        else if (num > minHeap.top()) {
            // Remove the smallest element from the heap and add the new number
            minHeap.pop();
            minHeap.push(num);
        }
        // Return the kth largest element in the stream
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: KthLargest kthLargest(3); kthLargest.add(4); kthLargest.add(5); kthLargest.add(8); kthLargest.add(2);
Output: 4
Input: KthLargest kthLargest(3); kthLargest.add(4); kthLargest.add(5); kthLargest.add(8); kthLargest.add(2); kthLargest.add(10); kthLargest.add(1); kthLargest.add(3);
Output: 5
```

## Key Takeaways
- Use a min-heap to store the k largest elements in the stream
- The add method has a time complexity of O(log k) due to the heap operations
- The space complexity is O(k) for storing the min-heap