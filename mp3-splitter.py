# mp3-splitter.py
from pydub import AudioSegment
import os

def split_mp3(input_file, output_dir, snippet_length_minutes):
    # Create the output directory inside the input directory
    output_dir = os.path.join(input_dir, "output")
    os.chmod(output_dir, 0o777)
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the input MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Calculate the length of snippets in milliseconds
    snippet_length_ms = snippet_length_minutes * 60 * 1000

    # Initialize the starting and ending positions for slicing
    start_time = 0
    end_time = snippet_length_ms

    # Initialize snippet count
    snippet_count = 1

    while end_time <= len(audio):
        # Extract the snippet
        snippet = audio[start_time:end_time]

        # Define the output file name
        output_file = os.path.join(output_dir, f'snippet_{snippet_count}.mp3')

        # Export the snippet as an MP3 file
        snippet.export(output_file, format="mp3")

        # Update start and end times for the next snippet
        start_time = end_time
        end_time = start_time + snippet_length_ms

        # Increment the snippet count
        snippet_count += 1

    print(f"Split {snippet_count - 1} snippets from {input_file}.")

if __name__ == "__main__":
    input_dir = input("Enter the path to the input directory containing the MP3 file: ")
    input_file = os.path.join(input_dir, input("Enter the name of the input MP3 file: "))
    snippet_length_minutes = float(input("Enter the snippet length in minutes: "))

    split_mp3(input_file, input_dir, snippet_length_minutes)
