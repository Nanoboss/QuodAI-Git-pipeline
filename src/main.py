import parser
import queries
import request
import os
import csv

runs = 20


def main():
    os.system("rm output.csv ; touch ranking.csv")
    cursor = None
    print("Retrieving repos from gitHub DB...")
    for i in range(runs):
        tmp = queries.get_repos(cursor)
        toprepos = request.run_query_with_var(tmp[0], tmp[1])
        cursor = parser.repo_to_csv(toprepos, i)

    print("Processing...")
    with open("ranking.csv", "r+") as file:
        reader = csv.reader(file)

        max_values = []
        for i in range(2, len(next(reader))):
            max_values.append(int(parser.get_max_val("ranking.csv", i)))

    scores = parser.score("ranking.csv", max_values)
    parser.update_csv_score("ranking.csv", scores)

    os.system("rm ranking.csv")
    print("Done.")


if __name__ == '__main__':
    main()
