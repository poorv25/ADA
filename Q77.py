def schedule_jobs(jobs):

    jobs = sorted(jobs, key=lambda x: x[0])  # sort jobs by their deadlines
    schedule = []
    time = 0
    for job in jobs:
        if time + job[1] <= job[0]:  # job can be completed before its deadline
            schedule.append((job, time + job[1]))
            time += job[1]
        else:  # job cannot be completed before its deadline
            continue
    return schedule
