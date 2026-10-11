from services.identifyExtension import identifyExtension
from services.EXIFExtract.ExtractPNG import extractPNG
from services.EXIFExtract.ExtractJPEG import extractJPEG
from services.EXIFExtract.ExtractHEIF import extractHEIF
def extractController(file):
    fileType = identifyExtension(file)
    if fileType == "PNG":
        return extractPNG(file)
    elif fileType == "JPEG":
        return extractJPEG(file)
    elif fileType == "HEIF":
        return extractHEIF(file)
    else: return {"result":"false"}