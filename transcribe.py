import whisper

language = "tr"
input_file = "soundfile.m4a"
output_file = "transcription_output.txt"

def transcribe_audio(input_file, output_file):
    # Change this to "small" or "base" for faster results
    model = whisper.load_model("large")

    result = model.transcribe(input_file, 
        language=language, 
        temperature=0, # Set to 0 for more accurate transcription
        beam_size=5, # Increase beam size for more thorough search
        fp16=False # Set to False for better CPU accuracy
    )     

    # Save the transcription result
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription saved to {output_file}")

transcribe_audio(input_file, output_file)
