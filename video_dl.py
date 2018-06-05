from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}



while True:
	try:
		vidURL = input("Enter video URL: ")
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([vidURL])
		print("\nDownload complete.....\n")
	except KeyboardInterrupt:
		print ("\nGood bye!")
		break
	except:
		pass
