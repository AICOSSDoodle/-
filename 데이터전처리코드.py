import os
import glob
import re
def extract_repeated_content(text):
    # 정규식을 사용하여 괄호 안의 내용을 찾습니다.
    pattern = r'\((.*?)\)'
    matches = re.findall(pattern, text)
    
    # 마지막 매치를 반환합니다 (마지막 괄호 쌍 안의 내용)
    if matches:
        return matches
    else:
        return None
    

def split_text_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
        result = extract_repeated_content(text)


        #문자열 공백 제거
        cleaned_list_result = [item.strip() for item in result]
        #print(cleaned_list_result)

        # () 기준으로 나누기
        result2 = re.split(r'\(|\)', text)

        # 빈 문자열 제거
        result3 = [item.strip() for item in result2 if item.strip()]

        remove_words = cleaned_list_result[0::2]
        keep_words = cleaned_list_result[1::2]
        #print(list(set(remove_words)))
        #print(list(set(keep_words)))
        remove_words = list(set(remove_words))
        keep_words = list(set(keep_words))     
        g=result3[:]
        #print(len(g))
        #print(g)
        g= [i for i in g if i not in remove_words]

        #결과 출력
        h=" ".join(g)

        return h



#directory = "C:/Users/강문성/Documents/파이썬 코드/TS7교육"

#_cleaned_cleaned.txt
#공중파방송
#기타녹음
#라디오
#인터넷방송

#경제
#교육
#문화
#사회
#생활
#세계
#스포츠
#연예
#의료
#정치
directory = "C:/Users/강문성/Desktop/TS/TS6_사회_인방"
#TS3경제
#TS3교육
#TS3문화
#TS3사회
#TS3생활
#TS3세계
#TS3스포츠
#TS4연예
#TS4의료
#TS4정치
stop_words_final = ["/(bgm)", "/(idiom)","@웃음","/(noise)",'@','/','idiom']

# 디렉토리 내의 모든 텍스트 파일을 처리
for file_name in glob.glob(os.path.join(directory, '*.txt')):
    texttt = split_text_file(file_name)
    # 결과를 새 파일에 저장
    with open(file_name.replace('.txt', '_cleaned.txt'), 'w', encoding='utf-8') as out_file:
        out_file.writelines(texttt)
print("같은의미의 단어를 제거하였습니다")

def remove_special_characters(text):
    pattern = r'[^0-9a-zA-Z가-힣\s]'  # 알파벳과 숫자를 제외한 문자를 찾는 정규표현식
    special_chars = re.findall(pattern, text)
    special_chars = list(set(special_chars))
    return special_chars


# 디렉토리 내의 모든 텍스트 파일을 처리
for file_name in glob.glob(os.path.join(directory, '*_cleaned.txt')):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 각 라인에서 필요없는 단어를 제거
    modified_lines = []
    for line in lines:
        for word in stop_words_final:
            line = line.replace(word, "")

        out_list = remove_special_characters(line)

        for word in out_list:
            line = line.replace(word, "")

        modified_lines.append(line)
    unifed_lines = " ".join(modified_lines)

    # 결과를 새 파일에 저장
    with open(file_name.replace('.txt', '3.txt'), 'w', encoding='utf-8') as file:
        file.writelines(unifed_lines)
print("필요없는 단어를 제거하였습니다")

def delete_existing_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith("_cleaned3.txt"):
            pass
        
        else:
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"{filename} 파일을 삭제했습니다.")

# 사용 예시

delete_existing_files(directory)

print("전처리 전 기존 텍스트 파일들을 모두 제거하였습니다")