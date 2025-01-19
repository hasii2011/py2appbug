
from pathlib import Path

from PIL.Image import Image
from PIL.Image import open as pilOpen
from PIL.ImageFile import ImageFile


def demoBug():
    print('Demo')
    fqPath: Path = Path('/tmp/CompactImageDump.png')

    imageToConvert: ImageFile = pilOpen(fqPath)
    convertedImage: Image = imageToConvert.convert('RGB')

    convertedImage.save('/tmp/CompactImageDump.pdf', format='pdf')


if __name__ == '__main__':
    demoBug()
