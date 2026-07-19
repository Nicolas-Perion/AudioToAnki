from yt_dlp import YoutubeDL

URL = ['https://youtu.be/45AqbjMp_kA?si=GX23z0xLl5O-NQn4']
# https://youtu.be/vVL6NFzr0Rg?si=uS-n4RibJY1hIyaj


ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        },
        {
            'key': 'SponsorBlock',
            'categories': ['sponsor', 'selfpromo', 'preview', 'interaction'],   # For both 'categories' and 'remove_sponsor_segments',
                                                                        # the available segments are :
                                                                        # 'sponsor', 'intro', 'outro', 'selfpromo', 'preview',
                                                                        # 'filler', 'interaction', 'music_offtopic', 'hook',
                                                                        # 'poi_highlight', 'chapter' and 'all'
        },
        {
            'key': 'ModifyChapters',
            'remove_sponsor_segments': ['sponsor', 'selfpromo', 'preview', 'interaction'],
        }
        ],
    'cookiefile': 'cookies.txt',
    'js_runtimes': {'deno': {'path': 'C:/Users/Portable1/.deno/bin/deno.exe'}},
    'outtmpl': 'temp_audio/%(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URL)