# Podcast Transcription Summarizer

This script automates the process of transcribing podcast episodes, generating summarized transcripts, and saving the results. It utilizes the OpenAI API and Python's `glob` module to achieve this.

## Prerequisites

- Python 3.6 or later
- An OpenAI API key
- Install required Python packages using the following command:

  ```bash
pip install openai

## Getting Started

Clone this repository:
Set up your OpenAI API key as an environment variable:

  ```bash
export OPENAI_API_KEY=your-api-key

Organize your podcast audio files in the ./podcasts/ directory. Supported audio format: .m4a. It's recommend to have the podcasts with AAC HE-V2 Audio to stay below whisper's file size limit of 25mb.
Usage

The script will iterate through the podcast files in the ./podcasts/ directory, transcribe them, and generate a summarized transcript using the OpenAI GPT-3.5 Turbo model.
Summarized transcripts will be saved in the ./results/ directory with the corresponding podcast number as the filename.

You can adjust the temperature parameter in the generate_corrected_transcript function to control the creativity of the generated summary.
Modify the system_prompt to tailor the instructions for summarizing according to your specific needs.