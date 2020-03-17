import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[:len(data) // 4]
    newdata2 = data[len(data) // 4:(len(data) // 4) * 2]
    newdata3 = data[(len(data) // 4) * 2:(len(data) // 4) * 3]
    newdata4 = data[(len(data) // 4) * 3:]
    newdata = newdata3 + newdata4 + newdata + newdata2
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()
