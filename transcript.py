import whisper

model = whisper.load_model('tiny.en')
result = model.transcribe('temp_audio/Mindset Speech.m4a', fp16=False)

print(result['text'])