from PIL import Image

def Load_Image(image_name):
    '''
    - Load_Image() loads an image that is specified and converts it into a binary string.
    - parameter passed is the filename of the image.
    - returns the binary string as well as dimensions of the image.
    '''   
    image_file = open(image_name, "rb")
    image_as_string = image_file.read()
    image = Image.open(image_name) 
    width, height = image.size
    return image_as_string, width, height

def Save_Image(image_name,param_string):
    '''
    - Save_Image() loads a file that is specified and converts it into a image.
    - parameter passed is the filename of the file and string to be made an image.
    - returns the PIL string form of the image to be displayed.
    '''
    fh = open(image_name,"wb")
    fh.write(param_string)
    fh.close()
    image = Image.open(image_name)
    image.show()

