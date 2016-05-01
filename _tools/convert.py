from PIL import Image
import glob, os

size = 550, 20000

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.crop((0, 0, 550, 350)).save(file + "-thumbnail.jpg", "JPEG")
    # im.save(file + "-thumbnail.jpg", "JPEG")
