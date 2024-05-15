import os
def split_text(text, max_length=5000):
    chunks = []
    current_chunk = ""
    for word in text.split():
        if len(current_chunk) + len(word) + 1 <= max_length:
            current_chunk += word + " "
            if word.endswith("요") or word.endswith("다"):
                chunks.append(current_chunk.strip())
                current_chunk = ""
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def split_text_file(input_file, output_directory, max_length=5000):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
        current_length = 0
        current_text = ''
        file_count = 1
        # Get the base name of the input file
        base_name = os.path.basename(input_file).split('.')[0]
        for section in split_text(text, max_length):
            if current_length + len(section) > max_length:
                with open(os.path.join(output_directory, f'{base_name}_output_{file_count}.txt'), 'w', encoding='utf-8') as output_file:
                    output_file.write(current_text)
                current_text = section
                current_length = len(section)
                file_count += 1
            else:
                current_text += ' ' + section
                current_length += len(section) + 1
        if current_text:
            with open(os.path.join(output_directory, f'{base_name}_output_{file_count}.txt'), 'w', encoding='utf-8') as output_file:
                output_file.write(current_text)

def process_multiple_txt_files(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            split_text_file(os.path.join(input_directory, filename), output_directory)

# Call the function to process multiple txt files
# Note: Replace 'input_directory' with the actual directory containing the txt files
# Replace 'output_directory' with the actual directory where you want to save the output files
directory = "C:/Users/강문성/Documents/파이썬 코드/Validation/인터넷방송/생활3"  #파일 불러오는 장소지정
directory2 = "C:/Users/강문성/Documents/파이썬 코드/Validation/인터넷방송/생활3_splited"  #분할된 파일 저장 장소지정
#공중파방송
#기타녹음
#라디오
#인터넷방송

#경제3
#교육3
#문화3
#사회3
#생활3
#세계3
#스포츠3
#연예3
#의료3
#정치3

#경제3_splited
#교육3_splited
#문화3_splited
#사회3_splited
#생활3_splited
#세계3_splited
#스포츠3_splited
#연예3_splited
#의료3_splited
#정치3_splited
process_multiple_txt_files(directory, directory2)
# Print a success message
print("각 파일당 5000자 이하로 쪼개서 출력되었습니다! 😊")

