from PIL import Image
import sys
import os


def parse_image(im, outfile):
    chars = "@%#x+=-,.  "
    character_bracket = 255 / len(chars)
    with open(outfile, 'w') as f:
        for y in range(im.size[1] - 1):
            for x in range(im.size[0] - 1):
                pixel = (x, y)
                val = im.getpixel(pixel)
                index = (val / character_bracket) - 1
                f.write(chars[index])
            f.write("\n")


def main():
    infile = sys.argv[1]
    extension = os.path.splitext(infile)[1]
    file_name = os.path.basename(infile)
    outFolder = os.path.dirname(os.path.realpath(__file__)) + "/output/"
    outfile = outFolder + file_name + ".txt"

    if infile != outfile:
        im = Image.open(infile)
        im = im.convert('L')
        ratio = float(im.size[0]) / float(im.size[1] / 0.6)
        new_image_size = 128, 128 * ratio
        im.thumbnail(new_image_size, Image.ANTIALIAS)
        parse_image(im, outfile)


if __name__ == '__main__':
    main()