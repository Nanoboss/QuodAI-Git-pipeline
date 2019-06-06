# QuodAI-Git-pipeline

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## General info
An application which will retrieve diverse metrics about the top 1000 open source repositories from GitHub database using GraphQl and compute a health score.

## Setup
In Request you will need to add your own access token. 
```
headers = {"Authorization": "token " + "YOUR_TOKEN"}
```

Follow the information at the link to request one:

https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

To run the program, open a terminal and enter the commands:
```
pip install -r requirements.txt
cd src
python3 main.py
```

Please note that given the Github Api [limitations](https://developer.github.com/v4/guides/resource-limitations/), sometime the program will return an error message with code 502. This is because the query took for some reason too much time and has been interrupted.

## Features
We use the following to compute the health score
* Star number
* Fork Number
* Commit Count

To-do list:
Add the following metrics to make the health core more accurate
* Average number of commits per day
* Average response time of first response to an issue
* Average time that an issue remains opened
* Average number of maintainers
* Maintainer growth over time
* Average time for a pull request to get merged
* Average number of comments per pull requests
* Ratio of closed to open issues
* Number of people opening new issues
* Ratio of commit per developers

## Status
Project is: _in progress_.
