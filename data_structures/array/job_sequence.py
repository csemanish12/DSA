"""
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time before which job needs to be completed to earn the profit.


Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

Your Task :
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 105
1 <= Deadline <= N
1 <= Profit <= 500
"""

'''
class Job:

    # Job class which stores profit and deadline.

    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''


class Solution:
    """
    deadline means job can be completed anywhere from day 1 to deadline.
    eg: deadline=4, means that job can be completed either on day4 or day3 or day2 or day1
    we will try to complete the job on last day, so we have remaining days to complete other jobs
    Greedy approach
    Sort by profit first
    """

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        jobs = sorted(Jobs, key=lambda x: -x.profit)
        max_deadline = 0
        for i in range(n):
            if jobs[i].deadline > max_deadline:
                max_deadline = jobs[i].deadline

        job_completed = [-1 for _ in range(max_deadline + 1)]
        profits = 0
        jobs_count = 0
        for job in jobs:
            for i in range(job.deadline, 0, -1):
                if job_completed[i] == -1:
                    profits += job.profit
                    jobs_count += 1
                    job_completed[i] = job.id
                    break

        return jobs_count, profits