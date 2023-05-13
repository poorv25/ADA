def job_schedule(jobs):
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1]) # sort jobs by end time
    last_end_time = 0
    schedule = []
    
    for i in range(n):
        if jobs[i][0] >= last_end_time:
            schedule.append(jobs[i])
            last_end_time = jobs[i][1]
    
    return schedule
