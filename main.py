import os
import glob
import openai


def generate_corrected_transcript(temperature, system_prompt, audio_transcription):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }, 
        {
            "role": "user",
            "content": audio_transcription
        },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",  # Replace with the correct model name
        temperature=temperature,
        messages=messages
    )
    return response['choices'][0]['message']['content']


# Execute
if __name__ == '__main__':
    # Read the API key from ENV variable
    openai.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")

    # Get all m4a files from the podcasts folder
    podcast_list = glob.glob("./podcasts/*.m4a")
    # Sort the podcast list
    podcast_list.sort()

    for podcast in podcast_list:
        # Get the file name without path and extension
        podcast_number = podcast.split("/")[-1].split(".")[0]
        print(podcast_number)
        # Skip the podcast if the result already exists
        if glob.glob("./results/{}.txt".format(podcast_number)):
            print("Skipping {}...".format(podcast_number))
            continue
        audio_file_path = podcast
        with open(audio_file_path, "rb") as audio_file:
            audio_transcription = openai.Audio.transcribe(
                file=audio_file, model='whisper-1')
        
        with open("./transcripts/{}.txt".format(podcast_number), "w") as text_file:
            text_file.write(audio_transcription['text'])

        print("Transcription completed!")

        system_prompt = "As a helpful assistant for the podcast host, your task is to review the provided podcast transcription and summarize the podcast episode in a brief and clear manner. Provide the top three key facts and the most important learnings from the discussion. Be concise, accurate, and focus on delivering high-quality content."

        output = generate_corrected_transcript(
            temperature=0.3, 
            system_prompt=system_prompt, 
            audio_transcription=audio_transcription['text'])

        # Save the corrected transcript to a text file
        # Set the name of the output file to the podcast number
        with open("./results/{}.txt".format(podcast_number), "w") as text_file:
            text_file.write(output)

        # Print a progress message
        print("Summary completed!")