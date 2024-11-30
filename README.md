### **Judul Proyek**
🎵 **Discord Music Bot** - Python

---

### **Deskripsi**
Bot musik Discord sederhana yang dibangun menggunakan Python dan `discord.py`. Bot ini memungkinkan pengguna untuk memutar musik langsung dari YouTube ke voice channel di Discord. 

**Fitur utama:**
- 🎶 **Play music**: Cari dan mainkan musik dari YouTube.
- ⏭️ **Skip track**: Lewati lagu yang sedang diputar.
- 📜 **Queue system**: Antrian lagu yang otomatis diputar satu per satu.
- 🔊 **Join & Leave channel**: Bergabung dan keluar dari voice channel.

---

### **Teknologi yang Digunakan**
- **Bahasa:** Python 3.8+
- **Library Utama:**
  - [`discord.py`](https://github.com/Rapptz/discord.py): Library Python untuk Discord API.
  - [`youtube-dl`](https://github.com/ytdl-org/youtube-dl): Ekstraksi metadata video/audio.
  - `ffmpeg`: Alat untuk streaming dan konversi audio.
  - `python-dotenv`: Untuk mengelola variabel lingkungan.

---

### **Cara Penggunaan**
1. Clone repositori ini:
   ```bash
   git clone https://github.com/Dodikz/BotMusic-Discord.git
   cd BotMusic-**Discord**
   ```

2. Buat virtual environment dan instal dependensi:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Tambahkan token bot Anda ke file `.env`:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```

4. Jalankan bot:
   ```bash
   python3 music_bot.py
   ```

---

### **Cara Kerja Bot**
1. Undang bot Anda ke server Discord.
2. Gunakan perintah:
   - `!join`: Memasukkan bot ke voice channel.
   - `!play [judul/URL YouTube]`: Memutar lagu.
   - `!skip`: Melewati lagu saat ini.
   - `!leave`: Mengeluarkan bot dari voice channel.
