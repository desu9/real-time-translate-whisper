# Whisper-vad-translate

This is a real-time translation system based on whisper model, vad speech activity recognition model and youdao translate.


## Setup

We used Python 3.9 and [PyTorch](https://pytorch.org/) 1.13.1+cuda11.7. 

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

You may need [`rust`](http://rust-lang.org) installed as well, in case [tiktoken](https://github.com/openai/tiktoken) does not provide a pre-built wheel for your platform. If you see installation errors during the `pip install` command above, please follow the [Getting started page](https://www.rust-lang.org/learn/get-started) to install Rust development environment. Additionally, you may need to configure the `PATH` environment variable, e.g. `export PATH="$HOME/.cargo/bin:$PATH"`. If the installation fails with `No module named 'setuptools_rust'`, you need to install `setuptools_rust`, e.g. by running:

```bash
pip install setuptools-rust
```


## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

The `.en` models for English-only applications tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models.

Whisper's performance varies widely depending on the language. The figure below shows a WER (Word Error Rate) breakdown by languages of the Fleurs dataset using the `large-v2` model (The smaller the numbers, the better the performance). Additional WER scores corresponding to the other models and datasets can be found in Appendix D.1, D.2, and D.4. Meanwhile, more BLEU (Bilingual Evaluation Understudy) scores can be found in Appendix D.3. Both are found in [the paper](https://arxiv.org/abs/2212.04356). 

![WER breakdown by language](https://raw.githubusercontent.com/openai/whisper/main/language-breakdown.svg)



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
