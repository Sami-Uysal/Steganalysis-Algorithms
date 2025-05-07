
# Steganography Algorithms Project

This repository contains 5 different implementations of steganography techniques that hide and reveal a 160-character text message inside image or video data. Each method represents a unique strategy in the field of steganography.

---

## LSB (Least Significant Bit Insertion)

**Technique**: Modifies the least significant bit of each BGR pixel.

**Use Case**: Works best with uncompressed formats like PNG or BMP.

**Visibility**: Imperceptible to the human eye.

[Detail](http://www.lia.deis.unibo.it/Courses/RetiDiCalcolatori/Progetti98/Fortini/lsb.html)

---

## JPEG Steganography (DCT-Based)

**Technique**: Embeds data into DCT coefficients in JPEG compression blocks.

**Use Case**: Designed specifically for JPEG files.

**Visibility**: Subtle if compression is handled carefully.

[Detail](https://digitnet.github.io/m4jpeg/about-steganography/dct-based-steganography.htm)

---

## BPCS (Bit-Plane Complexity Segmentation)

**Technique**: Replaces complex (noisy) bit-planes of 8×8 blocks with message data.

**Use Case**: High capacity; ideal for grayscale or color images.

**Visibility**: Balanced—targets areas where noise is naturally high.

[Detail](https://en.wikipedia.org/wiki/BPCS-steganography)

---

## Masking and Filtering Methods

**Technique**: Applies Gaussian blur to detect flat image regions, embeds message only in low-detail zones.

**Use Case**: Effective for natural images (e.g., sky, water).

**Visibility**: Changes go unnoticed due to visual smoothness.

[Detail](https://digitnet.github.io/m4jpeg/about-steganography/image-steganography-techniques.htm)

---

## Heuristic Steganography (Rule-Based)

**Technique**: Uses pixel brightness heuristics to determine "safe" areas for embedding.

**Use Case**: Avoids extreme pixel values for stealth.

**Visibility**: Embeds only where human eye is least sensitive.

[Detail](http://dde.binghamton.edu/butora/pdf/Butora_PhD_Dissertation.pdf)

---

## How to Run

Each method has its own encoder and decoder Python script.

Install dependencies:

```bash
pip install opencv-python
pip install numpy
```

Run an example:

```bash
python encode.py
python decode.py
```

---

## Message Format

* Max length: `160 characters`
* Padding: Extra characters filled with `#`
* Encoding: UTF-8 to binary (8 bits per character)

---

## License

This project is for educational purposes and experimentation with steganography techniques.
