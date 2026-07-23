import whisper
from record import record_voice

#strating the model
model = whisper.load_model("base")
print("Started!")


#recording the voice and transcribig it
rec = record_voice()
res = model.transcribe(rec, fp16=False)
print(res["text"])
