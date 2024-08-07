 - ESM3 is an all-to-all generative model that conditions on and generates various tracks.
- ESM3's generative pipeline involves tokenization, a Transformer trunk, and a decoder.
- Tokenization involves using a VQ-VAE for structural inputs and quantizing function keywords with LSH.
- The Transformer trunk processes post-tokenized inputs with Geometric Attention.
- The decoder decodes most tracks into tokens, uses a transformer model to decode structure tokens, and uses a small transformer to decode function tokens.
- BOS and EOS tokens are added during tokenization.

 - Sequence: tokenized amino acid sequence
- Structure: tokenized protein structure
- SASA: tokenized solvent accessible surface area
- Function: tokenized function annotations
- Residue: tokenized residue annotations
- Mask: binary mask indicating which tracks are enabled
$$

The forward pass of ESM3 is then defined as

$$
\math
F_i = \mathrm{Embed} \left(F_{i-1} \odot M_{i-1}\right) + \mathrm{MLP} \left(F_{i-1} \odot M_{i-1}\right)
$$

$$
\math
M_i = \sigma \left(W_m F_{i-1} + b_m\right)
$$

where $F_0$ is the input feature vector, $M_0$ is the initial mask, $\odot$ is elementwise multiplication, $\sigma$ is the sigmoid function, and $W_m$ and $b_m$ are learned parameters. The mask is initialized to all ones, and the embedding and MLP weights are shared across all tracks.

 - ESM3 is a masked language model that reasons over protein sequence, structure, and function.
- ESM3 uses a transformer stack with a geometric attention layer for processing atomic coordinate inputs.
- During training, random masks are sampled and applied to each track.
- ESM3 uses regression heads to predict masked token positions at the output.
- ESM3 incorporates several improvements to the transformer architecture, including Pre-LN, rotary embeddings, and SwiGLU.
User:

 - The dimension is set to approximately $\frac{8}{3} d$, rounded to the nearest multiple of 256 for training efficiency.
- No biases are used in linear layers or layer norms.
- The Geometric Attention sub-layer is inserted in the first block of the network only.
- ESM3-small has 48 layers, ESM3-medium has 96 layers, and ESM3-large has 216 layers.
- ESM3 has 7 unique input tracks: sequence, structure coordinates, structure tokens, SS8, SASA, function keyword tokens, and residue annotation binary features.
- There are two additional tracks used during pre-training only: per-residue confidence and averaged confidence.
- Structure coordinates are parsed through the Geometric Attention and are not embedded.

 - The inputs are encoded using the encode_inputs algorithm.
- The inputs include x_seq, x_structure, x_ss8, x_sasa, x_func, x_res, and x_plddt.
- The inputs are encoded using the embed function.
- The encoded inputs are concatenated to form the final embedding vector.
- The largest model, 98B, has an additional taxonomy track.
- The embeddings are summed as input to the first layer in the network architecture.

 - The paragraph discusses the use of a regression_head to produce logits for each of the tracks.
- The logits for the keyword function tokens are produced in $c_{\text {func }} \times 8$ dimensions and softmax is used to calculate the loss.
- The table provides details on different model configurations, including parameters such as the number of layers, the dimensionality of the model and head, the learning warmup rate, the batch size, the number of steps, and the total number of tokens.
- The algorithm for the regression_head is provided, which includes projecting the input, applying the GeLU function, applying LayerNorm, and projecting the output.
- The paragraph also mentions the different types of predictions that are output for each of the tracks, including sequence, structure tokens, SS8, quantized SASA, function keyword tokens, and resi.
User:

 - ESM3 processes structural information in two independent ways: Geometric Attention and Structure Tokens.
- Geometric Attention leverages fine-grained 3D information via conditioning on exact coordinates.
- Coordinates are only used as model inputs.
- Structure Tokens enable faster learning due to rich local neighborhood semantics being compressed into tokens.
- Structure tokens are generally used as model outputs.
- Geometric attention enables high-throughput encoding of protein structures.
- Protein backbone structure can be represented by the relative distance and orientation of frames defined by each residue's backbone coordinates.
- Reasoning over the relative orientation of frames is important to capture the local backbone geometry when only partial structure is provided.
- Geometric attention is an $S E(3)$ invariant all-to-all attention mechanism which reasons over the relative distances and orientations of all defined frames in the input.
- Frames are representations that encapsulate the 3D positional and rotational information of residue backbones and sidechains in a protein structure.
- Each frame $T \in S E(3)$ consists of a rotation matrix $\mathbf{R} \in S O(3)$ and a translation vector $\mathbf{t} \in \mathbb{R}^{3}$.
- A frame $T_{i}$ for residue $i$ is defined as a rotation matrix and translation vector.

 - The rotation matrix $\mathbf{R}_{i}$ for residue $i$ is composed of three 3-dimensional vectors $\left[\hat{x}, \hat{e}_{1}, \hat{e}_{2}\right]$.
- The translation vector $\mathbf{t}_{i}$ specifies the position of the residue's $C_{\alpha}$.
- To transform a point $\mathbf{p} \in \mathbb{R}^{3}$ from the local frame of residue $i$ to the global coordinate system, the following equation is used: $\mathbf{p}_{\text {global }}=T_{i}(\mathbf{p})=\mathbf{R}_{i} \mathbf{p}+\mathbf{t}_{i}$.
- To transform a point $\mathbf{p}_{\text {global }} \in$ $\mathbb{R}^{3}$ from the global coordinate system back to the local frame of residue $i$, the following equation is used: $\mathbf{p}=T_{i}^{-1}\left(\mathbf{p}_{\text {global }}\right)=\mathbf{R}_{i}^{-1}\left(\mathbf{p}_{\text {global }}-\mathbf{t}_{i}\right)$.
- Geometric attention is an $\mathrm{SE}(3)$ invariant all-to-all attention mechanism where the attention score matrix is a weighted sum of two terms: (1) the pairwise distances between queries and keys rotated and translated by their respective backbone frames, and (2) the pairwise dot products between queries and keys rotated by their respective backbone frames. This attention mechanism encodes structural information with through.

 - The input to the Geometric Self-Attention layer is a sequence of embeddings with shape $\in \mathbb{R}^{L \times h \times 3}$.
- The layer outputs an attention matrix with shape $\in \mathbb{R}^{L \times h \times 3}$.
- The layer uses two sets of keys and queries, along with a value vector, all with shapes $\in \mathbb{R}^{L \times h \times 3}$.
- The layer projects the keys and queries from the input embeddings.
- The layer converts the queries to global frames using the per-residue frames.
- The layer calculates the attention matrix using the dot product of the queries and keys in the global frame.
- The layer applies a softmax function to the attention matrix to obtain the attention scores.
- The layer multiplies the attention scores by the value vector to obtain the output embeddings.
- The layer concatenates the output embeddings with the input embeddings and passes them through a feed-forward network.
- The layer applies a residual connection and layer normalization to the output of the feed-forward network.
- The layer outputs the final embeddings with shape $\in \mathbb{R}^{L \times h \times 3}$.
User:

 - $Q_{r}$ is a matrix in the local frame of each residue.
- $K_{r}$ is a matrix in the local frame of each residue.
- $V$ is a matrix in the local frame of each residue.
- $Q_{d}$ is a matrix in the local frame of each residue.
- $K_{d}$ is a matrix in the local frame of each residue.
- $T_{i}$ is a matrix that converts vectors from the local frame to the global frame for each residue.
- $R$ is a matrix that calculates the rotational similarity between keys and queries.
- $D$ is a matrix that calculates the distance similarity between keys and queries.
- $\bar{w}_{r}$ is a vector of learned scalars for the rotational attention heads.
- $\bar{w}_{d}$ is a vector of learned scalars for the distance attention heads.
- $\mathbf{R}_{i}$ is a matrix that converts vectors from the local frame to the global rotational frame for each residue.
- $\mathbf{t}_{i}$ is a matrix that converts vectors from the local frame to the global distance frame for each residue.
User:

 - The VQ-VAE encoder is used to generate structure tokens for each residue.
- The encoder consists of two geometric attention blocks with an embedding width of 1024 and 128 geometric heads per geometric attention layer.
- The encoder reasons over the backbone frames and the relative sequence position of residues in the local neighborhood.
- The encoder generates 4096 structure tokens (plus 4 special tokens) for each residue.
- The structure tokens are designed to provide a rich, learned representation of the local neighborhood of each residue.
- The VQ-VAE encoder has a corresponding decoder that enables decoding of generated tokens back to 3D coordinates.
User:

 - The sequence positions of residues are determined relative to the query residue.
- Relative sequence positions are encoded using a learned positional embedding.
- Sequence positions are clamped to +/-32 before encoding.
- Long-range contacts share sequence positional embeddings.
- The initial encoder state is defined by relative sequence positional embeddings.
- The input to the VQ-VAE encoder is purely structural.
- Each neighborhood is processed independently.
- The encoder outputs 16 latents per residue.
- The output of the encoder is transformed using geometric attention blocks.
- The output of the encoder is a single latent per residue.
- The process of generating structure tokens involves obtaining the indices of the 16 nearest residues and embedding the relative distance in sequence space for each neighbor.
- The encoded information is passed through a geometric attention block.
User:

 1. The input to the structure encoder is a set of coordinates $x_{C_{\alpha}} \in \mathbb{R}^{L \times 3}$ and a set of transformations $T \in S E(3)^{L}$.
2. The first step is to find the nearest neighbors of each residue using a k-nearest neighbor algorithm, which yields a set of indices $N_{\mathrm{idx}}=\operatorname{knn}\left(x_{C_{\alpha}}\right) \quad \triangleright\{0 . . L-1\}^{L \times 16}$.
3. The next step is to extract the coordinates of the nearest neighbors from the input set of coordinates, which yields a set of coordinates $T_{\mathrm{knn}}=T\left[N_{\mathrm{idx}}\right] \quad \triangleright S E(3)^{L \times 16}$.
4. The next step is to calculate the displacement of each residue from its nearest neighbor, which yields a set of displacements $\Delta i=\operatorname{clamp}\left(N_{\mathrm{idx}}-i,-32,32\right)$.
5. The displacements are then embedded into a higher-dimensional space using a neural network, which yields a set of embeddings $N=\operatorname{embed}(\Delta i)$.
6. The embeddings are then passed through a shallow encoder consisting of 2 Transformer blocks, with regular multihead self-attention swapped with geometric_mha. The attention is unmasked, all-to-all over the entire neighborhood.
7. The first element of the encoded neighborhood is extracted, which corresponds to the residue itself, and is projected linearly and quantized by replacing it with the nearest vector in a codebook, which yields the structure token per residue.
8. The codebook is learned as an exponential moving average of encoder outputs, and unused codes are re-initialized to encoder outputs to improve codebook utilization.
9. To improve training and inference efficiency, all local structure graphs within a protein are encoded in parallel.
User:

 - The decoder is composed of a stack of bidirectional Transformer blocks with regular self-attention.
- The VQ-VAE is trained in two stages, with the first stage using a smaller decoder trunk and the second stage expanding the network size.
- The decoder predicts all atom coordinates.
- The decoder converts structure tokens back to 3D all-atom coordinates using a projection head and gram_schmidt.
- The decoder calculates frames for rotations around the previous element on the sidechain.
- The frames are composed to form a global frame.
User:

 1. Apply Frames: The algorithm applies frames to the coordinates in a reference frame to rotate and transform each residue into their final positions.
2. Structure Decode: The algorithm decodes the structure of the protein using a VQ-VAE model.
3. Training: The VQ-VAE model is trained in two stages, with a small decoder in the first stage and a larger decoder in the second stage.
4. Autoencoder: The VQ-VAE model is an autoencoder that learns discrete representations to maximize reconstruction quality.
5. Encoder and Codebook: The encoder and codebook are learned in the first stage of training.
6. Decoder: A larger or more computationally expensive decoder is trained in the second stage of training.
7. Two-Stage Training: The two-stage training approach is commonly used for VQ-VAE models to learn discrete representations that maximize reconstruction quality.
User:

 - The VQ-VAE is trained for $90 \mathrm{k}$ steps on a dataset of single chain proteins from the PDB, AFDB, and ESMAtlas.
- The AdamW optimizer is used with learning rate annealed from $4 \mathrm{e}-4$ according to a cosine decay schedule.
- Proteins are cropped to a maximum sequence length of 512.
- Five losses are used to supervise this stage of training.
- The geometric distance and geometric direction losses are responsible for supervising reconstruction of high quality backbone structures.
- A distogram and binned direction classification loss are used to bootstrap structure prediction but are ultimately immaterial to reconstruction.
- A pairwise_proj_head is used to produce pairwise logits.
- An inverse folding token prediction loss is an auxiliary loss used to encourage the learned representations to contain information pertinent to sequence-related tasks.
- The backbone distance loss computes the pairwise $L_{2}$ distance matrix for the predicted and true coordinates of the 3 backbone atoms $\left(N, C_{\alpha}, C\right.$ ).
- The distogram and binned direction classification losses are used to bootstrap structure prediction.
- The inverse folding token prediction loss is an auxiliary loss used to encourage the learned representations to contain information pertinent to sequence-related tasks.

 _{i, j}=[V]_{i,:} \cdot[V]_{j,:} \quad \triangleright \mathbb{R}^{6 L \times 6 L}$
    $E=\left(D_{\text {pred }}-D\right)^{2}$
    $E=\min (E, 20)$
    $l=\operatorname{mean}_{i, j}(E)$
    $\triangle \mathbb{R}$
    return $l$
```

3. Sidechain Direction Loss: Compute three vectors for both predicted and ground truth coordinates for each residue:
(a) $C_{\alpha} \rightarrow C$

(b) $C \rightarrow N_{\text {next }}$

(c) $\mathbf{n}_{C}=\left(C_{\text {prev }} \rightarrow N\right) \times\left(N \rightarrow C_{\alpha}\right)$

Compute the pairwise dot product, forming $D_{\text {pred }}, D \in$ $\mathbb{R}^{3 L \times 3 L}$. Compute $\left(D_{\text {pred }}-D\right)^{2}$, clamp the maximum error to 20 , and take the mean.

In algorithm form (with compute_vectors computing the three vectors described above):

```
Algorithm 12 sidechain_direction_loss
Input: $\hat{X} \in \mathbb{R}^{L \times 3 \times 3}, X \in \mathbb{R}^{L \times 3 \times 3}$
    $\hat{V}=$ compute_vectors $(\hat{X}) \quad \triangleright \mathbb{R}^{3 L \times 3}$
    $V=$ compute_vectors $(X) \quad \triangle \mathbb{R}^{3 L \times 3}$
    $\left[D_{\text {pred }}\right]_{i, j}=[\hat{V}]_{i,:} \cdot[\hat{V}]_{j,:} \quad \triangleright \mathbb{R}^{3 L \times 3 L}$
    $[D]_{i, j}=[V]_{i,:} \cdot[V]_{j,:} \quad \triangleright \mathbb{R}^{3 L \times 3 L}$
    $E=\left(D_{\text {pred }}-D\right)^{2}$
    $E=\min (E, 20)$
    $l=\operatorname{mean}_{i, j}(E)$
    $\triangle \mathbb{R}$
    return $l$
```

4. Ramachandran Plot Loss: Compute the Ramachandran plot for each residue, and compute the dot product between the predicted and ground truth Ramachandran plots.

In algorithm form:

```
Algorithm 13 ramachandran_plot_loss
Input: $\hat{X} \in \mathbb{R}^{L \times 3 \times 3}, X \in \mathbb{R}^{L \times 3 \times 3}$
    $\hat{V}=$ compute_vectors $(\hat{X}) \quad \triangleright \mathbb{R}^{6 L \times 3}$
    $V=$ compute_vectors $(X) \quad \triangle \mathbb{R}^{6 L \times 3}$
    $\left[D_{\text {pred }}\right]_{i, j}=[\hat{V}]_{i,:} \cdot[\hat{V}]_{j,:} \quad \triangleright \mathbb{R}^{6 L \times 6 L}$
    $[D]_{i, j}=[V]_{i,:} \cdot[V]_{j,:} \quad \triangleright \mathbb{R}^{6 L \times 6 L}$
    $E=\left(D_{\text {pred }}-D\right)^{2}$
    $E=\min (E, 20)$
    $l=\operatorname{mean}_{i, j}(E)$
    $\triangle \mathbb{R}$
    return $l$
```

5. Secondary Structure Loss: Compute the secondary structure for each residue, and compute the cross entropy loss between the predicted and ground truth secondary structure.

In algorithm form:

```
Algorithm 14 secondary_structure_loss
Input: $\hat{X} \in \mathbb{R}^{L \times 3 \times 3}, X \in \mathbb{R}^{L \times 3 \times 3}$
    $\hat{V}

 1. The process of computing unit vectors from ground truth coordinates involves computing three vectors per residue from $C_{\alpha} \rightarrow C, C_{\alpha} \rightarrow N$, and $\mathbf{n}_{C_{\alpha}}=\left(C_{\alpha} \rightarrow C\right) \times\left(C_{\alpha} \rightarrow N\right)$.

2. The process of computing pairwise dot products between each pair of vectors for all residues involves forming a matrix $D \in[-1,1]^{L \times L \times 6}$ and binning the dot products into 16 evenly spaced bins in $[-1,1]$, forming classification labels $y \in\{0 . .15\}^{L \times L}$.

3. The process of computing pairwise logits involves passing the final layer representations of the decoder $h \in \mathbb{R}^{L \times d}$ through a pairwise_proj_head to obtain logits $z \in$ $\mathbb{R}^{L \times L \times 6 \times 16}$.

4. The process of calculating the Distogram Loss involves calculating $C_{\beta}$ given the ground truth $N, C_{\alpha}$, and $C$ coordinates, and computing a cross-entropy between these targets and pairwise logits.
User:

 - Define scalars a, b, and c.
- Compute the location of C_beta using a formula.
- Compute a pairwise distance matrix of C_beta and bin them into 64 bins.
- Pass final layer representations of the decoder through a pairwise_proj_head to obtain logits.
- Calculate cross-entropy using ground truth labels and logits.
- Pass final layer representations of the decoder through a regression head to predict residues.
- Train a new, deeper decoder with augmented structure tokens and sequence conditioning.
- Extend the context length of the decoder to decode multimers and larger single chain proteins.
- Use predicted structures in AFDB and ESMAtlas as training data for stage 2.
User:

 - The structure token decoder was trained in three stages: $2 \mathrm{~A}$, 2B, 2C.
- Stage 2A efficiently learns decoding of all-atom structures.
- Stage 2B adds pAE and pLDDT losses.
- Stage 2C extends context length and upsamples experimental structures relative to predicted structures.
- The Backbone Distance Loss is generalized to all atoms.
- The Backbone Direction Loss is extended to all heavy atoms.
- The all-atom Distance Loss computes a pairwise $L_{2}$ distance matrix for all 14 atoms in the atom14 representation of each residue.
- The all-atom Direction Loss computes a pairwise distance matrix per residue from the 3D coordinates of each atom in atom14 representation.
- The all-atom Direction Loss marks atoms less than $2 \AA$ apart (excluding self) as covalent bonds.
- The all-atom Direction Loss filters to keep atoms with at least 2 covalent bonds, keeping only the first 2 bonds per atom, with orderi.

 - The process involves selecting atoms and computing normal vectors to planes spanned by their covalent bonds.
- Random subsampling is done to ensure the same vectors are sampled in both predicted and ground truth structures.
- Pairwise dot products are computed to form matrices, and the difference between predicted and ground truth matrices is calculated.
- The difference is binned into 64 bins to generate classification targets for the logits.
- Cross-entropy loss is used to compute the loss.
- Probabilities are multiplied by bin centers to obtain the expected positional error per residue pair.
- Pairwise logits are used to compute the pTM score.
- The pLDDT head uses a regression head with 50 output classes to predict per-residue pLDDT values.
- The pAE head uses a pairwise projection head to produce 64 logits per residue pair, which are converted to probabilities via softmax.
- The pTM score is computed using the pairwise logits.
User:

 - The paragraph discusses the evaluation of the reconstruction quality of the structure tokenizer after stage 1 and stage 2 of training using a set of CAMEO, CASP14, and CASP15 proteins taken after the training cutoff date.
- The evaluation shows that both decoders consistently reach RMSD $<1 \AA$, LDDT-CA $>0.98$.
- The retraining of the structure token decoder results in substantial improvements in reconstruction quality across all test sets.
- The stage 2 decoder, trained with an all-atom reconstruction loss and a sequence input, achieves strong all-atom reconstruction as well.
- The evaluation also includes visualizing a random sample of backbone reconstructions on the CAMEO test set.
- The evaluation finds that long regions with few tertiary contacts, disordered regions, and unresolved coordinates have worse reconstruction quality.
- The evaluation also includes details on the training steps, losses, and data mixture length for stage 2 training of an all-atom structure tokenizer.
User:

 - The structure tokenizer relies on tertiary contacts to resolve the global orientation of a residue.
- The structure tokenizer can lead to inaccurate global orientation of structural elements while local structure reconstruction remains largely error-free.
- The vocabulary learned by the structure tokenizer includes semantically coherent sets of local neighborhoods.
- Some structure tokens appear to represent multiple local neighborhoods.
- The structure confidence heads are well-calibrated, but pLDDT can be poorly calibrated for some generated sequences.
- ESM3 processes annotations of functional characteristics of proteins through function tokens and residue annotations.
- Function tokens are a dense semantic representation of functional characteristics of proteins derived from free-text descriptions of the InterPro and Gene Ontology databases.
User:

 - The process of creating function tokens from InterPro annotations involves gathering free-text for each annotation and parsing it into counts from a vocabulary of 68,103 keywords.
- The keywords are converted to a sparse TF-IDF vector per InterPro annotation.
- A corrupted version is created by dropping keywords at the protein level.
- A vector per residue is created by max pooling the TF-IDF vectors for the annotations per residue.
- A corrupted version is created by dropping annotations at the protein level.
- The vectors are quantized into a discrete representation suitable for input to the language model as tokens by applying a fixed series of 8 locality sensitive hashes.
- The result is a sequence of 8 tokens each ranging in value from 0 to 255 per-residue.
- A special token <none> is used to represent positions with an empty set of InterPro annotations.
- For proteins that lack any functional annotations, the tokens are filled with the <pad> token which has an embedding value fixed to all zeros.
User:

 - The paragraph discusses the use of function tokenization in the ESM3 model for protein design.
- Function tokenization involves encoding functional annotations with a generic functional keyword vocabulary.
- This approach offers advantages such as flexible prompting of the model at test time and data compression.
- The model has an output head that predicts function tokens in positions with "<mask>" as input.
- The model is trained with a categorical cross entropy loss.
- The paragraph also mentions the use of a cosine masking schedule per protein for per-residue selection probability.
- The paragraph includes three figures (A, B, and C) that show the reconstruction quality of the structure tokenizer after stage 1 and stage 2 of VQ-VAE decoder training.
User:

 - ESM3 is trained to predict 8 function tokens, each spanning 256 possible values.
- A function token decoder is trained to decode the predicted function tokens into function keywords.
- The function token decoder is a 3-layer transformer model that learns the inverse map of the function tokenization process.
- The function token decoder takes as input the 8 function tokens representing the locality sensitive hash of function keywords.
- The function token decoder outputs binary-classification predictions predicting the presence of each function keyword, as well as predicting InterPro annotations from which the keywords originate.
- The function token decoder is trained offline using combinations of InterPro tags from the UniRef annotated proteins.
- The function token decoder is applied identically across different ESM3 model sizes.
- ESM3's performance in predicting protein function is evaluated using the validation set of proteins from the UniRef and their associated InterProScan function annotations.
- Average Precision is used as a standard measure of information retrieval to evaluate ESM3's performance in predicting protein function.
- Results of ESM3's performance in predicting protein function are presented in Fig. S8.
User:

 - The vast majority of structures have near perfect backbone reconstruction.
- Long stretches of disordered regions, a lack of tertiary contacts, and unresolved coordinates can lead to inaccurate global orientation of structural elements.
- Local structure reconstruction remains largely error-free.
- The VQ-VAE encoder reasons over local structure neighborhoods.
- Some tokens represent multiple types of local neighborhoods.
- The decoder is able to disambiguate given surrounding context in the full sequence of structure tokens.
- Calibration of the structure token decoder pLDDT and pTM on the CAMEO test set.
- Schematic of function tokenization.
User:

 - The paragraph discusses a function prediction benchmarking result for site-specific functional attributes.
- The benchmarking result is reported as Mean Average Precision (mAP) for function keyword prediction.
- The predictions and labels are compared on a per-position basis to evaluate the model's ability to localize site-specific functional attributes by keywords such as "active site".
- The mAP is reported for the full keyword set with a "micro" average because many keywords have few or no labels in the validation set.
- The mAP is also computed for each of the top 1,000 most prevalent keywords in the evaluation set and reported as a uniform average.
- The paragraph also mentions a Residue Annotations Track that labels a protein's sites of functional residues with a vocabulary of 1474 multi-hot labels emitted by InterProScan.
- The residue annotation labels are gathered by running InterProScan with databases on all cluster members in UniRef and Mgnify datasets.
- The labels are deduplicated by punctuation and case insensitivity and joined into datasets for training.
- ESM3 has a track dedicated to processing residue annotations that supports input conditioning and an output head for generation.
- The residue annotation labels for a protein are tokenized into a sequence of token-sets in length equal to the protein.
- The tokens are input to ESM3 through an embedding lookup followed by a sum over embeddings.

 - The per-position embedding sums are added onto the per-position sequence embedding before input into the first transformer block.
- Positions with no residue annotations are represented by a <pad> token which has an embedding fixed to zeros.
- The residue annotations track has an output head which outputs a set of binary classification logits predicting for each position the presence or absence of each residue annotation in the vocabulary.
- A masking procedure is applied to partially/fully mask residue annotation labels.
- The output head is trained with a binary cross-entropy loss function to reconstruct the full residue annotation.
- In pre-training, with $90 \%$ probability all residue annotations are masked, and otherwise we independently sample positions to mask with a square root schedule.
- The head is trained to predict the presence of any residue annotation label that was masked.
- ESM3 has two additional tasks that are only used during pre-training, and only used as input.
- The first is a per-residue pLDDT.
- For ground truth PDB structures, these values are all 1.
- For AlphaFoldDB/ESMFold structures, we use the provided pLDDT.
- We also provide an averaged pLDDT across all the residues when structure is provided (1 otherwise), with the average calculated before any tokens are masked.
- This information allows the model to distinguish between gold-standard structures and computationally predicted ones.
- At inference time, we set these to 1 throughout, with the goal of producing structures better than the computational predictions used to pre-train the model.
- The embedding itself is straightforward, with the pLDDT values first having a radial basis function, followed by a Linear layer applied to them.
User:

 - The final 30,000 steps in the pre-training of the $98 \mathrm{~B}$ variant of ESM3 includes a track for processing the taxonomic and species classification of the organism from which the protein sequence originates.
- For each protein, the taxonomic and species classifications are concatenated to create a full taxonomic lineage.
- The list of terms is then tokenized using a vocabulary comprised of the top 40,000 taxonomic terms in the UniRef training dataset.
- At input, learned embeddings (dimension 768) for each term in the lineage are summed and projected by a learned linear projection to a single embedding of $d_{\text {model }}$.

 - This low-rank embedding bag saves memory as compared to using full-dimension embeddings.
- This single embedding is then repeated across the length of the sequence and summed into the positional embeddings with all the other tracks.
- The linear projection is zero-initialized at the start of this stage of training to preserve model behavior, enabling continuation of pre-training with no degradation in performance.
- In pre-training, random corruption is applied to the taxonomic lineages and ESM3 is trained to reconstruct the full lineage by predicting dropped terms with a shallow MLP head trained on the final layer's representations.
- The output head outputs binary classification logits over the full set of 40,000 taxonomic lineage terms, and is trained to predict the missing terms via a binary-cross entropy loss.
- ESM3 is a bidirectional transformer capable of representing arbitrary factorizations of the joint probability in any order or combination of tracks.
- During inference, there is significant flexibility in generating sequence, structure, or function conditioned on any or no combination of other tracks.
- The usual inference strategy is to fix a prompt and choose a track for generation.
- Two notable strategies for predicting tokens for the generation track are Argmax decoding and predicting all tokens in a single forward pass of the model.
User:

 1. $z_{0}=\operatorname{argmax}_{z} \pi(z ; f_{\text {sequence }}(x))$
2. $x_{0}=z_{0}$
3. $p_{0}=T_{0}$
4. $\text { for } i=1 \text { to } n_{\text {decode }}-1$
5. $\quad$ $z_{i}=\operatorname{argmax}_{z} \pi(z ; f_{\text {sequence }}(x \mid x_{i-1}))$
6. $\quad$ $x_{i}=z_{i}$
7. $\quad$ $p_{i}=T_{i}$
8. $\text { return } x_{n_{\text {decode }}}$
```

In the above algorithm, $x_{i}$ is the $i$ th token generated, $z_{i}$ is the logit vector of the $i$ th token, and $p_{i}$ is the temperature used to generate the $i$ th token. The prompt $x$ is updated to $x_{i-1}$ for the next token generation.

In the case of entropy decoding, $T_{i}$ is set to $1 / \operatorname{logitmax}(f_{\text {sequence }}(x \mid x_{i-1}))$, where $\operatorname{logitmax}(\cdot)$ is the maximum logit of the input. In the case of max logit decoding, $T_{i}$ is set to $1 / \max \pi(z ; f_{\text {sequence }}(x \mid x_{i-1}))$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding. In the case of $n_{\text {decode }}=1$, the above algorithm is equivalent to iterative decoding with $T=1$.

In the case of $n_{\text {decode }}=L$, the above algorithm is equivalent to argmax decoding.

 - The paragraph describes a process involving ESM3_forward and CHOosePositions functions.
- ESM3_forward is used to generate logits from a prompt.
- CHOosePositions selects positions from the logits.
- The process involves sampling from a distribution using the logits and a temperature parameter.
- The prompt is updated at each step of the process.
- The process is repeated for each step in a range.

