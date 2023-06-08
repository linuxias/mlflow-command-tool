import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description = "MLflow commandline tool for mlflow tracking server user")
    parser.add_argument("-u", "--uri", type=str, help="Tracking server uri", default="localhost:5000")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()   

if __main__ == "__main__":
    sys.exit(main())
