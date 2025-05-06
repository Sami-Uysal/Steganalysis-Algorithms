import wave

def encode_message(audio_in_path, audio_out_path, message):

    with wave.open(audio_in_path, 'rb') as audio:
        frames = bytearray(audio.readframes(audio.getnframes()))
        params = audio.getparams()

    message = message.ljust(160, '#')
    message_bits = ''.join([format(ord(char), '08b') for char in message])

    for i, bit in enumerate(message_bits):
        frames[i] = (frames[i] & 0b11111110) | int(bit)

    with wave.open(audio_out_path, 'wb') as encoded_audio:
        encoded_audio.setparams(params)
        encoded_audio.writeframes(frames)

    print("Message successfully hidden!")

if __name__ == "__main__":
    mg = input("Enter the message: ")
    encode_message("input.wav", "encoded.wav", mg)
