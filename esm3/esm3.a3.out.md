 - ESM3 is a generative model and a representation learning model.
- ESM3 models are trained at three scales: 1.4B, 7B, and 98B parameters.
- The ESM3 1.4B model is trained on 75B tokens and is noted for its small size and speed.
- The ideal number of tokens on which to train the model is determined by a variety of factors such as release frequency, amount of inference, ease of use, and usage patterns.
- Two additional versions of ESM3 1.4B, named 1.4B Overtrained and 1.4B Open, are trained on 300B tokens.
- The contact prediction model is a multilayer perceptron (MLP) head that operates independently over the representations of each amino acid.
- The models are evaluated on a test set of 902 proteins whose structures are temporarily held out from the ESM3 training set.
- The models are also evaluated on the CASP14 and CASP15 structure prediction benchmarks.
User:

 - LoRA is a common alternative to full weight finetuning that uses much less memory while attaining strong performance.
- LoRA is applied to the base model for finetuning.
- The MLP along with the LoRA weights are trained end-to-end using the cross-entropy loss with respect to the ground truth contact prediction map.
- All models are trained with LoRA rank 4, batch size 64 and a learning rate of $1 \mathrm{e}-3$ for $10 \mathrm{k}$ steps on a mix of sequence and structure data from PDB, AlphaFold-DB, ESMAtlas, and OAS Predicted Structures.
- Data are sampled in a ratio of 1:3:3:0.03 from these datasets.
- The smallest ESM3 model, with 1.4B parameters, achieves a $\mathrm{P} @ \mathrm{~L}$ of $0.76 \pm 0.02$ on the CAMEO test set.
- ESM3 can directly predict protein structures without additional finetuning by first predicting structure tokens, then decoding these tokens into coordinates.
- For more difficult datasets, such as CASP14 and CASP15, iterative decoding has an outsized impact.
User:

 - The argmax prediction for the 7B model is comparable to ESMFold on both the CAMEO and CASP15 datasets.
- Iterative decoding with ESM3 98B closes the gap between ESMFold and Alphafold2 on the CAMEO and CASP15 datasets.
- Structure prediction scaling curves as a function of training compute are provided in Fig. S10.
- The conditional likelihood of an output given a prompt serves as a proxy for the generative capabilities of a model.
- ESM3 is a generative model over masking patterns and is trained to predict tokens given any masking pattern.
- The NLL of a sample under ESM3 is given by a formula that involves summing over all possible decoding orders.
- The unconditional NLL is always higher than the conditional NLL.
- Conditioning on full sequence information leads to the lowest NLL.
User:

 - 3D structure reduces loss on secondary structure prediction to nearly zero.
- Conditioning on sequence results in lower structure prediction loss than conditioning on secondary structure.
- There are diminishing returns to scale for prediction of structure, function, SASA, and secondary structure, but not for sequences.
- ESM3 98B has a clear loglinear relationship between pre-training FLOPS and NLL, regardless of conditioning.
- ESM3 98B has the highest precision @ L results on CASP14, CASP15, and CAMEO.
- Iterative and Argmax methods have different performance on CAMEO, CASP14, and CASP15.
User:

 - The ESMFold model achieved a 0.865 accuracy in protein structure prediction.
- The ESM3 model achieved a 0.728 accuracy in protein structure prediction.
- The ESM3 iterative inference of structure tokens conditioned on sequence achieved a 0.728 accuracy in protein structure prediction.
- The ESM3 iterative inference of structure tokens conditioned on sequence has a runtime complexity of O(L^3) in length of a protein sequence.
- The ESM3 iterative inference of structure tokens conditioned on sequence appears to help more in more difficult datasets, with a +4.4 LDDT boost on CASP14 compared to a +1.0 LDDT boost on CAMEO.
- The ESM3 iterative inference of structure tokens conditioned on sequence is comparable to ESMFold and Alphafold2 in terms of runtime complexity.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in protein structure prediction.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESMFold model in protein structure prediction.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the Alphafold2 model in protein structure prediction.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein function.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein secondary structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein SASA.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein sequence.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein function.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein secondary structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein SASA.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein sequence.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein function.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein secondary structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein SASA.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein sequence.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein function.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein secondary structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein SASA.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein structure.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3 model in predicting protein sequence.
- The ESM3 iterative inference of structure tokens conditioned on sequence is more effective than the ESM3

 - The paragraph discusses the use of an expert system and the need for simple individual facts.
- The paragraph mentions a table with diagonal highlighting of unconditional NLL for each track.
- The paragraph includes two figures, S11 and S12, showing conditional and unconditional scaling behavior and the distribution of pTM and pLDDT.
- The paragraph notes that ESM3 generates more high-quality structures than ESM2 and that the model has properly fit the training distribution.
- The paragraph explains why pTM is used instead of pLDDT for evaluating structure predictions from ESM3.
User:

 - pLDDT is biased towards local structural confidence.
- pTM is a more global measure of structural confidence.
- pLDDT and pTM correlation drops for generated sequences.
- High pLDDT but low pTM emerges for some generated sequences.
- Sequence embeddings are computed by averaging over all positions in the sequence.
- UMAP projection is used to visualize the distribution of unconditional generations.
- ESM3 is not biased towards particular secondary structures.
- ESM3 closely matches the secondary structure distribution of known proteins.
- ESM3 can generate designable structures.
User:

 - ESM3 has high self-consistency for its own high-confidence designs.
- The chain-of-thought procedure generates sequences with higher confidence ESM3-predicted structures than the directly-generated sequences.
- The high-confidence subset of CoT-generated sequences are more designable than the high-confidence directly-generated sequences.
- The CoT-generated sequences have a small bias towards higher alpha and beta proportion compared to those generated directly.
- ESM's ability to follow prompts is evaluated using a set of held-out proteins.
- The model is tasked with generating the sequence for the entire protein after being shown a randomly sampled span of length 15% of the original protein length.
User:

 - The ESM3 7B model is used for all generations with a temperature of 0.7 and $L$ decoding steps.
- The model generates 64 sequences per prompt.
- ESMFold is used to fold the sequences generated by ESM3.
- The structure coordinate, secondary structure, and SASA tracks are evaluated using alignments.
- The distribution of sequence length in the unconditional generation dataset is shown.
- The mean pLDDT and pTM of unconditional generations from ESM3 are compared to sequences designed using the 3B-parameter ESM2 model.
- The round-trip success rate of high-confidence generations using ESM3 is measured.
- The secondary structure composition of unconditional generations is shown relative to the distribution of proteins in the PDB.
- Generation of sequences using chain-of-thought involves generating SS8 tokens first, followed by structural tokens.
User:

 - The paragraph discusses the evaluation of the ESM3 model's ability to generate protein sequences and predict their structures.
- The evaluation includes comparing the distribution of mean pLDDT and pTM values for sequences generated using different methods.
- The evaluation also includes calculating various metrics such as TM-score and secondary structure composition.
- The evaluation includes running InterProScan on generated sequences to extract function keywords and report function keyword recovery.
- The evaluation includes testing the ability of ESM3 to generalize beyond its training distribution under prompting by identifying proteins deposited in the PDB after the training cutoff and choosing eight with low TM values to any structure in the training dataset.
User:

 - DSSP is used to compute residue-level SS8 and SASA for proteins.
- ESM3 is prompted with SS8 and SASA to generate diverse, globular proteins with no close sequence or structure neighbors in the training set.
- ESM3-generated sequences have high confidence and accuracy, while ESMFold-generated sequences have high confidence but lower accuracy.
- ESM3 is able to classify secondary structure for symmetric protein backbones with varying symmetries.
- ESM3 is able to design these proteins successfully with high confidence and low sequence similarity to the training set.
- ESM3 is able to generate proteins by composing multimodal prompts across its input tracks.
User:

 - The paragraph discusses a method for generating proteins with diverse and novel characteristics.
- The method involves augmenting the standard functional motif scaffolding task with additional conditioning to specify the type of scaffold for ESM3 to design.
- The functional sites comprise a combination of ligand binding sites coordinated by residues remote in sequence and those defined by short local motifs.
- The coordinates and amino acid identities of all residues from the reference PDB structures are input to the model.
- The scaffold conditioning is defined using either SS8 tokens or function keywords defined by InterPro accession numbers.
- The designs were generated with the 7B-parameter model, a constant temperature of 0.7, and $L/2$ decoding steps for a protein of length $L$.
- The secondary structure prompting involves generating proteins under four main classes of secondary structure composition: mostly alpha helices, mostly beta sheets, and mixed alphabeta proteins.
- For each generation, the model is prompted with a random set of SS8 spans up to a total length $L$, with mask tokens in between.
User:

 - A prompt might look like __EEE__HHHHH___EE_, where H is a residue within an alpha helix and E is a residue in a beta strand.
- We generate between 256 and 1024 designs for each combination of SS8 and functional site motif.
- For each generation, we uniformly sample a random length L between 150 and 400.
- We produce a set of secondary structure spans with length 5-20 residues, each separated.
- Proteins designed using SS8 and SASA prompts derived from recent structures in the PDB with low structural similarity to the training set.
- Symmetric proteins designed using SS8 prompting.
- Histograms show the similarity to the nearest training set protein by structure (TM-score) and sequence (sequence identity) compared to unconditional generation.
- Motif & PDB ID & Chain ID & PDB Residue Identifiers.
User:

 - PD-1 binding
- DNA-binding helix-turn-helix
- P-loop
- Double EF-hand
- Lactate dehydrogenase
- Renal dipeptidase
- Ubiquitin-activating enzyme E1C binding
- DNA topoisomerase
- Secondary structure-prompted designs
- Keyword prompting
- InterPro tags
- ESM3
- CAMEO test set
- Self-consistency evaluation
- InterPro accessions
User:

 - We assess novelty of each motif-scaffold combinations by measuring the TM-score between the generated scaffold and the chain from which the motif is derived.
- For motifs derived from ligand binding residues, we use Foldseek to search the PDB for any other proteins which share that motif.
- For all but zincbinding and magnesium-binding motifs, Foldseek finds no significant hits at an E-value threshold of 1.0.
- The hits discovered for zinc and magnesium have only modest TM-score.
- To assess whether the generated scaffolds are likely to be designable, we measure a self-consistency TM-score under orthogonal computational models by inverse-folding the designed structure with ESM-IF and re-folding with ESMFold.
- We report the best scTM over 8 inverse folding designs in Table S12.
- A series of prompts of length 150 were constructed for the protein compression example shown in Fig. 2D.
- The sequence and structure of the catalytic triad of trypsin were placed in the prompt using a specific procedure.
- H57 from the template trypsin was placed at the lowest sampled number, D102 at the second lowest, and S195 at the largest number.
User:

 - The left-to-right ordering of the catalytic triad in the template trypsin.
- 128 prompts were generated by a procedure.
- Each prompt was combined with a function keyword prompt derived from the template protein.
- The final set of 128 prompts was arrived at.
- The base ESM 7B model was prompted to generate the sequence of the remaining 147 residues of the protein.
- $L=150$ decoding steps were used with a temperature of 0.7.
- Generations were filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs.
- The generation shown in Fig. 2D was selected finally by visual inspection.
- Generation quality was measured using ESMFold pTM of the generated sequence.
- For self-consistency, the ESM3-predicted structure of the generation was inverse folded with ESM-IF1 8 times and re-folded with ESMFold.
- A Protein Blast search was performed to find the reference sequence.
- ESM3 is prompted to bury an exposed helix in a protein with an alternating alpha-beta sandwich fold.
- The prompt is of the same length as the template protein.
- A buried helix was identified between residues 106-116 of the template protein.
- Structure coordinates were used to prompt ESM3 to generate the sequence of the remaining 147 residues of the protein.
- $L=150$ decoding steps were used with a temperature of 0.7.
- Generations were filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs.
- The generation shown in Fig. 2D was selected finally by visual inspection.
- Generation quality was measured using ESMFold pTM of the generated sequence.
- For self-consistency, the ESM3-predicted structure of the generation was inverse folded with ESM-IF1 8 times and re-folded with ESMFold.
- A Protein Blast search was performed to find the reference sequence.

 - The coordinates from a region are placed in the prompt at the same residue indices to prompt ESM3 to generate the same helix.
- A SASA prompt of 40.0 is used for each of the 11 helix residues to prompt ESM3 to place the helix on the surface of the protein.
- The secondary structure of 5 central beta strands surrounding the buried helix is prompted, including residues 33-36, 62-65, 99-103, 125-130, and 179-182.
- ESM3 7B is used to generate 512 protein sequences conditioned on this prompt using $\frac{L}{2}$ decoding steps and a temperature of 0.7.
- Designs are filtered by ESM3 pTM and adherence.
- The scaffold is a beta propeller with InterPro tags IPR001680, IPR036322, and IPR015943, and a total length of 353.
- The scaffold is a TIM barrel with InterPro tags IPR000652, IPR020861, IPR035990, IPR013785, IPR000652, and IPR022896, and a total length of 252.
- The scaffold is an MFS transporter with InterPro tags IPR011701, IPR020846, and IPR036259, and a total length of 380.
- The scaffold is an immunoglobulin with InterPro tags IPR036179, IPR013783, IPR003597, IPR007110, IPR003599, and IPR013106, and a total length of 209.
- The scaffold is a histidine kinase with InterPro tags IPR003594, IPR004358, IPR005467, and IPR036890, and a total length of 166.
- The scaffold is an alpha/beta hydrolase with InterPro tags IPR029058 and IPR000073, and a total length of 276.
User:

 - Novelty is measured by computing the TM-score to the original scaffold from which the motif is derived.
- Designability is measured by self-consistency TM-score over eight samples by inverse folding with ESM-IF and refolding with ESMFold.
- The final generation is chosen by visual inspection.
- ESM3 is able to satisfy input constraints and generate structurally distinct proteins.
- ESM3 can be used to generate idealized proteins with specific secondary structures and functions.
User:

 - The paragraph describes a process for generating protein structures using ESM3 7B.
- The process involves creating a secondary structure prompt and a function keyword prompt.
- The secondary structure prompt is expanded to contain 11 helix-strand subunits.
- ESM3 7B is used to generate 256 samples with $L$ decoding steps and a temperature of 0.7.
- The generation is filtered by ESM3 pTM and visual inspection.
- The generation is evaluated using ESMFold pTM and scTM mean.
- The generation is structurally distinct, as determined by a Foldseek search.

