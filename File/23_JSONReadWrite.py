# 23. JSON 파일 읽어 들여 처리하기

import json
import glob

def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f"{dirname}/*.json"):
        scores[filename] = {}

        with open(filename) as inputfile:
            for file in json.load(inputfile):
                for subject, subject_score in file.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(subject_score)
        
    for one_class in scores:
        print(one_class)
        for subject, subject_score in scores[one_class].items():
            print(subject_score)
            min_scores = min(subject_score)
            max_scores = max(subject_score)
            avg_scores = (sum(subject_score) / len(subject_score))

            print(subject)
            print(f"\tmin{min_scores}")
            print(f"\tmax{max_scores}")
            print(f"\tavg{avg_scores}")

print_scores("/Users/kdk/Desktop/scores")
