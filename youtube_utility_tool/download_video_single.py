from pytube import YouTube
from time import perf_counter
import shutil
import os
import sys
import file_search_gui as gui

print('''
---------------------------------------------
|||MINI YOUTUBE DOWNLOADER / UTILITY TOOLS|||
---------------------------------------------
--Download youtube videos at maximum resolution(mp4 format)
--Extract mp3 from a youtube video
---------------------------------------------
Script version: 0.1.0
Created by: JAS
---------------------------------------------
If BUGS were found or if you want to suggest new features,
DM me via email.
--> junealexis.santos13@gmail.com
---------------------------------------------
---------------------------------------------
remember to set the Save path Directory first
before downloading. If not set, the path where
the script was saved will become the default
save location.
---------------------------------------------
You can type 'exit' to prompt
main menu return.
---------------------------------------------
*********************************************
''')


prompt = input('What you want to do? \n[0]: Specify save point directory.\n[1]: Download \n[2]: Extract mp3 file from video\n[3]: Exit\n[]-> : ')
directory = None
if __name__ == '__main__':
    while int(prompt) != 3:
        if int(prompt) == 0:
            directory = gui.designate_save_point()
            print(f'Successfully set new save point: {directory}\n')
            prompt = input(
                'What do you want to do? \n[0]: Specify save point directory.\n[1]: Download \n[2]: Extract mp3 file from video\n[3]: Exit\n[]-> : ')


        elif int(prompt) == 1:
            try:
                url = input('Paste your link down.)--> ')
                if url.upper() != 'EXIT':
                    video = YouTube(url)
                    print(f"\nDownloading the video: {video.title}")
                    get_vid = video.streams.get_highest_resolution()
                    start = perf_counter()
                    get_vid.download(output_path=directory)
                    end = perf_counter()
                    print(f"Download finished.\nTime elapsed {round(end-start,2)}s.\n")
                    prompt = input('What do you want to do? \n[0]: Specify save point directory.\n[1]: Download \n[2]: Extract mp3 file from video\n[3]: Exit\n[]-> : ')
                else:
                    prompt = input('SYSTEM PROMPT:\n***Returning to main menu.*** \n[0]: Specify save point directory.\n[1]: Download \n[2]: Extract mp3 file from video\n[3]: Exit\n[]-> : ')
            except KeyError:
                print('An error has been encountered. The video you were trying to download may not be available. Try again with another video.')

            except:
                print('An internal error occured. Please contact the administrator.')
        elif int(prompt) == 2:
            url_mp3 = input('Paste your link down --> ')
            mp3 = YouTube(url_mp3)
            get_mp3 = mp3.streams.filter(only_audio=True).first()
            print(f"\nDownloading the mp3 file: {get_mp3.title}")
            start = perf_counter()
            audio = get_mp3.download(output_path=directory)
            gui.rename(audio)
            end = perf_counter()
            print(f"Download finished.\nTime elapsed {round(end - start, 2)}s.\n")

            prompt = input(
                'What do you want to do? \n[0]: Specify save point directory.\n[1]: Download \n[2]: Extract mp3 file from video\n[3]: Exit\n[]-> : ')
    else:
        print('---------------------------------------------')
        print("Closing script. Thank you! \nJunnie is great! Ryt? If not, tell him that he sucks!\nJust kidding. xD. Report any bugs or anomalies you could find to\njunealexis.santos13@gmail.com")
        print('---------------------------------------------')
        sys.exit()
