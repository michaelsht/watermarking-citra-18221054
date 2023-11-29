from watermark_encoder import encode_image_result
from image_comparator import perform_image_comparison

print('''

░██╗░░░░░░░██╗░█████╗░████████╗███████╗██████╗░███╗░░░███╗░█████╗░██████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
░╚██╗████╗██╔╝███████║░░░██║░░░█████╗░░██████╔╝██╔████╔██║███████║██████╔╝█████═╝░██║██╔██╗██║██║░░██╗░
░░████╔═████║░██╔══██║░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██║██║╚████║██║░░╚██╗
░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░

░█████╗░██╗████████╗██████╗░░█████╗░
██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░░██║░░░██████╔╝███████║
██║░░██╗██║░░░██║░░░██╔══██╗██╔══██║
╚█████╔╝██║░░░██║░░░██║░░██║██║░░██║
░╚════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
''')

print("Selamat Datang pada Program WATERMARKING CITRA")
print("dibuat oleh Michael Sihotang (18221054)\n")

# Informasi input
print("Proses ini akan memerlukan beberapa tahap, yaitu")
print(" ")
print("STEP 01")
print("Siapkan gambar yang akan digunakan untuk watermarks")
print(" ")
print("STEP 02")
print("Tempatkan gambar yang ingin diproses dalam folder input")
print(" ")
print("STEP 03")
original_image_path = input('''Masukkan path gambar asli dan (tambahkan .jpg atau .png di akhir): ''')
print(" ")
print("STEP 04")
intensity_level = int(input("Masukkan noise intensity: "))
print(" ")
print("STEP 05")
seed_value = int(input("Masukkan nilai seed yang digunakan: "))
print(" ")
print("STEP 06")
result_file_name = input("Masukkan nama file hasil: ")
print("")

# Melakukan encoding gambar
encode_image_result(result_file_name, "input\\" + original_image_path, intensity_level, seed_value)

# Memeriksa apakah gambar sudah di-watermark
user_answer = input("Apakah Anda ingin memeriksa apakah gambar sudah di-watermark? (Y/T): ")
while user_answer != "Y" and user_answer != "T":
    print("Input tidak valid!") 
    user_answer = input("Apakah Anda ingin memeriksa apakah gambar sudah di-watermark? (Y/T): ")

if user_answer == "Y":
    comparison_result = perform_image_comparison("input\\" + original_image_path, result_file_name + ".png")
    print("HASIL: " + comparison_result)

print('''
█████████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▄█▄─▀█▀─▄██▀▄─████▄─█─▄██▀▄─██─▄▄▄▄█▄─▄█─█─█
███─████─▄█▀██─▄─▄██─███─█▄█─███─▀─█████─▄▀███─▀─██▄▄▄▄─██─██─▄─█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▀▄▀
      ''')