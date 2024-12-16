import cv2
from Face_detect import (detect_faces, detect_and_process_faces)
from Face_function import pixelate_face
from Face_analize import analyze_face

def main_menu():
    image_path = "image/"
    image_path = image_path + input("Введите имя файла: ")
    while True:
        print("\nВыберите действие:")
        print("1. Просмотр изображения")
        print("2. Ручное выделение области лица")
        print("3. Распознавание лица (возраст, пол, эмоция)")
        print("4. Размытие лица")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            image = cv2.imread(image_path)
            if image is None:
                print("Не удалось загрузить изображение. Проверьте путь к файлу.")
            else:
                cv2.imshow("Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '2':
            detect_and_process_faces(image_path)

        elif choice == '3':
            analyze_face(image_path)

        elif choice == '4':
            image = cv2.imread(image_path)
            if image is None:
                print("Не удалось загрузить изображение. Проверьте путь к файлу.")
            else:
                original_image = image.copy()
                faces = detect_faces(image)
                if faces.any():
                    for (x, y, w, h) in faces:
                        pixelated_image = pixelate_face(original_image, x, y, x + w, y + h)
                    cv2.imshow("Blurred Image", pixelated_image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("На изображении не найдено ни одного лица для размытия.")


        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите из предложенных вариантов.")


if __name__ == '__main__':
    main_menu()