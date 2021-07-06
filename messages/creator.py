from telegram.utils.helpers import escape_markdown as es


def start_msg(name):
    msg = f"""*Hey {es(name,version=2)}* ✋✋ *Selamat Datang Di Bot Music Downloader* ⚡⚡\n
    _Segera Unduh Music Dari saya Dan Nikmatilah Ketika Selesai Mengunduh!_\n
Di Kelola ❤️ Oleh [ALAHSIAMY](https://t.me/LordGanss10"""
    return msg


def help_msg():
    help = """ℹ️⁉⁉ *help*\n
*just send me a jiosaavn song,album or playlist link, I will send you the audio with lyrics*⚡⚡"""
    return help
