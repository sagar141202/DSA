# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are non-overlapping if a person can attend all of them. For example, if there are two meetings, one from 0 to 30 and another from 5 to 10, the person cannot attend both. However, if there are two meetings, one from 0 to 5 and another from 5 to 10, the person can attend both. The problem requires to find the minimum number of rooms required such that all meetings can be accommodated.

## Approach
The algorithm uses a priority queue to store the end times of the meetings. It sorts the meetings by their start times and then iterates over them, updating the priority queue with the end times. If a meeting starts after the earliest end time, it updates the earliest end time; otherwise, it adds a new room.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    int start;
    int end;
};

bool compareIntervals(Interval a, Interval b) {
    return a.start < b.start;
}

int minMeetingRooms(vector<Interval>& intervals) {
    if (intervals.size() == 0) {
        return 0;
    }

    sort(intervals.begin(), intervals.end(), compareIntervals);
    priority_queue<int, vector<int>, greater<int>> endTimes;
    endTimes.push(intervals[0].end);

    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].start >= endTimes.top()) {
            endTimes.pop();
        }
        endTimes.push(intervals[i].end);
    }

    return endTimes.size();
}

int main() {
    vector<Interval> intervals = {{0, 30}, {5, 10}, {15, 20}};
    cout << minMeetingRooms(intervals) << endl;
    return 0;
}
```

## Test Cases
```
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
Input: [[7, 10], [2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently manage the end times of the meetings.
- Sort the meetings by their start times to ensure that we process them in the correct order.
- Update the priority queue with the end times of the meetings, adding a new room when necessary.