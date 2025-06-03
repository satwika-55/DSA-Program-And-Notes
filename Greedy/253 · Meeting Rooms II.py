# Intuiton first, code next (python, Java and c++) and time complexity analysis at the last. 

"""
Problem: "Find the minimum no of rooms required to schdule all meeting without any conflict".

Note: it basically asking what is the 'maximum no of overlapping meetings at any given point of time'.
Also this problem can be reduced to : 'Divide the intervals into minimum no of different parts 
such that no two intervals in respective parts are overlapping. Find the no of parts.
Meeting in same part can be executed after completion of previous meeting without any overlap.
so max no of room = no of parts.

Brute Force: O(n^2)
just sort and check the current meeting start time with the end of all the meetings before.
if none of previous meeting has ended, incr the count by '1' because we will have to arrange the current meeting in different conference room.'
at last return the count
"""

# Approach 1 - Using a heap (can also term it Greedy)

"""
As you might have understood from the problem statement, our main goal is to fit non-overlapping intervals into one day, as return the minimum days possible.

So, while iterating through the intervals, we want to know if there is any other interval, which is non-overlapping with it, that can we fit along with it in the same day.
To know more about overlapping and non-overlapping intervals, solve Meeting Rooms - 1. 

Heap is a data which the minimum value on its top and we can heappop it out.
So, if we can send the end times we encounter into the heap, and while iterating through the array, if we find the top is the heap <= satrt time of current interval, that means we can fit these both in a single day.
Hence, we will push the end times into a heap and heappop it each time the start time is more than it.

The, final length of the heap will be our answer.
This is because, the ones left in the heap are the ones which cant be merged anymore, and that is the minimum number of days required.
"""

# CODE: 

# PYTHON :


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)



# JAVA:



"""
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int[] interval : intervals) {
            if (!minHeap.isEmpty() && minHeap.peek() <= interval[0]) {
                minHeap.poll();
            }
            minHeap.offer(interval[1]);
        }

        return minHeap.size();
    }
}
"""



# C++ :



"""
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (auto& interval : intervals) {
            if (!minHeap.empty() && minHeap.top() <= interval[0]) {
                minHeap.pop();
            }
            minHeap.push(interval[1]);
        }

        return minHeap.size();
    }
};
"""


# TIME COMPLEXITY :

# -> heap opertaing takes 0(n log n ) time .
# -> itertaing throught the array is 0(n)
# -> overall time complexity is 0(nlogn)


# SPACE COMPLEXITY:

# -> 0(n) for the heap.




# METHOD 2 : Using Sweep Line Algorithm 


# Intuition : 


"""
If you do not have prior knowledge about the Sweep Line Algorithm, learn it and come back again - Prefix Sums is a pre-requisite.

For those have an idea about sweep Line - Here's a quick revision :
-> It is mostly used for interval related problems
-> To count or to populate the number of elements present at a certain time in 0(1) time, we used this algorithm.
-> We define an empty array set to 0 of n size.
-> We add 1 to the initial points of all the starting points of the intervals and -1 to the end points.
-> This way, while iterating through the created array, we can keep a count of the sum acquired at each point, giving us the population of it at that time in 0(1).


How is sweep line used in this question ? 

After making ready the prefix array, while iterating through it, we keep a count of the maximum sum encountered.
This, in turn will be the no. of days required.

You can do a dry run of this for better understanding.
"""


# CODE : 


# PYTHON : 


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res
    

# JAVA : 


"""
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for (int[] interval : intervals) {
            map.put(interval[0], map.getOrDefault(interval[0], 0) + 1);
            map.put(interval[1], map.getOrDefault(interval[1], 0) - 1);
        }

        int prev = 0, res = 0;
        for (int count : map.values()) {
            prev += count;
            res = Math.max(res, prev);
        }

        return res;
    }
}
"""




# C++ : 



"""
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> mp;
        for (auto& interval : intervals) {
            mp[interval[0]]++;
            mp[interval[1]]--;
        }

        int prev = 0, res = 0;
        for (auto& [time, count] : mp) {
            prev += count;
            res = max(res, prev);
        }

        return res;
    }
};
"""



# TIME COMPLEXITY ANALYSIS :

# -> We run through the array and the prefix array once each, making it 0(n)

# SPACE COMPLEXITY :

# -> 0(N) for storing the prefix array 






# Method 3 : 2 Pointer Approach - Just for reference..


# CODE : 


# PYTHON : 


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
    



# JAVA : 


"""
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        int[] start = new int[n];
        int[] end = new int[n];

        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        Arrays.sort(start);
        Arrays.sort(end);

        int s = 0, e = 0, count = 0, res = 0;
        while (s < n) {
            if (start[s] < end[e]) {
                count++;
                s++;
            } else {
                count--;
                e++;
            }
            res = Math.max(res, count);
        }

        return res;
    }
}
"""



# C++ : 



"""
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> start(n), end(n);

        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        int s = 0, e = 0, count = 0, res = 0;
        while (s < n) {
            if (start[s] < end[e]) {
                count++;
                s++;
            } else {
                count--;
                e++;
            }
            res = max(res, count);
        }

        return res;
    }
};
"""





# Time complexity: 0(N LOG N)


# Space complexity: 0(N LOG N)