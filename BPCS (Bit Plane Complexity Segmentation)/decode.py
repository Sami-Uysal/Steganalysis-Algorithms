import cv2
import numpy as np

def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def calc_complexity(block):
    transitions = np.sum(block[:, :-1] != block[:, 1:]) + np.sum(block[:-1, :] != block[1:, :])
    return transitions / 112

def decode_bpcs(image_path, threshold=0.3):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image not found.")

    h, w = img.shape
    bit_planes = np.unpackbits(img[:, :, None], axis=2)

    bits = ''
    for plane in range(7, -1, -1):
        for y in range(0, h, 8):
            for x in range(0, w, 8):
                if len(bits) >= 1280:
                    break

                block = bit_planes[y:y+8, x:x+8, plane]
                if block.shape != (8, 8):
                    continue

                complexity = calc_complexity(block)
                if complexity >= threshold:
                    for i in range(8):
                        for j in range(8):
                            if len(bits) >= 1280:
                                break
                            bits += str(block[i, j])

    message = bits_to_text(bits).split('#')[0]
    print("Extracted Message:", message)

if __name__ == "__main__":
    decode_bpcs("bpcs_encoded.png")