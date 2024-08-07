We explore the ability of ESM3 to follow complex prompts with different compositions.
ESM3 can be prompted with instructions from each of its input tracks: sequence, structure coordinates, secondary structure (SS8), solvent-accessible surface area (SASA), and function keywords.
This allows prompts to be specified at multiple levels of abstraction, from atomic level structure to high level keywords describ- ing the function and fold topology, using the learned generative model to find a coherent solution that respects the prompt.

We evaluate ESM3's ability to follow prompts in each of the tracks independently.
A set of prompts are constructed for each of the tracks using a temporally held out test set of natural proteins (Appendix A.3.7).
We evaluated the resulting generations for consistency with the prompt and foldability, the confidence of the structure prediction TM-score (pTM) under ESMFold.

We define consistency metrics for each track: constrained site RMSD (cRMSD) is the RMSD between the prompt coordinates and the corresponding coordinates in the generation; SS3 accuracy is the fraction of residues where three-class secondary structure between the prompt and generations match; SASA spearman $\rho$ is the correlation between the SASA prompt and the corresponding region of the generation; keyword recovery is the fraction of prompt keywords recovered by InterProScan (38).

Across all tracks, ESM3 finds solutions that follow the prompt, and have confidently predicted structures by ESMFold (pTM $>0.8$ ) (Fig. 2A).
Unconditional generations reflect the distribution of natural proteins.
Since we observed ESM3 can faithfully follow prompts, we reasoned that prompting could steer the model to generate proteins that differ from natural proteins.

First we test the ability of the model to follow out-of-distribution prompts.
We construct a set of prompts combining SS8 and SASA from held out structures (TM $<0.7$ to training set).
Under these prompts, while the model continues to generate coherent globular structures (mean pTM $0.85 \pm 0.03$ ), the distribution of similarities to the training set (as measured by TM-score and sequence identity) shifts to be more novel (average sequence identity to nearest training set protein $<20 \%$ and mean TM-score $0.48 \pm 0.09$; Fig. 2B top).

To test the ability to generalize to structures beyond the distribution of natural proteins, we use secondary structure prompts derived from a dataset of artificial symmetric protein designs distinct from the natural proteins found in the training dataset (Appendix A.3.8).

Similarly, ESM3 produces high confidence generations (pTM $>0.8$, pLDDT $>0.8$ ) with low sequence and structure similarity to proteins in the training set (sequence identity $<20 \%$ and TM-score $0.52 \pm 0.10$; Fig. 2B bottom), indicating that the model can be used to generate protein sequences and structures highly distinct from those that exist in nature.

ESM3 is able to follow complex prompts, and has the ability to compose prompts from different tracks, and at different levels of abstraction.

To evaluate this ability, we prompt ESM3 with motifs that require the model to solve for spatial coordination of individual atoms, including ones requiring tertiary coordination between residues far apart in the sequence, such as catalytic centers and ligand binding sites.

Figure 2. Generative programming with ESM3.
(A) ESM3 can follow prompts from each of its input tracks. Density of faithfulness to prompting for each of the tracks is shown. Generations achieve consistency with the prompt and high foldability (pTM).
(B) ESM3 can be prompted to generate proteins that differ in structure (left) and sequence (right) from natural proteins. Prompted generations (blue) shift toward a more novel space vs. unconditional generations (red), in response to prompts derived from out-of-distribution natural structures (upper panel) and computationally designed symmetric proteins (lower panel).
(C) ESM3 generates creative solutions to a variety of combinations of complex prompts. We show compositions of atomic level motifs with high level instructions specified through keyword or secondary structure. Fidelity to the prompt is shown via similarity to reference structure (for keyword prompts) and all-atom RMSD to the prompted structure (for atomic coordination prompts). Solutions differ from the scaffolds where the motif was derived (median TM-score $0.36 \pm 0.14$ ), and for many motifs (e.g. serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites), we could find no significant similarity to other proteins that contain the same motif.
(D) An example of especially creative behavior. ESM3 compresses a serine protease by $33 \%$ while maintaining the active site structure.

We combine these with prompts that specify the fold architecture. For each unique combination of motif and scaffold, we generate samples until the prompt is satisfied (cRMSD $<1.5 \AA$ for coordinates; $\mathrm{TM}>0.6$ to a representative structure for fold level prompts; and SS3 accuracy $>80 \%$ for secondary structure prompts) with high confidence ( $\mathrm{pTM}$ $>0.8$, pLDDT $>0.8$ ). We find that ESM3 is able to solve a wide variety of such tasks (Fig. 2C).

It does so without retrieving the motif's original scaffold (median TM-score of $0.40 \pm 0.10$ to reference protein; Appendix A.3.9).
In some cases, the scaffolds are transferred from existing proteins which have similar motifs (for example, the ESM3-designed alpha-helical scaffold for the zinc-binding motif has high similarity to $\mathrm{Ni}_{2+}$-binding proteins, PDB: 5DQW, 5DQY; Fig. 2C, row 3 column 1).
For many motifs (e.g., binding sites for serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor) Foldseek (39) finds no significant similarity to other proteins that contain the same motif.

In these cases we observe that sometimes the motif has been grafted into entirely different folds (e.g. a protease inhibitor binding site motif in a beta-barrel which is most similar to a membrane-bound copper transporter, PDB: 7PGE; Fig. 2C, row 3 column 3).

At other times, the scaffold appears to be entirely novel, such as an alpha/beta protein designed to scaffold the Mcl-1 inhibitor binding motif, which has low structural similarity to all known proteins in the PDB, ESMAtlas, and the AlphaFold databases (max. TM-score $<0.5$; Fig. 2C, row 4 column 1).

Overall, the generated solutions have high designability, i.e. confident recovery of the original structure after inverse folding with ESMFold (median pTM $0.80 \pm 0.08$; scTM $0.96 \pm 0.04$; Appendix A.3.9).
Through experiments with prompt engineering, we have observed especially creative responses to prompts.
Here, we highlight an example of protein compression.

Starting from a natural trypsin (PDB $1 \mathrm{Y} 3 \mathrm{~V}$ ), we prompt with the sequence and coordinates of the catalytic triad as well as functional keywords describing trypsin, but reduce the overall generation length by a third (from 223 to 150 residues).

ESM3 maintains the coordination of the active site (cRMSD $0.73 \AA$ ) and the overall fold with high designability (pTM 0.84 , scTM mean 0.97 , std 0.006), despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D).
These examples illustrate ESM3's ability to find creative solutions to prompts specified in any of its input tracks, individually or in combination.

This capability enables a rational approach to protein design, providing control at various levels of abstraction, from high-level topology to atomic coordinates, using a generative model to bridge the gap between the prompt and biological complexity.
