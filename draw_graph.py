import os
import csv
import numpy as np
import argparse
from matplotlib import pyplot as plt


def smooth(arr, n):
    end = -(len(arr)%n)
    if end == 0:
      end = None
    arr = np.reshape(arr[:end], (-1, n))
    arr = np.mean(arr, axis=1)
    return arr

def drawall(name, x, metrics, labels, n=100, begin=0):
    dir ='save_graph/%s'% name
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    x = smooth(x[-begin:], n)
    for i, metric in enumerate(metrics):
        metrics[i] = smooth(metric[-begin:], n)

    def draw(x, y, ylabel):
        plt.figure(figsize=(15,5))
        plt.plot(x, y)
        plt.xlabel('episode')
        plt.ylabel(ylabel)
        plt.savefig(dir+'/'+ylabel)
        plt.clf()

    for i, metric in enumerate(metrics):
        draw(x, metric, labels[i])


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, required=True)
    parser.add_argument('--n', type=int, default=1)
    parser.add_argument('--begin', type=int, default=0)
    args = parser.parse_args()

    name = args.agent
    filename = './save_stat/' + name + '_stat.csv'
    
    episodes = []
    step = []
    score = []
    bestY = []
    avgvel = []
    avgQ = []
    avgact = []

    with open(filename, 'r') as f:
        read = csv.reader(f)
        for i, row in enumerate(read):
            step.append(int(float(row[1])))
            score.append(float(row[2]))
            bestY.append(float(row[3]))
            avgvel.append(float(row[4]))
            avgQ.append(float(row[8]))
            avgact.append(float(row[9]))

    episodes = [i for i in range(len(bestY))]    
    metrics = [
        score,
        step,
        bestY,
        avgvel,
        avgQ,
        avgact
    ]

    labels = [
        'Score',
        'Step',
        'Best Y',
        'Avg velocity',
        'Avg Q',
        'Avg Action (noise)'
    ]

    drawall(name, episodes, metrics, labels, args.n, args.begin)
