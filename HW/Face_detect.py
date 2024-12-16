import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

roi_start = None
roi_end = None
cropping = False


def mouse_crop(event, x, y, flags, param):
    global roi_start, roi_end, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        roi_start = (x, y)
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        roi_end = (x, y)
        cropping = False
        cv2.rectangle(param, roi_start, roi_end, (0, 255, 0), 2)
        cv2.imshow("Image", param)


def detect_faces(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def pixelate_region(image, x1, y1, x2, y2, pixel_size=10):
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0] or x1 >= x2 or y1 >= y2:
        print("Некорректная область для пикселизации.")
        return image

    roi = image[y1:y2, x1:x2]
    if roi.size == 0:
        print("Выбранная область пустая. Пропускаем пикселизацию.")
        return image

    roi = cv2.resize(roi, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)
    image[y1:y2, x1:x2] = roi
    return image

def detect_and_process_faces(image_path):
    global roi_start, roi_end

    image = cv2.imread(image_path)
    if image is None:
        print("Не удалось загрузить изображение. Проверьте путь к файлу.")
        return

    original_image = image.copy()
    faces = detect_faces(image)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouse_crop, image)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")

    if roi_start and roi_end:
        x1, y1 = roi_start
        x2, y2 = roi_end
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

        pixelated_image = pixelate_region(original_image, x1, y1, x2, y2)
        cv2.imshow("Processed Image", pixelated_image)
        cv2.waitKey(0)
        cv2.destroyWindow("Processed Image")
        
        save_choice = input("Сохранить изменения в старый файл? (y/n): ")
        if save_choice.lower() == 'y':
            try:
              cv2.imwrite(image_path, pixelated_image)
              print("Изображение сохранено.")
            except Exception as e:
              print(f"Ошибка сохранения изображения: {e}")


if __name__ == "__main__":
    image_path = input("Введите путь к изображению: ")
    detect_and_process_faces(image_path)