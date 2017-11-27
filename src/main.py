from tree import Tree

import time
import datetime


def main():
    tree = Tree()
    tree.reset()
    while True:
        tree.tick(datetime.date.today())
        time.sleep(3600)


if __name__ == '__main__':
    main()
