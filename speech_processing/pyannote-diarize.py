
from pyannote.audio import Pipeline

# speaker diarization


if __name__ == "__main__":
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="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")




