import cv2


def pixelate_face(image, x1, y1, x2, y2, pixel_size=10):
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0] or x1 >= x2 or y1 >= y2:
        print("Некорректная область для пикселизации.")
        return image

    roi = image[y1:y2, x1:x2]
    
    roi_small = cv2.resize(roi, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
    
    roi_pixelated = cv2.resize(roi_small, (x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)
    
    image[y1:y2, x1:x2] = roi_pixelated
    
    return image