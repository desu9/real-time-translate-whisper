# Whisper-vad-translate

This is a real-time translation system based on whisper model, vad speech activity recognition model and youdao translate.


## Setup

We used Python 3.9  and [PyTorch](https://pytorch.org/) 1.13.1+cuda11.7. 

    pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
    pip install -r requirements.txt


It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```



## Available models and languages

[**Whisper**](https://github.com/openai/whisper/)


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |


## Command-line usage

The following command will start transcribe speech:

    python main.py

The default setting (which selects the `medium` model) works well for transcribing. The default translation language is Japanese, and you can specify the language using the `--language`option:

    main.py --language en
    main.py -l en

The default audio is system audio, if you want to record microphone input, enter the following command:

    main.py -m 1



## License

See [LICENSE](https://github.com/desu9/whiper-vad-translate/blob/main/LICENSE) for further details.
