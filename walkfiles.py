#! /usr/bin/env python3

import os, sys, glob, traceback
import argparse as ap




def listlogfiles(folder):
    files = glob.glob(folder + "/*/*/*.log")
    files.sort()
    return files






if __name__ == '__main__':

    p = ap.ArgumentParser()

    p.add_argument("-d", type = str, default = "irclogs/freenode/#ubuntu")

    args = p.parse_args()

    print(args.d)

    files = listlogfiles(args.d)

    for f in files:
        print f
