# Activity Selection

## Problem Statement
The Activity Selection problem is a classic problem in Greedy Algorithms. We are given a set of activities, each with a start and end time. The goal is to select the maximum number of activities that can be performed by a single person, given that a person can only work on a single activity at a time. The activities are selected based on their end times, with the activity having the earliest end time being selected first. The problem has the following constraints: (1) each activity has a start and end time, (2) a person can only work on one activity at a time, and (3) the activities are non-preemptive, meaning that once an activity is started, it cannot be interrupted. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of activities that can be selected is 4.

## Approach
The algorithm sorts the activities based on their end times and then iterates through the sorted activities, selecting the activities that do not conflict with the previously selected activities. This approach ensures that the maximum number of activities are selected. The algorithm works by always selecting the activity with the earliest end time that does not conflict with the previously selected activities.

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
int activitySelection(Activity arr[], int n) {
    // sort the activities based on end time
    sort(arr, arr + n, compare);

    // select the first activity
    int count = 1;
    int lastEnd = arr[0].end;

    // iterate through the remaining activities
    for (int i = 1; i < n; i++) {
        // if the current activity does not conflict with the last selected activity
        if (arr[i].start >= lastEnd) {
            // select the current activity
            count++;
            lastEnd = arr[i].end;
        }
    }

    return count;
}

int main() {
    // example usage
    Activity arr[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Maximum number of activities: " << activitySelection(arr, n);
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The Activity Selection problem can be solved using a Greedy Algorithm that selects the activities based on their end times.
- The algorithm has a time complexity of O(n log n) due to the sorting step.
- The algorithm has a space complexity of O(1) since it only uses a constant amount of space to store the last selected activity's end time.