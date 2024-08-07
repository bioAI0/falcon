ESM3 reasons over the sequence, structure, and function of proteins.

All three modalities are represented by tokens, and are input and output as separate tracks that are fused into a single latent space within the model.

ESM3 is trained with a generative masked language modeling objective:

A random mask $m$ is applied to the tokens $x$ describing the protein, and the model is supervised to predict the identity of the tokens that have been masked.

During training, the mask is sampled from a noise schedule so that ESM3 sees many different combinations of masked sequence, structure, and function, and predicts completions of any combination of the modalities from any other.

This differs from the classical masked language modeling (28) in that the supervision is applied across all possible masking rates rather than a single fixed masking rate.

This supervision factorizes the probability distribution over all possible predictions of the next token given any combination of previous tokens, ensuring that tokens can be generated in any order from any starting point (29-31).
To generate from ESM3, tokens are iteratively sampled.

Starting from a sequence of all mask tokens, tokens can be sampled one at a time, or in parallel, in any order, until all tokens are fully unmasked (Fig.1A).

Masking is applied independently to sequence, structure, and function tracks, which enables generation from any combination of empty, partial, or complete inputs.

ESM3's training objective is also effective for representation learning.

We choose a noise schedule that balances generative capabilities with representation learning (Appendix A.2.2).

Tokenization enables efficient reasoning over structure.

Protein structures are tokenized by a discrete auto-encoder (32), which is trained to compress the high dimensional space of three-dimensional structure into discrete tokens (Fig.1C).

We propose an invariant geometric attention mechanism to efficiently process three-dimensional structure.

The mechanism operates in local reference frames defined by the bond geometry at each amino acid, and allows local frames to interact globally through a transformation into the global frame (Appendix A.1.6).

This mechanism can be efficiently realized through the same computational primitives as attention (33), and is readily scalable.

The local structural neighborhoods around each amino acid are encoded into a sequence of discrete tokens, one for each amino acid.

When predicting or generating protein structure, structure tokens output by ESM3 are passed to the decoder, which reconstructs the all-atom structure.

The autoencoder is trained to encode and reconstruct atomic coordinates with a geometric loss that supervises the pairwise distances and relative orientations of bond vectors and normals (Appendix A.1.7.3.1).

This tokenization delivers nearperfect reconstruction of protein structure ( $<0.3 \AA$ RMSD on CAMEO, Fig.S3), enabling representation of structure at the input and output with atomic accuracy.

We also find that providing ESM3 direct access to atomic coordinates in the input via a geometric attention projection into the transformer improves the response to atomic coordinate prompts.

ESM3 can be conditioned on either or both of tokenized structure and atomic coordinates.

We supplement these structure representations with coarse grained tokens encoding secondary structure state (SS8) and solvent accessible surface area (SASA).

Function is presented to the model in the form of tokenized keyword sets for each position in the sequence.

ESM3 is a bidirectional transformer.

While extensive research has gone into creating specialized architectures and training objectives for proteins, we find that tokenization paired with a standard masked language modeling objective and the basic transformer architecture is highly effective for both representation learning and generative modeling.

Sequence, structure, and function tracks are input as tokens, which are embedded and fused, then processed through a


Figure 1. ESM3 is a generative language model that reasons over the sequence, structure, and function of proteins.

(A) Iterative sampling with ESM3. Sequence, structure, and function can all be used to prompt the model. At each timestep $\mathrm{t}$, a fraction of the masked positions are sampled until all positions are unmasked.

(B) ESM3 architecture. Sequence, structure, and function are represented as tracks of discrete tokens at the input and output. The model is a series of transformer blocks, where all tracks are fused within a single latent space; geometric attention in the first block allows conditioning on atomic coordinates. ESM3 is supervised to predict masked tokens.

(C) Structure tokenization. Local atomic structure around each amino acid is encoded into tokens.

(D) Models are trained at three scales: 1.4B, 7B, and 98B parameters. Negative log likelihood on test set as a function of training FLOPs shows response to conditioning on each of the input tracks, improving with increasing FLOPs.

(E) Unconditional generations from ESM3 98B (colored by sequence identity to the nearest sequence in the training set), embedded by ESM3, and projected by UMAP alongside randomly sampled sequences from UniProt (in gray). Generations are diverse, high quality, and cover the distribution of natural sequences.
stack of transformer blocks.

The first transformer block also includes a geometric attention layer for atomic structure coordinate conditioning.

At the output of the model, shallow MLP heads project the final layer representation into token probabilities for each of the tracks.

The largest ESM3 model is trained on 2.78 billion natural proteins derived from sequence and structure databases (2, 34-37).

As a small fraction of structures have been experimentally determined relative to sequences, we leverage predicted structures $(4,5)$.

We also generate synthetic sequences with an inverse folding model (described in Appendix A.2.1.3) for all structures, including predicted ones.

Function keywords are derived by predicting functional annotations from sequence using a library of hidden markov models (38).

Overall this increased training data to 3.15 billion protein sequences, 236 million protein structures, and 539 million proteins with function annotations, totaling 771 billion unique tokens.

Full details of the training dataset are described in Appendix A.2.1.8.

We train ESM3 models at three scales: 1.4 billion, 7 billion, and 98 billion parameters.

In an initial series of experiments to evaluate representation learning performance in response to architecture hyperparameters, we find a greater response to increasing depth than to width.

This informed the choice of relatively deep networks for the final architectures, with the 98 billion parameter model incorporating 216 Transformer blocks (Appendix A.1.5).

Scaling ESM3 from 1.4 billion to 98 billion parameters results in substantial improvements in the validation loss for all tracks, with the greatest improvements observed in sequence loss (Fig.1D, Fig.S11).

These gains in validation loss lead to better representation learning (Table S7 and Fig.S8).

In single sequence structure prediction (Table S8) on CAMEO, ESM3 98B obtains 0.895 mean local distance difference test (LDDT) and surpasses ESMFold (0.865 LDDT).

Unconditional generation produces high-quality proteins-with a mean predicted LDDT (pLDDT) 0.84 and predicted template modeling score (pTM) 0.52-that are diverse in both sequence (mean pairwise sequence identity 0.155 ) and structure (mean pairwise TM score 0.48 ), spanning the distribution of known proteins (Fig.1E, Fig.S13).
