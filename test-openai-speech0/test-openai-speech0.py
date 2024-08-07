from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define the text for each slide
slides = {
    "Intro": "Welcome back to our channel! Today, we’re diving into an exciting topic in the world of bioinformatics and machine learning: how we can enhance the understanding of protein structures using the VQ-VAE architecture. So, let’s get started!",
    "What is VQ-VAE?": "First, what exactly is VQ-VAE? The Variational Quantized Variational Autoencoder, or VQ-VAE, is a powerful neural network architecture designed for generating discrete representations of data. In our case, it helps in learning accurate structural representations of proteins.",
    "Why Two-Stage Training?": "Now, to maximize reconstruction quality when using VQ-VAE, we typically train the autoencoder in two stages. Here’s how it works:",
    "Decoding with a Small Decoder": "In the first stage, we focus on learning the encoder and the codebook. During this phase, we utilize a relatively small and efficient decoder, which allows us to train quickly while still capturing the essential features of our protein structures.",
    "Enhancing Reconstruction Quality": "Now, moving on to the second stage. Here, we freeze the encoder and codebook that we learned in the first stage, and shift our focus to training a larger and more computationally expensive decoder.",
    "The process": "The overall process helps us to generate what we call structure tokens. Let’s break down how these tokens are created: Local Neighborhood: For each residue in the protein, we find the 16 nearest residues based on the distance between their Cα atoms. Embed Neighbors: We then embed the relative positions of neighbors to retain spatial relationships. Encoding: These neighbors are passed through our VQ-VAE encoder. Quantization: Finally, we extract the first elements from this data, project it linearly, and quantize it to create our discrete structure tokens.",
    "Conclusion": "To sum it all up, the two-stage training approach for the VQ-VAE allows us to effectively learn discrete representations that maximize reconstruction quality for proteins. This method not only enhances accuracy but also provides a robust framework for understanding complex molecular structures.",
    "Outro": "If you found this video insightful, don’t forget to hit the like button and subscribe for more content on bioinformatics and machine learning! Also, if you have any questions or topics you’d like us to cover, drop them in the comments below. Thanks for watching, and we’ll see you next time!"
}

# Iterate through each slide text and create speech output
for title, text in slides.items():
    print(f"Generating speech for: {title}")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    # Specify the filename for the output MP3
    output_file = f"{title.replace(' ', '_').lower()}.mp3"
    response.stream_to_file(output_file)
    print(f"Saved: {output_file}")

print("All audio files generated successfully.")
