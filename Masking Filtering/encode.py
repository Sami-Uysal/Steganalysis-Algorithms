import cv2

def text_to_bits(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def encode_mask_filter(image_path, output_path, message):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    diff = cv2.absdiff(gray, blur)
    mask = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY_INV)[1] // 255

    message = message.ljust(160, '#')
    bits = text_to_bits(message)
    bit_idx = 0

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if mask[y, x] == 1 and bit_idx < len(bits):
                blue = img[y, x, 0]
                blue = (int(blue) & 0xFE) | int(bits[bit_idx])
                img[y, x, 0] = blue
                bit_idx += 1

    cv2.imwrite(output_path, img)
    print("Message successfully encoded using masking/filtering.")

if __name__ == "__main__":
    mg = input("Enter the message: ")
    encode_mask_filter("input.jpg", "masked_encoded.jpg", mg)