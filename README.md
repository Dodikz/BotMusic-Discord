# Discord Music Bot

Bot musik untuk Discord yang memungkinkan pengguna untuk memutar, melewati, dan menghentikan musik di voice channel. Bot ini menggunakan YouTube sebagai sumber musik dan FFmpeg untuk memproses audio.

## Fitur
- **Bergabung ke Voice Channel**: Bot akan bergabung dengan voice channel pengguna.
- **Memutar Musik**: Bot memutar musik berdasarkan pencarian di YouTube.
- **Melewati Lagu**: Bot dapat melewati lagu yang sedang diputar.
- **Menghentikan Musik**: Bot dapat menghentikan musik yang sedang diputar dan keluar dari voice channel.
- **Penggunaan Queue**: Daftar lagu akan diputar secara berurutan.

## Persyaratan
1. Python 3.6+
2. Discord.py
3. yt-dlp (untuk mengambil audio dari YouTube)
4. FFmpeg (untuk memproses audio)

## Instalasi

### 1. Kloning Repositori
Klon repositori ini ke komputer Anda:
```bash
git clone https://github.com/Dodikz/BotMusic-Discord.git
cd discord-music-bot
```

### 2. Membuat Virtual Environment
Disarankan untuk menggunakan virtual environment untuk mengelola dependensi:
```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```

### 3. Menginstal Dependensi
Instal semua dependensi yang diperlukan:
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg
Bot ini memerlukan FFmpeg untuk memproses audio. Pastikan FFmpeg sudah terinstal di sistem Anda.

- **Linux**: Anda bisa menginstal FFmpeg menggunakan apt:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Windows**: Unduh FFmpeg dari [FFmpeg.org](https://ffmpeg.org/download.html) dan tambahkan path binari ke dalam `PATH` lingkungan sistem Anda.

### 5. Konfigurasi Token
Buat file `.env` di direktori yang sama dengan bot dan masukkan token bot Discord Anda ke dalam file tersebut:
```
DISCORD_TOKEN=your_token_here
```
Gantilah `your_token_here` dengan token bot yang Anda dapatkan dari [Discord Developer Portal](https://discord.com/developers/applications).

### 6. Menjalankan Bot
Sekarang Anda bisa menjalankan bot dengan perintah:
```bash
python3 music-bot.py
```

## Perintah Bot
- `!join`: Bot akan bergabung dengan voice channel tempat Anda berada.
- `!leave`: Bot akan keluar dari voice channel.
- `!play <search>`: Memutar lagu berdasarkan pencarian (contoh: `!play Never Gonna Give You Up`).
- `!skip`: Melewati lagu yang sedang diputar dan melanjutkan ke lagu berikutnya.
- `!stop`: Menghentikan musik yang sedang diputar dan keluar dari voice channel.