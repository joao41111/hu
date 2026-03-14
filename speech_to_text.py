import json
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration

class SpeechToText:
    def __init__(self, model_name='openai/whisper-base'):
        self.processor = WhisperProcessor.from_pretrained(model_name)
        self.model = WhisperForConditionalGeneration.from_pretrained(model_name)

    def transcribe(self, audio_file):
        audio_input = self.processor(audio_file, return_tensors='pt', sampling_rate=16000).input_values
        with torch.no_grad():
            predicted_ids = self.model.generate(audio_input)
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription

    def extract_keywords(self, transcript):
        # Implement keyword extraction logic based on your needs
        keywords = set(transcript.split())  # Simplistic keyword extraction
        return list(keywords)

    def save_transcript_to_json(self, transcript, keywords, file_name='transcript.json'):
        transcript_data = {'transcript': transcript, 'keywords': keywords}
        with open(file_name, 'w') as json_file:
            json.dump(transcript_data, json_file)

# Example Usage:
# stt = SpeechToText()
# transcription = stt.transcribe('path_to_audio_file.wav')
# keywords = stt.extract_keywords(transcription[0])
# stt.save_transcript_to_json(transcription[0], keywords)