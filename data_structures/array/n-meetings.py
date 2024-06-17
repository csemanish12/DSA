"""
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output:
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Example 2:

Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output:
1
Explanation:
Only one meetings can be held
with given start and end timings.

Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ start[i] < end[i] ≤ 105


"""


class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        meetings = []
        for i in range(n):
            meeting = Meeting(start[i], end[i], i + 1)
            meetings.append(meeting)

        meetings = sorted(meetings, key=lambda x: (x.end, x.pos))
        count = 0
        prev_end = None
        for meeting in meetings:
            if prev_end is None:
                count += 1
                prev_end = meeting.end
            else:
                current_start = meeting.start
                if current_start > prev_end:
                    count += 1
                    prev_end = meeting.end

        return count


s = Solution()

start1 = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
end1 = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
n1 = 8
print("count for input 1 is:", s.maximumMeetings(n1, start1, end1))
