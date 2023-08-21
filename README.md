# Whisper-vad-translate
[**🌐English**](./README_EN.md)

这是一个基于whisper模型、vad语音活动识别模型和有道翻译的实时翻译系统。


## 配置

我们使用 Python 3.9  和 [PyTorch](https://pytorch.org/) 1.13.1+cuda11.7. 

    pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
    pip install -r requirements.txt


它还需要在您的系统上安装命令行工具[' ffmpeg '](https://ffmpeg.org/)，它可以从大多数包管理器中获得:

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



## 可用的模型和语言

[**Whisper**](https://github.com/openai/whisper/)

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |




## 命令行用法

下面的命令将开始转录语音:

    python main.py

默认设置(选择“medium”模式)对转录效果很好。默认的翻译语言是日语，你可以使用'——language '选项指定语言:

    main.py --language en
    main.py -l en

默认为捕获系统音频，如果需要捕获麦克风输入，请输入如下命令:

    main.py -m 1



## License

See [LICENSE](https://github.com/desu9/whiper-vad-translate/blob/main/LICENSE) for further details.
