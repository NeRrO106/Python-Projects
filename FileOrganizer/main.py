import os, shutil

folder = "C:/Users/Andrei/Desktop"

extensii = {
    "Imagini": [".jpg", ".png", ".jpeg"],
    "Documente": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".accdb", ".csv"],
    "Baze_De_Date": [".db"],
    "Video": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Arhive": [".rar", ".zip", ".7zip"],
    "Executabile": [".exe", ".msi"]
}

for fisier in os.listdir(folder):
    nume, ext = os.path.splitext(fisier)
    for tip, exts in extensii.items():
        if ext.lower() in exts:
            destinatie = os.path.join(folder, tip)
            os.makedirs(destinatie, exist_ok=True)
            try:
                shutil.move(os.path.join(folder, fisier),
                            os.path.join(destinatie, fisier))
                print(f"Mutat {fisier} -> {tip}")
            except PermissionError:
                print(f"Fisierul: {fisier} -> este folosit in alt program")
"""
from PIL import Image

# Înlocuiește căile de mai jos cu locațiile reale ale imaginilor tale
image1_path = "C:/Users/Andrei/Desktop/WhatsApp Image 2025-10-20 at 11.43.37_1a605560.jpg"
image2_path = "C:/Users/Andrei/Desktop/WhatsApp Image 2025-10-20 at 11.43.51_2c779d4a.jpg"

# Deschide imaginile
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Redimensionează ambele imagini la aceeași înălțime
height = min(image1.height, image2.height)
image1 = image1.resize((int(image1.width * height / image1.height), height))
image2 = image2.resize((int(image2.width * height / image2.height), height))

# Creează o imagine nouă care le îmbină pe cele două
combined_width = image1.width + image2.width
combined_image = Image.new("RGB", (combined_width, height))
combined_image.paste(image1, (0, 0))
combined_image.paste(image2, (image1.width, 0))

# Salvează imaginea rezultată
combined_image.save("combined_desktop.jpg")
print("Imaginea a fost salvată ca 'combined_desktop.jpg'")
"""