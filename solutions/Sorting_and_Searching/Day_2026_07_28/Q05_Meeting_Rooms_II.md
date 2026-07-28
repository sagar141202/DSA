# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If not, find the minimum number of meeting rooms required to hold all meetings. The meeting intervals are non-overlapping and are given in the form of [start, end]. The start time is inclusive, and the end time is exclusive. For example, if we have two meetings [0, 30] and [5, 10], we would need two rooms because the two meetings overlap.

## Approach
We can solve this problem by sorting the meeting intervals by their start times and using a priority queue to store the end times of the meetings. The size of the priority queue will represent the minimum number of meeting rooms required.

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
        
        // Sort the meeting intervals by their start times
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize a priority queue to store the end times of the meetings
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Add the end time of the first meeting to the priority queue
        endTimes.push(intervals[0][1]);
        
        // Iterate over the rest of the meeting intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, update the earliest end time
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the priority queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the priority queue represents the minimum number of meeting rooms required
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- We can use a priority queue to efficiently store and retrieve the end times of the meetings.
- The size of the priority queue represents the minimum number of meeting rooms required to hold all meetings.
- Sorting the meeting intervals by their start times allows us to efficiently iterate over the meetings and determine the minimum number of rooms required.