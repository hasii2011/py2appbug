
from pathlib import Path

from PIL.Image import Image
from PIL.Image import open as pilOpen
from PIL.ImageFile import ImageFile

#
# I am manually importing this plugin;  When this code gets packaged by
# py2app the plugin is NOT loaded and the code in py
#
# Uncomment out the import and repackage;   will now correctlly work
# noinspection PyUnresolvedReferences
# from PIL import PdfImagePlugin


def demoBug():
    print('Demo')
    fqPath: Path = Path('/tmp/CompactImageDump.png')

    imageToConvert: ImageFile = pilOpen(fqPath)
    convertedImage: Image = imageToConvert.convert('RGB')

    convertedImage.save('/tmp/CompactImageDump.pdf', format='pdf')


if __name__ == '__main__':
    demoBug()
