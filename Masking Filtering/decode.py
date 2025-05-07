import cv2

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def decode_mask_filter(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    diff = cv2.absdiff(gray, blur)
    mask = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY_INV)[1] // 255

    bits = ''
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if mask[y, x] == 1 and len(bits) < 1280:
                blue = img[y, x, 0]
                bits += str(blue & 1)

    message = bits_to_text(bits).split('#')[0]
    print("Extracted Message:", message)

if __name__ == "__main__":
    decode_mask_filter("masked_encoded.jpg")
