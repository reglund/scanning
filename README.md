# Invisible Ghost Vulnerability Scanner

## Overview

This project provides a Python script designed to scan a codebase for hidden Unicode characters, specifically targeting those that could be associated with the "Invisible Ghost" vulnerability in GitHub Copilot. This vulnerability involves invisible characters being introduced into code, potentially leading to security risks that are hard to detect through manual code review.

For more information on the "Invisible Ghost" vulnerability, refer to the original [blog post](https://www.apexhq.ai/blog/blog/invisible-ghost-alarming-vulnerability-in-github-copilot/).

## Features

- **Detects Hidden Unicode Characters**: Scans for characters that are often invisible in standard text editors but can influence the behavior of code.
- **Supports Multiple File Types**: The script is configured to scan Python, JavaScript, Java, HTML, CSS, and text files by default. This can be extended to other file types as needed.
- **Outputs Results to a File**: Generates a well-formatted text report highlighting where invisible characters were found, including the file name, line number, and the affected content.

## Requirements

- **Python 3.x**: Make sure you have Python 3 installed on your system.

## Installation

To get started with the Invisible Ghost Vulnerability Scanner:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd your-repository-name
    ```
3. **Ensure Python 3 is Installed**:
    Make sure that Python 3 is installed on your machine. You can check this by running:
    ```bash
    python3 --version
    ```

## Usage

To scan your codebase for hidden Unicode characters:

1. Place all the repositories you want to scan in the `~/git/` directory, or modify the script to point to the directory of your choice.

2. Run the script:
    ```bash
    python3 scan_invisible_ghost_to_file.py
    ```

3. The script will output a report named `scan_results.txt` in your home directory. This file will contain detailed information about any hidden characters found in your codebase, including:
   - File paths where the characters were detected
   - Line numbers within those files
   - The actual lines containing the invisible characters

## Customization

- **File Types**: By default, the script scans `.py`, `.js`, `.java`, `.html`, `.css`, and `.txt` files. You can customize the script to include other file types by modifying the file extensions in the script's `scan_directory()` function.
- **Additional Unicode Patterns**: If you need to search for other types of hidden characters, you can expand the regex patterns in the `invisible_characters_patterns` list.

## Example Output

Here is an example of what the output might look like in `scan_results.txt`:
 ```bash
File: /home/user/git/project/src/main.py
Line 42: def my_function():​ # Invisible character detected here
Found characters: ['\u200B']
File: /home/user/git/project/index.html
Line 10: <p>​This is an example paragraph.</p>
Found characters: ['\u200B']
 ```

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [Invisible Ghost: Alarming Vulnerability in GitHub Copilot](https://www.apexhq.ai/blog/blog/invisible-ghost-alarming-vulnerability-in-github-copilot/)
