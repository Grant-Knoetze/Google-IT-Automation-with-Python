#!/usr/bin/env python3

def main():
    scores = {'texas': 5666, 'london': 556, 'htown': 5555, 'jtown': 555}

    # for item in scores:
    #    scores[item] *= 2
    # print(scores)

    scores_2 = {key: value * 2 for (key, value) in scores.items()}
    print(scores_2)
    # Add a conditional
    scores_2 = {key: value * 2 for (key, value) in scores.items() if value % 2 == 0 and key == 'texas'}
    print(scores_2)


if __name__ == '__main__':
    main()
