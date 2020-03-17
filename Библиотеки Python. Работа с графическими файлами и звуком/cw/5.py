import struct
import wave


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    frames_count = source.getnframes()
    width = source.getsampwidth()
    rate = source.getframerate()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    new_data = [item for item in data if abs(item) > 5]
    new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
    dest = wave.open("out.wav", mode="wb")
    dest.setnchannels(1)
    dest.setsampwidth(width)
    dest.setframerate(rate)
    dest.writeframes(new_frames)
    source.close()
    dest.close()
