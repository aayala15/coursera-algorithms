with open("jobs.txt") as file:
	number_of_jobs = int(file.readline())
	jobs = {}
	for i in range(number_of_jobs):
		jobs[i] = [int(j) for j in str.split(file.readline())]

def greedyscheduler(jobs, type="ratio"):
	if type == "ratio":
		score = {key:[-(value[0]/value[1]), -value[0]] for key, value in jobs.items()}
	else:
		score = {key:[-(value[0]-value[1]), -value[0]] for key, value in jobs.items()}
	score = sorted(score, key=lambda k: (score[k][0], score[k][1]))
	return(score)

def computecost(schedule, jobs):
	time = 0
	cost = 0
	for i in schedule:
		time += jobs[i][1]
		cost += time*jobs[i][0]
	return(cost)
		
schedule = greedyscheduler(jobs, type="diff")
print(computecost(schedule, jobs))

schedule = greedyscheduler(jobs, type="ratio")
print(computecost(schedule, jobs))