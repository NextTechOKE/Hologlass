import sounddevice as sd
import asyncio
from scipy.io.wavfile import write
import soundfile as sf

import os
import wave



# async def record_audio(filename):
#     # Open the WAV file in write mode
#     with sf.SoundFile(filename, mode='x', samplerate=44100, channels=1) as file:
#         # Create an asynchronous generator that yields audio blocks
#         stream = sd.InputStream(callback=lambda data, frames, time, status: file.write(data))
        
#         # Start the stream
#         stream.start()
        
#         # Keep the coroutine running until interrupted
#         while True:
#             await asyncio.sleep(0.1)



async def mic_stream():
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))

    stream = sd.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=1024//24,
        dtype="int16",
    )
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status



async def record_continuously(wave_file: wave.Wave_write=None):

    if not wave_file:
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, 'audio/output.wav')
        wave_file = wave.open(filepath, 'wb')
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(16000)

    async for (chunk, status) in mic_stream():
        wave_file.writeframes(chunk)


if __name__ == "__main__":
    asyncio.run(record_continuously())


