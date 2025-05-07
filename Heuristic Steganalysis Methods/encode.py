import cv2

def text_to_bits(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def encode_heuristic(image_path, output_path, message):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found.")

    message = message.ljust(160, '#')
    bits = text_to_bits(message)
    bit_idx = 0

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if bit_idx >= len(bits):
                break

            pixel = img[y, x]
            brightness = int(0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0])

            if 80 < brightness < 180:
                blue = int(pixel[0])
                blue = (blue & 0xFE) | int(bits[bit_idx])
                img[y, x, 0] = blue
                bit_idx += 1

    if bit_idx < len(bits):
        raise ValueError("Message is too long for this image using heuristic rules.")

    cv2.imwrite(output_path, img)
    print("Message successfully encoded using heuristic method.")

if __name__ == "__main__":
    mg = input("Enter the message: ")
    encode_heuristic("input.jpg", "heuristic_encoded.jpg", mg)
