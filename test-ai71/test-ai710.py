import os
import re
import sys
import openai
from ai71 import AI71
from pprint import pprint

AI71_BASE_URL = "https://api.ai71.ai/v1/"
AI71_API_KEY = os.getenv('AI71_API_KEY')

client = AI71(AI71_API_KEY)

def process_file(file_path, output_file, full_output_file):
    with open(file_path, 'r') as file:
        input_content = file.read()
        #paragraphs = input_content.split(".")
        paragraphs = input_content.split("\n\n")
        #size = 100
        #paragraphs = [input_content[i:i + size] for i in range(0, len(input_content), size)]
        
        for paragraph in paragraphs:
            full_output_file.write("\n==============================\n")
            full_output_file.write(paragraph)
            print("\n==============================\n")
            print(paragraph)
            chat_completion = (client.chat.completions.create(
                model="tiiuae/falcon-180b-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Please explain this in detail for a scientist but non-expert in this field.  Please explain any terms that would be unfamilar to a layperson : " + paragraph}
                ],
            ))
            full_output_file.write("\n------------------------------\n")
            print("\n------------------------------\n")

            for choice in chat_completion.choices:
                content = choice.message.content
                output_content = content
                # output_content = "\n".join([f"[[{name.strip().lower().replace(' ', '_')}|{name.strip()}]]" for name in content.split('\n')])                
                output_file.write(output_content)
                output_file.write("\n\n")
                full_output_file.write(output_content)
                print(output_content,flush=True)
                output_file.flush()
                full_output_file.flush()

def main():
    if len(sys.argv) > 1:
        input_file_list = sys.argv[1]
        print(f"The first command-line argument is: {input_file_list}")
    else:
        print("No command-line arguments were provided.")
        exit()

    with open(input_file_list, 'r') as file:
        file_paths = file.read().splitlines()

    for file_path in file_paths:
        if os.path.isfile(file_path):
            print(f"Processing {file_path}...")
            output_file_path = f"{os.path.splitext(file_path)[0]}.out26.md"
            full_output_file_path = f"{os.path.splitext(file_path)[0]}.full26.md"
            output_file = open(output_file_path, 'w')
            full_output_file = open(full_output_file_path, 'w')
            process_file(file_path, output_file, full_output_file)
            
            print(f"Output saved to {output_file_path}")
        else:
            print(f"File {file_path} does not exist. Skipping.")

if __name__ == "__main__":
    main()
