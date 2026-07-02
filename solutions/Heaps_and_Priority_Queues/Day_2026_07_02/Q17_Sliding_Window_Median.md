# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k in an array of integers. The array is given as [1,3,-1,-3,5,3,6,7], and the window size k is 3. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given the array [1,3,-1,-3,5,3,6,7] and k = 3, the medians for each window are [1,-1,-1,3,5,6]. The goal is to design an efficient algorithm that can compute the median for each window.

## Approach
We will utilize a max heap to store the smaller half of the numbers in the current window and a min heap to store the larger half. By maintaining a balance between the two heaps, we can efficiently calculate the median of the current window. This approach ensures that the max heap always contains the smaller half of the numbers, and the min heap contains the larger half.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store the larger half

    void addNum(int num) {
        // Add the number to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // Calculate the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        MedianFinder mf;
        vector<double> medians;
        for (int i = 0; i < nums.size(); i++) {
            mf.addNum(nums[i]);
            if (i >= k) {
                // Remove the number that is out of the window
                int numToRemove = nums[i - k];
                if (numToRemove <= mf.maxHeap.top()) {
                    // Remove from max heap
                    priority_queue<int> newMaxHeap;
                    while (!mf.maxHeap.empty()) {
                        int num = mf.maxHeap.top();
                        mf.maxHeap.pop();
                        if (num != numToRemove) {
                            newMaxHeap.push(num);
                        }
                    }
                    mf.maxHeap = newMaxHeap;
                } else {
                    // Remove from min heap
                    priority_queue<int, vector<int>, greater<int>> newMinHeap;
                    while (!mf.minHeap.empty()) {
                        int num = mf.minHeap.top();
                        mf.minHeap.pop();
                        if (num != numToRemove) {
                            newMinHeap.push(num);
                        }
                    }
                    mf.minHeap = newMinHeap;
                }
                // Rebalance the heaps
                if (mf.maxHeap.size() > mf.minHeap.size() + 1) {
                    mf.minHeap.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
                } else if (mf.minHeap.size() > mf.maxHeap.size()) {
                    mf.maxHeap.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
            }
            if (i >= k - 1) {
                medians.push_back(mf.findMedian());
            }
        }
        return medians;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = solution.medianSlidingWindow(nums, k);
    for (double median : medians) {
        cout << median << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]
```

## Key Takeaways
- Utilize a max heap and a min heap to store the smaller and larger halves of the numbers in the current window.
- Maintain a balance between the two heaps to ensure efficient calculation of the median.
- Remove the number that is out of the window and rebalance the heaps when the window slides.