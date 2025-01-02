import json
import glob

def create_structure():
    filenames = ["一东","二冬", "三江", "四支", "五微", "六鱼", "七虞", "八齐", "九佳", "十灰", "十一真", "十二文", "十三元", "十四寒", "十五删",
                "一先","二萧", "三肴", "四豪", "五歌", "六麻", "七阳", "八庚", "九青", "十蒸", "十一尤", "十二侵", "十三覃", "十四盐", "十五咸"]
    for i in range(len(filenames)):
        filename =  f"{filenames[i]}.txt"
        with open  (filename, 'w') as f:
            pass                # empty file

def calculate_stats():
    #read all .json files in this folder/including its subfolders
    files = glob.glob('./**/dataset/*.json', recursive=True)
    total_couplets = 0
    total_files = 0
    total_words = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            total_files += 1
            total_couplets += len(data)
            for line in data:
                for key in line:
                    total_words += len(line[key])
    print(f"Total files: {total_files}")    
    print(f"Total couplets: {total_couplets}")
    print(f"Total words: {total_words}")

if __name__ == "__main__":
    calculate_stats()