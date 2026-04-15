# Activity Selection

## Problem Statement
The Activity Selection problem is a classic problem in Greedy Algorithms. We are given a set of activities, each with a start and end time, and we need to select the maximum number of activities that can be performed by a single person. The constraint is that a person can only work on a single activity at a time, and once an activity is started, it cannot be interrupted. The activities are given in the form of pairs (start_time, end_time), where start_time is the time at which the activity starts and end_time is the time at which the activity ends. The goal is to find the maximum number of activities that can be selected such that no two activities overlap.

## Approach
The algorithm sorts the activities based on their end times and then iterates through the sorted activities, selecting the activities that do not overlap with the previously selected activities. This approach ensures that the maximum number of activities are selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// structure to represent an activity
struct Activity {
    int start, end;
};

// comparison function to sort activities based on end time
bool compare(Activity a, Activity b) {
    return a.end < b.end;
}

// function to select the maximum number of activities
void selectActivities(Activity activities[], int n) {
    // sort the activities based on end time
    sort(activities, activities + n, compare);

    // select the first activity
    cout << "(" << activities[0].start << ", " << activities[0].end << ") ";
    int endTime = activities[0].end;

    // iterate through the remaining activities
    for (int i = 1; i < n; i++) {
        // check if the current activity does not overlap with the previously selected activity
        if (activities[i].start >= endTime) {
            cout << "(" << activities[i].start << ", " << activities[i].end << ") ";
            endTime = activities[i].end;
        }
    }
}

int main() {
    // test the function
    Activity activities[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(activities) / sizeof(activities[0]);
    selectActivities(activities, n);
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: (1, 4) (5, 7) (8, 11) (12, 14)
```

## Key Takeaways
- The Activity Selection problem can be solved using a Greedy Algorithm.
- The algorithm sorts the activities based on their end times and then iterates through the sorted activities to select the maximum number of non-overlapping activities.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(1) since no extra space is used.