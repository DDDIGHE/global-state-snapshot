import argparse
import shutil
import time
import threading

from bank import Bank
from inspector import Inspector
from commons import Constants

def stop_after_timeout(timeout, bank, inspector):
    time.sleep(timeout)
    print("Time's up! Stopping the program.")
    if bank is not None:
        bank.stop = True
    if inspector is not None:
        inspector.stop = True


if __name__ == '__main__':

    # create and parse arguments
    ap = argparse.ArgumentParser()

    ap.add_argument("-b", "--bank", required=False, action='store_true',
                    help="Use this option to run an instance of Bank (a branch).")
    ap.add_argument("-i", "--inspector", required=False, action='store_true',
                    help="Use this option to run the inspector")
    ap.add_argument("-c", "--clear", required=False, action='store_true',
                    help="Clear the branches information file.")

    args = ap.parse_args()

    if args.clear:
        try:
            shutil.rmtree(Constants.dir_logs)
            shutil.rmtree(Constants.dir_bank)
            print("bank/ and logs/ directories were removed.")
        except FileNotFoundError:
            print("directories do not exist. They were already removed.")

        exit(0)

    if args.bank and args.inspector:
        raise "You must only use one option."
    else:
        timeout = 9 * 60
        if args.bank:
            branch = Bank()
            timer = threading.Thread(target=stop_after_timeout, args=(timeout, branch, None))
            timer.start()
            branch.run()
        elif args.inspector:
            inspector = Inspector()
            timer = threading.Thread(target=stop_after_timeout, args=(timeout, None, inspector))
            timer.start()
            inspector.run()
        else:
            raise "Use one of the options (-b or -i)"