import wave

def decode_message(audio_path):
    with wave.open(audio_path, 'rb') as audio:
        frames = bytearray(audio.readframes(audio.getnframes()))

    bits = [str(frames[i] & 1) for i in range(160 * 8)]

    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars)

    return message.rstrip('#')

if __name__ == "__main__":
    message = decode_message("encoded.wav")
    print("Hidden Message:", message)
