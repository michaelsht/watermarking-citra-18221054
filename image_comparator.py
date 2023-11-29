import cv2
import numpy as np

def perform_image_comparison(original_path, watermarked_path):
    # Membandingkan dua gambar, asumsikan kedua gambar dalam skala abu-abu (grayscale)
    original_image = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    watermarked_image = cv2.imread(watermarked_path, cv2.IMREAD_GRAYSCALE)

    # Memeriksa apakah gambar-gambar tersedia
    if original_image is None or watermarked_image is None:
        print("File tidak ditemukan atau bukan gambar. Harap pastikan kedua file adalah gambar dengan format PNG atau JPG.")
        return None

    # Menghitung perbedaan antara kedua gambar
    difference = cv2.absdiff(original_image, watermarked_image)
    total_difference = np.sum(difference)

    # Menetapkan nilai ambang batas untuk menentukan apakah gambar mengandung watermark
    threshold_value = 100000

    # Mengembalikan hasil berdasarkan perbedaan total
    if total_difference > threshold_value:
        return "Gambar hasil mengandung watermark."
    else:
        return "Gambar hasil tidak mengandung watermark."