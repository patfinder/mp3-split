# MP3 Split

The MP3 Splitter is a Python script that allows you to split a large MP3 audio file into smaller snippets of a specified duration. This can be useful for creating shorter segments from long audio recordings, such as podcasts, lectures, or music tracks.

## Prerequisites

Before running the script, make sure you have Python and the required library installed. You can install the necessary library using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Additionally, you need to have FFmpeg installed on your system. If you don't have FFmpeg installed, you can install it via Homebrew (on macOS) with the following command:

```bash
brew install ffmpeg
```

## Usage

1. **Clone the Repository**: Download or clone this repository to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `mp3_splitter.py` script is located.

3. **Run the Script**: Execute the script by running the following command:

```bash
python mp3_splitter.py
```

4. **Provide Input**:

- Enter the path to the input MP3 file when prompted. This should be the full path to the MP3 file you want to split.
- Enter the output directory path where the smaller MP3 snippets will be saved.
- Specify the desired snippet length in minutes.

5. **Splitting Process**: The script will split the input MP3 file into smaller snippets of the specified length and save them in the output directory. Progress will be displayed in the terminal.

6. **Completed**: Once the script has finished splitting the MP3 file, it will display the number of snippets created and provide a summary.
