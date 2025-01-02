import json
import sys
import re
import os

## 训蒙骈句
def process_text(input_text):
    # Split text into lines and remove empty lines
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]
    print(f'# of lines detected: {len(lines)}')
    results = []
    
    for line in lines:
        # Skip lines that are just punctuation or whitespace
        if re.match(r'^[　\s\u3000,.。，；;]+$', line):
            continue
            
        sentences = line.split('。')
        # remove empty strings
        sentences = [sentence for sentence in sentences if sentence]
        assert len(sentences) ==5, f"Error: Expected 5 sentences per line, but got {len(sentences)} sentences"
        
        for i in range(len(sentences)):
            if i < 4:
                couplets = sentences[i].split('，')
                results.append({'0': couplets[0], '1': couplets[1]})
            if i== 4:
                couplets = sentences[-1].split('；')
                results.append({'0': couplets[0], '1': couplets[1]})

    return results

def main():
    base_foldername = './原文'
    # loop through the files in the folder
    files = os.listdir(base_foldername)
    assert len(files) == 30, f"Error: Expected 30 files, but got {len(files)} files"

    for filename in files:
        # Get the base filename (without extension)
        base_filename = filename.split('.')[0]

        input_filename = f"{base_foldername}/{base_filename}.txt"
        output_filename = f"dataset/{base_filename}.json"
        try:
            # Check if input file exists
            if not os.path.exists(input_filename):
                print(f"Error: Input file {input_filename} not found")
                sys.exit(1)
            print(f"Processing {input_filename}...")

            # Read input from text file
            with open(input_filename, 'r', encoding='utf-8') as f:
                input_text = f.read()

            # Process the text
            result = process_text(input_text)

            # Write to JSON file
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)

    print(f"Successfully processed {base_foldername}.")

if __name__ == "__main__":
    main()