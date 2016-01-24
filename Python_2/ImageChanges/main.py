import sys
from image import PortablePixmap, read_ppm, read_ppm2, read_ppm3
def main(args):
    if len(args) < 2:
        print('Usage:', __name__, '<input-file>.ppm', file=sys.stderr)
        return 1
    if args[1] == 'flop':
        image = read_ppm3(args[2])
        print(image)
    elif args[1] == 'flip':
        image = read_ppm2(args[2])
        print(image)
    elif args[1] == 'grayscale':
        image = read_ppm(args[2])
        print(image)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
