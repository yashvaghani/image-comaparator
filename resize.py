import cv2
def image_resize(image,width= None,height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = width / float(w)
        dim = (int(w * r), height)
        #print(dim)
    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = height / float(h)
        dim = (width, int(h * r))
        #print(dim)
    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    #print(resized.shape)
    # return the resized image
    return resized
'''shopped = cv2.imread("4.png")
print(shopped.shape)
image_resize(shopped,1920,1080)'''
