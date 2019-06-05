import csv

offset = 2 #number of non numerical rows


# this function will write to a csv fill and return the next cursor

def repo_to_csv(data, x):
    file = open("ranking.csv", "a")
    writer = csv.writer(file, delimiter=',')
    fieldnames = ['org', 'repo_name', 'stars_count', 'fork_count', 'commit_count', 'pull_requests']

    if x == 0:
        writerdict = csv.DictWriter(file, fieldnames=fieldnames)
        writerdict.writeheader()

    for i in range(len(data['data']['search']['edges'])):
        writer.writerow(
            [
                data['data']['search']['edges'][i]['node']['owner']['login'],
                data['data']['search']['edges'][i]['node']['name'],
                data['data']['search']['edges'][i]['node']['stargazers']['totalCount'],
                data['data']['search']['edges'][i]['node']['forkCount'],
                data['data']['search']['edges'][i]['node']['defaultBranchRef']['target']['history']['totalCount'],
                data['data']['search']['edges'][i]['node']['pullRequests']['totalCount']

            ])
    file.close()
    return data['data']['search']['pageInfo']['endCursor']


def get_max_val(f, index):
    file = open(f, "r")
    reader = csv.reader(file)
    next(reader)
    return max(reader, key=lambda row: int(row[index]))[index]


def update_csv_score(f, scores):
    with open(f) as fdin, open('output.csv', 'w', newline='') as fdout:
        rd = csv.DictReader(fdin)
        fields = list(rd.fieldnames)
        fields.insert(2, 'score')
        wr = csv.DictWriter(fdout, fieldnames=fields)
        wr.writeheader()
        tmp = 0
        for row in rd:
            row['score'] = scores[tmp]    # or score(*row)
            wr.writerow(row)
            tmp += 1


def score(fi, max_values ):
    f = open(fi, "r")
    score_list = []
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        tmp = 1
        for i in range(offset, len(max_values)+offset):
            tmp = tmp * (int(row[i])+1)/max_values[i-offset]
        score_list.append(tmp)

    return score_list
