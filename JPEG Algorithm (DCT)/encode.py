import cv2
import numpy as np

def text_to_bits(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def encode_dct(image_path, output_path, message):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found.")

    message = message.ljust(160, '#')
    bits = text_to_bits(message)

    img = img.astype(np.float32)
    h, w = img.shape
    bit_idx = 0

    for y in range(0, h - 8 + 1, 8):
        for x in range(0, w - 8 + 1, 8):
            if bit_idx >= len(bits):
                break

            block = img[y:y+8, x:x+8]
            dct_block = cv2.dct(block)

            coeff = round(dct_block[4, 3])
            coeff = (int(coeff) & ~1) | int(bits[bit_idx])
            dct_block[4, 3] = float(coeff)
            bit_idx += 1

            idct_block = cv2.idct(dct_block)
            img[y:y+8, x:x+8] = idct_block

    img = np.clip(img, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, img)
    print("Message successfully encoded.")

if __name__ == "__main__":
    mg = input("Enter the message: ")
    encode_dct("input.jpg", "encoded.jpg", mg)
