import asyncio

# This example uses aiofile for asynchronous file reads.
# It's not a dependency of the project but can be installed
# with `pip install aiofile`.
import aiofile
import pyaudio
from sys import platform
import argparse

from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent
from amazon_transcribe.utils import apply_realtime_delay

"""
Here's an example of a custom event handler you can extend to
process the returned transcription results as needed. This
handler will simply print the text out to your interpreter.
"""


SAMPLE_RATE = 16000
BYTES_PER_SAMPLE = 2
CHANNEL_NUMS = 1

# An example file can be found at tests/integration/assets/test.wav
AUDIO_PATH = "test.wav"
CHUNK_SIZE = 1024 * 8
REGION = "us-west-2"

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    if 'linux' in platform:
            mic_name = args.default_microphone
            if not mic_name or mic_name == 'list':
                print("Available microphone devices are: ")
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    print(f"Microphone with name \"{name}\" found")   
                return
            else:
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    if mic_name in name:
                        source = sr.Microphone(sample_rate=16000, device_index=index)
                        break
    else:
        source = sr.Microphone(sample_rate=16000)



class MyEventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                print(alt.transcript)


async def basic_transcribe():
    main()
    # Setup up our client with our chosen AWS region
    client = TranscribeStreamingClient(region=REGION)

    # Start transcription to generate our async stream
    stream = await client.start_stream_transcription(
        language_code="en-US",
        media_sample_rate_hz=SAMPLE_RATE,
        media_encoding="pcm",
    )

    async def write_chunks():
        # Set chunk size and audio format
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1
        fs = 44100  # Record at 44100 samples per second

        p = pyaudio.PyAudio()

        # Rename the variable from 'stream' to 'p_stream'
        p_stream = p.open(format=sample_format,
                      channels=channels,
                      rate=fs,
                      frames_per_buffer=chunk,
                      input=True)

        # Send audio in chunks to transcribe service
        while True:
            data = p_stream.read(chunk)
            await stream.input_stream.send_audio_event(audio_chunk=data)

        # Stop and close the stream 
        p_stream.stop_stream()
        p_stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        await stream.input_stream.end_stream() 

    # Instantiate our handler and start processing events
    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(), handler.handle_events())


loop = asyncio.get_event_loop()
loop.run_until_complete(basic_transcribe())
loop.close()
