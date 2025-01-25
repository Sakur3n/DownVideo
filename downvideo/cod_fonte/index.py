import yt_dlp

def baixar_video(url, caminho="downloads"):
    try:
        ydl_opts = {
            "outtmpl": f"{caminho}/%(title)s.%(ext)s",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo no YouTube: ")
    baixar_video(url)
        