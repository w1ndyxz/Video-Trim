import os

def Folder(Folder):
    if not os.path.exists('Output'):
        print('[!] Создаём папку Output')
        os.makedirs('Output')

    print('[!] Создаём папку с названием файла')
    if not os.path.exists('Output\\' + Folder):
        os.makedirs('Output\\' + Folder)



VideoName = str(input('[?] Название видео: '))
VideoDurationMins = int(input('[?] Сколько минут в видео: '))
DurationCut = int(input('[?] На сколько минут обрезать: '))
Count = 0
CurrentStart = 0

print('')
Folder(VideoName)
print(f'\n[=] {Count} | Обрезаем')
os.system(f"ffmpeg.exe -hide_banner -loglevel error -i {VideoName} -ss 00:{CurrentStart}:00 -t 00:{DurationCut}:00 -c:v copy -c:a copy Output\\{VideoName}\\Out_{Count}.mp4")
Count += 1

CurrentStart = DurationCut
while CurrentStart <= VideoDurationMins:
    print(f'[=] {Count} | Обрезаем')
    os.system(f"ffmpeg.exe -hide_banner -loglevel error -i {VideoName} -ss 00:{CurrentStart}:00 -t 00:{DurationCut}:00 -c:v copy -c:a copy Output\\{VideoName}\\Out_{Count}.mp4")
    Count += 1
    CurrentStart += DurationCut

input('\n[!] Готово!\n[!] Чтобы закрыть, нажмите любую клавишу...')