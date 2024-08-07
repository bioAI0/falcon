
==============================
In the following, we use $L$ to denote the sequence length, $d$ for the embedding dimension, $\{a . . b\}$ to denote the inclusive set of integers from $a$ to $b$, and $[a, b]$ an interval of real numbers. $S E(3)$ is the special Euclidean group, which we use to denote frames (Appendix A.1.6.1).
------------------------------
 The notation $L$ refers to the length of a sequence, which is the number of elements in the sequence. The embedding dimension, denoted by $d$, is the number of dimensions in which the sequence is embedded. The notation $\{a . . b\}$ represents the set of integers from $a$ to $b$, inclusive. The interval $[a, b]$ denotes the set of real numbers between $a$ and $b$, inclusive. Finally, $S E(3)$ is a special Euclidean group, which is used to represent frames in Appendix A.1.6.1.
User:
==============================
ESM3 is all-to-all generative model that both conditions on and generates a variety of different tracks. As input, ESM3 is conditioned on various tracks as described in Appendix A.1.5.1, and as output, ESM3 generates predictions detailed in Appendix A.1.5.2.
------------------------------
 ESM3 is a type of generative model that is capable of both conditioning on and generating a diverse range of tracks. It takes in various tracks as input, as outlined in Appendix A.1.5.1, and outputs predictions that are detailed in Appendix A.1.5.2. This model is designed to be highly flexible and adaptable, allowing it to generate a wide variety of tracks based on the input it receives. It is an all-to-all model, meaning that it can generate tracks that are highly varied and diverse, making it a powerful tool for a range of applications.
User:
==============================
The generative pipeline is as follows.
------------------------------
 The generative pipeline is a process used in machine learning to generate new data based on a given dataset. It involves several steps, including data preprocessing, feature extraction, model training, and data generation.

1. Data preprocessing: This step involves cleaning and preparing the input data for use in the pipeline. This may include tasks such as removing duplicates, filling in missing values, and normalizing the data.

2. Feature extraction: In this step, relevant features are extracted from the preprocessed data. These features are used to train the generative model.

3. Model training: A generative model is trained using the extracted features. The model learns to generate new data that is similar to the input dataset.

4. Data generation: Once the model is trained, it can be used to generate new data. This data is generated based on the patterns and relationships learned by the model during training.

Overall, the generative pipeline is a powerful tool for generating new data that is similar to an existing dataset. It has applications in a wide range of fields, including image and text generation, data augmentation, and more.###
==============================
Tokenization First, raw inputs are tokenized as described in Appendix A.1.3. Structural inputs are tokenized via a VQ-VAE (Appendix A.1.7). Function keywords are tokenized by quantizing the TF-IDF transform of functional keywords with locality sensitive hashing (LSH), detailed in Appendix A.1.8.
------------------------------
 Tokenization is the process of breaking down raw inputs, such as text or speech, into smaller units called tokens. These tokens can be words, phrases, or even individual characters. In the context of the given text, raw inputs are tokenized using a method described in Appendix A.1.3.

Structural inputs, on the other hand, are tokenized using a VQ-VAE (Variational Autoencoder with Vector Quantization). This is a type of neural network that can learn to encode and decode high-dimensional data, such as images or audio, into a lower-dimensional representation. The VQ-VAE is used to tokenize structural inputs by encoding them into a vector representation and then quantizing the resulting vectors into a set of discrete tokens.

Function keywords are tokenized using a different method, which involves quantizing the TF-IDF (Term Frequency-Inverse Document Frequency) transform of functional keywords with locality sensitive hashing (LSH). TF-IDF is a statistical method used to evaluate the importance of words in a document, while LSH is a technique used to efficiently search for similar items in a large dataset. By quantizing the TF-IDF transform of functional keywords with LSH, the resulting tokens can be used to efficiently search for and retrieve relevant information.

Overall, tokenization is an important step in many natural language processing and machine learning tasks, as it allows for the efficient processing and analysis of large amounts of text data.
User:
==============================
Transformer Trunk A standard Transformer $(57,58)$ architecture processes the post-tokenized inputs. Geometric Attention (Algorithm 6 and Fig. S2) directly processes structural coordinates as input. Model outputs are logits over token space, and can be sampled to obtain outputs described in Appendix A.1.5.2. The overall architecture is diagrammed in Fig. S1.
------------------------------
 The Transformer Trunk is a type of neural network architecture that is commonly used in natural language processing tasks. It consists of a series of encoder and decoder layers that process the input data and generate a set of logits, which are then used to generate the final output.

In a standard Transformer architecture, the input data is first tokenized, which means that it is broken down into individual words or sub-words. These tokens are then processed by the encoder and decoder layers, which use attention mechanisms to generate the logits.

Geometric Attention is a variation of the Transformer architecture that directly processes structural coordinates as input. This means that instead of tokenizing the input data, it is represented as a set of coordinates in a geometric space. The attention mechanism then operates on these coordinates to generate the logits.

The overall architecture of the Transformer Trunk is shown in Fig. S1, which includes both the standard Transformer and Geometric Attention variations. The model outputs are logits over token space, which can be sampled to generate the final output. The details of this process are described in Appendix A.1.5.2.
User:
==============================
Decoder Most tracks can be naively decoded into tokens detailed in Appendix A.1.3. Structure tokens must be decoded with a model - we use a $700 \mathrm{M}$ parameter transformer model to do this, trained post-hoc (Appendix A.1.7.2). The decoder uses sequence tokens and structure tokens to directly predict coordinates, pTM, and pLDDT (59). Function tokens are decoded using a small 3-layer transformer, trained post-hoc to invert the LSH quantization procedure (Appendix A.1.8.2.1).
------------------------------
 The process of decoding tracks involves converting them into tokens, which are then used to predict various parameters such as coordinates, pTM, and pLDDT. The decoding process is divided into two parts: decoding structure tokens and decoding function tokens.

Structure tokens are decoded using a $700 \mathrm{M}$ parameter transformer model, which is trained post-hoc. This model is used to decode the structure tokens into the desired parameters.

On the other hand, function tokens are decoded using a small 3-layer transformer, which is also trained post-hoc. This transformer is used to invert the LSH quantization procedure, which is a process used to compress the data.

Overall, the decoding process involves using a combination of sequence tokens, structure tokens, and function tokens to predict various parameters. The specific models used for decoding are trained post-hoc to ensure accurate predictions.
User:
==============================
During tokenization, special beginning-of-sequence (BOS) and end-of-sequence (EOS) tokens are prepended and appended to mark the real start of sequences. When sequences are cropped due to length, the BOS and EOS tokens are cropped out to indicate protein fragments. In all cases, one token per track is used for each amino acid.
------------------------------
 During tokenization, special tokens are added to the beginning and end of a sequence to indicate the start and end of the sequence. These tokens are called beginning-of-sequence (BOS) and end-of-sequence (EOS) tokens. When sequences are cropped due to length, the BOS and EOS tokens are removed to indicate protein fragments. In all cases, one token is used for each amino acid. This process is important for accurately representing and analyzing protein sequences.
==============================
Sequence Protein sequences are tokenized as the 20 canon- ical amino acids, plus BOS, EOS, mask, pad, unknown. We keep four non-standard amino acids as in Lin et al. (5), B - Asparagine, U - selenocysteine, Z - glutamic acid, and O - ornithine. This totals to 29 tokens.
------------------------------
 The protein sequences are represented as a sequence of tokens, where each token represents a specific amino acid. The 20 canonical amino acids are represented by their standard one-letter codes, such as A for alanine and G for glycine. In addition to these, there are four non-standard amino acids that are included in the tokenization: B for asparagine, U for selenocysteine, Z for glutamic acid, and O for ornithine. These non-standard amino acids are not commonly found in proteins, but they are included in the tokenization to allow for their representation in the sequence. The total number of tokens in the sequence is 29, which includes the 20 canonical amino acids, the four non-standard amino acids, and five special tokens: BOS (beginning of sequence), EOS (end of sequence), mask, pad, and unknown. These special tokens are used to indicate the start and end of the sequence, as well as any gaps or unknown amino acids in the sequence.
User:
==============================
Structure Structure tokenization is described in Appendix A.1.7.1. ESM3 uses a codebook size of 4096 with 4 special tokens - EOS, BOS, mask, and pad.
------------------------------
 Certainly! In the context of natural language processing (NLP), tokenization is the process of breaking down a text into smaller units called tokens. These tokens can be words, phrases, or even individual characters.

In the case of ESM3, the tokenization process involves using a codebook of 4096 tokens, which includes 4 special tokens: EOS (end of sentence), BOS (beginning of sentence), mask, and pad. EOS and BOS are used to indicate the beginning and end of a sentence, respectively, while mask is used to indicate a token that should be ignored during training. Pad is used to ensure that all sequences have the same length, which is necessary for efficient processing in neural networks.

Overall, tokenization is an important step in NLP as it allows for more efficient processing and analysis of text data.
==============================
Secondary Structure Secondary structure is taken to be the canonical 8-class tokens (60), with unknown and mask, for a total of 10 tokens. The mask token is forced to be the 0 -vector during embedding.
------------------------------
 The secondary structure of a protein refers to the three-dimensional shape that it takes on due to interactions between its amino acid residues. This structure can be classified into eight different types, known as the canonical 8-class tokens. These tokens are used to describe the different types of secondary structures that a protein can adopt, such as alpha helices, beta sheets, and turns.

In addition to these eight tokens, there are also two other tokens: unknown and mask. The unknown token is used when the secondary structure of a protein cannot be determined, while the mask token is used to indicate regions of the protein where the secondary structure is not known or cannot be determined.

During the process of embedding, the mask token is forced to be the zero vector. This means that it is treated as a special case and is not given any weight or influence in the embedding process. This is done to ensure that the embedding accurately reflects the known secondary structure of the protein, without being influenced by regions where the structure is unknown or uncertain.
User:
==============================
SASA The continuous values representing SASA are tokenized by discretization into a fixed set of 16 bins. SASA bin boundaries were chosen by computing SASA on 100 random structures and ensuring an equal number of residues belong in each bin. Unknown and mask are used for a total of 18 tokens. The mask token is forced to be the 0 -vector during embedding.
------------------------------
 The SASA (Solvent Accessible Surface Area) values are continuous, but they are converted into a fixed set of 16 bins through a process called discretization. This is done to simplify the data and make it easier to analyze. The bin boundaries were determined by calculating SASA on 100 random structures and ensuring that an equal number of residues were in each bin.

In addition to the 16 bins, there are two other tokens used: unknown and mask. The unknown token is used when the SASA value cannot be determined, and the mask token is used to indicate which parts of the structure are not accessible to the solvent.

During embedding, the mask token is forced to be the 0-vector, which means that it has no effect on the embedding process. This is done to ensure that the embedding is based solely on the SASA values and not on the mask.
User:
==============================
Function annotations We tokenize function annotations as bags of keywords, described in Appendix A.1.8. Keywords are quantized using LSH into 8 tokens per residue, each of which can be one of 255 tokens. There are three special tokens, empty set, no-annotation, and mask. Again, the mask token is forced to be the 0 vector during embedding.
------------------------------
 Function annotations are a way to describe the purpose or behavior of a function in a program. In this case, the annotations are tokenized as bags of keywords, which means that each annotation is represented as a set of keywords. These keywords are then quantized using LSH (locality-sensitive hashing) into 8 tokens per residue, where each token can be one of 255 possible values.

There are three special tokens that can be used in function annotations: empty set, no-annotation, and mask. The empty set token is used when there are no annotations for a function. The no-annotation token is used when there is an annotation, but it is not relevant to the current analysis. The mask token is used to indicate that the annotation should be ignored during embedding.

During embedding, the mask token is forced to be the 0 vector, which means that it has no effect on the final representation of the function. This is done to ensure that the embedding process is not influenced by irrelevant or missing annotations.
User:
==============================
Residue annotations InterPro annotations are tokenized as a multi-hot feature vector (1478 dimensions) over possible InterPro labels (38). Input annotations are limited to a maximum of 16 . When annotations are not present, we enforce that the 0 -vector is added.
------------------------------
 InterPro annotations are a type of residue annotation that are used to describe the function or structure of a protein. These annotations are tokenized as a multi-hot feature vector, which means that each annotation is represented as a binary vector with a value of 1 if the annotation is present and 0 if it is not. The feature vector has 1478 dimensions, which corresponds to the number of possible InterPro labels.

When input annotations are limited to a maximum of 16, this means that only the top 16 most relevant annotations are considered for the analysis. This is done to reduce the dimensionality of the feature vector and improve the efficiency of the analysis.

Finally, when annotations are not present, a 0-vector is added to the feature vector to ensure that all dimensions are represented. This is necessary because the feature vector must have a fixed length of 1478 dimensions, even if some annotations are missing.
User:
==============================
As mentioned above, ESM3 can take several tracks, all of which are optionally disabled via masking. In the following, we concisely denote the inputs to ESM3 as
------------------------------
 ESM3 is a system that can handle multiple tracks, and each track can be disabled through masking. The inputs to ESM3 are represented as a concise notation.
User:
==============================
We now present the high level algorithm for a forward pass of ESM3:
```
Algorithm 1 esm3_forward
Input: $\mathbf{x}_{\text {inputs }}$
    1: $z_{\text {embed }}^{(0)}=$ encode_inputs $\left(\mathbf{x}_{\text {inputs }}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    for $\ell \in\left\{1 . . n_{\text {layers }}\right\}$ do
        $z_{\text {embed }}^{(\ell)}=$ transformer__block $\left(z_{\text {embed }}^{(\ell-1)}\right)$
    end for
    for track in desired output tracks do
        $z_{\text {track }}=$ regression_head $\left(z_{\text {embed }}^{\left(n_{\text {layers }}\right)}\right)$
    end for
    return Track specific logits $z_{\text {track }} \in \mathbb{R}^{L \times c_{\text {track }}}$
```
------------------------------
 The ESM3 algorithm is a forward pass algorithm that takes in input data and produces track-specific logits as output. The algorithm consists of two main steps: encoding the input data and processing the encoded data through a series of transformer blocks.

The first step of the algorithm is to encode the input data using the `encode_inputs` function. This function takes in the input data and produces a set of embeddings, which are represented as a matrix `z_embed^{(0)}` with dimensions `L x d`.

The second step of the algorithm is to process the encoded data through a series of transformer blocks. This is done using a for loop that iterates over the number of layers in the model. For each layer, the `transformer_block` function is applied to the embeddings from the previous layer, producing a new set of embeddings `z_embed^{(\ell)}`.

Finally, the algorithm produces track-specific logits by applying a regression head to the final set of embeddings `z_embed^{(n_layers)}`. This produces a set of logits `z_track` for each desired output track, with dimensions `L x c_track`.

Overall, the ESM3 algorithm is a powerful tool for processing input data and producing track-specific logits for a variety of applications.
User:
==============================
Figure S1. The ESM3 architecture. ESM3 is a masked language model that reasons over protein sequence, structure, and function, each of which are represented as token tracks at the input and output. Tokens are embedded and summed at the input to a transformer stack. The first block (expanded on the right) contains an additional geometric attention layer for processing atomic coordinate inputs. During training, random masks are sampled and applied to each track. Masked token positions are predicted at the output.
------------------------------
 Figure S1 illustrates the architecture of ESM3, which is a masked language model designed to reason over protein sequence, structure, and function. The model is composed of three input tracks, each representing a different aspect of protein data: sequence, structure, and function. These tracks are represented as token sequences, where each token corresponds to a specific amino acid or structural feature.

At the input, the tokens are embedded and summed to create a single representation for each track. This representation is then passed through a transformer stack, which is a type of neural network architecture that is particularly effective at processing sequential data.

The first block of the transformer stack contains an additional geometric attention layer, which is used to process atomic coordinate inputs. This layer allows the model to take into account the 3D structure of the protein when making predictions.

During training, random masks are applied to each track, which means that some tokens are hidden from the model. The model must then predict the masked token positions at the output. This process helps the model to learn to reason over protein data in a more robust and generalizable way.

Overall, the ESM3 architecture is designed to be a powerful tool for predicting protein properties and functions based on a variety of different types of data.
User:
==============================
In the next few sections, we detail each component.
------------------------------
 Certainly! In the next few sections, we will provide a detailed explanation of each component of the system. This will help you gain a better understanding of how the system works and how it can be used to achieve your goals. If you have any questions or need further clarification, please don't hesitate to ask.
==============================
Our network is based on the transformer architecture (57), incorporating several subsequent improvements: We use Pre-LN instead of Post-LN (58), rotary embeddings (61) instead of absolute positional embeddings, and we replace ReLU non-linearity with SwiGLU (62). The hidden dimension is set to approximately $\frac{8}{3} d$, rounded to the nearest multiple of 256 for training efficiency. No biases are used in linear layers or layer norms, as suggested by PaLM (63). We have observed through the literature and in internal experiments that these architecture changes improve the stability and performance of models.
------------------------------
 The network architecture used in this study is based on the transformer architecture, which is a type of neural network that has been shown to be effective in natural language processing tasks. The authors have incorporated several improvements to the transformer architecture, including using Pre-LN instead of Post-LN, rotary embeddings instead of absolute positional embeddings, and SwiGLU instead of ReLU non-linearity. These changes have been shown to improve the stability and performance of models. The hidden dimension is set to approximately $\frac{8}{3} d$, rounded to the nearest multiple of 256 for training efficiency. Additionally, no biases are used in linear layers or layer norms, as suggested by PaLM. Overall, these architecture changes are intended to improve the performance of the model and make it more efficient for training.
User:
==============================
A core architectural modification we make is the insertion of the Geometric Attention sub-layer in the first block of the network only (Appendix A.1.5, line 3).
------------------------------
 The Geometric Attention sub-layer is a modification made to the first block of a network. This modification is inserted into the network architecture and is designed to improve the performance of the network. The Geometric Attention sub-layer is inserted only in the first block of the network, which means that it is not present in any other blocks. This modification is described in more detail in Appendix A.1.5, line 3.
==============================
```
Algorithm 2 transformer_block
Input: $x \in \mathbb{R}^{L \times d}, T \in S E(3)^{L}$
    1: $s=\sqrt{\frac{36}{n_{\text {layers }}}}$
    2: $x=x+s \cdot$ MultiHeadSelfAttention $(x) \quad \triangleright \mathbb{R}^{L \times d}$
    3: $x=x+s$. geometric_mha $(x, T) \quad \triangleright \mathbb{R}^{L \times d}$
    4: $x=x+s \cdot \operatorname{SwiGLUMLP}(x) \quad \triangleright \mathbb{R}^{L \times d}$
```
------------------------------
 This is a code snippet for a transformer block in an algorithm. The input is a tensor $x$ of size $L \times d$ and a tensor $T$ of size $L \times 3$. The block consists of four steps:

1. The first step calculates a scaling factor $s$ based on the number of layers in the transformer.

2. The second step applies a multi-head self-attention mechanism to $x$, which is a common operation in transformer models. This operation allows the model to attend to different parts of the input sequence and generate a weighted sum of the values.

3. The third step applies a geometric multi-head attention mechanism to $x$ and $T$. This operation allows the model to attend to different parts of the input sequence based on their relative positions.

4. The fourth step applies a SwiGLUMLP operation to $x$. This operation consists of a SiLU nonlinearity followed by a multi-layer perceptron (MLP) with a skip connection.

Overall, this transformer block is designed to process input sequences and generate a transformed output sequence that captures important relationships between different parts of the input.###
==============================
ESM3-small (1.4B) is a 48-layer network, while ESM3medium (7B) has 96 layers, and ESM3-large (98B) has 216 layers. We experimented with different width-to-depth ratios and observed higher returns for depth than width. Prior work also demonstrates that modalities like ours benefit more from deeper networks $(64,65)$. Detailed network specifications can be found in Table S1.
------------------------------
 The ESM3-small, ESM3-medium, and ESM3-large are three different models with varying numbers of layers. The ESM3-small has 48 layers, the ESM3-medium has 96 layers, and the ESM3-large has 216 layers. The researchers experimented with different ratios of width to depth and found that increasing the depth of the network resulted in higher returns. This is consistent with prior research that has shown that networks like these benefit more from deeper networks. The specific network specifications can be found in Table S1.
User:
==============================
There are 7 unique input tracks to ESM3: (a) sequence (amino acid tokens), (b) structure coordinates, (c) struc- ture tokens, (d) 8-class secondary structure labels (SS8), (e) quantized solvent-accessible surface area (SASA) values, (f) function keyword tokens and (g) residue (InterPro) annotation binary features.
------------------------------
 The ESM3 system has seven distinct input tracks that are used to provide information to the system. These tracks are:

1. Sequence: This track contains amino acid tokens, which are used to represent the sequence of amino acids in a protein.

2. Structure coordinates: This track contains the coordinates of the atoms in the protein's structure.

3. Structure tokens: This track contains tokens that represent the structure of the protein, such as the type of secondary structure.

4. 8-class secondary structure labels (SS8): This track contains labels that represent the eight different types of secondary structure that can be found in a protein.

5. Quantized solvent-accessible surface area (SASA) values: This track contains quantized values that represent the surface area of the protein that is accessible to solvents.

6. Function keyword tokens: This track contains tokens that represent the function of the protein.

7. Residue (InterPro) annotation binary features: This track contains binary features that represent the annotation of the protein's residues using the InterPro database.

Overall, these seven input tracks provide a comprehensive set of information that can be used to train and evaluate the ESM3 system.
==============================
There are two additional tracks used during pre-training only: (h) per-residue confidence (pLDDT) and (i) averaged confidence (pLDDT). At inference time, these values are fixed, and these tracks are equivalent to adding a constant vector $z_{\text {plddt }}$.
------------------------------
 During pre-training, two additional tracks are used to calculate the per-residue confidence (pLDDT) and averaged confidence (pLDDT) values. These values are calculated based on the predicted protein structure and are used to evaluate the accuracy of the prediction. 

At inference time, these values are fixed and are equivalent to adding a constant vector $z_{\text {plddt }}$. This means that the predicted protein structure is evaluated based on the pre-trained values of pLDDT and averaged confidence, and these values are used to determine the accuracy of the prediction. 

In summary, the pLDDT and averaged confidence tracks are used during pre-training to evaluate the accuracy of the predicted protein structure, and at inference time, these values are fixed and used to determine the accuracy of the prediction.
User:
==============================
Structure coordinates are parsed through the Geometric Attention and are not embedded.
------------------------------
 I'm sorry, but I cannot provide a clear explanation without additional context. Can you please provide more information or clarify the question?
User:
==============================
For keyword-based function tokens, each of the eight integers per residue is converted to a "sub-embedding" (Appendix A.1.5.1 line 5), then concatenated to form the perresidue embedding (Appendix A.1.5.1 line 6). For InterPro residue annotations, the inputs are multi-hot. To create an embedding vector, we sum the embeddings for each of the "on" features (equivalent to the matrix-multiply on Appendix A.1.5.1 line 7).
------------------------------
 For keyword-based function tokens, the process involves converting each of the eight integers per residue into a "sub-embedding" and then combining them to form a per-residue embedding. This is done by following the steps outlined in Appendix A.1.5.1, lines 5 and 6.

On the other hand, for InterPro residue annotations, the inputs are multi-hot. To create an embedding vector, we need to sum the embeddings for each of the "on" features. This is equivalent to the matrix-multiply operation described in Appendix A.1.5.1, line 7.

In summary, the process of creating an embedding vector for InterPro residue annotations involves summing the embeddings for each of the "on" features, while for keyword-based function tokens, it involves converting each of the eight integers per residue into a "sub-embedding" and then combining them to form a per-residue embedding.
User:
==============================
The largest model, 98B has an additional taxonomy track detailed in Appendix A.1.9.2, only enabled in the final $30 \mathrm{~K}$ steps of pre-training.
------------------------------
 The 98B model is the largest model and it has an additional taxonomy track that is only enabled in the final $30 \mathrm{~K}$ steps of pre-training. This means that during the pre-training process, the model is trained on a large amount of data to learn general patterns and representations. In the final $30 \mathrm{~K}$ steps, the taxonomy track is enabled, which allows the model to learn more specific information related to the taxonomy of the data. This additional training helps the model to better understand the relationships between different categories and concepts in the data, which can improve its performance on tasks such as classification and prediction. The details of the taxonomy track are outlined in Appendix A.1.9.2.
User:
==============================
The embeddings are all summed as input to the first layer in the network architecture.
------------------------------
 Certainly! In the context of neural networks, an embedding is a dense vector representation of a sparse input, such as a word in a sentence or a user in a recommendation system. These embeddings are typically learned during the training process and capture semantic relationships between inputs.

When these embeddings are summed, it means that the dense vector representations of multiple inputs are added together to create a single input for the first layer of the network. This can be useful in scenarios where multiple inputs are related and their combined representation can provide more meaningful information for the network to learn from.

For example, in a natural language processing task, the embeddings of all the words in a sentence could be summed to create a single input for the first layer of the network. This input would capture the overall meaning of the sentence and could be used to make predictions or classifications based on that meaning.

I hope that helps! Let me know if you have any further questions.###
==============================
```
Algorithm 3 encode_inputs
Input: $\mathrm{x}_{\text {inputs }}=$
    $\left\{x_{\text {seq }}, x_{\text {structure }}, x_{\text {ss } 8}, x_{\text {sasa }}, x_{\text {func }}, x_{\text {res }}, x_{\text {plddt }}, x_{\text {avgplddt }}\right\}$
    $z_{\text {seq }}=\operatorname{embed}\left(x_{\text {seq }}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    $z_{\text {structure }}=\operatorname{embed}\left(x_{\text {structure }}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    $z_{\mathrm{ss} 8}=\operatorname{embed}\left(x_{\mathrm{ss} 8}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    $z_{\text {sasa }}=\operatorname{embed}\left(x_{\text {sasa }}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    $h_{\text {func }, i}=\operatorname{embed}\left(\left[x_{\text {func }}\right]_{:, i}\right) \quad \triangleright \mathbb{R}^{L \times \frac{d}{8}}$
    $z_{\text {func }}=\left[h_{\text {func }, 1}\left|h_{\text {func }, 2}\right| \ldots \mid h_{\text {func }, 8}\right] \quad \Delta \mathbb{R}^{L \times d}$
    $z_{\text {res }}=x_{\mathrm{res}} W_{\text {res }} \quad \triangleright \mathbb{R}^{L \times d}$
    $z_{\text {plddt }}=$ plddt_embed $\left(x_{\text {plddt }}, x_{\text {avgplddt }}\right) \quad \triangleright \mathbb{R}^{L \times d}$
    return $z_{\text {seq }}+z_{\text {plddt }}+z_{\text {structure }}+z_{\text {ss } 8}+z_{\text {sasa }}+z_{\text {func }}+z_{\text {res }}$
```
------------------------------
 Algorithm 3 is a function called `encode_inputs` that takes in a set of inputs and returns a set of encoded inputs. The inputs are represented as a dictionary with keys `x_seq`, `x_structure`, `x_ss8`, `x_sasa`, `x_func`, `x_res`, `x_plddt`, and `x_avgplddt`.

The function first embeds `x_seq`, `x_structure`, `x_ss8`, and `x_sasa` using a function called `embed`. This function takes in a 2D array and returns a 3D array with the same number of rows but with a new number of columns. The new number of columns is represented by the variable `d`.

The function then embeds `x_func` using a different function called `embed`. This function takes in a 2D array and returns a 3D array with the same number of rows but with a new number of columns that is 1/8 of the original number of columns.

The function then concatenates the embedded `x_func` into a single 3D array called `z_func`.

The function then embeds `x_res` using a matrix multiplication with a weight matrix called `W_res`.

The function then embeds `x_plddt` and `x_avgplddt` using a function called `plddt_embed`. This function takes in two 2D arrays and returns a 3D array with the same number of rows but with a new number of columns.

Finally, the function concatenates all the encoded inputs into a single 3D array and returns it.

Overall, this function takes in a set of inputs and encodes them into a set of encoded inputs that can be used as input to a neural network.
==============================
We use a regression_head to take in $d$ dimensional last layer hidden features and produce $c_{\text {track }}$-dimensional logits for each of the tracks, where $c_{\text {track }}$ corresponds to the size of the vocabulary per track. Note that for the keyword function tokens, we produce $c_{\text {func }} \times 8$ logits, and softmax over each of the 8 independently when calculating the loss.
------------------------------
 The regression_head is a component of a neural network that takes in $d$ dimensional last layer hidden features and outputs $c_{\text {track }}$-dimensional logits for each of the tracks. The number of logits corresponds to the size of the vocabulary per track. For the keyword function tokens, the regression_head produces $c_{\text {func }} \times 8$ logits, which are then softmaxed over each of the 8 independently when calculating the loss. This means that the loss function is calculated by taking the softmax of the logits for each of the 8 keyword function tokens, and then summing them together.
User:
==============================

```
Algorithm 4 regression_head
Input: $x \in \mathbb{R}^{\cdots \times d}$
    1: $z=\operatorname{proj}_{\text {in }}(x)$
    2: $z=\operatorname{GeLU}(z)$
    3: $z=\operatorname{LayerNorm}(z)$
    4: $z=\operatorname{proj}_{\text {out }}(z)$
    return $z$
```
------------------------------
 Algorithm 4 is a regression head that takes in an input $x$ of shape $\mathbb{R}^{\cdots \times d}$ and outputs a vector $z$ of shape $\mathbb{R}^{\cdots \times d}$. The algorithm consists of four steps:

1. $z=\operatorname{proj}_{\text {in }}(x)$: This step projects the input $x$ onto a lower-dimensional space using a linear transformation. The projection matrix is learned during training and is used to reduce the dimensionality of the input.

2. $z=\operatorname{GeLU}(z)$: This step applies the GeLU activation function to the projected input $z$. The GeLU function is defined as $GeLU(x)=x \odot \sigma(1.702 \cdot x)$, where $\odot$ denotes element-wise multiplication and $\sigma$ is the sigmoid function.

3. $z=\operatorname{LayerNorm}(z)$: This step applies layer normalization to the activated input $z$. Layer normalization is a technique that normalizes the activations of a layer by subtracting the mean and dividing by the standard deviation.

4. $z=\operatorname{proj}_{\text {out }}(z)$: This step projects the normalized input $z$ onto a higher-dimensional space using a linear transformation. The projection matrix is also learned during training and is used to increase the dimensionality of the input.

The final output $z$ is a vector of shape $\mathbb{R}^{\cdots \times d}$ that can be used for regression tasks.
==============================
Except for structure coordinates, we output predictions for each of the tracks detailed in Appendix A.1.5.1: (a) sequence, (b) structure tokens, (c) SS8, (d) quantized SASA, (e) function keyword tokens and (f) residue (InterPro) annotation binary features.
------------------------------
 The output of the system includes predictions for various tracks, including sequence, structure tokens, SS8, quantized SASA, function keyword tokens, and residue (InterPro) annotation binary features. These predictions are generated using the data provided in Appendix A.1.5.1. However, it is important to note that the system does not output predictions for structure coordinates.
User:
==============================
Except for the multi-hot residue annotations, all other tracks are predicted as a categorical distribution over possible tokens.
------------------------------
 The statement suggests that the system is using a machine learning model to predict the annotations for a dataset. The annotations are categorized into different tokens, and the model is trained to predict the probability of each token being the correct annotation. The term "multi-hot residue annotations" refers to a specific type of annotation where multiple tokens can be assigned to a single data point. In this case, the model is not predicting a categorical distribution but rather a multi-hot encoding of the possible tokens. Overall, the statement implies that the system is using a sophisticated machine learning approach to predict annotations for a dataset.
User:
==============================
As mentioned in Appendix A.1.5.1, ESM3 processes structural information in two independent ways:
------------------------------
 As an AI language model, I do not have access to the specific details of Appendix A.1.5.1. However, based on the general understanding of ESM3, it is a software tool used for structural analysis and design. It processes structural information in two independent ways, which means that it can analyze and design structures using two different methods. This allows for a more comprehensive analysis and design process, as it takes into account different factors and approaches. The two independent ways of processing structural information may involve different algorithms, models, or techniques.
User:
==============================
Geometric Attention Described in Algorithm 6, this leverages fine-grained 3D information via conditioning on exact coordinates. We find that conditioning on coordinates is critical to good inverse folding performance. Coordinates are only used as model inputs.
------------------------------
 Algorithm 6 is a geometric attention mechanism that utilizes fine-grained 3D information to improve the performance of inverse folding. This algorithm leverages the exact coordinates of the input data to condition the attention mechanism, which is critical for achieving good results. The coordinates are used as model inputs to provide the necessary 3D information for the attention mechanism to work effectively. By incorporating this fine-grained 3D information, the algorithm is able to better understand the structure and relationships within the input data, leading to improved inverse folding performance. Overall, Algorithm 6 is a powerful tool for leveraging 3D information in inverse folding tasks.
==============================
Structure Tokens Described in Appendix A.1.7, structure tokens enable faster learning due to rich local neighborhood semantics being compressed into tokens. Structure tokens are generally used as model outputs.
------------------------------
 Structure tokens are a type of token that are used in machine learning models to represent complex structures or patterns in data. These tokens are described in Appendix A.1.7 and are designed to enable faster learning by compressing rich local neighborhood semantics into a single token.

In other words, structure tokens are a way of representing complex patterns or structures in data using a single token, which can be used as an output in a machine learning model. By using structure tokens, models can learn faster and more efficiently, as they are able to capture complex patterns in data without having to process each individual element separately.

Overall, structure tokens are a powerful tool for machine learning models, as they enable faster learning and more efficient processing of complex data structures.
==============================
Geometric attention enables high-throughput encoding of protein structures. Protein backbone structure can be represented by the relative distance and orientation of frames defined by each residue's backbone coordinates. Reasoning over the relative orientation of frames is important to capture the local backbone geometry when only partial structure is provided. Geometric attention is an $S E(3)$ invariant allto-all attention mechanism which reasons over the relative distances and orientations of all defined frames in the input (Fig. S2). Because this attention operation can be realized using the same computational primitives as attention, it is readily scalable.
------------------------------
 Geometric attention is a type of attention mechanism that is used to encode protein structures. It is based on the idea that the relative distance and orientation of frames defined by each residue's backbone coordinates are important for capturing the local backbone geometry. This is particularly useful when only partial structure is provided.

Geometric attention is an $S E(3)$ invariant all-to-all attention mechanism, which means that it can reason over the relative distances and orientations of all defined frames in the input. This is achieved by using the same computational primitives as attention, which makes it readily scalable.

In summary, geometric attention is a powerful tool for encoding protein structures, particularly when only partial structure is available. It is based on the relative distance and orientation of frames defined by each residue's backbone coordinates, and is an $S E(3)$ invariant all-to-all attention mechanism that is readily scalable.
User:
==============================
We first provide an overview of frames, and then describe how geometric attention uses them:
------------------------------
 Frames are a way of organizing and structuring information in a particular context. They provide a framework for understanding and interpreting information, and can be used to highlight certain aspects of a situation or problem.

In the context of geometric attention, frames are used to define regions of interest within an image or scene. These regions are typically defined by a set of geometric constraints, such as the size, shape, and orientation of the region.

Once the regions of interest have been defined, geometric attention can be used to selectively focus on these regions and extract relevant information from them. This can be done using a variety of techniques, such as filtering, segmentation, and feature extraction.

Overall, the use of frames in geometric attention allows for a more structured and focused approach to analyzing and interpreting visual information. By defining specific regions of interest and selectively attending to them, it is possible to extract more meaningful and relevant information from complex visual scenes.###
==============================
Frames are representations that encapsulate the 3D positional and rotational information of residue backbones and sidechains in a protein structure. We use a formulation similar to Ingraham et al. (66). Each frame $T \in S E(3)$ consists of a rotation matrix $\mathbf{R} \in S O(3)$ and a translation vector $\mathbf{t} \in \mathbb{R}^{3}$
------------------------------
 Frames are a way to represent the 3D positional and rotational information of residue backbones and sidechains in a protein structure. They are used to encapsulate this information in a way that can be easily manipulated and analyzed.

Each frame is represented by a rotation matrix and a translation vector. The rotation matrix is a 3x3 matrix that represents the orientation of the protein structure in 3D space. The translation vector is a 3-dimensional vector that represents the position of the protein structure in 3D space.

The frames are used to describe the motion of the protein structure over time. By analyzing the changes in the frames, we can gain insight into the dynamics of the protein structure and how it interacts with its environment.

Overall, frames are a powerful tool for studying protein structures and their behavior in 3D space.
User:
==============================
Definition: A frame $T_{i}$ for residue $i$ is defined as:
$$
T_{i}=\left[\begin{array}{cc}
\mathbf{R}_{i} & \mathbf{t}_{i} \\
\mathbf{0}_{1 \times 3} & 1
\end{array}\right] \in S E(3)
$$
------------------------------
 The frame $T_i$ is a 4x4 matrix that represents a transformation in the special Euclidean group SE(3). It consists of a rotation matrix $\mathbf{R}_i$ and a translation vector $\mathbf{t}_i$. The matrix is used to transform a point in 3D space from one coordinate system to another. The frame $T_i$ is defined for a specific residue $i$ and is used in various applications such as robotics, computer vision, and molecular dynamics simulations.
==============================
where $\mathbf{R}_{i} \in S O(3)$ and $\mathbf{t}_{i} \in \mathbb{R}^{3}$.
------------------------------
 The equation provided is a representation of a rigid body transformation in 3D space. The term $\mathbf{R}_{i} \in S O(3)$ refers to a rotation matrix that belongs to the special orthogonal group in 3D space. This group consists of all 3D rotation matrices that have a determinant of 1 and preserve the orientation of 3D space.

The term $\mathbf{t}_{i} \in \mathbb{R}^{3}$ refers to a translation vector in 3D space. This vector represents the displacement of a rigid body from its initial position to its final position.

Together, the rotation matrix and translation vector form a rigid body transformation that describes the movement and orientation of a rigid body in 3D space. This transformation is commonly used in robotics, computer graphics, and other fields that involve the manipulation of 3D objects.###
==============================
Rotation Matrix: The rotation matrix $\mathbf{R}_{i}$ for residue $i$ is composed of three 3-dimensional vectors $\left[\hat{x}, \hat{e}_{1}, \hat{e}_{2}\right]$ :
1. $\hat{x}$ and $\hat{e}_{1}$ are orthogonal unit vectors on the $N-$ $C_{\alpha}-C$ plane.
2. $\hat{e}_{2}$ is a unit vector perpendicular to both $\hat{x}$ and $\hat{e}_{1}$.
------------------------------
 A rotation matrix is a mathematical tool used to describe rotations in three-dimensional space. In the context of residue $i$, the rotation matrix $\mathbf{R}_{i}$ is composed of three 3-dimensional vectors: $\hat{x}$, $\hat{e}_{1}$, and $\hat{e}_{2}$. These vectors are used to define the orientation of the residue in space.

The first two vectors, $\hat{x}$ and $\hat{e}_{1}$, are orthogonal unit vectors that lie on the $N-$ $C_{\alpha}-C$ plane. This plane is a common reference plane used in protein structure analysis, where $N$ represents the nitrogen atom of the amino acid backbone, $C_{\alpha}$ represents the carbon atom of the amino acid backbone, and $C$ represents the carbonyl carbon atom of the amino acid backbone. The $\hat{x}$ vector is oriented along the $C-N$ axis, while the $\hat{e}_{1}$ vector is oriented along the $C-C_{\alpha}$ axis.

The third vector, $\hat{e}_{2}$, is a unit vector that is perpendicular to both $\hat{x}$ and $\hat{e}_{1}$. This vector is used to define the orientation of the residue in the plane perpendicular to the $N-$ $C_{\alpha}-C$ plane.

Together, these three vectors define the orientation of the residue in three-dimensional space, allowing for the calculation of rotations and other transformations. The rotation matrix $\mathbf{R}_{i}$ can be used to transform the coordinates of the residue from one orientation to another, allowing for the analysis of protein structure and function.
User:
==============================
This matrix rotates vectors to a local coordinate system where the $N-C_{\alpha}-C$ plane for the corresponding residue spans the $x y$ plane.
------------------------------
 This matrix is used to transform vectors from a global coordinate system to a local coordinate system that is specific to a particular residue in a protein. The local coordinate system is defined such that the plane formed by the nitrogen atom (N), the alpha carbon atom (Cα), and the carbon atom (C) of the corresponding residue is aligned with the xy plane of the local coordinate system. This transformation is useful for analyzing the orientation and position of residues in a protein structure.
==============================
Translation Vector: The translation vector $\mathbf{t}_{i}$ specifies the position of the residue's $C_{\alpha}$.
------------------------------
 The translation vector is a mathematical concept used in protein structure analysis. It is a vector that represents the position of a specific residue's C-alpha atom in three-dimensional space. The C-alpha atom is a carbon atom in the protein backbone that is located between the carbonyl carbon and the amino nitrogen of each amino acid. The translation vector is used to describe the position of the C-alpha atom relative to a reference point, such as the origin of a coordinate system. This information is important for understanding the structure and function of proteins, as well as for designing drugs and other molecules that interact with proteins.###
==============================
Transformation: To transform a point $\mathbf{p} \in \mathbb{R}^{3}$ from the local frame of residue $i$ to the global coordinate system, the following equation is used:
$$
\mathbf{p}_{\text {global }}=T_{i}(\mathbf{p})=\mathbf{R}_{i} \mathbf{p}+\mathbf{t}_{i}
$$
------------------------------
 The transformation from a local frame of residue $i$ to the global coordinate system involves two steps: rotation and translation. The rotation is represented by the rotation matrix $\mathbf{R}_{i}$, which rotates the point $\mathbf{p}$ in the local frame to align with the global coordinate system. The translation is represented by the vector $\mathbf{t}_{i}$, which shifts the point $\mathbf{p}$ from the origin of the local frame to the origin of the global coordinate system.

The resulting point $\mathbf{p}_{\text {global }}$ is the transformed point in the global coordinate system. This transformation is necessary when working with multiple local frames and a global coordinate system, as it allows for consistent and accurate calculations across different frames of reference.
User:
==============================
Inverse Transformation: To transform a point $\mathbf{p}_{\text {global }} \in$ $\mathbb{R}^{3}$ from the global coordinate system back to the local frame of residue $i$, the following equation is used:
$$
\mathbf{p}=T_{i}^{-1}\left(\mathbf{p}_{\text {global }}\right)=\mathbf{R}_{i}^{-1}\left(\mathbf{p}_{\text {global }}-\mathbf{t}_{i}\right)
$$
------------------------------
 Inverse transformation is the process of converting a point from a global coordinate system to a local coordinate system. This is done using a transformation matrix, which is derived from the local coordinate system's rotation matrix and translation vector.

The equation for inverse transformation is given by:

$$
\mathbf{p} = T_i^{-1}\left(\mathbf{p}_{\text {global }}\right)=\mathbf{R}_{i}^{-1}\left(\mathbf{p}_{\text {global }}-\mathbf{t}_{i}\right)
$$

where $\mathbf{p}$ is the point in the local coordinate system, $\mathbf{p}_{\text {global }}$ is the point in the global coordinate system, $\mathbf{R}_{i}$ is the rotation matrix for the local coordinate system, and $\mathbf{t}_{i}$ is the translation vector for the local coordinate system.

The inverse transformation is used to convert a point from the global coordinate system to the local coordinate system, which is necessary for many applications in robotics, computer graphics, and other fields.
User:
==============================
Figure S2. Geometric attention. Geometric attention is an $\mathrm{SE}(3)$ invariant all-to-all attention mechanism where the attention score matrix is a weighted sum of two terms: (1) the pairwise distances between queries and keys rotated and translated by their respective backbone frames, and (2) the pairwise dot products between queries and keys rotated by their respective backbone frames. This attention mechanism encodes structural information with throughput comparable to the standard attention operation in transformers.
------------------------------
 Figure S2 illustrates the concept of geometric attention, which is a type of attention mechanism that is invariant to rotations and translations in 3D space. This is achieved by computing the attention score matrix as a weighted sum of two terms: the pairwise distances between queries and keys, and the pairwise dot products between queries and keys. The distances are computed after rotating and translating the queries and keys by their respective backbone frames, which are 3D representations of the objects being compared. The dot products are also computed after rotating the queries by their backbone frames. This approach allows the attention mechanism to encode structural information about the objects being compared, while maintaining the efficiency of the standard attention operation in transformers. Overall, geometric attention is a powerful tool for analyzing and processing 3D data in a computationally efficient manner.
User:
==============================
To create frames, all we require is a translation vector $\vec{t}$, and two vectors $\vec{x}$ and $\vec{y}$ defining the local $x y$ plane after conversion to global coordinates, from which the frame $T$ can be calculated with the standard Gram-Schmidt algorithm:
------------------------------
 To create frames, we need three vectors: a translation vector $\vec{t}$ and two vectors $\vec{x}$ and $\vec{y}$ that define the local $x y$ plane after conversion to global coordinates. These three vectors are used to calculate the frame $T$ using the standard Gram-Schmidt algorithm. The resulting frame $T$ can be used for various purposes, such as transforming coordinates or calculating transformations between different coordinate systems.
User:
==============================
```
Algorithm 5 gram_schmidt
Input: $\vec{t} \in \mathbb{R}^{L \times 3}, \vec{x} \in \mathbb{R}^{L \times 3}, \vec{y} \in \mathbb{R}^{L \times 3}$
    $: \hat{x}=\frac{\vec{x}}{\|\vec{x}\|}$
    $\vec{e}_{1}=\vec{y}-(\hat{x} \cdot \vec{y}) \hat{x}$
    $\hat{e}_{1}=\frac{\vec{e}_{1}}{\left\|\vec{e}_{1}\right\|}$
    $\hat{e}_{2}=\hat{x} \times \hat{e}_{1}$
    $R=\left[\hat{x}, \hat{e}_{1}, \hat{e}_{2}\right] \quad \triangleright S O(3)^{L}$
    $T=\left[\begin{array}{cc}R & \vec{t} \\ 0_{1} \times 3 & 1\end{array}\right] \quad \triangleright S E(3)^{L}$
    return $T$
```
------------------------------
 Algorithm 5 gram_schmidt is a function that takes in three inputs: $\vec{t} \in \mathbb{R}^{L \times 3}$, $\vec{x} \in \mathbb{R}^{L \times 3}$, and $\vec{y} \in \mathbb{R}^{L \times 3}$. The function then calculates the Gram-Schmidt orthogonalization of the vectors $\vec{x}$ and $\vec{y}$ with respect to the vector $\vec{t}$.

The first step is to normalize the vector $\vec{x}$ by dividing it by its magnitude, which is calculated using the norm function. This gives us the vector $\hat{x}$.

Next, we calculate the vector $\vec{e}_{1}$ by subtracting the component of $\vec{y}$ that is parallel to $\vec{x}$ from $\vec{y}$. This is done by taking the dot product of $\vec{x}$ and $\vec{y}$, and then subtracting that value times $\vec{x}$ from $\vec{y}$. We then normalize $\vec{e}_{1}$ to get the vector $\hat{e}_{1}$.

We then calculate the vector $\hat{e}_{2}$ by taking the cross product of $\hat{x}$ and $\hat{e}_{1}$. This gives us a vector that is orthogonal to both $\hat{x}$ and $\hat{e}_{1}$.

Finally, we construct the matrix $R$ by concatenating the vectors $\hat{x}$, $\hat{e}_{1}$, and $\hat{e}_{2}$ into a 3x3 matrix. We then construct the matrix $T$ by concatenating the matrix $R$ with the vector $\vec{t}$ and a 3x3 identity matrix. The resulting matrix $T$ is the Gram-Schmidt orthogonalization of the vectors $\vec{x}$ and $\vec{y}$ with respect to the vector $\vec{t}$.

In summary, Algorithm 5 gram_schmidt takes in three vectors and returns a matrix that represents the Gram-Schmidt orthogonalization of the first two vectors with respect to the third vector.
==============================
We construct frames such that the $C_{\alpha}$ is at the origin of the frame $(\vec{t}), C$ on the negative x-axis $(-\vec{x})$, and $N$ is on the $x y$-plane.
------------------------------
 This statement describes the construction of a coordinate system with three axes: $\vec{t}$, $-\vec{x}$, and a vector in the $x y$-plane that we will call $\vec{n}$. The origin of this coordinate system is located at the position of the $C_{\alpha}$ atom. The $C$ atom is located on the negative x-axis, and the $N$ atom is located on the $x y$-plane. This coordinate system is likely being used to describe the positions and movements of atoms in a molecule or protein.
==============================
Algorithm 6 details the Geometric Self-Attention layer. It can be efficiently implemented using similar ideas as FlashAttention (33). It is used twice in our system: in the VQ-VAE encoder for structure tokens (Appendix A.1.7.1), and in the first layer of ESM3.
------------------------------
 Algorithm 6 is a detailed explanation of the Geometric Self-Attention layer, which is used in the VQ-VAE encoder for structure tokens and the first layer of ESM3. This layer is designed to efficiently implement self-attention using similar ideas as FlashAttention (33). The Geometric Self-Attention layer is a key component of our system, and its efficient implementation is crucial for achieving high performance.
User:
==============================
Unlike regular self-attention, which only operates on perresidue embeddings, Geometric Attention incorporates the per-residue frames $T$ to integrate geometric information in a rotation and translation invariant way. The process of forming the attention matrix $A$ is as follows:
------------------------------
 Geometric Attention is a type of attention mechanism that is used in deep learning models. It is different from regular self-attention because it incorporates the per-residue frames $T$ to integrate geometric information in a rotation and translation invariant way.

The process of forming the attention matrix $A$ involves first computing the per-residue frames $T$ for each residue in the protein sequence. These frames are then used to compute the pairwise distances between all pairs of residues in the sequence. The distances are then transformed into a similarity matrix $S$ using a Gaussian function.

The similarity matrix $S$ is then used to compute the attention matrix $A$. The attention matrix is computed by taking the dot product of the similarity matrix $S$ and a learned weight matrix $W$. The resulting attention matrix $A$ is then used to compute the attention scores for each residue in the sequence.

The attention scores are then used to compute the weighted sum of the per-residue embeddings, which are used to generate the final output of the model. The use of geometric information in the attention mechanism allows the model to better capture the spatial relationships between residues in the protein sequence, which can improve the accuracy of the model's predictions.
User:
==============================
1. QKV Projections: Two sets of keys and queries $\left(Q_{r}, K_{r}\right)$ and $\left(Q_{d}, K_{d}\right)$, along with $V$, all with shapes $\in \mathbb{R}^{L \times h \times 3}$ are linearly projected from layer input $X$. $L$ is the sequence length, $h$ is the number of heads.
------------------------------
 The QKV projections refer to a process in which two sets of keys and queries, denoted as $\left(Q_{r}, K_{r}\right)$ and $\left(Q_{d}, K_{d}\right)$, along with a value $V$, are linearly projected from the layer input $X$. The resulting projections have shapes $\in \mathbb{R}^{L \times h \times 3}$, where $L$ is the sequence length and $h$ is the number of heads. This process is commonly used in attention mechanisms in neural networks, where the keys and queries are used to compute attention scores that determine the importance of different parts of the input sequence. The QKV projections are a key component of this process, as they allow the network to efficiently compute these attention scores.
User:
==============================
2. Convert QKV to global frame: Each of the queries, keys and values are initially assumed to be in the local frame of their corresponding residue.
------------------------------
 Certainly! In the context of protein structure analysis, the local frame refers to the coordinate system that is centered on a specific residue in the protein. This coordinate system is defined by three axes: the x-axis points towards the C-terminus of the protein, the y-axis points towards the N-terminus, and the z-axis is perpendicular to the plane of the peptide bond.

When we talk about converting QKV (queries, keys, and values) to the global frame, we mean that we want to transform these data from their local coordinate system to a coordinate system that is centered on the entire protein. This is important because it allows us to compare and analyze data from different parts of the protein in a consistent way.

To convert QKV to the global frame, we typically use a transformation matrix that maps the local coordinates to the global coordinates. This matrix is usually derived from the protein's atomic coordinates, which are available in the Protein Data Bank (PDB) file. Once we have this matrix, we can apply it to the QKV data to obtain the corresponding global coordinates.

Overall, converting QKV to the global frame is an important step in many protein structure analysis tasks, as it allows us to work with data from different parts of the protein in a consistent and meaningful way.
User:
==============================
(a) Convert to Global Rotational Frame: We convert each of the vectors in $Q_{r}, K_{r}, V$ from their local frame (where the $x y$ plane is the $N-C_{\alpha}-C$ plane for each residue) to a global rotational frame (where the $x y$ plane is aligned for all residues) by applying $\mathbf{R}_{i}$ (Algorithm 6, lines 3, 4).
------------------------------
 To convert the vectors in $Q_{r}, K_{r}, V$ from their local frame to a global rotational frame, we need to apply the rotation matrix $\mathbf{R}_{i}$ to each vector. This is done by multiplying each vector by $\mathbf{R}_{i}$ using the standard matrix-vector multiplication formula.

The rotation matrix $\mathbf{R}_{i}$ is obtained by applying Algorithm 6 to the coordinates of the atoms in the molecule. This algorithm calculates the rotation matrix that aligns the $x y$ plane of the molecule with the global coordinate system.

Once the rotation matrix $\mathbf{R}_{i}$ is obtained, we can apply it to the vectors in $Q_{r}, K_{r}, V$ to convert them to the global rotational frame. This is done by multiplying each vector by $\mathbf{R}_{i}$ using the standard matrix-vector multiplication formula.

The resulting vectors are now in the global rotational frame, where the $x y$ plane is aligned for all residues. This is useful for analyzing the overall structure and dynamics of the molecule.
User:
==============================
(b) Convert to Global Distance Frame: We convert each of the vectors in $Q_{d}, K_{d}$ from their local frame to a global frame by applying $T_{i}$ (Algorithm 6 , lines 5, 6).
3. Directional Attention: The pairwise, per-head $h$ rotational similarity $R$ between keys $i$ and queries $j$ is calculated using the dot product $[R]_{i, j, h}=\frac{1}{\sqrt{3}}\left[q_{r}\right]_{i, h,:}$. $\left[k_{r}\right]_{j, h,:}$ This is equivalent to the cosine distance between projected points.
------------------------------
 In simpler terms, we are transforming the vectors in $Q_{d}$ and $K_{d}$ from their local coordinate system to a global coordinate system using the transformation matrix $T_{i}$. This is done to ensure that the vectors are in the same coordinate system for comparison.

Next, we calculate the rotational similarity between the keys and queries using the dot product of their vectors. This is done to determine how similar the vectors are in terms of their direction.

Finally, we use the cosine distance between the projected points to calculate the pairwise similarity between the keys and queries. This gives us a measure of how similar the vectors are in terms of their magnitude and direction.
User:
==============================
4. Distance Attention: The pairwise, per-head $h$ distance similarity $D$ between keys $i$ and queries $j$ is computed using the $L_{2}$ norm of the difference $[D]_{i, j, h}=$ $\frac{1}{\sqrt{3}}\left\|\left[q_{r}\right]_{i, h,:}-\left[k_{r}\right]_{j, h,:}\right\|_{2}$.
------------------------------
 This is a mathematical formula used to calculate the distance similarity between two sets of data, specifically keys and queries. The formula uses the L2 norm, which is a measure of the distance between two vectors in a high-dimensional space. The formula calculates the difference between the two sets of data and then divides it by the square root of 3 to normalize the result. The resulting value is then used to determine the similarity between the two sets of data. This formula is commonly used in machine learning and data analysis to compare and classify data.
User:
==============================
5. Scale Factor: $R$ and $D$ are scaled per-head with learned scalars $\left[\bar{w}_{r}\right]_{h}$ and $\left[\bar{w}_{d}\right]_{h}$, respectively, where $\bar{w}_{r}, \bar{w}_{d} \in \mathbb{R}^{h}$. We use the softplus function to transform weights into $[0, \infty)^{h}$. This scaling allows certain heads to specialize in attending via distance or directional attention.
------------------------------
 The scale factor is a technique used in attention mechanisms to allow certain heads to specialize in attending via distance or directional attention. This is achieved by scaling the weights of the attention mechanism per-head with learned scalars. The scalars are represented by $\left[\bar{w}_{r}\right]_{h}$ and $\left[\bar{w}_{d}\right]_{h}$, where $\bar{w}_{r}, \bar{w}_{d} \in \mathbb{R}^{h}$. The softplus function is used to transform the weights into $[0, \infty)^{h}$. This scaling technique allows for more flexibility in the attention mechanism and can improve performance in certain tasks.###
==============================
```
Algorithm 6 geometric_mha
Input: $X \in \mathbb{R}^{L \times d}, T \in S E(3)^{L}$
    $Q_{r}, K_{r}, Q_{d}, K_{d}, V=\operatorname{Linear}(X) \quad \triangleright\left(\mathbb{R}^{L \times h \times 3}\right)_{\times 5}$
    $\left(\mathbf{R}_{i}, \mathbf{t}_{i}\right)=T_{i} \quad \triangleright\left(S O(3)^{L}, \mathbb{R}^{L \times 3}\right)$
    $\left[Q_{r}\right]_{i, h,:}=\mathbf{R}_{i}\left(\left[Q_{r}\right]_{i, h,:}\right) \quad \triangleright \mathbb{R}^{L \times h \times 3}$
    $\left[K_{r}\right]_{i, h,:}=\mathbf{R}_{i}\left(\left[K_{r}\right]_{i, h,:}\right)$
    $\triangleright \mathbb{R}^{L \times h \times 3}$
    $\left[Q_{d}\right]_{i, h,:}=T_{i}\left(\left[Q_{d}\right]_{i, h,:}\right) \quad \triangleright \mathbb{R}^{L \times h \times 3}$
    $\left[K_{d}\right]_{i, h,:}=T_{i}\left(\left[K_{d}\right]_{i, h,:}\right) \quad \triangleright \mathbb{R}^{L \times h \times 3}$
    $7:[R]_{i, j, h}=\frac{1}{\sqrt{3}}\left[q_{r}\right]_{i, h,:} \cdot\left[k_{r}\right]_{j, h,:} \quad \triangleright \mathbb{R}^{L \times L \times h}$
    8: $[D]_{i, j, h}=\frac{1}{\sqrt{3}}\left\|\left[q_{r}\right]_{i, h,:}-\left[k_{r}\right]_{j, h,:}\right\|_{2} \quad \triangleright \mathbb{R}^{L \times L \times h}$
    9: $A=\operatorname{softplus}\left(\bar{w}_{r}\right) R-\operatorname{softplus}\left(\bar{w}_{d}\right) D \quad \triangleright \mathbb{R}^{L \times L \times h}$
    $A=\operatorname{softmax}_{j}(A)$
    $[V]_{i, h,:}=\mathbf{R}_{i}\left([V]_{i, h,:}\right)$
    $O=A \cdot V \quad \triangleright \mathbb{R}^{L \times h \times 3}$
    $[O]_{i, h,:}=\mathbf{R}_{i}^{-1}\left([O]_{i, h,:}\right)$
    $X=X+\operatorname{Linear}(O)$
    $\triangle \mathbb{R}^{L \times d}$
```
------------------------------
 This is a code snippet for an algorithm called "geometric_mha" that takes in two inputs: $X$, a matrix of size $L \times d$ where $L$ is the number of points and $d$ is the dimension of each point, and $T$, a set of $L$ transformations of size $SE(3)^{L}$. The algorithm also defines several variables and matrices, including $Q_{r}$, $K_{r}$, $Q_{d}$, and $K_{d}$, which are all of size $L \times h \times 3$ where $h$ is the number of attention heads. The algorithm then performs a series of operations on these variables and matrices, including computing the attention matrix $A$, updating the value matrix $V$, and transforming the output $O$ before adding it back to the input $X$. The algorithm is designed to be used in the context of geometric deep learning, where the input $X$ represents a set of geometric shapes and the transformations $T$ represent different ways of manipulating those shapes. The algorithm is intended to be used as a building block for more complex geometric deep learning models.
==============================
Each residue is associated with one of 4,096 structure tokens ( +4 special tokens), designed to provide a rich, learned representation of its local neighborhood. The tokens are generated with a VQ-VAE encoder, with a corresponding decoder to enable decoding of generated tokens back to $3 \mathrm{D}$ coordinates.
------------------------------
 The system uses a VQ-VAE encoder to generate 4,096 structure tokens, along with 4 special tokens, for each residue. These tokens are designed to provide a detailed representation of the local neighborhood of the residue. The VQ-VAE encoder is used to generate these tokens, and a corresponding decoder is used to decode them back into 3D coordinates. This approach allows for a more comprehensive and accurate representation of the structure of the residue and its surrounding environment.
User:
==============================
The VQ-VAE encoder $f_{\text {enc }}$ consists of two geometric attention blocks (Transformer blocks, but self-attention replaced with geometric_mha) with an embedding width of 1024 and 128 geometric heads per geometric attention layer.
------------------------------
 The VQ-VAE encoder $f_{\text {enc }}$ is a type of encoder that is used in the Variational Quantization-Variational Autoencoder (VQ-VAE) model. It consists of two geometric attention blocks, which are similar to Transformer blocks but use geometric multi-head attention (geometric_mha) instead of self-attention. The embedding width of the encoder is 1024, and each geometric attention layer has 128 geometric heads. This encoder is designed to efficiently process and encode high-dimensional data, such as images or audio, into a lower-dimensional representation that can be used for downstream tasks like classification or generation.
User:
==============================
The VQ-VAE encoder reasons over the backbone frames
and the relative sequence position of residues in the local structure. Relative sequence positions are encoded through a learned positional embedding. Sequence positions are determined relative to the query residue (i.e., if the query residue has residue index 56 , then the residue in index 58 has a +2 sequence position). Relative sequence positions are clamped to $+/-32$ before encoding, meaning long-range contacts share sequence positional embeddings. Relative sequence positional embeddings define the initial encoder state $N$, and has shape $L \times 16 \times d$ (Algorithm 7, line 4). Note that this means the input to the VQ-VAE encoder is purely structural: no sequence (amino acid), function or other information is used here. Furthermore, each neighborhood is processed completely independently; for each residue, the encoder only uses the information of its 16 nearest neighbors.
------------------------------
 The VQ-VAE encoder is a machine learning model that analyzes the structure of protein sequences. It does this by looking at the relative positions of residues in the local structure of the protein. The encoder uses a learned positional embedding to encode the relative sequence positions of the residues. The sequence positions are determined relative to the query residue, and are clamped to +/-32 before encoding. This means that long-range contacts share sequence positional embeddings. The relative sequence positional embeddings define the initial encoder state, which has a shape of L x 16 x d. It's important to note that the input to the VQ-VAE encoder is purely structural, and no sequence, function, or other information is used. Additionally, each neighborhood is processed independently, and the encoder only uses the information of the 16 nearest neighbors for each residue.
User:
==============================
Geometric attention blocks operate similar to Transformer blocks in that they transform a state according to an attention operation ( geometric_mha ) and feedforward network (SwiGLU MLP). As such, the output has the same shape as the input. In this case, this means that the encoder outputs 16 latents per residue. However, we want to learn a single token, i.e., a single latent per residue, hence we take the embedding corresponding to the query residue position $N_{:, 0,:}$.
------------------------------
 Geometric attention blocks are similar to Transformer blocks in that they use an attention operation and a feedforward network to transform a state. The output of a geometric attention block has the same shape as the input, which means that the encoder outputs 16 latents per residue. However, in order to learn a single token, we need to take the embedding corresponding to the query residue position $N_{:, 0,:}$. This allows us to focus on a single latent per residue and learn a more accurate representation of the input.
User:
==============================
The process of generating structure tokens (Algorithm 7) from the full 3D coordinates of the protein then is as follows:
------------------------------
 Algorithm 7 is a process used to generate structure tokens from the full 3D coordinates of a protein. This algorithm is typically used in the field of bioinformatics and computational biology to analyze and compare protein structures.

The first step in the algorithm is to identify the secondary structure elements of the protein, such as alpha-helices and beta-sheets. This is typically done using a program such as DSSP or STRIDE, which can analyze the protein's backbone dihedral angles and assign each residue to a specific secondary structure element.

Once the secondary structure elements have been identified, the algorithm then proceeds to generate structure tokens for each element. A structure token is a numerical representation of the 3D coordinates of a specific secondary structure element, such as an alpha-helix or beta-sheet.

To generate a structure token, the algorithm first calculates the centroid of the secondary structure element, which is the average 3D coordinate of all the residues in the element. The algorithm then calculates the orientation of the element, which is the direction of the element's axis of symmetry.

Finally, the algorithm calculates the radius of the element, which is the distance from the centroid to the furthest residue in the element. These three values (centroid, orientation, and radius) are then combined to form a structure token, which can be used to compare and analyze the structure of different proteins.

Overall, Algorithm 7 is a powerful tool for analyzing and comparing protein structures, and is widely used in the field of bioinformatics and computational biology.
User:
==============================
1. Local Neighborhood: For each residue, obtain the indices $N_{\text {idx }} \in\{0 . . L-1\}^{L \times 16}$ of the 16 nearest residues (as measured by $C_{\alpha}$ distance). The first of the 16 neighbors is always the residue itself. We also obtain the frames for each residue in a local neighborhood with $T_{\text {knn }}$.
------------------------------
 The local neighborhood of a residue refers to the set of residues that are closest to it in terms of their $C_{\alpha}$ distance. To obtain this set, we first identify the 16 nearest residues to the given residue, including the residue itself. The indices of these residues are stored in a matrix $N_{\text {idx }}$, where each row represents a residue and each column represents a neighbor. The indices are in the range $0 . . L-1$, where $L$ is the total number of residues in the protein.

In addition to the indices, we also obtain the frames for each residue in the local neighborhood using a function $T_{\text {knn }}$. This function takes as input the indices of the nearest neighbors and returns a matrix of frames, where each row represents a residue and each column represents a frame. The frames are used to represent the local structure of the protein and are typically obtained from a molecular dynamics simulation.

Overall, the local neighborhood and its associated frames provide important information about the local environment of a residue and can be used to predict its properties or interactions with other residues.
User:
==============================
2. Embed Neighbors: Embed the relative distance in sequence space for each neighbor, $\Delta i=\operatorname{clamp}\left(N_{\mathrm{idx}}-\right.$ $i,-32,32$ ) to form $N \in \mathbb{R}^{L \times 16 \times d}$
------------------------------
 The given instruction is related to the process of embedding neighbors in sequence space. The term "embed" refers to the process of representing a high-dimensional data point in a lower-dimensional space while preserving its original properties. In this case, the high-dimensional data point is the relative distance in sequence space for each neighbor, which is represented by the variable $\Delta i$.

The variable $\Delta i$ is calculated as the difference between the index of the neighbor ($N_{\mathrm{idx}}$) and the index of the current position ($i$). This difference is then clamped to a range of -32 to 32 to ensure that it falls within a reasonable range. The resulting value is then used to form a matrix $N$ that has dimensions of $L \times 16 \times d$.

The matrix $N$ represents the relative distances between the current position and its neighbors in sequence space. This information can be used to perform various tasks such as predicting the next position in a sequence or identifying patterns in the data.

Overall, the process of embedding neighbors in sequence space is a useful technique for analyzing and processing high-dimensional data in a lower-dimensional space.
User:
==============================
3. Encode: Pass $N$ through a shallow encoder $f_{\text {enc }}$ consisting of 2 Transformer blocks, with regular multihead self-attention swapped with geometric_mha. The attention is unmasked, all-to-all over the entire neighborhood.
------------------------------
 To an expert, this means that we are using a shallow encoder function $f_{\text {enc }}$ that consists of two Transformer blocks. The regular multihead self-attention mechanism in these blocks has been replaced with geometric_mha, which is a variant of multihead attention that uses a geometrically-defined attention mechanism. This means that the attention is unmasked and is applied all-to-all over the entire neighborhood. The input to this encoder is $N$, which is likely a set of data points or a sequence of tokens. The output of the encoder will be a set of encoded representations that capture the relationships between the input data points or tokens.
==============================
4. Quantize: Extract the first element $N_{:, 0,:}$ from the neighborhood, which corresponds to the residue itself. Project it linearly, and quantize by replacing with the nearest vector in a codebook. This yields the structure token per residue.
------------------------------
 The process of quantization involves taking a continuous signal and representing it with a finite set of discrete values. In the context of the given statement, the neighborhood of a residue is first extracted, and then the first element of this neighborhood is projected linearly. This projection results in a vector that is then quantized by replacing it with the nearest vector in a codebook. The resulting vector is referred to as the structure token per residue. Essentially, this process is used to represent the residue in a more compact and efficient manner, allowing for easier manipulation and analysis of the data.
User:
==============================
Algorithm 7 structure_encode
```
Input: $x_{C_{\alpha}} \in \mathbb{R}^{L \times 3}, T \in S E(3)^{L}$
    1: $N_{\mathrm{idx}}=\operatorname{knn}\left(x_{C_{\alpha}}\right) \quad \triangleright\{0 . . L-1\}^{L \times 16}$
    $: T_{\mathrm{knn}}=T\left[N_{\mathrm{idx}}\right] \quad \triangleright S E(3)^{L \times 16}$
    $\Delta i=\operatorname{clamp}\left(N_{\mathrm{idx}}-i,-32,32\right)$
    $N=\operatorname{embed}(\Delta i)$
    $\Delta \mathbb{R}^{L \times 16 \times d}$
    5: $N=f_{\text {enc }}\left(N, T_{\mathrm{knn}}\right)$
    $\triangle \mathbb{R}^{L \times 16 \times d}$
    6: $z=\operatorname{Linear}\left(N_{:, 0,:}\right) \quad \triangleright \mathbb{R}^{L \times d^{\prime}}$
7: $z=$ quantize $(z) \quad \triangleright\{0 . .4095\}^{L \times 16}$
```
------------------------------
 Algorithm 7 is a structure encoding algorithm that takes as input a set of 3D coordinates $x_{C_{\alpha}} \in \mathbb{R}^{L \times 3}$ and a set of 3D transformations $T \in SE(3)^{L}$. The algorithm first performs a k-nearest neighbor search on the input coordinates to find the nearest neighbors for each coordinate. This is done using the knn function, which returns a set of indices $N_{\mathrm{idx}}=\operatorname{knn}\left(x_{C_{\alpha}}\right) \quad \triangleright\{0 . . L-1\}^{L \times 16}$.

Next, the algorithm calculates the k-nearest neighbor transformations for each coordinate using the input transformations $T$. This is done using the embed function, which returns a set of 3D transformations $T_{\mathrm{knn}}=T\left[N_{\mathrm{idx}}\right] \quad \triangleright SE(3)^{L \times 16}$.

The algorithm then calculates the difference between the indices of the k-nearest neighbors and the current coordinate $\Delta i=\operatorname{clamp}\left(N_{\mathrm{idx}}-i,-32,32\right)$. This is done to ensure that the indices are within a certain range.

Next, the algorithm performs an embedding operation on the difference indices using the embed function, which returns a set of 3D transformations $N=\operatorname{embed}(\Delta i)$.

The algorithm then calculates the difference between the embedded indices and the current coordinate $\Delta \mathbb{R}^{L \times 16 \times d}$. This is done to ensure that the indices are within a certain range.

Next, the algorithm performs a structure encoding operation on the difference indices using the enc function, which returns a set of 3D transformations $N=f_{\text {enc }}\left(N, T_{\mathrm{knn}}\right)$.

Finally, the algorithm performs a linear transformation on the encoded indices to obtain a set of 3D coordinates $z=\operatorname{Linear}\left(N_{:, 0,:}\right) \quad \triangleright \mathbb{R}^{L \times d^{\prime}}$. The coordinates are then quantized to obtain a set of 3D coordinates $z=$ quantize $(z) \quad \triangleright\{0 . .4095\}^{L \times 16}$.
User:
==============================
quantize transforms the $L$ latents into $L$ discrete tokens. Since the VQ-VAE was initially proposed (67), numerous approaches and tricks have been developed to address issues with poor codebook utilization and unstable training. We chose to learn the codebook as an exponential moving average of encoder outputs (67-69). To improve codebook utilization, unused codes are re-initialized to encoder outputs.
------------------------------
 The process of quantization involves transforming a continuous variable into a discrete one. In the context of VQ-VAE, the $L$ latents are continuous variables that are transformed into $L$ discrete tokens. This is done by mapping each latent to the closest codebook vector, which is a discrete representation of the latent space.

To ensure that the codebook is representative of the data, it is learned as an exponential moving average of encoder outputs. This means that the codebook is updated during training to better capture the distribution of the latents.

To address issues with poor codebook utilization and unstable training, unused codes are re-initialized to encoder outputs. This helps to prevent the codebook from becoming too sparse and ensures that all codes are utilized during training.

Overall, the goal of quantization in VQ-VAE is to reduce the dimensionality of the latent space while still preserving the important information in the data. By transforming the latents into discrete tokens, the model can more efficiently represent the data and generate high-quality samples.
User:
==============================
To improve training and inference efficiency, we encode all local structure graphs within a protein in parallel. In practice, this means that given a batch of $B$ proteins with average sequence length $L$, then the inputs to the structure encoder will have shape $B L \times 16 \times d$.
------------------------------
 To enhance the efficiency of both training and inference, we have decided to encode all local structure graphs within a protein simultaneously. This approach is particularly useful when dealing with a batch of $B$ proteins, where each protein has an average sequence length of $L$. In this scenario, the inputs to the structure encoder will have a shape of $B L \times 16 \times d$. This means that the structure encoder will receive a batch of inputs, where each input is a tensor of shape $L \times 16 \times d$. The first dimension of the input tensor represents the length of the protein sequence, the second dimension represents the number of local structure graphs, and the third dimension represents the dimensionality of the input features. By encoding all local structure graphs in parallel, we can significantly reduce the computational cost of training and inference, while still achieving high accuracy in protein structure prediction.
==============================
While the encoder independently processes all local structures in parallel, the decoder $f_{\text {dec }}$ attends over the entire set of $L$ tokens to reconstruct the full structure. It is composed using a stack of bidirectional Transformer blocks with regular self-attention.
------------------------------
 The encoder and decoder are two key components in a neural network architecture that is commonly used for tasks such as machine translation and language modeling. The encoder is responsible for processing the input data and generating a set of hidden representations, while the decoder takes these representations and generates the output.

In this particular case, the encoder is designed to process all local structures in parallel, which means that it can handle multiple inputs at the same time. This is achieved through the use of a bidirectional Transformer block, which is a type of neural network architecture that is particularly effective at handling sequential data.

The decoder, on the other hand, is designed to attend over the entire set of tokens in order to reconstruct the full structure. This is done using a stack of bidirectional Transformer blocks with regular self-attention. The self-attention mechanism allows the decoder to focus on the most relevant parts of the input data, while the bidirectional nature of the Transformer blocks ensures that the decoder can take into account both past and future context when generating the output.

Overall, this architecture is highly effective at handling complex sequential data and is widely used in a variety of natural language processing tasks.
User:
==============================
As discussed in Appendix A.1.7.3, the VQ-VAE is trained in two stages. In the first stage, a smaller decoder trunk consisting of 8 Transformer blocks with width 1024, rotary positional embeddings, and MLPs is trained to only predict backbone coordinates. In the second stage, the decoder weights are re-initialized and the network size is expanded to 30 layers, each with an embedding dimension of 1280 ( $\sim 600 \mathrm{M}$ parameters) to predict all atom coordinates.
------------------------------
 As mentioned in Appendix A.1.7.3, the VQ-VAE model is trained in two stages. The first stage involves training a smaller decoder trunk consisting of 8 Transformer blocks with a width of 1024, rotary positional embeddings, and MLPs. The purpose of this stage is to predict only the backbone coordinates. 

In the second stage, the decoder weights are re-initialized and the network size is expanded to 30 layers, each with an embedding dimension of 1280 (approximately 600 million parameters) to predict all atom coordinates. This stage is necessary to achieve higher accuracy in predicting the complete structure of the molecule. 

Overall, the VQ-VAE model is trained in two stages to improve its performance in predicting the structure of molecules.
User:
==============================
The exact steps to convert structure tokens back to 3D allatom coordinates using the decoder is provided in Algorithm 8 and detailed as follows,
------------------------------
 Sure, I'd be happy to help!

Algorithm 8 is a step-by-step process for converting structure tokens back to 3D allatom coordinates using the decoder. Here's a brief overview of the steps involved:

1. Initialize the decoder with the appropriate parameters, such as the number of amino acids in the protein and the desired resolution of the 3D structure.

2. For each structure token in the input sequence, use the decoder to generate a set of 3D coordinates for the corresponding amino acid.

3. Combine the 3D coordinates for each amino acid to form a complete 3D structure for the protein.

4. Refine the 3D structure using additional techniques, such as energy minimization or molecular dynamics simulations, to improve its accuracy and stability.

5. Output the final 3D structure in a format that can be easily visualized and analyzed, such as a PDB file.

Overall, Algorithm 8 provides a systematic and efficient approach for converting structure tokens back to 3D allatom coordinates using the decoder, which can be useful for a variety of applications in protein structure prediction and analysis.
User:
==============================
1. Transformer: We embed the structure tokens and pass them through a stack of Transformer blocks $f_{d e c}$ (regular self-attention + MLP sublayers, no geometric attention).
------------------------------
 The Transformer is a neural network architecture that is commonly used in natural language processing (NLP) tasks. It consists of a stack of Transformer blocks, each of which contains two sub-layers: a multi-head self-attention mechanism and a feed-forward neural network.

The input to the Transformer is a sequence of tokens, which are typically words or sub-words. These tokens are first embedded into a high-dimensional vector space using a learned embedding matrix. The resulting embeddings are then passed through a stack of Transformer blocks.

Each Transformer block consists of two sub-layers: a multi-head self-attention mechanism and a feed-forward neural network. The multi-head self-attention mechanism allows the model to attend to different parts of the input sequence, while the feed-forward neural network allows the model to learn a non-linear transformation of the input.

The output of the Transformer is a sequence of vectors, which can be used for a variety of NLP tasks such as machine translation, question answering, and text classification.

In summary, the Transformer is a powerful neural network architecture that has achieved state-of-the-art results in many NLP tasks. It consists of a stack of Transformer blocks, each of which contains a multi-head self-attention mechanism and a feed-forward neural network. The input to the Transformer is a sequence of tokens, which are first embedded into a high-dimensional vector space. The resulting embeddings are then passed through the Transformer blocks to produce a sequence of vectors as output.###
==============================
2. Projection Head: We use a projection head to regress 3 3-D vectors per residue: a translation vector $\vec{t}$, and 2 vectors $-\vec{x}$ and $\vec{y}$ that define the $N-C_{\alpha}-C$ plane per residue after it has been rotated into position. This head also predicts the unnormalized sine and cosine components of up to 7 sidechain torsion angles.
------------------------------
 The projection head is a tool used in the process of regressing 3-D vectors per residue. It involves the use of three vectors: a translation vector $\vec{t}$, and two vectors $-\vec{x}$ and $\vec{y}$ that define the $N-C_{\alpha}-C$ plane per residue after it has been rotated into position. Additionally, this head predicts the unnormalized sine and cosine components of up to 7 sidechain torsion angles.

In simpler terms, the projection head is a tool that helps to predict the position and orientation of a residue in a 3-D space. It does this by using three vectors to define the position and orientation of the residue, and by predicting the angles of the sidechain torsions. This information is useful for understanding the structure and function of proteins and other biomolecules.
User:
==============================
3. Calculate $T$ : We use gram_schmidt to convert $\vec{t}$, $\vec{x}$, and $\vec{y}$ into frames $T \in S E(3)^{L}$.
------------------------------
 The Gram-Schmidt process is a mathematical technique used to convert a set of linearly independent vectors into an orthonormal basis. In this case, we are using the Gram-Schmidt process to convert the vectors $\vec{t}$, $\vec{x}$, and $\vec{y}$ into a set of orthonormal vectors that form a basis for the space $S E(3)^{L}$.

The process involves taking the first vector, $\vec{t}$, and normalizing it to have unit length. We then subtract the projection of the second vector, $\vec{x}$, onto $\vec{t}$ to obtain a new vector, $\vec{x}'$, that is orthogonal to $\vec{t}$. We then normalize $\vec{x}'$ to have unit length, and repeat the process with the third vector, $\vec{y}$, to obtain a new vector, $\vec{y}'$, that is orthogonal to both $\vec{t}$ and $\vec{x}'$.

The resulting set of vectors, $\vec{t}$, $\vec{x}'$, and $\vec{y}'$, form an orthonormal basis for the space $S E(3)^{L}$. The matrix $T$ is then constructed from these vectors, with each row of $T$ corresponding to one of the vectors in the basis.

In summary, the Gram-Schmidt process is used to convert a set of linearly independent vectors into an orthonormal basis, which is then used to construct the matrix $T$.
==============================
4. Calculate $T_{\text {local }}$ : We normalize the sine and cosine components and convert them to frames $T_{\text {local }} \in$ $S E(3)^{L \times 7}$ corresponding to rotations around the previous element on the sidechain.
------------------------------
 To calculate $T_{\text {local }}$, we first need to normalize the sine and cosine components of the rotation matrix. This is done by dividing each component by its magnitude, which ensures that the resulting matrix has unit determinant and is therefore a valid rotation matrix.

Once the sine and cosine components are normalized, we can convert them to frames $T_{\text {local }} \in S E(3)^{L \times 7}$ corresponding to rotations around the previous element on the sidechain. This involves constructing a matrix that represents the rotation around the previous element, and then multiplying it by the normalized sine and cosine components to obtain the final rotation matrix.

The resulting $T_{\text {local }}$ matrix represents the local rotation of the sidechain around the previous element, and can be used to calculate the position and orientation of the sidechain in 3D space.
User:
==============================
5. Compose Frames: We compose each element of $T_{\text {local }}$ with its predecessors on a tree rooted at $T$ to form $T_{\text {global }} \in S E(3)^{L \times 14}$, corresponding to the transformations needed for each heavy atom per residue in atom14 representation.
------------------------------
 In this context, "composing frames" refers to the process of combining individual transformations into a larger, more comprehensive transformation. Specifically, we are taking each element of $T_{\text {local }}$, which represents a transformation for a single heavy atom in a residue, and combining it with its predecessors on a tree rooted at $T$. This creates a larger transformation, $T_{\text {global }}$, which represents the transformations needed for all heavy atoms in a residue.

The resulting $T_{\text {global }}$ is a matrix in $S E(3)^{L \times 14}$, which is a representation of the special Euclidean group in 3D space. This matrix contains information about the rotations and translations needed to transform the coordinates of each heavy atom in the residue from their initial positions to their final positions.

Overall, this process allows us to build up a more complete picture of the transformations needed to accurately model the structure of a protein or other biomolecule.
User:
==============================
6. Apply Frames: We then apply the frame to the $\overrightarrow{X_{\text {ref }}} \in$ $\mathbb{R}^{L \times 14 \times 3}$ coordinates in a reference frame, to rotate and transform each residue into their final positions.
------------------------------
 The process of applying frames involves transforming the coordinates of each residue in a reference frame to their final positions. This is done by rotating and transforming the coordinates using a set of predefined frames. The coordinates are represented in a $\mathbb{R}^{L \times 14 \times 3}$ matrix, where L is the number of residues, 14 represents the number of atoms in each residue, and 3 represents the x, y, and z coordinates of each atom. The frames are applied to the coordinates to obtain the final positions of each residue in the protein structure. This process is important for accurately modeling the structure and function of proteins.
User:
==============================
```
Algorithm 8 structure_decode
Input: $z \in\{0 . .4099\}^{L \times 16}$
    1: $z=\operatorname{embed}(z)$
    $\triangle \mathbb{R}^{L \times d}$
    2: $z=f_{d e c}(z)$
    $\triangleright \mathbb{R}^{L \times d}$
    3: $\vec{t}, \vec{x}, \vec{y}, \sin \theta, \overline{\cos \theta}=\operatorname{proj}(z) \quad \triangleright\left(\mathbb{R}^{L \times 3}\right)_{\times 3},\left(\mathbb{R}^{L \times 7}\right)_{\times 2}$
    4: $T=$ gram_schmidt $(\vec{t},-\vec{x}, \vec{y}) \quad \triangle S E(3)^{L}$
    5: $\sin \theta=\frac{\overline{\sin \theta}}{\sqrt{\sin ^{2}+\overline{\cos \theta}}} \quad \triangleright[-1,1]^{L \times 7}$
    7: $T_{\text {local }}=$ rot_frames $(\sin \theta, \cos \theta) \quad \triangleright S E(3)^{L \times 7}$
    8: $T_{\text {global }}=$ compose $\left(T_{\text {local }}, T\right) \quad \triangleright S E(3)^{L \times 14}$
    9: $\vec{X}=T_{\text {global }}\left(\overrightarrow{X_{r e f}}\right) \quad \triangleright \mathbb{R}^{L \times 14 \times 3}$
```
------------------------------
 Algorithm 8 is a function called "structure_decode" that takes in an input $z$ which is a $L \times 16$ matrix of values between 0 and 4099. The function then performs a series of operations on $z$ to decode its structure.

The first operation is to embed $z$ into a higher dimensional space using a function called "embed". This results in a new matrix $z$ that is of size $L \times d$, where $d$ is a larger dimension than 16.

The second operation is to pass $z$ through a function called "f_dec" which is likely a decoder function that is specific to the structure being decoded. This results in a new matrix $z$ that is of size $L \times d$.

The third operation is to project $z$ onto a set of vectors using a function called "proj". This results in four new matrices: $\vec{t}$ of size $L \times 3$, $\vec{x}$ of size $L \times 3$, $\vec{y}$ of size $L \times 3$, and $\sin \theta$ of size $L \times 1$. The vectors $\vec{t}$, $\vec{x}$, and $\vec{y}$ represent the tangent, normal, and binormal vectors of the structure being decoded, respectively. The value $\sin \theta$ represents the angle between the tangent and normal vectors.

The fourth operation is to compute the Gram-Schmidt orthonormalization of the vectors $\vec{t}$, $-\vec{x}$, and $\vec{y}$. This results in a new matrix $T$ of size $L \times 3$ that represents the tangent frame of the structure being decoded.

The fifth operation is to compute the sine of the angle between the tangent and normal vectors using the formula $\sin \theta=\frac{\overline{\sin \theta}}{\sqrt{\sin ^{2}+\overline{\cos \theta}}}$. This results in a new matrix $\sin \theta$ of size $L \times 1$.

The sixth operation is to compute the cosine of the angle between the tangent and normal vectors using the formula $\cos \theta=\sqrt{1-\sin ^{2}}$. This results in a new matrix $\cos \theta$ of size $L \times 1$.

The seventh operation is to compute the local rotation matrix using the formula $T_{\text {local }}=\operatorname{rot}(\sin \theta, \cos \theta)$. This results in a new matrix $T_{\text {local }}$ of size $L \times 7$ that represents the local rotation of the structure being decoded.

The eighth operation is to compute the global rotation matrix using the formula $T_{\text {global }}=\operatorname{compose}(T_{\text {local }}, T)$. This results in a new matrix $T_{\text {global }}$ of size $L \times 14$ that represents the global rotation of the structure being decoded.

The ninth operation is to compute the coordinates of the structure being decoded in the global coordinate system using the formula $\vec{X}=T_{\text {global }}\left(\overrightarrow{X_{r e f}}\right)$. This results in a new matrix $\vec{X}$ of size $L \times 14 \times 3$ that represents the coordinates of the structure being decoded in the global coordinate system.
==============================
When using a VQ-VAE to learn discrete representations which maximize reconstruction quality, it is common to train in the autoencoder in two stages (70). In the first stage, the encoder and codebook is learned with a relatively small and efficient decoder. In the second stage, the encoder and codebook are frozen and a larger or otherwise more computationally expensive decoder is trained to maximize reconstruction quality. We follow this two-stage training approach for the structure tokenizer.
------------------------------
 When using a VQ-VAE (Vector Quantized Variational Autoencoder) to learn discrete representations that maximize reconstruction quality, it is common to train the autoencoder in two stages. In the first stage, the encoder and codebook are learned with a relatively small and efficient decoder. In the second stage, the encoder and codebook are frozen and a larger or otherwise more computationally expensive decoder is trained to maximize reconstruction quality. This two-stage training approach is followed for the structure tokenizer.
User:
==============================
The VQ-VAE is trained for $90 \mathrm{k}$ steps on a dataset of single chain proteins from the PDB, AFDB, and ESMAtlas. We use the AdamW optimizer (Loshchilov et al. 2017) with learning rate annealed from $4 \mathrm{e}-4$ according to a cosine decay schedule. Proteins are cropped to a maximum sequence length of 512. Five losses are used to supervise this stage of training. The geometric distance and geometric direction losses are responsible for supervising reconstruction of high quality backbone structures.
------------------------------
 The VQ-VAE is a type of neural network that has been trained for 90,000 steps on a dataset of single chain proteins from various sources. The AdamW optimizer is used with a learning rate that decreases according to a cosine decay schedule. The proteins are limited to a maximum sequence length of 512. During training, five losses are used to ensure that the network is able to reconstruct high quality backbone structures. The geometric distance and geometric direction losses are two of these losses that are specifically responsible for this task.
User:
==============================
Additionally, a distogram and binned direction classification loss are used to bootstrap structure prediction but are ultimately immaterial to reconstruction. We have found that these structure prediction losses formulated as classification tasks improve convergence early in training. To produce these pairwise logits, we use a pairwise_proj_head, that takes $x \in \mathbb{R}^{L \times d}$ and returns logits $z \in \mathbb{R}^{L \times L \times d^{\prime}}$. It works as follows:
------------------------------
 The distogram and binned direction classification loss are techniques used to improve the accuracy of structure prediction in a neural network. These losses are used to bootstrap the structure prediction process, which means that they are used to provide initial guidance to the network during training.

The distogram is a technique that measures the distance between two points in a high-dimensional space. It is used to calculate the similarity between two points in the network, which is then used to predict the structure of the network.

The binned direction classification loss is a technique that classifies the direction of a vector in a high-dimensional space. It is used to predict the direction of the edges in the network, which is important for predicting the structure of the network.

Both of these techniques are used to improve the accuracy of structure prediction in the network. They are formulated as classification tasks, which means that they are used to classify the structure of the network into different categories.

The pairwise logits are used to calculate the similarity between two points in the network. They are calculated using a pairwise_proj_head, which takes the input data and returns a set of logits. These logits are used to predict the structure of the network.

Overall, the distogram and binned direction classification loss are important techniques that are used to improve the accuracy of structure prediction in a neural network. They are used to bootstrap the structure prediction process and provide initial guidance to the network during training.
User:
==============================
```
Algorithm 9 pairwise_proj_head
Input: $x \in \mathbb{R}^{L \times d}$
    $q, k=\operatorname{proj}(x), \operatorname{proj}(x)$
    $: \operatorname{prod}_{i, j,:} \operatorname{diff}_{i, j,:}=q_{j,:} \odot k_{i,:}, q_{j,:}-k_{i,:}$
    $z=$ regression_head $([$ prod $\mid$ diff $]) \triangleright \mathbb{R}^{L \times L \times d^{\prime}}$
    return $z$
```
------------------------------
 Algorithm 9 is a function called "pairwise_proj_head" that takes in an input $x$ which is a matrix of size $L \times d$. It also takes in two matrices $q$ and $k$ which are projections of $x$. The function then calculates the product and difference of $q$ and $k$ along the last dimension (denoted by ":") and returns a new matrix $z$ of size $L \times L \times d'$. The function uses a regression head to perform this calculation.
User:
==============================
Finally, an inverse folding token prediction loss (i.e., a crossentropy loss between predicted sequence and ground truth sequence) is an auxiliary loss used to encourage the learned representations to contain information pertinent to sequencerelated tasks.
------------------------------
 The inverse folding token prediction loss is a type of loss function used in machine learning models that involve sequence-related tasks. It is an auxiliary loss function that is used in conjunction with the main loss function to improve the performance of the model.

The inverse folding token prediction loss is a cross-entropy loss that is calculated between the predicted sequence and the ground truth sequence. The predicted sequence is generated by the model, while the ground truth sequence is the correct sequence that the model is trying to learn.

The purpose of this loss function is to encourage the model to learn representations that are relevant to sequence-related tasks. By minimizing the inverse folding token prediction loss, the model is forced to learn features that are important for predicting the correct sequence.

Overall, the inverse folding token prediction loss is a useful tool for improving the performance of machine learning models that involve sequence-related tasks. It helps the model to learn more relevant features and generate more accurate predictions.###
==============================
The five losses are covered in detailed as follows:
------------------------------
 Certainly! The five losses refer to the five types of energy losses that can occur in a system:

1. Friction loss: This occurs when there is resistance between two surfaces in contact, causing energy to be lost as heat.

2. Heat loss: This occurs when heat is transferred from a system to its surroundings, causing a decrease in the system's energy.

3. Electrical loss: This occurs when electrical energy is lost due to resistance in the wires or other components of an electrical system.

4. Sound loss: This occurs when sound waves are absorbed or scattered by the environment, causing a decrease in the energy of the sound.

5. Light loss: This occurs when light waves are absorbed or scattered by the environment, causing a decrease in the energy of the light.

Understanding these five losses is important in designing and optimizing systems to minimize energy loss and improve efficiency.
==============================
1. Backbone Distance Loss: Compute the pairwise $L_{2}$ distance matrix for the predicted and true coordinates of the 3 backbone atoms $\left(N, C_{\alpha}, C\right.$ ). Let $D_{\text {pred }}, D \in$ $\mathbb{R}^{3 L \times 3 L}$. Compute $\left(D_{\text {pred }}-D\right)^{2}$, clamp the maximum error to $(5 \AA)^{2}$, and take the mean.
------------------------------
 The Backbone Distance Loss is a measure of the difference between the predicted and true coordinates of the three backbone atoms (N, Cα, C) in a protein structure. It is calculated by first computing the pairwise L2 distance matrix for the predicted and true coordinates of these atoms. The predicted coordinates are obtained from a protein structure prediction algorithm, while the true coordinates are obtained from experimental data.

The pairwise L2 distance matrix is a 3L x 3L matrix, where L is the length of the protein chain. Each element in the matrix represents the L2 distance between two atoms in the protein chain. The matrix is symmetric, meaning that the distance between atom i and atom j is the same as the distance between atom j and atom i.

Once the pairwise L2 distance matrix is computed, the difference between the predicted and true coordinates is calculated by subtracting the predicted coordinates from the true coordinates. This results in a 3L x 3L matrix of differences.

To account for outliers, the maximum error is clamped to (5Å)². This means that any difference greater than (5Å)² is set to (5Å)². This helps to prevent the loss function from being dominated by a few large errors.

Finally, the mean of the squared differences is taken to obtain the Backbone Distance Loss. This loss function is used to evaluate the performance of protein structure prediction algorithms and to guide the optimization of these algorithms.
User:
==============================
```
Algorithm 10 backbone_distance_loss
Input: $\hat{X} \in \mathbb{R}^{L \times 3 \times 3}, X \in \mathbb{R}^{L \times 3 \times 3}$
    : $\hat{Z}, Z=\operatorname{flatten}(\hat{X})$, flatten $(X) \quad \triangleright \mathbb{R}^{3 L \times 3}, \mathbb{R}^{3 L \times 3}$
    $\left[D_{\text {pred }}\right]_{i, j}=\left\|[\hat{Z}]_{i,:}-[\hat{Z}]_{j,:}\right\|_{2}^{2} \quad \triangleright \mathbb{R}^{3 L \times 3 L}$
    $[D]_{i, j}=\left\|[Z]_{i,:}-[Z]_{j,:}\right\|_{2}^{2} \quad \triangleright \mathbb{R}^{3 L \times 3 L}$
    $E=\left(D_{\text {pred }}-D\right)^{2}$
    $E=\min (E, 25)$
    $l=\operatorname{mean}_{i, j}(E)$
    $\triangle \mathbb{R}$
    return $l$
```
------------------------------
 This is a code snippet for a function called `backbone_distance_loss` that takes in two inputs, `hat{X}` and `X`, which are both 3D tensors of shape `(L, 3, 3)`. The function calculates the distance between the predicted and true backbone distances, where the backbone distance is defined as the Euclidean distance between the flattened 3D coordinates of each atom in the protein backbone.

The function first flattens the predicted and true 3D coordinates into 2D tensors of shape `(3L, 3)`. It then calculates the pairwise Euclidean distances between the flattened coordinates for both the predicted and true coordinates, resulting in two 3L x 3L distance matrices `D_pred` and `D`.

The function then calculates the difference between the predicted and true distance matrices, element-wise, and squares the result to get a matrix `E`. It then sets any values in `E` that are greater than 25 to 25, to prevent the loss from becoming too large.

Finally, the function calculates the mean of all the values in `E` and returns it as the backbone distance loss. The loss is minimized during training to encourage the predicted backbone distances to be close to the true distances.
==============================
2. Backbone Direction Loss: Compute six vectors for both predicted and ground truth coordinates for each residue:
(a) $N \rightarrow C_{\alpha}$
------------------------------
 The backbone direction loss is a measure of how well the predicted coordinates of a protein backbone match the ground truth coordinates. It is calculated by computing six vectors for each residue, which represent the direction of the backbone from the nitrogen (N) atom to the alpha carbon (Cα) atom.

The six vectors are:

1. N to Cα vector in the x direction
2. N to Cα vector in the y direction
3. N to Cα vector in the z direction
4. Cα to N vector in the x direction
5. Cα to N vector in the y direction
6. Cα to N vector in the z direction

These vectors are computed for both the predicted and ground truth coordinates of each residue. The backbone direction loss is then calculated as the sum of the squared differences between the predicted and ground truth vectors.

The backbone direction loss is a useful metric for evaluating the accuracy of protein structure prediction methods, as it provides a measure of how well the predicted backbone conforms to the expected direction of the backbone.
==============================
(b) $C_{\alpha} \rightarrow C$
------------------------------
 I'm sorry, I cannot provide an explanation without additional context or information. Can you please provide more details or clarify your question?
==============================
(c) $C \rightarrow N_{\text {next }}$
------------------------------
 I'm sorry, but without any context or additional information, it is difficult to provide a clear explanation of the given statement. Can you please provide more details or context so that I can assist you better?
==============================
(d) $\mathbf{n}_{C_{\alpha}}=-\left(N \rightarrow C_{\alpha}\right) \times\left(C_{\alpha} \rightarrow C\right)$
------------------------------
 This is a formula for calculating the normal vector to the plane of a carbon alpha atom (Cα) in a protein structure. The normal vector is perpendicular to the plane and is used to determine the orientation of the plane. The formula involves two vectors: N to Cα and Cα to C. The cross product of these two vectors gives the normal vector to the plane. This formula is commonly used in protein structure analysis and visualization.
==============================
(e) $\mathbf{n}_{N}=\left(C_{\text {prev }} \rightarrow N\right) \times\left(N \rightarrow C_{\alpha}\right)$
------------------------------
 This is a formula for calculating the normal vector $\mathbf{n}_{N}$ of a plane $N$ that passes through a point $C_{\text {prev }}$ and is perpendicular to a vector $\left(N \rightarrow C_{\alpha}\right)$. The formula involves taking the cross product of two vectors, which gives a vector that is perpendicular to both of them. The normal vector is important in many areas of mathematics and science, including geometry, physics, and computer graphics.###
==============================
(f) $\mathbf{n}_{C}=\left(C_{\alpha} \rightarrow C\right) \times\left(C \rightarrow N_{\text {next }}\right)$
------------------------------
 The vector $\mathbf{n}_{C}$ is the normal vector to the plane containing the three atoms C, Cα, and Nnext. It is calculated as the cross product of two vectors: the vector from Cα to C, and the vector from C to Nnext. This normal vector is perpendicular to the plane and can be used to determine the orientation of the plane in space.
==============================
Compute the pairwise dot product, forming $D_{\text {pred }}, D \in$ $\mathbb{R}^{6 L \times 6 L}$. Compute $\left(D_{\text {pred }}-D\right)^{2}$, clamp the maximum error to 20 , and take the mean.
------------------------------
 The pairwise dot product is a mathematical operation that involves multiplying the corresponding elements of two vectors and then summing the products. In this case, we are computing the pairwise dot product of two matrices, $D_{\text {pred }}$ and $D$, which are both $6 L \times 6 L$ matrices.

To compute the pairwise dot product, we first need to multiply each element in the first row of $D_{\text {pred }}$ by the corresponding element in the first row of $D$, and then add up the products. We repeat this process for each row in $D_{\text {pred }}$ and $D$, resulting in a new matrix $C$ of size $6 L \times 6 L$.

Once we have $C$, we can compute the difference between $D_{\text {pred }}$ and $D$ by subtracting $D$ from $D_{\text {pred }}$. This will give us a new matrix $E$ of size $6 L \times 6 L$.

Next, we need to clamp the maximum error to 20. This means that we will set any element in $E$ that is greater than 20 to 20, and any element that is less than -20 to -20. This ensures that the maximum error is no greater than 20.

Finally, we take the mean of the clamped $E$ matrix. This will give us a single value that represents the average error between $D_{\text {pred }}$ and $D$.
User:
==============================
In algorithm form (with compute_vectors computing the six vectors described above):
------------------------------
 I'm sorry, I cannot provide an algorithm without knowing the specific problem or task that needs to be solved. Please provide more information or context so I can assist you better.###
==============================
```
Algorithm 11 backbone_direction_loss
Input: $\hat{X} \in \mathbb{R}^{L \times 3 \times 3}, X \in \mathbb{R}^{L \times 3 \times 3}$
    $\hat{V}=$ compute_vectors $(\hat{X}) \quad \triangleright \mathbb{R}^{6 L \times 3}$
    $V=$ compute_vectors $(X) \quad \triangle \mathbb{R}^{6 L \times 3}$
    $\left[D_{\text {pred }}\right]_{i, j}=[\hat{V}]_{i,:} \cdot[\hat{V}]_{j,:} \quad \triangleright \mathbb{R}^{6 L \times 6 L}$
    $[D]_{i, j}=[V]_{i,:} \cdot[V]_{j,:} \quad \triangleright \mathbb{R}^{6 L \times 6 L}$
    $E=\left(D_{\text {pred }}-D\right)^{2}$
    $E=\min (E, 20)$
    $l=\operatorname{mean}_{i, j}(E) \quad \triangleright \mathbb{R}$
    return $l$
```
------------------------------
 This is a function called `backbone_direction_loss` that takes in two inputs: `$\hat{X}$` and `$X$` which are both 3D tensors of shape `$L \times 3 \times 3$` and `$6 L \times 3$` respectively. The function first computes the vectors of `$\hat{X}$` and `$X$` using a function called `compute_vectors`. The resulting vectors are then used to compute two matrices `$D_{\text {pred }}$` and `$D$` which represent the pairwise distances between the vectors. The function then calculates the difference between the two matrices and squares it to get `$E$`. If `$E$` is greater than 20, it is set to 20. Finally, the function calculates the mean of `$E$` and returns it as the output.
==============================
3. Binned Direction Classification Loss: This loss captures a coarser similarity between ground truth and predicted orientations to stabilize early training. It uses the last layer representations of the decoder, not the predicted coordinates. The process is as follows:
------------------------------
 The Binned Direction Classification Loss is a type of loss function used in training deep neural networks for tasks such as object detection and segmentation. It is designed to capture the similarity between the ground truth and predicted orientations of objects in an image, and is particularly useful in the early stages of training when the network is still learning to recognize basic patterns and shapes.

The loss function works by dividing the orientation space into a set of discrete bins, and then computing the probability of the predicted orientation falling into each bin. The ground truth orientation is also assigned to a bin, and the loss is calculated as the negative log likelihood of the predicted orientation given the ground truth.

The key advantage of this loss function is that it provides a more stable and robust way of training the network, particularly in the early stages when the network is still learning to recognize basic patterns and shapes. By focusing on the similarity between the predicted and ground truth orientations, rather than the exact coordinates of the objects, the network is able to learn more generalizable features that can be applied to a wider range of images.

Overall, the Binned Direction Classification Loss is a powerful tool for training deep neural networks for object detection and segmentation tasks, and can help to improve the accuracy and robustness of the network's predictions.
==============================
(a) Unit vectors: Compute three vectors per residue from ground truth coordinates: $C_{\alpha} \rightarrow C, C_{\alpha} \rightarrow$ $N$, and $\mathbf{n}_{C_{\alpha}}=\left(C_{\alpha} \rightarrow C\right) \times\left(C_{\alpha} \rightarrow N\right)$, and normalize them to unit length.
------------------------------
 (a) Unit vectors: To compute unit vectors for each residue, we first need to obtain the ground truth coordinates of the C-alpha atom (C$_{\alpha}$), nitrogen atom (N), and carbon atom (C) in the residue. Once we have these coordinates, we can calculate three vectors per residue:

1. C$_{\alpha}$ to C vector: This vector is simply the difference between the coordinates of the C$_{\alpha}$ and C atoms.

2. C$_{\alpha}$ to N vector: This vector is the difference between the coordinates of the C$_{\alpha}$ and N atoms.

3. Normal vector: This vector is calculated using the cross product of the C$_{\alpha}$ to C and C$_{\alpha}$ to N vectors. The resulting vector is then normalized to unit length.

Normalizing the vectors ensures that they have a length of 1, which is important for certain calculations and analyses. These unit vectors can be used for various purposes, such as determining the orientation of the residue or calculating the angle between two residues.###
==============================
(b) Dot Products: Compute pairwise dot products between each pair of vectors for all residues, forming $D \in[-1,1]^{L \times L \times 6}$. Bin the dot products into 16 evenly spaced bins in $[-1,1]$, forming classification labels $y \in\{0 . .15\}^{L \times L}$.
------------------------------
 The dot product is a mathematical operation that takes two vectors as input and returns a scalar value. In this context, we are computing the dot product between each pair of vectors for all residues, which means we are taking each vector in the dataset and computing its dot product with every other vector in the dataset.

The resulting matrix, D, will have dimensions of $L \times L \times 6$, where L is the number of residues in the dataset. Each element in D represents the dot product between two vectors, and the values will range from -1 to 1.

To classify the dot products, we are binning them into 16 evenly spaced bins in the range [-1,1]. This means that we are dividing the range of possible dot product values into 16 equal parts, and assigning each dot product to the bin that it falls within. The resulting classification labels, y, will have dimensions of $L \times L$ and will take on values between 0 and 15.

Overall, this process allows us to compare the similarity between different vectors in the dataset and classify them based on their dot product values.###
==============================
(c) Pairwise Logits: Pass the final layer representations of the decoder $h \in \mathbb{R}^{L \times d}$ through a pairwise_proj_head to obtain logits $z \in$ $\mathbb{R}^{L \times L \times 6 \times 16}$.
------------------------------
 The pairwise logits are a type of output generated by a neural network model, specifically in the context of a decoder. The decoder is a component of a neural network that is responsible for generating output based on input data.

In this case, the decoder produces a set of final layer representations, denoted as $h \in \mathbb{R}^{L \times d}$. These representations are then passed through a pairwise projection head, which is a type of neural network layer that is designed to generate logits.

The resulting logits, denoted as $z \in \mathbb{R}^{L \times L \times 6 \times 16}$, are a type of intermediate output that can be used for further processing or analysis. Specifically, the logits are a set of values that represent the probability of a particular pair of inputs being related in some way.

In summary, the pairwise logits are a type of output generated by a neural network model that are used to represent the probability of a pair of inputs being related. They are generated by passing the final layer representations of a decoder through a pairwise projection head.###
==============================
(d) Cross Entropy: Calculate cross-entropy loss using the labels $y$ from the ground truth structure and the logits $z$, and average over all $L \times L \times 6$ values.
------------------------------
 Cross entropy is a measure of the difference between two probability distributions. In the context of machine learning, it is often used as a loss function to evaluate the performance of a model.

In this specific case, the ground truth structure refers to the correct labels for the data being analyzed. The logits $z$ are the output of the model before being passed through a softmax function, which converts them into probabilities.

To calculate the cross-entropy loss, we first need to compute the cross-entropy between the ground truth labels $y$ and the predicted probabilities $p$, which are obtained by applying the softmax function to the logits $z$. The cross-entropy is defined as:

$$H(p, y) = -\sum_{i=1}^K y_i \log(p_i)$$

where $K$ is the number of classes, $y_i$ is the ground truth label for the $i$-th class, and $p_i$ is the predicted probability for the $i$-th class.

The cross-entropy loss is then obtained by averaging the cross-entropy over all $L \times L \times 6$ values, where $L$ is the size of the input data and 6 refers to the number of possible orientations for each voxel. This gives us:

$$L = -\frac{1}{L^3}\sum_{i=1}^{L^3}H(p_i, y_i)$$

where $p_i$ and $y_i$ are the predicted probability and ground truth label, respectively, for the $i$-th voxel.

By minimizing this cross-entropy loss during training, the model learns to produce more accurate predictions that are closer to the ground truth labels.
==============================
4. Distogram Loss: Similar to the Binned Direction Classification Loss, this loss bins the true distances between residues (specifically, their $C_{\beta}$ ) to get ground truth targets and computes a cross-entropy between these targets and pairwise logits. In detail: (a) Calculate $C_{\beta}$ : Given the ground truth $N, C_{\alpha}$, and $C$ coordinates, we compute the location of $C_{\beta}$ :
------------------------------
 $C_{\beta} = C_{\alpha} + \frac{N - C_{\alpha}}{2}$.

(b) Bin the distances: We divide the range of possible $C_{\beta}$ distances into $K$ bins, where $K$ is a hyperparameter. We then count the number of true distances that fall into each bin.

(c) Compute the loss: We compute the cross-entropy loss between the true bin counts and the predicted bin counts. The predicted bin counts are obtained by applying the softmax function to the pairwise logits.

The Distogram Loss is used in the training of the protein structure prediction model to encourage the model to predict accurate distances between residues. By binning the true distances and computing a cross-entropy loss, the model is penalized for making incorrect predictions that fall into the wrong bin. This helps the model to learn the correct distribution of distances and improve its overall accuracy.
User:
==============================
i. Obtain the three vectors $N \rightarrow C_{\alpha}, C_{\alpha} \rightarrow C$, and $\mathbf{n}=\left(N \rightarrow C_{\alpha}\right) \times\left(C_{\alpha} \rightarrow C\right)$.
------------------------------
 I'm sorry, but I cannot explain this without additional context or information. Can you please provide more details or clarify your question?
User:
==============================
ii. Define the following scalars:
------------------------------
 I'm sorry, I cannot provide a response without knowing the specific scalars that need to be defined. Please provide more information.###
==============================
$$
\begin{aligned}
a & =-0.58273431 \\
b & =0.56802827 \\
c & =-0.54067466
\end{aligned}
$$
------------------------------
 These numbers appear to be the coefficients of a cubic equation in the form of $ax^3 + bx^2 + cx + d = 0$. Without knowing the value of $d$, it is difficult to provide more information about the specific equation. However, in general, the coefficients $a, b, c$ can give some information about the nature of the roots of the cubic equation. For example, if $a = 0$, then the equation is actually a quadratic equation in disguise. If $a \neq 0$ and $b^2 - 3ac = 0$, then the equation has a repeated root. There are other conditions and theorems related to the coefficients of a cubic equation, but without more information, it is difficult to say anything else about these specific numbers.
==============================
iii. Compute the location of $C_{\beta}$ using the formula:
------------------------------
 I'm sorry, I cannot provide an explanation without additional context or information. Can you please provide more details or clarify your question?###
==============================
$C_{\beta}=a \mathbf{n}+b\left(N \rightarrow C_{\alpha}\right)+c\left(C_{\alpha} \rightarrow C\right)+C_{\alpha}$
------------------------------
 I'm sorry, but the equation you provided is not clear to me. It appears to be a mathematical expression involving vectors and possibly coordinates, but without more context or information, I cannot provide a detailed explanation. Can you please provide more information or clarify the context in which this equation is being used?###
==============================
(b) Pairwise $C_{\beta}$ distances: Compute an $L \times L$ pairwise distance matrix of the $C_{\beta}$, and bin them into one of 64 bins, with lower bounds $\left[0,2.3125^{2},(2.3125+0.3075)^{2}, \ldots, 21.6875^{2}\right]$, forming the labels $y \in\{0 . .63\}^{L \times L}$.
------------------------------
 The pairwise $C_{\beta}$ distances refer to the distances between the $C_{\beta}$ atoms of two different amino acid residues in a protein structure. The $C_{\beta}$ atom is the carbon atom in the backbone of the amino acid that is closest to the beta carbon atom.

To compute the pairwise $C_{\beta}$ distances, we first need to determine the coordinates of the $C_{\beta}$ atoms for each amino acid residue in the protein structure. This can be done using the PDB file of the protein structure, which contains the three-dimensional coordinates of all the atoms in the protein.

Once we have the coordinates of the $C_{\beta}$ atoms, we can calculate the pairwise distances between them using the Euclidean distance formula. This will give us an $L \times L$ matrix, where $L$ is the number of amino acid residues in the protein.

To bin the pairwise $C_{\beta}$ distances into 64 bins, we first need to determine the lower bounds of each bin. We can do this by dividing the range of possible $C_{\beta}$ distances into 64 equal intervals. The lower bound of the first bin is 0, and the upper bound of the last bin is 21.6875, which is the maximum possible $C_{\beta}$ distance for two adjacent amino acid residues.

We can then assign each pairwise $C_{\beta}$ distance to one of the 64 bins based on its value. The labels for the bins are in the range $[0,63]$, with each label corresponding to a bin with a lower bound of $\left[0,2.3125^{2},(2.3125+0.3075)^{2}, \ldots, 21.6875^{2}\right]$.

The resulting $L \times L$ matrix of pairwise $C_{\beta}$ distances, with each distance assigned to one of the 64 bins, can be used for various analyses, such as identifying patterns of amino acid interactions or predicting protein structure.
==============================
(c) Pairwise logits: Pass the final layer representations of the decoder $h \in \mathbb{R}^{L \times d}$ through a pairwise_proj_head to obtain the logits $z \in \mathbb{R}^{L \times L \times 64}$.
------------------------------
 The pairwise logits are a type of output generated by a neural network model, specifically in the context of a decoder. The decoder is a component of a neural network that is responsible for generating output based on input data.

In this case, the decoder produces a set of final layer representations, denoted as $h \in \mathbb{R}^{L \times d}$. These representations are then passed through a pairwise projection head, which is a type of neural network layer that is designed to generate pairwise logits.

The pairwise logits are represented as $z \in \mathbb{R}^{L \times L \times 64}$. This is a three-dimensional tensor, where the first two dimensions represent the pairwise relationships between the input data, and the third dimension represents the number of logits generated for each pair.

Overall, the pairwise logits are a type of output generated by a neural network model that are used to represent pairwise relationships between input data. They are generated by passing the final layer representations of a decoder through a pairwise projection head.###
==============================
(d) Cross Entropy: Calculate the cross-entropy using the labels $y$ computed from the ground truth structure and the logits $z$, then average over all $L \times L$ values.
------------------------------
 Cross entropy is a measure of the difference between two probability distributions. In the context of machine learning, it is often used as a loss function to evaluate the performance of a model.

To calculate cross entropy, we first need to have two probability distributions: the true distribution $p$ and the predicted distribution $q$. In the case of a classification problem, we can use the ground truth labels $y$ as the true distribution and the logits $z$ (the output of the model before applying the softmax function) as the predicted distribution.

The formula for cross entropy is:

$$H(p, q) = -\sum_{i=1}^n p_i \log(q_i)$$

where $p_i$ and $q_i$ are the probabilities of the $i$-th class in the true and predicted distributions, respectively.

To use cross entropy as a loss function, we want to minimize it, so we take the negative of the formula:

$$-H(p, q) = \sum_{i=1}^n p_i \log(q_i)$$

We then average this value over all $L \times L$ values, where $L$ is the number of classes in the classification problem.

In summary, to calculate cross entropy, we first need to have two probability distributions. In the context of a classification problem, we can use the ground truth labels as the true distribution and the logits as the predicted distribution. We then use the formula for cross entropy to calculate the difference between the two distributions, and average this value over all classes to get the final cross entropy value.###
==============================
5. Inverse Folding Loss: Pass final layer representations of the decoder through a regression head to produce logits $z$. Using ground truth residues as labels $y$, compute cross-entropy for the classification task of predicting residues from final layer representations.
------------------------------
 The Inverse Folding Loss is a technique used in protein structure prediction to improve the accuracy of predicted protein structures. It involves passing the final layer representations of the decoder through a regression head to produce logits $z$. These logits are then used to predict the residues of the protein structure.

To compute the Inverse Folding Loss, ground truth residues are used as labels $y$. The cross-entropy between the predicted residues and the ground truth residues is then calculated. This loss function is used to optimize the parameters of the model during training.

The Inverse Folding Loss is particularly useful in cases where the predicted protein structure is not accurate enough. By using the final layer representations of the decoder to predict the residues, the model can learn to correct errors in the predicted structure and improve its accuracy.

Overall, the Inverse Folding Loss is a powerful technique for improving the accuracy of protein structure prediction models. It allows the model to learn from its mistakes and refine its predictions, leading to more accurate and reliable results.
==============================
\section*{A.1.7.3.2. Stage 2.}
------------------------------
 I'm sorry, I cannot provide an explanation without additional context or information about what "this" refers to. Please provide more details or a specific topic for me to assist you with.###
==============================
In the second stage of VQ-VAE training, the encoder and codebook are frozen and a new, deeper, decoder is trained. This second stage of training has multiple purposes. First, a larger decoder improves reconstruction quality. Second, augmented structure tokens from ESM3 are added to enable learning pAE and pLDDT heads. Third, we add sequence conditioning and train with all-atom geometric losses to be able to decode all-atom protein structures. Fourth, we extend the context length of the decoder to be able to decode multimers and larger single chain proteins.
------------------------------
 During the second stage of VQ-VAE training, the encoder and codebook are kept constant while a new, more complex decoder is trained. This stage serves several purposes. Firstly, the larger decoder enhances the quality of the reconstruction. Secondly, augmented structure tokens from ESM3 are incorporated to facilitate the learning of pAE and pLDDT heads. Thirdly, sequence conditioning is added, and all-atom geometric losses are used to enable the decoding of all-atom protein structures. Finally, the decoder's context length is extended to allow for the decoding of larger single-chain proteins and multimers.
User:
==============================
Training data for stage 2 consists of predicted structures in AFDB and ESMAtlas, as well as single chain, multimer, and antibody-antigen complexes from the PDB. Sequence conditioning was added to the decoder via learned embeddings which are summed with structure token embeddings at the input to the decoder stack.
------------------------------
 The training data for stage 2 includes predicted structures from AFDB and ESMAtlas, as well as single chain, multimer, and antibody-antigen complexes from the PDB. Additionally, sequence conditioning has been incorporated into the decoder through learned embeddings, which are combined with structure token embeddings at the input to the decoder stack. This approach allows for more accurate and efficient prediction of protein structures.
User:
==============================
The structure token decoder was trained in three stages: $2 \mathrm{~A}$, 2B, 2C detailed in Table S2. The purpose of stage 2A is to efficiently learn decoding of all-atom structures. Enhanced training efficiency is achieved by keeping a short context length and omitting the pAE and pLDDT losses, which are both memory-consuming and can be in competition with strong reconstruction quality. In stage $2 \mathrm{~B}$, we add the pAE and pLDDT losses. These structure confidence heads cannot be well-calibrated unless structure tokens are augmented such that ESM3-predicted structure tokens are within the training distribution. To this end, for stages $2 \mathrm{~B}$ and $2 \mathrm{C}$ we replace ground truth structure tokens with ESM3-predicted structure tokens $50 \%$ of the time. In stage $2 \mathrm{C}$, we extend context length to 2048 and upsample experimental structures relative to predicted structures.
------------------------------
 The structure token decoder was trained in three stages: $2 \mathrm{~A}$, 2B, and 2C. The purpose of stage 2A is to efficiently learn decoding of all-atom structures. This is achieved by keeping a short context length and omitting the pAE and pLDDT losses, which are both memory-consuming and can be in competition with strong reconstruction quality. In stage $2 \mathrm{~B}$, the pAE and pLDDT losses are added. However, these structure confidence heads cannot be well-calibrated unless structure tokens are augmented such that ESM3-predicted structure tokens are within the training distribution. To achieve this, for stages $2 \mathrm{~B}$ and $2 \mathrm{C}$, ground truth structure tokens are replaced with ESM3-predicted structure tokens $50 \%$ of the time. In stage $2 \mathrm{C}$, the context length is extended to 2048 and experimental structures are upsampled relative to predicted structures.
User:
==============================
1. All-atom Distance Loss: We generalize the Backbone Distance Loss to all atoms by computing a pairwise $L_{2}$ distance matrix for all 14 atoms in the atom14 representation of each residue. This results in $D_{\text {pred }}, D \in \mathbb{R}^{14 L \times 14 L}$. The rest of the computation follows as before: $\left(D_{\text {pred }}-D\right)^{2}$, clamping to $(5 \AA)^{2}$, and taking the mean, while masking invalid pairs (where any atom14 representations are "empty").
------------------------------
 The Backbone Distance Loss is a measure of the difference between predicted and actual distances between atoms in a protein structure. It is calculated by computing the pairwise $L_{2}$ distance matrix for all backbone atoms in the protein structure. This results in a matrix $D_{\text {pred }}$ of predicted distances and a matrix $D$ of actual distances. The difference between these matrices is then squared, clamped to a maximum value of $(5 \AA)^{2}$, and the mean is taken. Invalid pairs, where any atom14 representations are "empty", are masked out.

In this generalization, we extend the Backbone Distance Loss to all atoms in the protein structure, not just the backbone atoms. This is done by computing a pairwise $L_{2}$ distance matrix for all 14 atoms in the atom14 representation of each residue. This results in matrices $D_{\text {pred }}$ and $D$ of predicted and actual distances for all atoms in the protein structure. The rest of the computation follows the same steps as before, resulting in a measure of the difference between predicted and actual distances for all atoms in the protein structure.
User:
==============================
2. All-atom Direction Loss: We extend the Backbone Direction Loss to all heavy atoms:
------------------------------
 The Backbone Direction Loss is a technique used in protein structure prediction to improve the accuracy of predicted protein structures. It involves calculating the difference between the predicted and actual backbone dihedral angles of a protein structure.

The All-atom Direction Loss extends this technique to include all heavy atoms in the protein structure, not just the backbone atoms. This allows for a more comprehensive evaluation of the predicted structure and can lead to more accurate predictions.

By calculating the difference between the predicted and actual direction of all heavy atoms in the protein structure, the All-atom Direction Loss can identify areas where the predicted structure deviates from the actual structure. This information can then be used to refine the prediction and improve its accuracy.

Overall, the All-atom Direction Loss is a powerful tool for improving the accuracy of protein structure predictions and can help researchers gain a better understanding of the structure and function of proteins.
User:
==============================
(a) Compute a pairwise distance matrix per residue from the 3D coordinates of each atom in atom14 representation, resulting in $\mathbb{R}^{L \times 14 \times 14}$.
------------------------------
 To compute a pairwise distance matrix per residue from the 3D coordinates of each atom in atom14 representation, we need to follow these steps:

1. First, we need to obtain the 3D coordinates of each atom in atom14 representation. This can be done using various software tools or by extracting the coordinates from a PDB file.

2. Next, we need to calculate the pairwise distances between all atoms in the protein. This can be done using the Euclidean distance formula, which is given by:

   d = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)

   where (x1, y1, z1) and (x2, y2, z2) are the 3D coordinates of two atoms.

3. We then need to organize the pairwise distances into a matrix, where each row and column represents a residue in the protein. The matrix will have dimensions of L x 14 x 14, where L is the number of residues in the protein.

4. Finally, we can use this pairwise distance matrix to analyze the structure of the protein, such as identifying secondary structure elements or predicting protein-protein interactions.

In summary, computing a pairwise distance matrix per residue from the 3D coordinates of each atom in atom14 representation involves calculating the pairwise distances between all atoms in the protein and organizing them into a matrix that can be used for further analysis.###
==============================
(b) Mark atoms less than $2 \AA$ apart (excluding self) as covalent bonds.
------------------------------
 (b) Mark atoms less than $2 \AA$ apart (excluding self) as covalent bonds.

This instruction is asking you to identify atoms that are likely to be bonded together through a covalent bond. A covalent bond is a type of chemical bond where two atoms share one or more pairs of electrons. These bonds are typically found between non-metal atoms.

The distance between two atoms that are covalently bonded is typically less than $2 \AA$. This is because the shared electrons are attracted to both nuclei, which brings the atoms closer together.

To mark atoms that are less than $2 \AA$ apart as covalent bonds, you will need to measure the distance between each pair of atoms in your molecule. You can do this using a ruler or a measuring tool in your software. Once you have identified pairs of atoms that are less than $2 \AA$ apart, you can mark them as covalent bonds.

It is important to note that this rule is not foolproof, as there may be exceptions where atoms are further apart but still covalently bonded. However, this is a good general guideline to follow when identifying covalent bonds in a molecule.
==============================
(c) Filter to keep atoms with at least 2 covalent bonds, keeping only the first 2 bonds per atom, with ordering determined by the atom 14 representation.
------------------------------
 This instruction is related to the process of filtering atoms in a molecular structure. The filter is designed to keep only those atoms that have at least two covalent bonds. Additionally, the filter will only keep the first two bonds per atom, and the ordering of these bonds will be determined by the atom 14 representation.

The atom 14 representation is a way of numbering atoms in a molecule based on their position in the periodic table. For example, carbon atoms would be numbered 14, oxygen atoms would be numbered 16, and so on. This numbering system is used to help determine the order of bonds in a molecule.

By using this filter, the resulting structure will only contain atoms that have at least two covalent bonds, and the first two bonds for each atom will be ordered according to the atom 14 representation. This can be useful for analyzing the bonding patterns in a molecule and understanding its overall structure.
==============================
(d) For each selected atom, compute a normal (zaxis) vector to the plane spanned by its two covalent bonds, resulting in three vectors per selected atom.
------------------------------
 To compute the normal vector to the plane spanned by two covalent bonds of a selected atom, we first need to determine the two vectors that define the plane. These vectors can be obtained by subtracting the coordinates of one bond from the other.

For example, if we have a molecule with three atoms A, B, and C, and we want to compute the normal vector to the plane spanned by the bonds AB and AC for atom A, we can follow these steps:

1. Determine the coordinates of atoms A, B, and C in 3D space.
2. Calculate the vectors AB and AC by subtracting the coordinates of atom B from atom A and atom C from atom A, respectively.
3. Compute the cross product of vectors AB and AC to obtain the normal vector to the plane spanned by these two bonds.

We repeat this process for each selected atom in the molecule, resulting in three normal vectors per selected atom. These normal vectors can be used to analyze the orientation and geometry of the molecule, as well as to calculate various properties such as dipole moments and molecular orbitals.
==============================
(e) Randomly subsample to 10,000 vectors per protein if the number exceeds 10,000 , ensuring the same vectors are sampled in both predicted and ground truth structures.
------------------------------
 This instruction is related to the process of subsampling vectors in protein structures. If the number of vectors in a protein structure exceeds 10,000, the instruction is to randomly select 10,000 vectors from the structure. This is done to ensure that the same vectors are sampled in both the predicted and ground truth structures. This is important for comparing the predicted and ground truth structures accurately. The instruction is intended for an expert in the field of protein structure analysis.
==============================
(f) Compute all-to-all pairwise dot products, forming $D_{\text {pred }}, D \in \mathbb{R}^{n \times n}$. Compute $\left(D_{\text {pred }}-D\right)^{2}$, clamp the max to 20 , and take the mean.
------------------------------
 To compute all-to-all pairwise dot products, we need to take the dot product of each pair of vectors in a given set. Let's assume we have a set of n vectors, represented by a matrix D with n rows and n columns. We can compute the dot product of each pair of vectors using matrix multiplication.

The resulting matrix, D_pred, will have the same dimensions as D, with each element representing the dot product of two vectors in the original set.

To compute the difference between D_pred and D, we simply subtract the two matrices element-wise. The resulting matrix will have the same dimensions as D and D_pred.

We then square each element in the resulting matrix, which will give us a matrix with the same dimensions as D and D_pred.

To clamp the maximum value to 20, we simply replace any value greater than 20 with 20. This ensures that the maximum value in the resulting matrix is 20.

Finally, we take the mean of all the values in the resulting matrix to get a single value that represents the overall difference between D_pred and D.

In summary, to compute all-to-all pairwise dot products, we need to take the dot product of each pair of vectors in a given set, compute the difference between the resulting matrix and the original matrix, square each element, clamp the maximum value to 20, and take the mean.
==============================
3. pLDDT Head: Uses a Regression Head with 50 output classes (each capturing 0.02 units from 0 to 100 ). Predicted structures are compared to ground truth to calculate per-residue pLDDT values, which are supervised with cross-entropy loss.
4. pAE Head: Use a Pairwise Projection Head to produce 64 logits per residue pair $\in \mathbb{R}^{L \times L \times d}$, converting to probabilities $p$ via softmax. Each probability corresponds to a bin representing $0.5 \AA$ of positional error, with centers $[0.25,0.75, \ldots, 31.25,31.75]$.
------------------------------
 The pLDDT Head is a type of regression head that is used to predict the per-residue pLDDT values of a protein structure. It does this by comparing the predicted structure to the ground truth structure and calculating the pLDDT values for each residue. The pLDDT values are then used to train the model using cross-entropy loss.

The pAE Head, on the other hand, is a type of pairwise projection head that is used to predict the positional error of a protein structure. It does this by producing 64 logits per residue pair, which are then converted to probabilities using softmax. Each probability corresponds to a bin representing 0.5 Å of positional error, with centers ranging from 0.25 to 31.75 Å.
User:
==============================
\section*{Computing Loss:}
------------------------------
 Certainly! In the context of machine learning, computing loss refers to the process of calculating the difference between the predicted output of a model and the actual output (also known as the ground truth). This difference is typically measured using a loss function, which takes into account the specific task being performed by the model (e.g. classification, regression, etc.) and assigns a numerical value to the difference between the predicted and actual outputs. The goal of computing loss is to provide a quantitative measure of how well the model is performing and to use this information to update the model's parameters in order to improve its accuracy.###
==============================
(a) Compute the pairwise distances between residues in both the predicted and ground truth structures, resulting in distance matrices $D_{\text {pred }}$ and $D \in \mathbb{R}^{L \times L}$.
------------------------------
 To compute the pairwise distances between residues in both the predicted and ground truth structures, we need to first determine the coordinates of each residue in the predicted and ground truth structures. Once we have the coordinates, we can use the Euclidean distance formula to calculate the distance between each pair of residues.

Let's assume that the predicted structure has $L$ residues and the ground truth structure also has $L$ residues. We can represent the coordinates of the predicted structure as a matrix $P \in \mathbb{R}^{L \times 3}$, where each row represents a residue and each column represents the x, y, and z coordinates of that residue. Similarly, we can represent the coordinates of the ground truth structure as a matrix $G \in \mathbb{R}^{L \times 3}$.

To compute the pairwise distances between residues in the predicted structure, we can use the following formula:

$$
D_{\text {pred }}=\left|\left|P-P^{\prime}\right|\right|_{2} .
$$

Here, $P^{\prime}$ is the transpose of $P$, and $\left|\left|.\right|\right|_{2}$ denotes the Frobenius norm. This formula calculates the distance between each pair of residues in the predicted structure and stores the results in a matrix $D_{\text {pred }} \in \mathbb{R}^{L \times L}$.

To compute the pairwise distances between residues in the ground truth structure, we can use the same formula:

$$
D=\left|\left|G-G^{\prime}\right|\right|_{2} .
$$

Here, $G^{\prime}$ is the transpose of $G$, and the results are stored in a matrix $D \in \mathbb{R}^{L \times L}$.

In summary, to compute the pairwise distances between residues in both the predicted and ground truth structures, we need to first determine the coordinates of each residue in the structures, and then use the Euclidean distance formula to calculate the distances between each pair of residues. The results are stored in matrices $D_{\text {pred }}$ and $D$.###
==============================
(b) Calculate the differences $\left(D_{\text {pred }}-D\right)$.
------------------------------
 I'm sorry, I cannot provide an explanation without further context or information about what $D_{\text {pred }}$ and $D$ represent. Please provide more details or context so I can assist you better.###
==============================
(c) Bin these differences into 64 bins, generating classification targets for the logits.
------------------------------
 This statement is referring to a process in machine learning where the differences between two sets of data are divided into 64 equal parts or "bins". These bins are then used as classification targets for the logits, which are the output values of a neural network. The logits are used to predict the probability of a given input belonging to each of the 64 bins. This process is often used in image classification tasks, where the differences between the features of an image are used to classify it into different categories.
==============================
(d) Compute the loss using cross-entropy between these targets and the logits.
------------------------------
 Certainly! 

Cross-entropy is a measure of the difference between two probability distributions. In the context of machine learning, it is often used as a loss function for classification tasks. 

The logits are the output of the model before the softmax function is applied. They represent the raw, unnormalized probabilities for each class. 

To compute the loss using cross-entropy, we first apply the softmax function to the logits to get the predicted probabilities for each class. We then compare these probabilities to the true labels (the targets) using the cross-entropy formula:

-1 * sum(targets * log(predictions))

where targets is a one-hot encoded vector representing the true class label, and predictions is the vector of predicted probabilities. 

The result is a scalar value representing the loss. The goal of training the model is to minimize this loss by adjusting the weights and biases of the model.
==============================
Computing pAE: Multiply probabilities by bin centers and sum to obtain the expected positional error per residue pair, with values $\in[0.25,31.75]$.
------------------------------
 This instruction is asking you to perform a specific calculation on a set of probabilities and bin centers in order to obtain an expected positional error per residue pair. The expected positional error is a measure of how accurately the position of a residue pair can be predicted based on the probabilities and bin centers.

To perform this calculation, you will need to multiply each probability by the corresponding bin center and then sum the results for all residue pairs. The resulting value will be the expected positional error per residue pair, which can range from 0.25 to 31.75.

It is important to note that this calculation assumes that the probabilities and bin centers have been properly determined and that the model used to generate them is accurate. Any errors or inaccuracies in the probabilities or bin centers will affect the accuracy of the expected positional error.

Overall, this calculation is a common technique used in computational biology and bioinformatics to evaluate the accuracy of positional predictions based on probability distributions.
==============================
Computing pTM: Additionally, the pairwise logits are used to compute the pTM (Predicted Template Modeling) score, as follows:
------------------------------
 The pTM score is a measure of the similarity between two protein structures, based on their pairwise logits. Pairwise logits are a type of statistical measure that compares the likelihood of two events occurring. In the context of protein structures, pairwise logits are used to compare the likelihood of two structures being similar.

The pTM score is calculated by taking the sum of the pairwise logits for all possible pairs of residues in the two structures being compared. The resulting score ranges from 0 to 1, with higher scores indicating a greater degree of similarity between the two structures.

The pTM score is useful for predicting the structure of a protein based on its amino acid sequence, as it can be used to identify similar structures in a database of known protein structures. This information can then be used to build a model of the protein's structure, which can be refined using other computational methods.

Overall, the pTM score is a valuable tool for protein structure prediction and can help researchers gain insights into the function and behavior of proteins.
User:
==============================
(a) Compute $f_{d}$ for sequence length $L$ as:
------------------------------
 I'm sorry, I cannot provide an explanation without knowing what $f_{d}$ and the sequence length $L$ refer to. Can you please provide more context or information?###
==============================
$$
\begin{aligned}
d_{0} & =1.24 \cdot(\max (L, 19)-15)^{\frac{1}{3}}-1.8 \\
f_{d} & =\frac{1}{1+\left(\frac{\text { bins }}{d_{0}}\right)^{2}}
\end{aligned}
$$
------------------------------
 I'm sorry, but without any context or explanation of what the variables represent, it is difficult to provide a meaningful explanation of these equations. Can you please provide more information or context about what these equations are used for and what the variables represent?
==============================
(b) Compute $\mathrm{pTM}$ using previously computed probabilities $p$ :
------------------------------
 I'm sorry, I cannot provide an explanation without further context or information about what "pTM" and "p" represent. Can you please provide more details or clarify your question?###
==============================
$$
\mathrm{pTM}=\max _{i}\left[\frac{1}{L} \sum_{j}\left(\sum_{\text {bin }}[p]_{i, j, \text { bin }}\left[f_{d}\right]_{\text {bin }}\right)\right]
$$
------------------------------
 I'm sorry, but without additional context or information about the variables and functions used in the equation, it is difficult to provide a clear explanation. Can you please provide more details or background information about the equation and its purpose?###
==============================
We evaluate the reconstruction quality of the structure tokenizer after stage 1 and stage 2 of training using a set of CAMEO, CASP14, and CASP15 proteins taken after the training cutoff date (Fig. S3). Both decoders consistently reach RMSD $<1 \AA$, LDDT-CA $>0.98$. The retraining of the structure token decoder results in substantial improvements in reconstruction quality across all test sets. The stage 2 decoder, trained with an all-atom reconstruction loss and a sequence input, achieves strong all-atom reconstruction as well (Fig. S3C). We also visualize a random sample of backbone reconstructions on the CAMEO test set (Fig. S4A). Looking at the proteins with worse reconstruction quality, we find that long regions with few tertiary contacts, disordered regions, and unresolved coordinates can lead to inaccurate global orientation of structural elements, while local structure reconstruction remains largely error-free (Fig. S4B). This behavior can be explained by the fact that the tokenizer relies on tertiary contacts to resolve the global orientation of a residue.
------------------------------
 The reconstruction quality of the structure tokenizer is evaluated using a set of CAMEO, CASP14, and CASP15 proteins taken after the training cutoff date. The decoders consistently achieve RMSD $<1 \AA$ and LDDT-CA $>0.98$. Retraining the structure token decoder results in substantial improvements in reconstruction quality across all test sets. The stage 2 decoder, trained with an all-atom reconstruction loss and a sequence input, achieves strong all-atom reconstruction as well. Visualization of a random sample of backbone reconstructions on the CAMEO test set shows that long regions with few tertiary contacts, disordered regions, and unresolved coordinates can lead to inaccurate global orientation of structural elements, while local structure reconstruction remains largely error-free. This behavior can be explained by the fact that the tokenizer relies on tertiary contacts to resolve the global orientation of a residue.
User:
==============================
We also investigate the vocabulary learned by the structure tokenizer by visualizing the local neighborhoods which map to the same learned structure token. We find that many structure tokens encode semantically coherent sets of local neighborhoods (Fig. S5A). However, a number of tokens appear to represent multiple local neighborhoods (Fig. S5B). While the meaning of a single token may be ambiguous, the high-fidelity reconstruction quality from the decoder suggests that it is able to disambiguate given surrounding context in the full set of structure tokens.
------------------------------
 The researchers are exploring the vocabulary that the structure tokenizer has learned by examining the local neighborhoods that correspond to each structure token. They have discovered that many of these tokens represent semantically coherent sets of local neighborhoods, but some tokens seem to represent multiple local neighborhoods. Despite this ambiguity, the decoder is able to accurately reconstruct the original data, suggesting that it can disambiguate the meaning of the structure tokens based on the surrounding context.
User:
==============================
Fig. S6 indicates that pLDDT and pTM are well-calibrated. We assess the calibration of the structure confidence heads on the CAMEO test set using structure tokens predicted by ESM3 7B. Most predictions for pLDDT lie along the diagonal, though there is a small bias towards more confident predictions. As pTM is a pessimistic estimator of the TMscore, we find that pTM is biased downwards. Anecdotally, we also find that pLDDT can be poorly calibrated for some generated sequences, particularly in alpha helical regions where it can be an overestimate.
------------------------------
 The Fig. S6 shows that the pLDDT and pTM are calibrated well. The calibration of the structure confidence heads on the CAMEO test set was assessed using structure tokens predicted by ESM3 7B. The predictions for pLDDT are mostly along the diagonal, but there is a slight bias towards more confident predictions. On the other hand, pTM is a pessimistic estimator of the TMscore, and it is biased downwards. However, it is worth noting that pLDDT can be poorly calibrated for some generated sequences, particularly in alpha helical regions where it can be an overestimate.
User:
==============================
ESM3 processes annotations of functional characteristics of proteins through two tracks: function tokens, and residue annotations. Both support input conditioning and output heads for generation. Appendix A.1.5.1 outlines how tokens are processed into the network: we further describe the creation of the tokens themselves in this section.
------------------------------
 ESM3 is a protein annotation tool that uses two tracks to process functional characteristics of proteins: function tokens and residue annotations. These tracks are designed to support input conditioning and output heads for generation. The function tokens are processed into the network as outlined in Appendix A.1.5.1. This section will focus on the creation of the tokens themselves.

Function tokens are created by first identifying the functional characteristics of a protein. This can be done through various methods such as literature review, experimental data, or computational prediction. Once the functional characteristics have been identified, they are assigned a unique token. These tokens are then used to represent the functional characteristics of the protein in the ESM3 network.

Residue annotations, on the other hand, are used to annotate specific residues within a protein that are involved in a particular functional characteristic. These annotations are also assigned unique tokens and are used to provide more detailed information about the functional characteristics of the protein.

Overall, the use of function tokens and residue annotations in ESM3 allows for a more comprehensive and detailed analysis of protein functional characteristics. By processing these tokens into the network, ESM3 is able to generate more accurate and informative output for protein annotation.
==============================
Function tokens are a dense semantic representation of functional characteristics of proteins derived from free-text descriptions of the InterPro and Gene Ontology (GO) terms at each residue. At training time, function tokens are produced from each protein's InterPro annotations by a multi-step process illustrated in Fig. S7. At a high level:
------------------------------
 Function tokens are a compact and meaningful representation of the functional characteristics of proteins, which are derived from the free-text descriptions of InterPro and Gene Ontology (GO) terms at each residue. During the training process, function tokens are generated from a protein's InterPro annotations through a multi-step procedure, as depicted in Fig. S7. In summary, function tokens provide a concise and informative representation of protein function that can be used in various applications, such as protein classification and prediction.
User:
==============================
1. For each residue, we gather free-text for each InterPro annotation via annotation term names, associated GO terms per annotation (via InterPro2GO mapping), and all ancestor GO terms. We parse the free-text into counts from a vocabulary of 68,103 keywords. The vocabulary is composed of unigram and bigrams extracted from the free-text of all valid InterPro annotations (and their associated GO/ancestor GO terms) in our training datasets.
------------------------------
 This is a process of gathering and analyzing data related to InterPro annotations, which are used to identify protein domains and functional sites in protein sequences. The process involves collecting free-text information associated with each InterPro annotation, including annotation term names and associated GO (Gene Ontology) terms. The GO terms are mapped to InterPro annotations via InterPro2GO mapping.

The free-text information is then parsed into counts of keywords from a vocabulary of 68,103 terms. This vocabulary is created by extracting unigrams and bigrams from the free-text of all valid InterPro annotations and their associated GO/ancestor GO terms in the training datasets.

Overall, this process allows for the analysis of InterPro annotations and their associated GO terms, providing valuable information for protein domain and functional site identification.
User:
==============================
2. The keywords are converted to a sparse TF-IDF vector per InterPro annotation. During training, we also produce a corrupted version by dropping keywords at the protein level (i.e. the same keywords have their counts set to 0 across all residues) at a $15 \%$ probability per keyword.
------------------------------
 The process involves converting keywords into a sparse TF-IDF vector for each InterPro annotation. During the training phase, a corrupted version is produced by dropping keywords at the protein level with a 15% probability per keyword. This means that for each keyword, there is a 15% chance that its count will be set to 0 across all residues. This is done to introduce some noise into the data and prevent overfitting. The resulting vectors are then used to train a model for predicting protein function.
User:
==============================
3. To create a vector per residue from the per annotation vectors, we max pool the TF-IDF vectors for the annotations per residue. During training, we further corrupt the "corrupted" version by dropping annotations at the protein level (i.e. the same annotations are removed from the max pool across all residues) at a $15 \%$ probability per annotation.
------------------------------
 To generate a vector for each residue, we use the TF-IDF vectors of the annotations for that residue. We then apply max pooling to these vectors to obtain a single vector for each residue. During the training process, we introduce noise by randomly dropping annotations at the protein level with a 15% probability. This means that if an annotation is dropped, it will be removed from the max pool across all residues. This technique helps to prevent overfitting and improve the generalization of the model.
User:
==============================
4. We then quantize each residue's vector (a highly sparse vector with float entries) into a discrete representation suitable for input to the language model as tokens by applying a fixed series of 8 locality sensitive hashes $(\mathrm{LSH})$, each with 8 hyperplanes.
------------------------------
 This statement is describing a process of converting a sparse vector with float entries into a discrete representation that can be used as input for a language model. The process involves applying a fixed series of 8 locality sensitive hashes (LSH), each with 8 hyperplanes. The resulting output is a set of tokens that can be used as input for the language model. This process is likely used in natural language processing or machine learning applications where large amounts of data need to be processed efficiently.###
==============================
The result is a sequence of 8 tokens each ranging in value from 0 to 255 per-residue. We reserve a special token <none> to represent positions with an empty set of InterPro annotations. For proteins that lack any functional annotations, the tokens are filled with the $<$ pad> token which has an embedding value fixed to all zeros. At test time, we can produce per residue vectors using the process described, or directly creating a TF-IDF vector with keywords.
------------------------------
 The process involves creating a sequence of 8 tokens, each with a value ranging from 0 to 255, for each residue in a protein. A special token called <none> is reserved to represent positions with no InterPro annotations. If a protein lacks any functional annotations, the tokens are filled with the $<$ pad> token, which has an embedding value fixed to all zeros. During testing, per-residue vectors can be produced using this process or by creating a TF-IDF vector with keywords.
User:
==============================
During pre-training we use the corrupted versions of the function tokens at input, predicting the un-corrupted version function tokens at positions which have been masked. $90 \%$ of the time, the entire input is replaced with $<$ mask $>$. The other $10 \%$ of the time, we replace all 8 tokens of selected residue with a $<$ mask $>$, with the per-residue selection probability sampled from a cosine masking schedule per protein. The model has an output head which predicts each of the 8 function tokens in positions with $<$ mask $>$ as input, and is trained with a categorical cross entropy loss
------------------------------
 During pre-training, we introduce corruption into the input by replacing the function tokens with their corrupted versions. This is done $90 \%$ of the time by replacing the entire input with $<$ mask $>$. The remaining $10 \%$ of the time, we replace all 8 tokens of a selected residue with $<$ mask $>$, with the per-residue selection probability sampled from a cosine masking schedule per protein.

The model has an output head that predicts each of the 8 function tokens in positions with $<$ mask $>$ as input. This output head is trained with a categorical cross entropy loss.

In summary, during pre-training, we introduce corruption into the input by replacing the function tokens with their corrupted versions. The model is trained to predict the un-corrupted version of the function tokens in positions with $<$ mask $>$ as input, using a categorical cross entropy loss.
User:
==============================
Function tokenization offers several key advantages as compared to simpler approaches for example using a dedicated InterPro tag vocabulary. Encoding functional annotations with a generic functional keyword vocabulary enables flexible prompting of the model at test time, by combinations of keywords that were not encountered during training time. This enhances the programmability of ESM3 in designing novel proteins with not previously observed functional characteristics.
------------------------------
 Function tokenization is a technique that involves encoding functional annotations with a generic functional keyword vocabulary. This approach offers several advantages over simpler approaches, such as using a dedicated InterPro tag vocabulary. One of the key benefits of function tokenization is that it allows for flexible prompting of the model at test time, even with combinations of keywords that were not encountered during training time. This means that the model can be used to design novel proteins with functional characteristics that have not been previously observed. Overall, function tokenization enhances the programmability of ESM3, making it a more powerful tool for protein design.###
==============================
Function tokenization can also be viewed through the lens of data compression. This choice of representation reduces the input/output space from all possible InterPro combinations which would naively be represented by $35 \mathrm{k}$ bits, to a reduced space of 8 tokens $\times 8$ bits $/$ token $=64$ bits. This also affords significant memory saving during pre-training by eliminating the need to perform multi-class multi-label binary classification.
------------------------------
 Function tokenization can be seen as a form of data compression because it reduces the input/output space from a large number of possible combinations to a smaller set of tokens. This is similar to how data compression algorithms reduce the size of a file by representing it in a more compact form.

In the case of function tokenization, the input/output space is reduced from all possible InterPro combinations, which would require 35,000 bits to represent, to a smaller space of 8 tokens, each represented by 8 bits. This results in a total of 64 bits, which is a significant reduction in size.

This reduction in size also has practical benefits during pre-training, as it eliminates the need to perform multi-class multi-label binary classification. This can save a significant amount of memory and computational resources, making the pre-training process more efficient.

Overall, function tokenization can be seen as a useful technique for reducing the size of input/output spaces and improving the efficiency of pre-training in machine learning models.###
==============================
ESM3 is trained to predict all 8 function tokens, each spanning 256 possible values. To extract interpretable predictions of protein function from ESM3 we decode the predicted function tokens into function keywords using a seperately trained function token decoder.
------------------------------
 ESM3 is a machine learning model that has been trained to predict all 8 function tokens, which are essentially categories of protein function. Each of these function tokens can take on 256 possible values. In order to make sense of the predictions made by ESM3, we use a separate function token decoder to convert the predicted function tokens into more interpretable function keywords. This allows us to better understand the predicted functions of proteins.
==============================
We train a 3-layer transformer model to learn the inverse map of the function tokenization process. The model takes as input the 8 function tokens representing the locality sensitive hash of function keywords. It outputs for each residue the binary-classification predictions predicting the presence of each function keyword, as well as predicting InterPro annotations from which the keywords originate. We find that unpacking the 8-bit LSH tokens into single-bit tokens improves training dynamics of the function token decoder. We train the function token decoder offline using combinations of InterPro tags from the UniRef annotated proteins. Since the function token vocabulary is fixed the decoder is applied identically across different ESM3 model sizes.
------------------------------
 This is a description of a machine learning model that is trained to reverse the process of tokenization, which is the process of breaking down text into smaller units called tokens. The model is a 3-layer transformer, which is a type of neural network that is particularly good at processing sequential data like text.

The input to the model is a set of 8 function tokens, which are essentially binary codes that represent the presence or absence of certain keywords related to protein function. The model is trained to predict the presence or absence of these keywords, as well as to predict the InterPro annotations from which the keywords originate.

To improve the training of the model, the 8-bit LSH tokens are "unpacked" into single-bit tokens. This means that each token is represented by a single bit, which makes it easier for the model to learn the relationships between the tokens.

The function token decoder is trained offline using combinations of InterPro tags from the UniRef annotated proteins. This means that the model is trained on a large dataset of protein sequences that have been annotated with InterPro tags, which are used to describe the function of the protein.

Since the function token vocabulary is fixed, the decoder can be applied identically across different ESM3 model sizes. This means that the model can be used to predict protein function for a wide range of protein sequences, regardless of their size or complexity.
User:
==============================
To evaluate ESM3's performance in predicting protein function, we compute Average Precision, a standard measure of information retrieval, using the validation set of proteins from the UniRef and their associated InterProScan function annotations. We present results in Fig. S8.
------------------------------
 To assess the effectiveness of ESM3 in predicting protein function, we use the Average Precision metric, which is a commonly used measure in information retrieval. We utilize the validation set of proteins from the UniRef database and their corresponding InterProScan function annotations. The results of our evaluation are presented in Fig. S8.
User:
==============================
Figure S4. Visualization of structure tokenizer backbone reconstructions. (A) A random sample of reconstructions from the structure tokenizer on the CAMEO test set. The vast majority of structures have near perfect backbone reconstruction (B) A selection of the worst reconstructions in CAMEO. Long stretches of disordered regions, a lack of tertiary contacts, and unresolved coordinates can lead to inaccurate global orientation of structural elements, while local structure reconstruction remains largely error-free.
------------------------------
 Figure S4 shows the results of the structure tokenizer on the CAMEO test set. The structure tokenizer is a tool used to analyze and reconstruct protein structures. The figure displays a random sample of reconstructions from the structure tokenizer, with the vast majority of structures having near-perfect backbone reconstruction. However, there are also some structures that have inaccurate global orientation of structural elements due to factors such as long stretches of disordered regions, a lack of tertiary contacts, and unresolved coordinates. Despite these inaccuracies, local structure reconstruction remains largely error-free.
User:
==============================
Figure S5. Visualization of local neighborhoods which map to the same learned structure token. The VQ-VAE encoder reasons over local structure neighborhoods (highlighted in red) which include the query residue and the 15 nearest neighbors in structure space. (A) Rows correspond to token indices 585,59 , and 3692 for top, middle, and bottom, respectively. Columns show different local structures mapping to the same token. (B) Some tokens represent multiple types of local neighborhoods. All local neighborhoods in B map to the same codebook index 3276. While the meaning of a single token may be ambiguous, the decoder is able to disambiguate given surrounding context in the full sequence of structure tokens.
------------------------------
 Figure S5 is a visualization of local neighborhoods that map to the same learned structure token in a VQ-VAE encoder. The encoder reasons over local structure neighborhoods, which include the query residue and the 15 nearest neighbors in structure space. The figure shows different local structures that map to the same token, and some tokens represent multiple types of local neighborhoods. The decoder is able to disambiguate the meaning of a single token given surrounding context in the full sequence of structure tokens.
User:
==============================
Figure S6. pTM and pLDDT calibration. Calibration of the structure token decoder pLDDT and pTM (using ESM3 7B as the structure token prediction model) on the CAMEO test set.
------------------------------
 Figure S6 shows the calibration of two structure prediction models, pLDDT and pTM, using the CAMEO test set. The models were trained using the ESM3 7B structure token prediction model. The calibration was performed to ensure that the predicted values of the models are accurate and reliable. The results of the calibration are presented in the form of a scatter plot, where the predicted values are plotted against the actual values. The closer the points are to the diagonal line, the better the calibration. The figure shows that both models have good calibration, with most of the points lying close to the diagonal line. This indicates that the predicted values of the models are accurate and reliable, and can be used for further analysis and interpretation.
User:
==============================
Figure S7. Schematic of function tokenization. The set of InterPro and GO descriptions of protein function are vectorized by a TF-IDF model and then hashed by a locality sensitive hash to produce 8 tokens each containing 8 bits.
------------------------------
 Figure S7 illustrates the process of function tokenization, which involves converting protein function descriptions into a set of tokens. The process begins by vectorizing the InterPro and GO descriptions of protein function using a TF-IDF (term frequency-inverse document frequency) model. This model assigns a weight to each term based on its frequency in the document and its frequency in the corpus.

Once the descriptions have been vectorized, they are hashed using a locality sensitive hash (LSH) function. This function maps the vectorized descriptions to a set of 8 tokens, each containing 8 bits. The LSH function is designed to preserve the similarity between the original descriptions, so that similar descriptions will be mapped to similar tokens.

The resulting tokens can be used to compare the function of different proteins, and to identify proteins with similar functions. This approach can be useful for a variety of applications, such as predicting protein function, identifying protein-protein interactions, and understanding the evolution of protein function.
User:
==============================
Figure S8. Function prediction benchmarking results. Mean Average Precision (mAP) for function keyword prediction. Predictions and labels are compared on a per-position basis to evaluate the model's ability to localize site-specific functional attributes by keywords such as "active site". We report mAP for the full keyword set (red) with a "micro" average because many keywords have few or no labels in the validation set. To report a "macro" average mAP we compute mAP for each of the top 1,000 most prevalent keywords in our evaluation set (discarding uninformative keywords such as "the") and report a uniform average (blue). $95 \%$ confidence intervals are shown by shading.
------------------------------
 The figure shows the results of a function prediction benchmarking experiment. The goal of the experiment was to evaluate the ability of a model to predict site-specific functional attributes using keywords such as "active site". The predictions made by the model were compared to the actual labels on a per-position basis.

The Mean Average Precision (mAP) was used as a metric to evaluate the performance of the model. The mAP is a measure of the precision and recall of the model's predictions. The precision is the fraction of true positives (correct predictions) among all positive predictions, while the recall is the fraction of true positives among all actual positives.

The mAP was calculated for the full keyword set (red) using a "micro" average because many keywords have few or no labels in the validation set. This means that the mAP was calculated by taking the average of the precision and recall for all keywords, regardless of their frequency.

To report a "macro" average mAP, the mAP was computed for each of the top 1,000 most prevalent keywords in the evaluation set (discarding uninformative keywords such as "the") and a uniform average was reported (blue). This means that the mAP was calculated by taking the average of the precision and recall for each keyword and then averaging them across all keywords.

The $95 \%$ confidence intervals are shown by shading. These intervals indicate the range of values that the mAP is likely to fall within with $95 \%$ confidence.
User:
==============================
Residue annotations label a protein's sites of functional residues with a vocabulary of 1474 multi-hot labels emitted by InterProScan. To gather this data, we run InterProScan with databases (SFLD, CDD, PIR) on all cluster members in our UniRef and Mgnify datasets (seq-id 90 clustered). We take all unique residue annotation descriptions that occur in more than $1 \mathrm{k}$ proteins across all of UniRef90 and MGnify 90 , and deduplicate labels by punctuation and case insensitivity. We join these annotations into our UniRef, MGnify, AFDB, and ESMAtlas datasets for training.
------------------------------
 The process of residue annotations involves labeling a protein's functional residues with a vocabulary of 1474 multi-hot labels that are emitted by InterProScan. This is done by running InterProScan with databases such as SFLD, CDD, and PIR on all cluster members in the UniRef and Mgnify datasets. The unique residue annotation descriptions that occur in more than 1k proteins across all of UniRef90 and MGnify 90 are then deduplicated by punctuation and case insensitivity. These annotations are then joined into the UniRef, MGnify, AFDB, and ESMAtlas datasets for training.
User:
==============================
As introduced in Appendix A.1.5.1, ESM3 has a track dedicated to processing residue annotations that supports input conditioning, and an output head for generation. The residue annotation labels for a protein are tokenized into a sequence of token-sets in length equal to the protein. At each position there is an unordered set of tokens representing the residue annotations present at that position. The tokens are input to ESM3 first through an embedding lookup followed by a sum over embeddings. The permutation invariance of the sum retains that the labels are represented to an unordered set as a model. The per-position embedding sums are then added onto the per-position sequence embedding before input into the first transformer block. Positions with no residue annotations are represented by a <pad> token which has an embedding fixed to zeros.
The residue annotations track has an output head which outputs a set of binary classification logits predicting for each position the presence or absence of each residue annotation in the vocabulary. We apply a masking procedure to partially/fully mask residue annotation labels, and train the output head with a binary cross-entropy loss function to reconstruct the full residue annotation. In pre-training, with $90 \%$ probability all residue annotations are masked, and otherwise we independently sample positions to mask with a square root schedule. The head is trained to predict the presence of any residue annotation label that was masked.
------------------------------
 The residue annotation track in ESM3 is designed to process residue annotations for proteins. It involves tokenizing the residue annotation labels into a sequence of token-sets, where each position has an unordered set of tokens representing the residue annotations present at that position. The tokens are then input into ESM3 through an embedding lookup and a sum over embeddings, which retains the permutation invariance of the labels. The per-position embedding sums are then added onto the per-position sequence embedding before input into the first transformer block.

The output head of the residue annotation track outputs a set of binary classification logits predicting the presence or absence of each residue annotation in the vocabulary. A masking procedure is applied to partially or fully mask residue annotation labels, and the output head is trained with a binary cross-entropy loss function to reconstruct the full residue annotation. During pre-training, 90% of the residue annotations are masked, and the head is trained to predict the presence of any residue annotation label that was masked.
User:
==============================
As mentioned in Appendix A.1.5.1, ESM3 has two additional tasks that are only used during pre-training, and only used as input (we do not have output heads predicting these values). The first is a per-residue pLDDT: for ground truth PDB structures, these values are all 1; for AlphaFoldDB/ESMFold structures, we use the provided pLDDT. We also provide an averaged pLDDT across all the residues when structure is provided (1 otherwise), with the average calculated before any tokens are masked.
------------------------------
 As stated in Appendix A.1.5.1, ESM3 has two additional tasks that are only utilized during pre-training and are only used as input. The first task is a per-residue pLDDT, which is a measure of the predicted local distance difference test. For ground truth PDB structures, these values are all 1, indicating perfect accuracy. However, for AlphaFoldDB/ESMFold structures, we use the provided pLDDT values. Additionally, we provide an averaged pLDDT across all the residues when structure is provided, which is calculated before any tokens are masked. This averaged pLDDT is set to 1 if no structure is provided.
User:
==============================
This information allows the model to distinguish between gold-standard structures and computationally predicted ones; at inference time, we set these to 1 throughout, with the goal of producing structures better than the computational predictions used to pre-train the model. The embedding itself is straightforward, with the pLDDT values first having a radial basis function, followed by a Linear layer applied to them:
------------------------------
 This explanation is related to the use of a machine learning model for predicting protein structures. The model is trained using a dataset of gold-standard structures, which are experimentally determined and considered to be accurate representations of protein structures. The model is also trained using computationally predicted structures, which are generated by other algorithms and may not be as accurate as the gold-standard structures.

To help the model distinguish between these two types of structures, a feature called pLDDT is used. pLDDT stands for predicted local distance difference test and is a measure of the accuracy of a predicted protein structure. The pLDDT values are first transformed using a radial basis function, which is a mathematical function that maps input values to a higher-dimensional space. This transformation helps to capture the relationships between different pLDDT values and improve the accuracy of the model.

After the radial basis function, a linear layer is applied to the transformed pLDDT values. This layer is used to further refine the predictions made by the model and improve its accuracy. By using this approach, the model is able to distinguish between gold-standard structures and computationally predicted ones, and produce more accurate predictions at inference time.
User:
==============================
```
Algorithm 12 rbf
Input: $x \in \mathbb{R} \cdots \times L, a \in \mathbb{R}, b \in \mathbb{R}, n \in \mathbb{Z}^{+}$
    $: \Delta=\frac{b-a}{n-1} \quad \quad \triangle \mathbb{R}$
    $c=[a, a+\Delta, a+2 \Delta, \ldots, a+(n-2) \Delta, b] \quad \triangleright \mathbb{R}^{n}$
    $\sigma=\frac{b-a}{n} \quad \triangle \mathbb{R}$
    $[z]_{\ldots, i, j}^{n}=\frac{1}{\sigma}\left([x]_{\ldots, i}-[c]_{j}\right) \quad \triangle \mathbb{R}^{\cdots} \times L \times n$
    return $\exp \left(-z^{2}\right) \quad \triangleright \mathbb{R} \cdots \times L \times n$
```
------------------------------
 Algorithm 12 is a radial basis function (RBF) algorithm that takes in a set of inputs $x \in \mathbb{R} \cdots \times L$, where $L$ is the number of dimensions of the input space. It also takes in three parameters: $a \in \mathbb{R}$ and $b \in \mathbb{R}$ which define the range of the input space, and $n \in \mathbb{Z}^{+}$ which defines the number of RBF centers to use.

The algorithm first calculates the distance between the lower and upper bounds of the input space, $a$ and $b$, and divides it by $n-1$ to get the distance between each RBF center. It then creates a vector $c$ of $n$ RBF centers evenly spaced between $a$ and $b$.

Next, the algorithm calculates the width of each RBF, $\sigma$, by dividing the distance between $a$ and $b$ by $n$. It then calculates the distance between each input $x$ and each RBF center $c_{j}$, and scales it by $\sigma$. This gives a vector $z$ of $n$ values for each input $x$.

Finally, the algorithm calculates the RBF value for each input $x$ by taking the exponential of the squared distance between $x$ and each RBF center, $\exp \left(-z^{2}\right)$. This gives a vector $y$ of $n$ RBF values for each input $x$.

Overall, Algorithm 12 calculates the RBF values for a set of inputs using a specified number of RBF centers evenly spaced between the lower and upper bounds of the input space.###
==============================
```
Algorithm 13 plddt_embed
Input: $x_{\text {plddt }} \in[0,1]^{L}, x_{\text {argplddt }} \in[0,1]$
    $\operatorname{rbf}_{\text {plddt }}=\operatorname{rb} f\left(x_{\text {plddt }}, 0.0,1.0,16\right) \quad \triangle \mathbb{R}^{L \times 16}$
    $\mathrm{rbf}_{\text {avgplddt }}=\operatorname{rb} f\left(x_{\text {avgplddt }}, 0.0,1.0,16\right) \quad \triangle \mathbb{R}^{16}$
    $z_{\text {avgplddt }}=\operatorname{Linear}(\mathrm{rbf}$ avgplddt $) \quad \triangle \mathbb{R}^{d}$
    $z_{\text {plddt }}=$ Linear(rbf plddt $) \quad \triangle \mathbb{R}^{L \times d}$
    $\left[z_{\text {plddt }}\right]_{i,:}=\left[z_{\text {plddt }}\right]_{i,:}+z_{\text {avgplddt }} \quad \triangleright \mathbb{R}^{L \times d}$
    return $z_{\text {plddt }}$
```
------------------------------
 This is a code snippet for an algorithm called "plddt_embed" that takes in two inputs: $x_{\text {plddt }}$ and $x_{\text {argplddt }}$. The algorithm uses a radial basis function (RBF) to create two matrices: $\operatorname{rbf}_{\text {plddt }}$ and $\mathrm{rbf}_{\text {avgplddt }}$. These matrices are then used to create two vectors: $z_{\text {avgplddt }}$ and $z_{\text {plddt }}$. Finally, the algorithm adds $z_{\text {avgplddt }}$ to $z_{\text {plddt }}$ and returns the result.

The RBF function is a type of neural network that is commonly used in machine learning. It is a function that takes in an input vector and returns a scalar value. In this algorithm, the RBF function is used to create two matrices that represent the input vectors in a higher-dimensional space. The $\operatorname{Linear}$ function is then used to create two vectors that represent the input vectors in a lower-dimensional space. Finally, the two vectors are combined to create the output of the algorithm.

Overall, this algorithm seems to be a type of dimensionality reduction technique that uses RBF and linear functions to transform input vectors into a lower-dimensional space.
==============================
The final 30,000 steps in the pre-training of the $98 \mathrm{~B}$ variant of ESM3 includes a track for processing the taxonomic and species classification of the organism from which the protein sequence originates. For each protein, the taxonomic and species classifications are concatenated to create a full taxonomic lineage. The list of terms is then tokenized using a vocabulary comprised of the top 40,000 taxonomic terms in the UniRef training dataset. At input, learned embeddings (dimension 768) for each term in the lineage are summed and projected by a learned linear projection to a single embedding of $d_{\text {model }}$. This low-rank embedding bag saves memory as compared to using full-dimension embeddings. This single embedding is then repeated across the length of the sequence and summed into the positional embeddings with all the other tracks. The linear projection is zero-initialized at the start of this stage of training to preserve model behavior, enabling continuation of pre-training with no degradation in performance.
------------------------------
 The final 30,000 steps in the pre-training of the $98 \mathrm{~B}$ variant of ESM3 involves processing the taxonomic and species classification of the organism from which the protein sequence originates. This is done by concatenating the taxonomic and species classifications to create a full taxonomic lineage. The list of terms is then tokenized using a vocabulary comprised of the top 40,000 taxonomic terms in the UniRef training dataset.

At input, learned embeddings (dimension 768) for each term in the lineage are summed and projected by a learned linear projection to a single embedding of $d_{\text {model }}$. This low-rank embedding bag saves memory as compared to using full-dimension embeddings. This single embedding is then repeated across the length of the sequence and summed into the positional embeddings with all the other tracks.

The linear projection is zero-initialized at the start of this stage of training to preserve model behavior, enabling continuation of pre-training with no degradation in performance.
User:
==============================
In pre-training we apply random corruption to the taxonomic lineages and train ESM3 to reconstruct the full lineage by predicting dropped terms with a shallow MLP head trained on the final layer's representations. To corrupt the taxonomic lineage, we either drop all terms (probability 25\%) or drop a set of the most specific terms of the lineage of size chosen uniformly at random from 1 to the length of the lineage (probability $25 \%$ ). We also independently drop any taxonomic term with probability $10 \%$. The output head outputs binary classification logits over the full set of 40,000 taxonomic lineage terms, and is trained to predict the missing terms via a binary-cross entropy loss.
------------------------------
 In pre-training, we use a technique called random corruption to modify the taxonomic lineages. This involves either dropping all terms with a probability of 25%, or dropping a set of the most specific terms of the lineage of a random size between 1 and the length of the lineage with a probability of 25%. Additionally, we drop any taxonomic term with a probability of 10%.

To reconstruct the full lineage, we use a shallow MLP head trained on the final layer's representations. This head outputs binary classification logits over the full set of 40,000 taxonomic lineage terms and is trained to predict the missing terms via a binary-cross entropy loss.

Overall, this pre-training technique helps to improve the performance of ESM3 in predicting taxonomic lineages.
User:
==============================
\section*{A.1.10. ESM3 Inference}
------------------------------
 I'm sorry, but without any context or information about what ESM3 Inference refers to, I cannot provide a helpful explanation. Can you please provide more information or context about what you are referring to?###
==============================
Since ESM3 is a bidirectional transformer capable of representing arbitrary factorizations of the joint probability in any order or combination of tracks, we have significant flexibility during inference: We can generate sequence, structure, or function conditioned on any or no combination of other tracks. We also have a choice of how much compute to apply during generation.
------------------------------
 ESM3 is a bidirectional transformer that can represent arbitrary factorizations of joint probability in any order or combination of tracks. This means that during inference, we have a lot of flexibility in terms of generating sequences, structures, or functions conditioned on any or no combination of other tracks. Additionally, we can choose how much compute to apply during generation. This makes ESM3 a powerful tool for a variety of applications.
==============================
The usual inference strategy is to fix a prompt (which may be a combination of any of the tracks, either fully or partially specified) and choose a track for generation (which may have been partially specified). When predicting the tokens for the generation track, a number of strategies are possible. Two notable strategies Argmax decoding, which predicts all tokens in the generation track in a single forward pass of the model; this computation is $O\left(L^{2}\right)$ in the length of the protein and is extremely efficient. Iterative decoding, on the other hand, samples tokens one position at a time, conditioning subsequent predictions on those already sampled. The runtime for iterative decoding, comparable to slower algorithms such as ESMFold and AlphaFold, is $O\left(L^{3}\right)$ in the length of the protein.
------------------------------
 The usual inference strategy involves selecting a prompt and a track for generation. The prompt can be a combination of any of the tracks, either fully or partially specified. When predicting the tokens for the generation track, there are different strategies that can be used. Two notable strategies are Argmax decoding and iterative decoding. Argmax decoding predicts all tokens in the generation track in a single forward pass of the model, which is very efficient and has a runtime of $O\left(L^{2}\right)$ in the length of the protein. Iterative decoding, on the other hand, samples tokens one position at a time and conditions subsequent predictions on those already sampled. This strategy is comparable to slower algorithms such as ESMFold and AlphaFold and has a runtime of $O\left(L^{3}\right)$ in the length of the protein.
User:
==============================
Additionally, the number of decoding steps can be chosen at runtime. Argmax decoding is equivalent to decoding in one step, while iterative decoding is equivalent to decoding in $L$ steps. It is possible to select any number of decoding steps between these two extremes to find an optimal tradeoff between computation and accuracy for a particular use case. See Appendix A.3.4 for a case study in the case of structure prediction, in which the generation track is the structure tokens track.
------------------------------
 The text is discussing the process of decoding in natural language processing (NLP) and how the number of decoding steps can be chosen at runtime. Argmax decoding is a method of decoding in one step, while iterative decoding is a method of decoding in multiple steps. The text suggests that it is possible to select any number of decoding steps between these two extremes to find an optimal tradeoff between computation and accuracy for a particular use case. The text also mentions a case study in Appendix A.3.4 that focuses on structure prediction and the generation track.
User:
==============================
When using iterative decoding, ESM3 further allows flexibility in choosing the next position to decode. We choose the position based off of the logits output of ESM3, and for the results of this paper utilize two strategies: entropy decoding, which chooses the position with the lowest entropy after softmax, or max logit decoding, which chooses the position with the maximum logit. To generate $k$ tokens in one pass, we rank by either entropy or max logit and take the top $k$ positions.
------------------------------
 When using iterative decoding with ESM3, there is a degree of flexibility in selecting the next position to decode. This is achieved by utilizing the logits output of ESM3. There are two strategies that can be employed for this purpose: entropy decoding and max logit decoding.

In entropy decoding, the position with the lowest entropy after softmax is chosen. This means that the position with the least uncertainty is selected for decoding. On the other hand, in max logit decoding, the position with the maximum logit is chosen. This means that the position with the highest probability of being correct is selected for decoding.

To generate $k$ tokens in one pass, the positions are ranked either by entropy or max logit, and the top $k$ positions are selected. This allows for efficient decoding of multiple tokens in a single pass.
User:
==============================
In the following algorithm, assume a single forward pass of ESM3 is a function $f$ of a prompt $x$, and that we can access the logits of a specific token track through a subscript; e.g. sequence logits would be $f_{\text {sequence }}(x) \in \mathbb{R}^{L \times 32}$. Furthermore, denote $\pi(\cdot ; z)$ as the probability distribution induced by the logits $z$, including an implicit softmax, and $T \in \mathbb{R}^{L}$ a temperature schedule.
------------------------------
 The algorithm is using a function $f$ that takes a prompt $x$ as input and outputs a set of logits. These logits are represented as a matrix $f_{\text {sequence }}(x) \in \mathbb{R}^{L \times 32}$, where $L$ is the length of the sequence and 32 is the number of possible tokens.

The algorithm then uses the logits to generate a probability distribution $\pi(\cdot ; z)$ for each token in the sequence. This is done using a softmax function, which takes the logits as input and outputs a probability distribution over the possible tokens.

Finally, the algorithm uses a temperature schedule $T \in \mathbb{R}^{L}$ to adjust the temperature of the probability distribution for each token. The temperature determines the level of randomness in the generated sequence, with higher temperatures resulting in more randomness and lower temperatures resulting in more deterministic sequences.

Overall, the algorithm is using a neural network to generate a sequence of tokens based on a given prompt, and is adjusting the temperature of the probability distribution to control the level of randomness in the generated sequence.
User:
==============================
```
Algorithm 14 generate from track
Input: $x_{\text {prompt }}, n_{\text {decode }} \in\{1 . . L\}, T \in \mathbb{R}^{n_{\text {decode }}}$
    : $k=L / n_{\text {decode }} \quad \triangleright \#$ steps to decode at each step
    for $s \in\left\{1 . . n_{\text {decode }}\right\}$ do
        $z_{\text {logits }}=$ esm3_forward $\left(x_{\text {prompt }}\right) \triangleright z \in \mathbb{R}^{L \times c_{\text {track }}}$
        $\left\{p_{1}, \ldots, p_{k}\right\}=$ CHOosePositions $(z)$
        for $i \in\left\{p_{1}, \ldots, p_{k}\right\}$ in parallel do
            $x_{i} \sim \pi\left(x ; z_{i} / T_{s}\right) \quad \triangle$ Sample $i$ with temp $T_{s}$
            $x_{\text {prompt }}=\left\{x_{\text {prompt }}, x_{i}\right\} \quad \triangleright$ Update prompt
        end for
    end for
```

------------------------------
 This is a code snippet that implements an algorithm for generating a track from a given prompt. The algorithm takes as input the prompt $x_{\text {prompt }}$, the number of decoding steps $n_{\text {decode }}$, and a temperature vector $T \in \mathbb{R}^{n_{\text {decode }}}$.

The algorithm first calculates the number of steps to decode at each step, which is given by $k=L / n_{\text {decode }}$. It then iterates over each decoding step $s \in\left\{1 . . n_{\text {decode }}\right\}$ and performs the following steps:

1. It uses the esm3_forward function to compute the logits $z_{\text {logits }}$ for the prompt $x_{\text {prompt }}$.

2. It selects $k$ positions from the logits using the CHOosePositions function, which returns a list of positions $\left\{p_{1}, \ldots, p_{k}\right\}$.

3. For each position $i \in\left\{p_{1}, \ldots, p_{k}\right\}$, it samples a new token $x_{i}$ from the distribution $\pi\left(x ; z_{i} / T_{s}\right)$, where $T_{s}$ is the temperature vector for the current decoding step.

4. It updates the prompt by concatenating the new token $x_{i}$ with the previous prompt $x_{\text {prompt }}$.

The algorithm repeats this process for each decoding step, generating a new track at each step. The final track is the concatenation of all the generated tracks.