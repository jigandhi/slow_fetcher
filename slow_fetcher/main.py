__author__ = 'jigar'

import time
from tasks import echo


def main():
    task_number = 0
    while True:
        start = time.time()
        result = echo.delay(task_number)
        if result != task_number:
            print "Task Failed"
        end = time.time()
        print "Received Task {} in {} seconds".format(task_number,
                                                      end-start)
        task_number += 1


if __name__ == "__main__":
    main()