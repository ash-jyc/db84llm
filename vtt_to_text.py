import re
import sys

def vtt_to_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    text_lines = []
    for line in lines:
        # Remove WEBVTT headers and other metadata
        if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', line) or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:') or line.strip() == '':
            continue
        # Remove time codes within text
        cleaned_line = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}>', '', line)
        # Remove tags like <c> and </c>
        cleaned_line = re.sub(r'<[^>]+>', '', cleaned_line)
        text_lines.append(cleaned_line.strip())

    plain_text = ' '.join(text_lines)
    plain_text = re.sub(r'\s+', ' ', plain_text).strip()

    # output to txt
    with open("output.txt", "w") as file:
        file.write(plain_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vtt_to_text.py <path_to_vtt_file>")
        sys.exit(1)

    vtt_file = sys.argv[1]
    vtt_to_text(vtt_file)
