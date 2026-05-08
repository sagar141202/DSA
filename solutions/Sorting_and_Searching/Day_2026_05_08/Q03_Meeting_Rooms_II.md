# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the person can attend all meetings, return 0. Otherwise, return the minimum number of rooms required. The intervals are non-overlapping when [s1,e1] and [s2,e2] do not overlap, i.e., s1 >= e2 or s2 >= e1. For example, given intervals [[0,30],[5,10],[15,20]], the minimum number of rooms required is 2 because we need two rooms to accommodate all meetings.

## Approach
The algorithm uses a priority queue to store the end times of the meetings. We sort the intervals based on their start times and then iterate over them. If the start time of the current meeting is greater than or equal to the smallest end time in the queue, we update the smallest end time. Otherwise, we add the end time of the current meeting to the queue.

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
        // If there are no meetings, we don't need any rooms.
        if (intervals.empty()) {
            return 0;
        }

        // Sort the meetings in increasing order of their start time.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;
        endTimes.push(intervals[0][1]);

        // Iterate over the rest of the meetings.
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, update the earliest end time.
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the priority queue.
            endTimes.push(intervals[i][1]);
        }

        // The size of the priority queue is the minimum number of rooms required.
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
Input: [[5,8],[9,15]]
Output: 1
```

## Key Takeaways
- We use a priority queue to efficiently manage the end times of the meetings.
- The size of the priority queue represents the minimum number of rooms required to accommodate all meetings.
- Sorting the intervals based on their start times allows us to process them in a way that minimizes the number of rooms needed.