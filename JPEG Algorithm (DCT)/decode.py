import cv2
import numpy as np

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def decode_dct(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found.")

    img = img.astype(np.float32)
    h, w = img.shape
    bits = ''

    for y in range(0, h - 8 + 1, 8):
        for x in range(0, w - 8 + 1, 8):
            if len(bits) >= 160 * 8:
                break

            block = img[y:y+8, x:x+8]
            dct_block = cv2.dct(block)
            bit = int(round(dct_block[4, 3])) & 1
            bits += str(bit)

    message = bits_to_text(bits).split('#')[0]
    print("Extracted Message:", message)

if __name__ == "__main__":
    decode_dct("encoded.jpg")
