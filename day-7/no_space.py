"""

Parse filesystem output into a tree-like structure?

Commands (all start with '$' in input file and are mostly consistent with *nix systems.
    - `cd x` --> moves in one level to directory `x`
    - `cd ..` --> moves out one level to parent directory of current directory
    - `cd /` --> moves to outermost (top level) directory
    - `ls`
            `123 abc` --> file name: abc, file size: 123 
            `dir xyz` --> current directory contains sub directory `xyz`

Solution:
    1. Parse all content of input file into directory tree
                    (/)
           /    |       |        \
        a     b.txt    c.dat      d
     / | | \                 /  |   |   \ 
    e  f g  h               j d.log d.ext k
   /
  i    

    Use 'Dir' and 'File' Node Types 

    2. Calculate the size of all directories (total and with sub-directories re-counted, per the example)
"""


def main():
    pass


if __name__ == "__main__":
    main()
