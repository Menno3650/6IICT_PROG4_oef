import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
img = cv2.imread(r'C:\Users\Menno\OneDrive\Documenten\GitHub\6IICT_PROG4_oef\hfst_5_AI\smash.jpg')
imgplot = plt.imshow(img)
obj = DeepFace.analyze(img_path = r"C:\Users\Menno\OneDrive\Documenten\GitHub\6IICT_PROG4_oef\hfst_5_AI\smash.jpg", actions = ['age', 'gender', 'race', 'emotion'])
print(obj)
