
import asyncio
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent
import sounddevice
import wave
import os


"""
code mostly from:
https://github.com/awslabs/amazon-transcribe-streaming-sdk/blob/develop/examples/simple_mic.py
"""


transcript_parts = []


class EventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        for result in results:
            for i, alt in enumerate(result.alternatives):
                for part in transcript_parts:
                    if part["start_time"] == result.start_time:
                        part["transcript"] = alt.transcript
                        break
                else:
                    transcript_parts.append({"start_time": result.start_time, "transcript": alt.transcript})
                print(str(transcript_parts) + "\n")


async def mic_stream():
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))

    stream = sounddevice.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=int(1024 * 2),
        dtype="int16",
    )
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status



async def write_chunks(transcript_stream, wave_file: wave.Wave_write):
    async for (chunk, status) in mic_stream():
        wave_file.writeframes(chunk)
        await transcript_stream.input_stream.send_audio_event(audio_chunk = chunk)
    await transcript_stream.input_stream.end_stream()


async def transcribe():

    client = TranscribeStreamingClient(region='us-east-1')
    transcript_stream = await client.start_stream_transcription(
        language_code="en-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm",
    )

    # Instantiate our handler and start processing events
    handler = EventHandler(transcript_stream.output_stream)
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'audio/output.wav')
    wave_file = wave.open(filepath, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(16000)
    await asyncio.gather(write_chunks(transcript_stream, wave_file), handler.handle_events())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(transcribe())
    loop.close()
