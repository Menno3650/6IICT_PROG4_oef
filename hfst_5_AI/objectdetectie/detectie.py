import cv2
import numpy as np
import matplotlib.pylab as plt
import os
import sys
import time
import pathlib
from Webcam import Webcam


# Functie om een afbeelding weer te geven via matplotlib
def plt_imshow(title, image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.grid(False)
    plt.show()

# Functie om camera te openen
def open_camera(keuze_camera = 0):
    key = cv2.waitKey(1)
    # Moet 0, 1, 2, ... zijn. Afhankelijk van de gebruikte camera.
    # Maak een camera aan die loopt op een aparte thread
    cam = Webcam(fps=60, src=keuze_camera).start()
    while True:

        try:
            _, afbeelding = cam.read()
            cv2.imshow("Capturing", afbeelding)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='afbeelding_camera.jpg', img=afbeelding)
                plt_imshow("Genomen foto", afbeelding)
            
            elif key == ord('q'):
                cam.stop()
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            print("Camera uitzetten.")
            cam.stop()
            print("Programma gestopt.")
            cv2.destroyAllWindows()
            break

# Overloop alle camera's die op het toestel gedetecteerd zijn.
# Returen alle gevonden SRCs.
def get_camera_src():
    index = 0
    lijst_src = []
    while index < 10:           # Ik ga ervanuit dat 10 camera's wel genoeg zijn.
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        try:
            cap.getBackendName() # Geeft error als camera niet bestaat.
            lijst_src.append(index)
        except:
            pass
        cap.release()
        index += 1
    return lijst_src

# Functie om een afbeelding te verwerken via het yolo-model
def yolo_verwerking(pad):
    # Enkele vaste parameters
    ZEKERHEID_THRESHOLD = 0.5
    SCORE_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.5

    # De bestanden oproepen die het yolo netwerk nodig zal hebben
    yolo_pad = str(pathlib.Path(__file__).parent.resolve())
    config_path = yolo_pad+"/yolo/yolov3.cfg"
    weights_path = yolo_pad+"/yolo/yolov3.weights"


    # alle labels (herkenbare objecten) inladen
    labels = open(yolo_pad+"/yolo/coco.names").read().strip().split("\n")
    # een random kleur genereren voor ieder object om later te gebruiken op de figuur
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    # inladen van het YOLO-model in een (Convolutionaal) Neuraal Netwerk
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # afbeelding inladen, waarop de objecten gedetecteerd zullen worden
    # VB: pad = "images/hond-cake.jpg"
    afbeelding = cv2.imread(pad)
    file_name = os.path.basename(pad)
    filename, ext = file_name.split(".")


    # Ontleed afbeelding naar 4D blob (dit is de input voor het YOLO-model)
    blob = cv2.dnn.blobFromImage(afbeelding, 1/255.0, (416, 416), swapRB=True, crop=False)
    # De blob inladen in YOLO
    net.setInput(blob)

    # Doorloop het model en haal het resultaat van iedere laag op
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    # Doorzoek alle lagen van het model naar gedetecteerde objecten (in de blob)
    layer_outputs = net.forward(ln)

    # Variabelen klaarzetten
    kaders_lijst, zekerheden_lijst, labels_lijst, font_scale, thickness = [], [], [], 1, 1
    # Voor elke laag
    for output in layer_outputs:
        # Doorloop alle gedetecteerde objecten (per laag)
        for detectie in output:
            # Bepaal hoe zeker het model is dat de afbeelding dit voorwerp bevat
            scores = detectie[5:]
            class_id = np.argmax(scores) # class_id is het label van dit voorwerp
            zekerheid = scores[class_id]

            # ALS de zekerheid hoger is dan een bepaalde grenswaarde...
            # DAN zet een kader rond de afbeelding en label het.
            if zekerheid > ZEKERHEID_THRESHOLD:
                # Zet kader klaar en voeg toe aan lijst met kaders
                h, w = afbeelding.shape[:2]
                kader = detectie[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = kader.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                kaders_lijst.append([x, y, int(width), int(height)])

                # Voeg zekerheid en label toe aan voorziene lijsten
                zekerheden_lijst.append(float(zekerheid))
                labels_lijst.append(class_id)

    # Verwerk alle zeker gevonden objecten met openCV
    idxs = cv2.dnn.NMSBoxes(kaders_lijst, zekerheden_lijst, SCORE_THRESHOLD, IOU_THRESHOLD)

    # ALS er minstens 1 object gedetecteerd is...
    # Dan voeg kader, label en zekerheid toe aan dit voorwerp
    if len(idxs) > 0:
        # overloop de gevonden voorwerpen
        for idx in idxs.flatten():
            # Teken een kader rond het gevonden voorwerp (kleur bepaald door label)
            x, y = kaders_lijst[idx][0], kaders_lijst[idx][1]
            w, h = kaders_lijst[idx][2], kaders_lijst[idx][3]
            kleur = [int(c) for c in colors[labels_lijst[idx]]]
            cv2.rectangle(afbeelding, (x, y), (x + w, y + h), kleur, 5)
            tekst = f"{labels[labels_lijst[idx]]}: {zekerheden_lijst[idx]:.2f}"
            (breedte, hoogte) = cv2.getTextSize(tekst, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)[0]
            offset_x, offset_y = x, y-5
            kader_coords = ((offset_x, offset_y), (offset_x + breedte + 2, offset_y - hoogte))
            overlay = afbeelding.copy()
            cv2.rectangle(afbeelding, kader_coords[0], kader_coords[1], kleur, -1)
            afbeelding = cv2.addWeighted(overlay, 0.6, afbeelding, 0.4, 0)

            # Schrijf het label en de zekerheid bij het gevonden voorwerp.
            cv2.putText(afbeelding, tekst, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                1, [0,0,0], 2)

    plt_imshow(filename + "_yolo3." + ext, afbeelding)

def realtime(keuze_camera = 0, keuze_yolo = "normal"):
    yolo_pad = str(pathlib.Path(__file__).parent.resolve())
    if keuze_yolo == "normal":
        weights_path, config_path = yolo_pad+"/yolo/yolov3.weights", yolo_pad+"/yolo/yolov3.cfg"
        names_path = yolo_pad+"/yolo/coco.names"
        REGIO_GROOTTE = 288
        ZEKERHEID_THRESHOLD, SCORE_THRESHOLD, IOU_THRESHOLD = 0.5, 0.5, 0.5
    elif keuze_yolo == "tiny":
        weights_path, config_path = yolo_pad+"/yolo/yolov3_tiny.weights", yolo_pad+"/yolo/yolov3_tiny.cfg"
        names_path = yolo_pad+"/yolo/coco.names"
        REGIO_GROOTTE = 412
        ZEKERHEID_THRESHOLD, SCORE_THRESHOLD, IOU_THRESHOLD = 0.5, 0.5, 0.5
    elif keuze_yolo == "custom":
        weights_path, config_path = yolo_pad+"/yolo/yolov3-tiny-custom.weights", yolo_pad+"/yolo/yolov3-tiny-custom.cfg"
        names_path = yolo_pad+"/yolo/custom.names"
        REGIO_GROOTTE = 412
        ZEKERHEID_THRESHOLD, SCORE_THRESHOLD, IOU_THRESHOLD = 0.2, 0.2, 0.2
    else:
        print("Geef 'normal', 'tiny' of 'custom' op als tweede paramter.")
        return

    # alle labels (herkenbare objecten) inladen
    labels = open(names_path).read().strip().split("\n")
    # een random kleur genereren voor ieder object om later te gebruiken op de figuur
    kleuren = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    # inladen van het YOLO-model in een (Convolutionaal) Neuraal Netwerk
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # Haal alle lagen van het model
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    # Open camera. Moet 0, 1, 2, ... zijn, afhankelijk van de gebruikte camera
    cam = Webcam(fps=60, src=keuze_camera).start()


    # Zet enkele variabelen van de camera klaar
    start_tijd, frame_id  = time.time(), 0
    while True:
        # Haal frame op, verhoog frame_id met 1,  bepaal de hoogte en de breedte
        _, frame = cam.read()
        frame_id += 1
        height, width, _ = frame.shape

        # Ontleed afbeelding naar 4D blob (dit is de input voor het YOLO-model)
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (REGIO_GROOTTE, REGIO_GROOTTE), (0, 0, 0), True, crop=False)
        # De blob inladen in YOLO
        net.setInput(blob)
        # Doorzoek alle lagen van het model naar gedetecteerde objecten (in de blob)
        layers_outputs = net.forward(ln)

        # Variabelen klaarzetten
        kaders_lijst, zekerheden_lijst, labels_lijst, font_scale, thickness = [], [], [], 1, 1
        # Voor elke laag
        for out in layers_outputs:
            # Doorloop alle gedetecteerde objecten
            for detectie in out:
                # Bepaal hoe zeker het model is dat de afbeelding dit voorwerp bevat
                scores = detectie[5:]
                class_id = np.argmax(scores) # class_id is het label van dit voorwerp
                zekerheid = scores[class_id]

                # ALS de zekerheid hoger is dan een bepaalde grenswaarde...
                # DAN zet een kader rond de afbeelding en label het.
                if zekerheid > ZEKERHEID_THRESHOLD:
                    # Zet kader van voorwerp klaar
                    center_x = int(detectie[0] * width)
                    center_y = int(detectie[1] * height)
                    w = int(detectie[3] * width)
                    h = int(detectie[3] * height)
                    x = int(center_x - w / 1.8)
                    y = int(center_y - h / 1.8)

                    # Voeg kader, zekerheid en label toe aan voorziene lijsten
                    kaders_lijst.append([x, y, w, h])
                    zekerheden_lijst.append(float(zekerheid))
                    labels_lijst.append(class_id)

        # Verwerk alle zeker gevonden objecten met openCV
        indexen = cv2.dnn.NMSBoxes(kaders_lijst, zekerheden_lijst, SCORE_THRESHOLD, IOU_THRESHOLD)

        # Voor alle opgeslagen kaders
        for index in range(len(kaders_lijst)):
            # ALS de index voorkomt in de indexen van openCV
            if index in indexen:
                # Teken een kader rond het gevonden voorwerp (kleur bepaald door label)
                x, y, w, h = kaders_lijst[index]
                label = str(labels[labels_lijst[index]])
                zekerheid = zekerheden_lijst[index]
                kleur = [int(c) for c in kleuren[labels_lijst[index]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), kleur, 2)
                # Schrijf het label en de zekerheid bij het gevonden voorwerp.
                cv2.putText(frame, label + " " + str(round(zekerheid, 2)), (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 2, kleur, 2)



        elapsed_time = time.time() - start_tijd
        fps = frame_id / elapsed_time
        cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50),  cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
        cv2.imshow("Image", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cam.stop()
    cv2.destroyAllWindows()

def yolo_papier(pad):
    # Enkele vaste parameters
    ZEKERHEID_THRESHOLD = 0.05
    SCORE_THRESHOLD = 0.05
    IOU_THRESHOLD = 0.05

    # De bestanden oproepen die het yolo netwerk nodig zal hebben
    yolo_pad = str(pathlib.Path(__file__).parent.resolve())
    weights_path = yolo_pad+"/yolo/yolov3-tiny-custom.weights"
    config_path = yolo_pad+"/yolo/yolov3-tiny-custom.cfg"
    names_path = yolo_pad+"/yolo/custom.names"

    # alle labels (herkenbare objecten) inladen
    labels = open(names_path).read().strip().split("\n")
    # een random kleur genereren voor ieder object om later te gebruiken op de figuur
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    # inladen van het YOLO-model in een (Convolutionaal) Neuraal Netwerk
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # afbeelding inladen, waarop de objecten gedetecteerd zullen worden
    # VB: pad = "images/hond-cake.jpg"
    afbeelding = cv2.imread(pad)
    file_name = os.path.basename(pad)
    ext = file_name.split(".")[-1]
    filename = file_name.replace(f".{ext}", "")

    # Ontleed afbeelding naar 4D blob (dit is de input voor het YOLO-model)
    blob = cv2.dnn.blobFromImage(afbeelding, 1/255.0, (416, 416), swapRB=True, crop=False)
    # De blob inladen in YOLO
    net.setInput(blob)

    # Doorloop het model en haal het resultaat van iedere laag op
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    # Doorzoek alle lagen van het model naar gedetecteerde objecten (in de blob)
    layer_outputs = net.forward(ln)

    # Variabelen klaarzetten
    kaders_lijst, zekerheden_lijst, labels_lijst, font_scale, thickness = [], [], [], 1, 1
    # Voor elke laag
    for output in layer_outputs:
        # Doorloop alle gedetecteerde objecten (per laag)
        for detectie in output:
            # Bepaal hoe zeker het model is dat de afbeelding dit voorwerp bevat
            scores = detectie[5:]
            class_id = np.argmax(scores) # class_id is het label van dit voorwerp
            zekerheid = scores[class_id]

            # ALS de zekerheid hoger is dan een bepaalde grenswaarde...
            # DAN zet een kader rond de afbeelding en label het.
            if zekerheid > ZEKERHEID_THRESHOLD:
                # Zet kader klaar en voeg toe aan lijst met kaders
                h, w = afbeelding.shape[:2]
                kader = detectie[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = kader.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                kaders_lijst.append([x, y, int(width), int(height)])

                # Voeg zekerheid en label toe aan voorziene lijsten
                zekerheden_lijst.append(float(zekerheid))
                labels_lijst.append(class_id)

    # Verwerk alle zeker gevonden objecten met openCV
    idxs = cv2.dnn.NMSBoxes(kaders_lijst, zekerheden_lijst, SCORE_THRESHOLD, IOU_THRESHOLD)

    # ALS er minstens 1 object gedetecteerd is...
    # Dan voeg kader, label en zekerheid toe aan dit voorwerp
    if len(idxs) > 0:
        # overloop de gevonden voorwerpen
        for idx in idxs.flatten():
            # Teken een kader rond het gevonden voorwerp (kleur bepaald door label)
            x, y = kaders_lijst[idx][0], kaders_lijst[idx][1]
            w, h = kaders_lijst[idx][2], kaders_lijst[idx][3]
            kleur = [int(c) for c in colors[labels_lijst[idx]]]
            cv2.rectangle(afbeelding, (x, y), (x + w, y + h), kleur, 5)
            tekst = f"{labels[labels_lijst[idx]]}: {zekerheden_lijst[idx]:.2f}"
            (breedte, hoogte) = cv2.getTextSize(tekst, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)[0]
            offset_x, offset_y = x, y-5
            kader_coords = ((offset_x, offset_y), (offset_x + breedte + 2, offset_y - hoogte))
            overlay = afbeelding.copy()
            cv2.rectangle(afbeelding, kader_coords[0], kader_coords[1], kleur, -1)
            afbeelding = cv2.addWeighted(overlay, 0.6, afbeelding, 0.4, 0)

            # Schrijf het label en de zekerheid bij het gevonden voorwerp.
            cv2.putText(afbeelding, tekst, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                1, [0,0,0], 2)

    plt_imshow(filename + "_yolo3." + ext, afbeelding)

# realtime(2, "custom")
# yolo_papier(r"")