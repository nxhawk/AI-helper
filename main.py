import datetime
from datetime import date
import requests
import os
import regex
import time
import ctypes
import wikipedia
import speech_recognition as sr
from gtts import gTTS
import playsound
from time import strftime
import webbrowser
from youtube_search import YoutubeSearch
import urllib.request as urll
import json

wikipedia.set_lang('vi')
language = 'vi'

# chuyen van ban thanh giong noi


def speak(text):
    print("[AI]:", text)
    tts = gTTS(text=text, lang='vi', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

# chuyen giong noi thanh van ban


def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("[AI]: Đang nghe ....")

        audio = ear_robot.record(source, duration=4)

        try:
            print(("[AI] :  ...  "))
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("[Me]:  ", text)
            return text
        except Exception as ex:
            print("[AI]: Lỗi Rồi ! ... !")
            return 0


def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        speak("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
        text = input("Mời nhập: ")
    return text.lower()


def stop():
    speak("Hẹn gặp lại sau nha ! ... ")


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Trợ Lý Ảo không nghe rõ bạn nói. Vui lòng nói lại nha !")
    time.sleep(3)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))
    if 0 <= day_time <= 11:
        speak(f"Chào {name}. Chúc bạn buổi sáng tốt lành.")
    elif 11 <= day_time < 13:
        speak(f"Chào {name}. Chúc bạn có một buổi trưa thật vui vẻ.")
    elif 13 <= day_time < 18:
        speak(f"Chào {name}. Chúc bạn buổi chiều vui vẻ.")
    elif 18 <= day_time < 22:
        speak(f"Chào {name}. Tối rồi, Bạn đã cơm nước gì chưa ?")
    elif 22 <= day_time <= 23:
        speak(f"Chào {name}. Muộn rồi bạn nên đi nghủ sớm nha.")
    else:
        speak(f"Thời gian bên tôi chưa đúng hoặc gặp lỗi. Bạn nên xem lại nha.")


def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
    elif "ngày" in text:
        speak(f"hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Lý Hành chưa hiểu ý bạn.")


def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile(
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(
            "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(
            "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    elif "code1" in text or "vs" in text or "visual studio" in text:
        speak("Mở Visual Studio")
        os.startfile(
            "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe")
    elif "code2" in text or "code" in text or "visual studio code" in text:
        speak("Mở Visual Studio Code")
        os.startfile(
            "C:\\Users\\MY COMPUTER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "thư mục" in text:
        speak("Mở thư mục")
        os.system("explorer.exe  file:")
    elif "terminal" in text or "cmd" in text:
        speak("Mở command prompt")
        os.system("start cmd")
    else:
        speak("Ứng dụng chưa cài đặt. Vui Lòng cài đặt cho tui nha !")


def open_website(text):
    reg_ex = regex.search('mở (.+)', text)
    print(reg_ex)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain+".com"
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở. ")
        if input("Nếu muốn tiếp tục thì nhấn q: ") == "q":
            pass
        return True
    else:
        return False


def open_google_and_search(text):
    if text.find('kiếm') != -1:
        search_for = str(text).split("kiếm", 1)[1]
    else:
        search_for = text
    print(search_for)
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")


def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    #city = get_text()
    city = "Tiền Giang"
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "b4750c6250a078a943b3bf920bb138a0"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    print(call_url)


def play_youtube():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")


def play_youtube_2():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=10).to_dict()
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")
    print(result)


def change_wallpaper():
    api_key = "XFyV6boeltUQBb9ROo5nPsWWvoPPDCPLRSwMaO_IXc4"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    f = urll.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    img_data = requests.get(photo).content
    default_dir = "C:\\Users\\MY COMPUTER\\Downloads\\a_image.png"
    with open(default_dir, 'wb') as handler:
        handler.write(img_data)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, default_dir, 3)
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn ra home xem có đẹp không nha ?")


def parse_thu(today):
    thu = "monday"
    t = "thứ hai"
    if today == 0:
        thu = "monday"
        t = "thứ hai"
    elif today == 1:
        thu = "tuesday"
        t = "thứ ba"
    elif today == 2:
        thu = "wednesday"
        t = "thứ tư"
    elif today == 3:
        thu = "thursday"
        t = "thứ năm"
    elif today == 4:
        thu = "friday"
        t = "thứ sáu"
    elif today == 5:
        thu = "saturday"
        t = "thứ bảy"
    elif today == 6:
        thu = "sunday"
        t = "chủ nhật"
    return [thu, t]


def timetable(text):
    with open('timetable.json', encoding='utf-8') as fh:
        data = json.load(fh)
    # print(len(data['monday']))
    today = date.today().weekday()
    if "now" in text or "nay" in text:
        pass
    elif "mai" in text or "tomorrow" in text:
        today = (today + 1) % 7
    elif "hai" in text or "2" in text:
        today = 0
    elif "ba" in text or "3" in text:
        today = 1
    elif "tư" in text or "4" in text or "bốn" in text:
        today = 2
    elif "năm" in text or "5" in text:
        today = 3
    elif "sáu" in text or "6" in text:
        today = 4
    elif "bảy" in text or "7" in text:
        today = 5
    elif "chủ nhật" in text or "cuối" in text:
        today = 6
    # get data
    aty = parse_thu(int(today))
    thu = aty[0]
    t = aty[1]
    if len(data[thu]) < 1:
        speak("bạn không có lịch gì vào " + t)
    else:
        st = "Đây là thời khóa biểu của "+t+": "
        for x in data[thu]:
            st += x['hour']+" giờ "+x['minute'] + \
                " phút "+"môn "+x['subject']+", "
        speak(st)


def main_brain():
    hello("Hào")
    speak(f"Bạn cần tôi giúp gì không ?")
    while True:
        text = get_text()
        if not text:
            break
        elif ('tạm biệt' in text) or ('hẹn gặp lại' in text):
            stop()
            break
        elif "mấy giờ" in text or "bây giờ" in text or "hôm nay" in text or "hiện tại" in text or "ngày nào" in text:
            get_time(text)
        elif "mở" in text:
            if "trang" in text:
                open_website(text)
            else:
                open_application(text)
        elif 'youtube' in text:
            speak("Bạn muốn tìm kiếm đơn giản hay phức tạp")
            yeu_cau = get_text()
            if "đơn giản" in yeu_cau:
                play_youtube()
                if input():
                    pass
            elif "phức tạp" in yeu_cau:
                play_youtube_2()
                if input("Tiếp tục y/n: ") == "y":
                    pass
        elif "tìm kiếm" in text or "search" in text or "thế nào" in text or "là gì" in text or "khi nào" in text or "ở đâu" in text:
            open_google_and_search(text)
        elif "thời khóa biểu" in text or "khóa biểu" in text or "lịch" in text:
            timetable(text)
        elif "hình nền" in text:
            change_wallpaper()


if __name__ == '__main__':
    main_brain()
