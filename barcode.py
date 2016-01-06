import zbar
import cv2

def get_barcode(img):
    # create a reader
    data = []
    scanner = zbar.ImageScanner()
    
    # configure the reader
    scanner.parse_config('enable')
    
    # obtain image data
    pil = img#pil = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width, height = pil.shape
    raw = pil.tostring()
    
    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)
    
    # scan the image for barcodes
    scanner.scan(image)
    
    # extract results
    for symbol in image:
        # do something useful with results
        data.append(symbol.data)
    
    # clean up
    del(image)
    return data
