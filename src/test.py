from tree import Tree

import datetime


def main():
    tree = Tree()
    delta = datetime.timedelta(days=-1)

    date = datetime.date(2017, 11, 30)
    print("-----Testing 30.11. All lights should be off-----")
    tree.tick(date)
    input("-----Press Enter to continue...")
    while date < datetime.date(2017, 12, 25):
        date = date + delta
        print("-----Testing %d.%d. Lights %d to %d should be on-----" % (date.day, date.month, 1, date.day))
        tree.tick(date)
        input("-----Press Enter to continue...")
    while date < datetime.date(2018, 1, 1):
        date = date + delta
        print("-----Testing %d.%d. All lights should blink-----" % (date.day, date.month))
        tree.tick(date)
        input("-----Press Enter to continue...")
    date = date + delta
    print("-----Testing 1.1. All lights should be off-----")
    tree.tick(date)
    input("-----Testing done!-----")


if __name__ == '__main__':
    main()
