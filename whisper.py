import whisper
import opencc
import os
import json
import torchaudio
import argparse
import torch
lang2token = {
    'zh': "[ZH]",
    'ja': "[JA]",
    "en": "[EN]",
}
assert (torch.cuda.is_available()), "Please enable GPU in order to run Whisper!"
model = whisper.load_model("medium")
converter = opencc.OpenCC('t2s.json')
#ffmpeg一定要安装，不然无法跑whisper模型
def transcribe_one(audio_path):
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")
    lang = max(probs, key=probs.get)
    # decode the audio
    options = whisper.DecodingOptions(beam_size=5)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    return lang, result.text
def process(time):
    wav, sr = torchaudio.load(time, frame_offset=0, num_frames=-1,
                              normalize=True,
                              channels_first=True)
    wav = wav.mean(dim=0).unsqueeze(0)
    with open("./configs/finetune_speaker.json", 'r', encoding='utf-8') as f:
        hps = json.load(f)
    target_sr = hps['data']['sampling_rate']
    if sr != target_sr:
        wav = torchaudio.transforms.Resample(orig_freq=sr, new_freq=target_sr)(wav)
    if wav.shape[1] / sr > 20:
        print(f"audio too long, ignoring\n")
    save_path = "./processed.wav"
    torchaudio.save(save_path, wav, target_sr, channels_first=True)
    # transcribe text
    lang, text = transcribe_one(save_path)
    if lang not in list(lang2token.keys()):
        print(f"{lang} not supported, ignoring\n")
    text = converter.convert(text)
    return text

