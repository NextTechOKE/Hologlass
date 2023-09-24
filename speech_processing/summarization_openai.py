import openai

def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks
async def record_audio(filename, duration, fs=44100):

    while True:
        recording = sounddevice.rec(int(duration * fs), samplerate=fs, channels=2)
        await asyncio.sleep(duration)  # Wait for the recording to finish
        write(filename, fs, recording)  # Save as WAV file
        print(f"Recording saved to {filename}.")


def generate_summary(text):
    input_chunks = split_text(text)
    output_chunks = []
    for chunk in input_chunks:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(
                f"Please summarize the following text in one sentence:\n{chunk}\n\nSummary:"),
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
        break
    return " ".join(output_chunks)


