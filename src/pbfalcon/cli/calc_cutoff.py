from __future__ import print_function
import sys

def calc(fofn, fraction):
    """Return the read-length above which we have fraction
    of total reads.
    """
    return 0

def main(argv=sys.argv):
    prog, fofn, fraction = argv
    print(calc(fofn, fraction))

if __name__ == "__main__":
    main()
