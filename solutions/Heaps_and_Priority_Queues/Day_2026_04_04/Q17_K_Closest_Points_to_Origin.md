# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin. The distance between two points on a 2D plane can be calculated using the Euclidean distance formula: √(x2 - x1)^2 + (y2 - y1)^2. The origin is at (0, 0). Return the k closest points. You can return the answer in any order. The input array will have at least one point, and the number of points will not exceed 10^4. The value of k will be between 1 and the number of points.

## Approach
We can use a max heap to store the k closest points. The max heap will automatically keep track of the point with the maximum distance. We iterate over all points, push them into the heap, and if the heap size exceeds k, we remove the point with the maximum distance. The remaining points in the heap are the k closest points to the origin.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        // Calculate the Euclidean distance
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Create a max heap
    priority_queue<Point, vector<Point>, Compare> maxHeap;
    
    // Push all points into the heap
    for (auto& point : points) {
        maxHeap.push(Point(point[0], point[1]));
        
        // If the heap size exceeds k, remove the point with the maximum distance
        if (maxHeap.size() > k) {
            maxHeap.pop();
        }
    }
    
    // Create the result vector
    vector<vector<int>> result;
    while (!maxHeap.empty()) {
        Point point = maxHeap.top();
        maxHeap.pop();
        result.push_back({point.x, point.y});
    }
    
    return result;
}

int main() {
    vector<vector<int>> points = {{1, 3}, {-2, 2}};
    int k = 1;
    vector<vector<int>> result = kClosest(points, k);
    for (auto& point : result) {
        cout << "[" << point[0] << ", " << point[1] << "]" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

## Key Takeaways
- We can use a max heap to keep track of the k closest points to the origin.
- The max heap automatically removes the point with the maximum distance when the heap size exceeds k.
- The time complexity is O(n log k) due to the heap operations.