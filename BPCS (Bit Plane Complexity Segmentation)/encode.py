import cv2
import numpy as np

def text_to_bits(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def calc_complexity(block):
    transitions = np.sum(block[:, :-1] != block[:, 1:]) + np.sum(block[:-1, :] != block[1:, :])
    return transitions / 112

def encode_bpcs(image_path, output_path, message, threshold=0.3):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found.")

    h, w = img.shape
    if h % 8 != 0 or w % 8 != 0:
        raise ValueError("Image dimensions must be divisible by 8.")

    message = message.ljust(160, '#')
    bits = text_to_bits(message)
    bit_idx = 0

    bit_planes = np.unpackbits(img[:, :, None], axis=2)

    for plane in range(7, -1, -1):
        for y in range(0, h, 8):
            for x in range(0, w, 8):
                if bit_idx >= len(bits):
                    break

                block = bit_planes[y:y+8, x:x+8, plane]
                if block.shape != (8, 8):
                    continue

                complexity = calc_complexity(block)
                if complexity >= threshold:
                    for i in range(8):
                        for j in range(8):
                            if bit_idx >= len(bits):
                                break
                            block[i, j] = int(bits[bit_idx])
                            bit_idx += 1

    encoded_img = np.packbits(bit_planes, axis=2).reshape(h, w)
    cv2.imwrite(output_path, encoded_img)
    print("Message encoded using BPCS.")

if __name__ == "__main__":
    mg = input("Enter the message: ")
    encode_bpcs("input.png", "bpcs_encoded.png", mg)