import cv2
import numpy as np

def generate_watermark(height, width, strength, seed_value):
    # Membuat watermark menggunakan bilangan acak biner dan mengonversi ke tipe data int16
    np.random.seed(seed_value)
    watermark = np.random.randint(2, size=(width, height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1  # Mengubah 0 menjadi -1
    watermark = watermark * strength  # Mengalikan watermark dengan kekuatan yang diberikan
    return watermark

def perform_encoding(image_path, strength, seed_value):
    # Mengenkripsi gambar dengan menambahkan watermark
    file_name = image_path.split("/")[-1]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("File tidak ditemukan atau bukan gambar. Harap masukkan gambar dengan format PNG atau JPG.")
        return None

    image = np.array(image, dtype=np.int16)
    image_width, image_height = image.shape[:2]
    watermark = generate_watermark(image_height, image_width, strength, seed_value)
    watermarked_image = cv2.add(image, watermark)
    return watermarked_image

def encode_image_result(result_image, image_path, strength, seed_value):
    result_data = perform_encoding(image_path, strength, seed_value)
    # Implementasi untuk menyimpan atau menangani hasil encoding

    if result_data is not None:
        cv2.imwrite(result_image + ".png", result_data)
        print("Encode berhasil! Hasil disimpan sebagai: " + result_image)
        print(" ")
        print ('''
█▀▀ █▀▀ █▄▀   █▀█ █▀█ █▀█ ▀█▀   █▀▀ █▀█ █░░ █▀▄ █▀▀ █▀█ █   █▀▀ ▄▀█ █▀▄▀█ █▄▄ ▄▀█ █▀█   █░█ ▄▀█ █▀ █ █░░
█▄▄ ██▄ █░█   █▀▄ █▄█ █▄█ ░█░   █▀░ █▄█ █▄▄ █▄▀ ██▄ █▀▄ ▄   █▄█ █▀█ █░▀░█ █▄█ █▀█ █▀▄   █▀█ █▀█ ▄█ █ █▄▄

█▀ █▀▀ █░█ ▄▀█ █▀█ █░█ █▀ █▄░█ █▄█ ▄▀█   █▀ █░█ █▀▄ ▄▀█ █░█   ▄▀█ █▀▄ ▄▀█   █▀▄ █   █▀ ▄▀█ █▄░█ ▄▀█
▄█ ██▄ █▀█ █▀█ █▀▄ █▄█ ▄█ █░▀█ ░█░ █▀█   ▄█ █▄█ █▄▀ █▀█ █▀█   █▀█ █▄▀ █▀█   █▄▀ █   ▄█ █▀█ █░▀█ █▀█
               ''')
        print(" ")
    else:
        print("Encode gagal.")