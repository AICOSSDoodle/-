directory 에 한국어 텍스트 파일이 저장된 폴더 주소 지정 필요

(한시간)(1시간) ------------> 1시간 or 한시간으로 처리

stop_words_final = ["/(bgm)", "/(idiom)","@웃음","/(noise)",'@','/','idiom'] ----------->  와 같이 반복되는 쓸모없는 단어들 제거

def remove_special_characters(text):
    pattern = r'[^0-9a-zA-Z가-힣\s]'  ------------->  숫자, 알파벳, 한국말를 제외한 모든 문자를 제거하기 위해 사용


def delete_existing_files(directory):        ----------------> 기존 _cleand3.txt 말고 모든 파일 삭제
    for filename in os.listdir(directory):
        if filename.endswith("_cleaned3.txt"):
            pass
        
        else:
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"{filename} 파일을 삭제했습니다.")
