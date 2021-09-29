# BeatstarBot

Bot for Android game Beatstar using OpenCV pattern matching.

## Description

Using an Android emulator, this bot will continually search for a matching note image. It takes a screenshot and runs the pattern matching algorithm. If two notes are found at the same time, then it will press them at the same time. Currently this bot is completely dependant on a particular setup for the game. See dependencies for more details.

## Getting Started

### Dependencies

* Windows
* LDPlayer (or other Android VM)
* Tap lanes must be assigned to A, S, D keys*
* Template images matching VM window size*

*Beatstar has 3 lanes for notes, left, center, right. Your VM must be configured to have the A, S, D keys correspond to these tap lanes.

*The provided bar.png and beatstar_text.png are sized to the default LDPlayer window size. If your window size is different, you may have to update the images using screenshots of the game from your VM.

### Executing program

* Launch Beatstar in Android VM and choose a song
* Before starting the song, run main.py
* Choose top left and bottom right points by clicking to define focus region*
* Bot should automatically begin playing!

*We could grab the entire VM window, but the smaller the focus region, the faster it can process pattern matching. Therefore it would make the most sense to choose only the hit region as the focus region. This also makes the most sense because the bot does not check if the note is located in the hit region.

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Thanks to
* ClarityCoders [Github](https://github.com/ClarityCoders) [YouTube](https://www.youtube.com/channel/UC9Q4rw4dkey9lhK5FnYuigg)