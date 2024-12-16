from deepface import DeepFace

def analyze_face(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['age', 'gender', 'emotion'])
    
    if isinstance(analysis, list):
        for i, face in enumerate(analysis):
            print(f"Лицо {i + 1}:")
            print("  Возраст:", face['age'])
            print("  Пол:", face['dominant_gender'])
            print("  Эмоция:", face['dominant_emotion'])
    else:
        print("Возраст:", analysis['age'])
        print("Пол:", analysis['dominant_gender'])
        print("Эмоция:", analysis['dominant_emotion'])
