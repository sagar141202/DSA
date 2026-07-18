# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If not, find the minimum number of meeting rooms required. Each meeting room can hold one meeting at a time. The intervals are given as a 2D vector of integers, where intervals[i] = [start_i, end_i]. For example, if the input is [[0, 30], [5, 10], [15, 20]], the minimum number of meeting rooms required is 2 because the meeting from 5 to 10 overlaps with the meeting from 0 to 30, and the meeting from 15 to 20 overlaps with both.

## Approach
The approach to solve this problem is to use a priority queue to store the end times of the meetings. We sort the meetings by their start times and then iterate through them. If the start time of the current meeting is greater than or equal to the smallest end time in the queue, we remove the smallest end time from the queue. We then add the end time of the current meeting to the queue.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        // Sort the meetings by their start times
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize a priority queue to store the end times of the meetings
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Add the end time of the first meeting to the queue
        endTimes.push(intervals[0][1]);
        
        // Iterate through the rest of the meetings
        for (int i = 1; i < intervals.size(); i++) {
            // If the start time of the current meeting is greater than or equal to the smallest end time in the queue,
            // remove the smallest end time from the queue
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the queue is the minimum number of meeting rooms required
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
Input: [[7, 10], [2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to store the end times of the meetings to efficiently find the smallest end time.
- Sort the meetings by their start times to ensure that we process them in the correct order.
- The size of the priority queue at the end is the minimum number of meeting rooms required.