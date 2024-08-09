import os
import re

# Definer mappen som skal skannes
directory_to_scan = os.path.expanduser('~/git/')

# Output-fil for funnene
output_file = os.path.expanduser('~/scan_results.txt')

# Regex-mønstre for å fange opp usynlige Unicode-tegn
invisible_characters_patterns = [
    re.compile(r'[\u200B-\u200D\uFEFF]'),  # Zero Width Characters og BOM
    re.compile(r'[\u00A0\u00AD]'),         # Non-Breaking Space og Soft Hyphen
    re.compile(r'[\u202A-\u202E]'),        # Bidirectional Control Characters
    re.compile(r'[\u2060]'),               # Word Joiner (U+2060)
    re.compile(r'[\uE000-\uF8FF]'),        # Private Use Area (PUA)
]

def scan_file(file_path, output):
    """Skann en enkelt fil for usynlige Unicode-tegn og skriv funnene til output-fil."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            for pattern in invisible_characters_patterns:
                matches = pattern.findall(line)
                if matches:
                    output.write(f"Fil: {file_path}\n")
                    output.write(f"Linje {i}: {line.strip()}\n")
                    output.write(f"Funnet tegn: {matches}\n")
                    output.write(f"{'-'*40}\n")
                    break  # Hvis ett mønster matcher, går vi videre til neste linje

def scan_directory(directory, output):
    """Skann alle filer i et gitt directory rekursivt."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.java', '.html', '.css', '.txt')):  # Juster etter behov
                scan_file(os.path.join(root, file), output)

if __name__ == "__main__":
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(f"Starter skanning av {directory_to_scan}...\n\n")
        scan_directory(directory_to_scan, output)
        output.write("Skanning fullført.\n")
    print(f"Skanningen er ferdig. Resultatene er lagret i {output_file}")
