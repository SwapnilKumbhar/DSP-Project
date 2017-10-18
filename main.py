import sys
import IO

if __name__ == '__main__':
    file_name = sys.argv[1]
    io = IO.IO(file_name)
    print(io.load())
