import cv2

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def decode_heuristic(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found.")

    bits = ''
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if len(bits) >= 1280:
                break

            pixel = img[y, x]
            brightness = int(0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0])

            if 80 < brightness < 180:
                blue = img[y, x, 0]
                bits += str(blue & 1)

    message = bits_to_text(bits).split('#')[0]
    print("Extracted Message:", message)

if __name__ == "__main__":
    decode_heuristic("heuristic_encoded.jpg")