# Discord Music Bot

This project is a Discord music bot that can play music from various platforms including Apple Music, YouTube, Spotify, and SoundCloud. The bot is designed to provide a seamless music experience within Discord servers.

## Features

- Play music from multiple sources
- Control playback with commands (play, pause, resume, stop, skip)
- Easy to set up and use

## Requirements

- Python 3.8 or higher
- Discord.py
- youtube-dl
- Additional libraries as specified in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-music-bot.git
   cd discord-music-bot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Open `config/config.json` and add your bot token and any necessary API keys.

4. Run the bot:
   ```
   python src/bot.py
   ```

## Usage

- Invite the bot to your server using the OAuth2 URL generated in the Discord Developer Portal.
- Use commands in a text channel to control music playback.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.