# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. The car i has position = positions[i] and speed = speeds[i] at time 0. If a car i catches up with a car j and overtakes it, then the two cars become a fleet. A fleet's position and speed are the same as the lead car's. Return the number of fleets that will arrive at the destination, where the destination is target. The answer is guaranteed to be 1 if there is only one car. 1 <= n <= 10^4, 0 < target <= 10^8, 0 <= positions[i] < target, 0 < speeds[i] <= 10^8.

## Approach
To determine the number of car fleets, we calculate the time it takes for each car to reach the target and sort them based on their positions and times. We then iterate over the sorted list and count the number of fleets. If a car's time to reach the target is less than or equal to the previous car's time, it joins the same fleet.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, double>> cars;
        
        // Create a list of pairs containing the position and time to reach the target for each car
        for (int i = 0; i < n; i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }
        
        // Sort the cars based on their positions in descending order
        sort(cars.begin(), cars.end(), [](pair<int, double>& a, pair<int, double>& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double prevTime = -1;
        
        // Count the number of fleets
        for (int i = 0; i < n; i++) {
            if (cars[i].second > prevTime) {
                fleets++;
                prevTime = cars[i].second;
            }
        }
        
        return fleets;
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- The key to solving this problem is to calculate the time it takes for each car to reach the target.
- Sorting the cars based on their positions and times allows us to efficiently count the number of fleets.
- If a car's time to reach the target is less than or equal to the previous car's time, it joins the same fleet.