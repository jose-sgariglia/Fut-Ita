import cv2
import os

import cv2
import os

def crea_video_da_immagini(cartella_immagini, nome_video, durata_immagine=0.1, fps=200):
    immagini = [img for img in os.listdir(cartella_immagini) if img.endswith((".png", ".jpg", ".jpeg"))]
    immagini.sort()

    if not immagini:
        print("Nessuna immagine trovata nella cartella.")
        return

    prima_immagine = cv2.imread(os.path.join(cartella_immagini, immagini[0]))
    altezza, larghezza, _ = prima_immagine.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(nome_video, fourcc, fps, (larghezza, altezza))
    
    frame_count = int(durata_immagine * fps)

    for immagine_nome in immagini:
        img_path = os.path.join(cartella_immagini, immagine_nome)
        immagine = cv2.imread(img_path)

        if immagine.shape[1] != larghezza or immagine.shape[0] != altezza:
            immagine = cv2.resize(immagine, (larghezza, altezza))

        for _ in range(frame_count):
            video_writer.write(immagine)

    video_writer.release()
    print(f"Video {nome_video} creato con successo.")

path = "../products/charts/demographics/year/ITA"
crea_video_da_immagini(path, "video_output.mp4")
