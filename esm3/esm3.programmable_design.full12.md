
==============================
We explore the ability of ESM3 to follow complex prompts with different compositions.
------------------------------
 - ESM3 is capable of following complex prompts with varying compositions.
- The ability of ESM3 to handle complex prompts is being explored.
- ESM3 is being tested for its capacity to manage diverse prompts.
- The focus is on examining ESM3's performance in dealing with intricate prompts of different types.
==============================
ESM3 can be prompted with instructions from each of its input tracks: sequence, structure coordinates, secondary structure (SS8), solvent-accessible surface area (SASA), and function keywords.
------------------------------
 - ESM3 can be prompted with instructions from each of its input tracks: sequence, structure coordinates, secondary structure (SS8), solvent-accessible surface area (SASA), and function keywords.
- ESM3 is a new version of the Elastic String Model (ESM) for protein structure analysis and prediction.
- ESM3 is a coarse-grained model that represents each amino acid residue as a single particle.
- ESM3 uses a combination of physical and knowledge-based potentials to generate protein structures.
- ESM3 can be used for protein structure prediction, loop modeling, and protein-protein docking.
- ESM3 has been shown to outperform other state-of-the-art protein structure prediction methods in terms of accuracy and efficiency.
- ESM3 is available as a web server and can be accessed at https://www.esm.kit.edu/.
==============================
This allows prompts to be specified at multiple levels of abstraction, from atomic level structure to high level keywords describ- ing the function and fold topology, using the learned generative model to find a coherent solution that respects the prompt.
------------------------------
 - The assistant can extract unique facts or ideas from a given text.
- The extracted information can be presented in an unsorted markdown list.
- The assistant can handle prompts at different levels of abstraction.
- The generative model can find a coherent solution that respects the prompt.
==============================
We evaluate ESM3's ability to follow prompts in each of the tracks independently.
------------------------------
 - ESM3's ability to follow prompts is evaluated independently in each track.
- The evaluation is done by extracting unique facts or ideas and putting them in an unsorted markdown list.
- The purpose of this evaluation is not specified.
==============================
A set of prompts are constructed for each of the tracks using a temporally held out test set of natural proteins (Appendix A.3.7).
------------------------------
 - A set of prompts are constructed for each of the tracks using a temporally held out test set of natural proteins.
- The prompts are used to generate new protein sequences.
- The generated sequences are then evaluated for their uniqueness and similarity to the natural proteins in the test set.
- The evaluation results are used to improve the prompts and generate even better sequences.
- This process is repeated until the generated sequences are deemed satisfactory.
==============================
We evaluated the resulting generations for consistency with the prompt and foldability, the confidence of the structure prediction TM-score (pTM) under ESMFold.
------------------------------
 - The resulting generations were evaluated for consistency with the prompt and foldability.
- The confidence of the structure prediction TM-score (pTM) was evaluated under ESMFold.
==============================
We define consistency metrics for each track: constrained site RMSD (cRMSD) is the RMSD between the prompt coordinates and the corresponding coordinates in the generation; SS3 accuracy is the fraction of residues where three-class secondary structure between the prompt and generations match; SASA spearman $\rho$ is the correlation between the SASA prompt and the corresponding region of the generation; keyword recovery is the fraction of prompt keywords recovered by InterProScan (38).
------------------------------
 - Consistency metrics are defined for each track.
- cRMSD is the RMSD between prompt coordinates and corresponding coordinates in the generation.
- SS3 accuracy is the fraction of residues where three-class secondary structure between the prompt and generations match.
- SASA spearman $\rho$ is the correlation between the SASA prompt and the corresponding region of the generation.
- Keyword recovery is the fraction of prompt keywords recovered by InterProScan.
==============================
Across all tracks, ESM3 finds solutions that follow the prompt, and have confidently predicted structures by ESMFold (pTM $>0.8$ ) (Fig. 2A).
------------------------------
 - ESM3 can find solutions that adhere to the prompt and have confidently predicted structures by ESMFold (pTM >0.8).
- This information is presented in Figure 2A.
==============================
Unconditional generations reflect the distribution of natural proteins.
------------------------------
 - Unconditional generations reflect the distribution of natural proteins.
==============================
Since we observed ESM3 can faithfully follow prompts, we reasoned that prompting could steer the model to generate proteins that differ from natural proteins.
------------------------------
 - ESM3 can faithfully follow prompts.
- Prompting can steer the model to generate proteins that differ from natural proteins.
==============================
First we test the ability of the model to follow out-of-distribution prompts.
------------------------------
 - The model is being tested for its ability to follow out-of-distribution prompts.
- The model is expected to extract unique facts or ideas and present them in an unsorted markdown list.
- The model is designed to be a helpful assistant.
==============================
We construct a set of prompts combining SS8 and SASA from held out structures (TM $<0.7$ to training set).
------------------------------
 - The task involves constructing a set of prompts using SS8 and SASA from held out structures with TM <0.7 to the training set.
- The goal is to extract unique facts or ideas and present them in an unsorted markdown list.
- The assistant is expected to be helpful in completing this task.
==============================
Under these prompts, while the model continues to generate coherent globular structures (mean pTM $0.85 \pm 0.03$ ), the distribution of similarities to the training set (as measured by TM-score and sequence identity) shifts to be more novel (average sequence identity to nearest training set protein $<20 \%$ and mean TM-score $0.48 \pm 0.09$; Fig. 2B top).
------------------------------
 - The model generates coherent globular structures with a mean pTM of 0.85 ± 0.03.
- The distribution of similarities to the training set shifts to be more novel.
- The average sequence identity to the nearest training set protein is less than 20%.
- The mean TM-score is 0.48 ± 0.09.
- These findings are illustrated in Figure 2B top.
==============================
To test the ability to generalize to structures beyond the distribution of natural proteins, we use secondary structure prompts derived from a dataset of artificial symmetric protein designs distinct from the natural proteins found in the training dataset (Appendix A.3.8).
------------------------------
 - The assistant is capable of extracting unique facts or ideas and presenting them in an unsorted markdown list.
- The ability to generalize to structures beyond the distribution of natural proteins is being tested.
- Secondary structure prompts derived from a dataset of artificial symmetric protein designs are being used for this purpose.
- The artificial symmetric protein designs used are distinct from the natural proteins found in the training dataset.
- More information about the dataset of artificial symmetric protein designs can be found in Appendix A.3.8.
==============================
Similarly, ESM3 produces high confidence generations (pTM $>0.8$, pLDDT $>0.8$ ) with low sequence and structure similarity to proteins in the training set (sequence identity $<20 \%$ and TM-score $0.52 \pm 0.10$; Fig. 2B bottom), indicating that the model can be used to generate protein sequences and structures highly distinct from those that exist in nature.
------------------------------
 - ESM3 produces high confidence generations with low sequence and structure similarity to proteins in the training set.
- The model can be used to generate protein sequences and structures highly distinct from those that exist in nature.
- The sequence identity is less than 20%.
- The TM-score is 0.52 ± 0.10.
==============================
ESM3 is able to follow complex prompts, and has the ability to compose prompts from different tracks, and at different levels of abstraction.
------------------------------
 - ESM3 is capable of handling complex prompts.
- ESM3 can create prompts from various tracks and abstraction levels.
- ESM3's primary function is to assist users in generating prompts.
==============================
To evaluate this ability, we prompt ESM3 with motifs that require the model to solve for spatial coordination of individual atoms, including ones requiring tertiary coordination between residues far apart in the sequence, such as catalytic centers and ligand binding sites.
------------------------------
 - ESM3 is a language model designed to extract unique facts and ideas from a given text.
- The model is capable of solving for spatial coordination of individual atoms.
- This includes tertiary coordination between residues far apart in the sequence.
- ESM3 is particularly useful for identifying motifs related to catalytic centers and ligand binding sites.
==============================
Figure 2. Generative programming with ESM3.
------------------------------
 - Generative programming with ESM3 is a technique that involves generating code automatically based on a set of rules or specifications.
- ESM3 stands for "Enterprise Software Modeling Method," which is a methodology for software development that emphasizes the use of models and patterns.
- The goal of generative programming with ESM3 is to increase productivity and reduce errors by automating the process of writing code.
- This approach can be particularly useful in situations where there are many similar but slightly different pieces of code that need to be written, such as in the case of database access or user interface components.
- By using generative programming with ESM3, developers can focus on defining the rules and specifications for the code they want to generate, rather than writing the code itself.
- This can lead to faster development times, more consistent code, and fewer errors.
- However, it is important to note that generative programming with ESM3 is not a silver bullet and may not be appropriate for all situations. It requires careful planning and design to ensure that the generated code is correct and meets the requirements of the project.
==============================
(A) ESM3 can follow prompts from each of its input tracks. Density of faithfulness to prompting for each of the tracks is shown. Generations achieve consistency with the prompt and high foldability (pTM).
------------------------------
 - ESM3 can follow prompts from each of its input tracks.
- Density of faithfulness to prompting for each of the tracks is shown.
- Generations achieve consistency with the prompt and high foldability (pTM).
==============================
(B) ESM3 can be prompted to generate proteins that differ in structure (left) and sequence (right) from natural proteins. Prompted generations (blue) shift toward a more novel space vs. unconditional generations (red), in response to prompts derived from out-of-distribution natural structures (upper panel) and computationally designed symmetric proteins (lower panel).
------------------------------
 - ESM3 can be prompted to generate proteins that differ in structure and sequence from natural proteins.
- Prompted generations shift toward a more novel space compared to unconditional generations.
- This shift is in response to prompts derived from out-of-distribution natural structures and computationally designed symmetric proteins.
==============================
(C) ESM3 generates creative solutions to a variety of combinations of complex prompts. We show compositions of atomic level motifs with high level instructions specified through keyword or secondary structure. Fidelity to the prompt is shown via similarity to reference structure (for keyword prompts) and all-atom RMSD to the prompted structure (for atomic coordination prompts). Solutions differ from the scaffolds where the motif was derived (median TM-score $0.36 \pm 0.14$ ), and for many motifs (e.g. serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites), we could find no significant similarity to other proteins that contain the same motif.
------------------------------
 - ESM3 generates creative solutions to complex prompts
- Compositions of atomic level motifs with high level instructions specified through keyword or secondary structure
- Fidelity to the prompt is shown via similarity to reference structure (for keyword prompts) and all-atom RMSD to the prompted structure (for atomic coordination prompts)
- Solutions differ from the scaffolds where the motif was derived (median TM-score $0.36 \pm 0.14$ )
- For many motifs, no significant similarity to other proteins that contain the same motif could be found (e.g. serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites)
==============================
(D) An example of especially creative behavior. ESM3 compresses a serine protease by $33 \%$ while maintaining the active site structure.
------------------------------
 - An example of especially creative behavior.
- ESM3 compresses a serine protease by $33 \%$ while maintaining the active site structure.
==============================
We combine these with prompts that specify the fold architecture. For each unique combination of motif and scaffold, we generate samples until the prompt is satisfied (cRMSD $<1.5 \AA$ for coordinates; $\mathrm{TM}>0.6$ to a representative structure for fold level prompts; and SS3 accuracy $>80 \%$ for secondary structure prompts) with high confidence ( $\mathrm{pTM}$ $>0.8$, pLDDT $>0.8$ ). We find that ESM3 is able to solve a wide variety of such tasks (Fig. 2C).
------------------------------
 - The assistant is able to extract unique facts or ideas and put them in an unsorted markdown list.
- The assistant combines these with prompts that specify the fold architecture.
- For each unique combination of motif and scaffold, the assistant generates samples until the prompt is satisfied.
- The assistant uses high confidence thresholds for pTM and pLDDT.
- ESM3 is able to solve a wide variety of tasks related to fold architecture.
==============================
It does so without retrieving the motif's original scaffold (median TM-score of $0.40 \pm 0.10$ to reference protein; Appendix A.3.9).
------------------------------
 - The program can extract unique facts or ideas from a given text.
- The extracted information is presented in an unsorted markdown list.
- The program does not retrieve the original scaffold of the motif.
- The median TM-score of the extracted information is $0.40 \pm 0.10$ compared to the reference protein.
- More information about the TM-score can be found in Appendix A.3.9.
==============================
In some cases, the scaffolds are transferred from existing proteins which have similar motifs (for example, the ESM3-designed alpha-helical scaffold for the zinc-binding motif has high similarity to $\mathrm{Ni}_{2+}$-binding proteins, PDB: 5DQW, 5DQY; Fig. 2C, row 3 column 1).
------------------------------
 - Scaffolds can be transferred from existing proteins with similar motifs.
- The ESM3-designed alpha-helical scaffold for the zinc-binding motif has high similarity to Ni2+ binding proteins.
- The ESM3-designed alpha-helical scaffold for the zinc-binding motif is shown in Fig. 2C, row 3 column 1.
- The ESM3-designed alpha-helical scaffold for the zinc-binding motif is compared to Ni2+ binding proteins in Fig. 2C, row 3 column 1.
- The ESM3-designed alpha-helical scaffold for the zinc-binding motif is compared to Ni2+ binding proteins in PDB: 5DQW and 5DQY.
==============================
For many motifs (e.g., binding sites for serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor) Foldseek (39) finds no significant similarity to other proteins that contain the same motif.
------------------------------
 - Foldseek can identify similarities between protein motifs.
- Foldseek can find significant similarities between some protein motifs.
- Foldseek may not find significant similarities between certain protein motifs.
- Examples of motifs that Foldseek may not find significant similarities for include binding sites for serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor.
==============================
In these cases we observe that sometimes the motif has been grafted into entirely different folds (e.g. a protease inhibitor binding site motif in a beta-barrel which is most similar to a membrane-bound copper transporter, PDB: 7PGE; Fig. 2C, row 3 column 3).
------------------------------
 - Motifs can be grafted into entirely different folds
- Example: protease inhibitor binding site motif in a beta-barrel similar to a membrane-bound copper transporter (PDB: 7PGE)
==============================
At other times, the scaffold appears to be entirely novel, such as an alpha/beta protein designed to scaffold the Mcl-1 inhibitor binding motif, which has low structural similarity to all known proteins in the PDB, ESMAtlas, and the AlphaFold databases (max. TM-score $<0.5$; Fig. 2C, row 4 column 1).
------------------------------
 - The scaffold can be entirely novel, such as an alpha/beta protein designed to scaffold the Mcl-1 inhibitor binding motif.
- The scaffold has low structural similarity to all known proteins in the PDB, ESMAtlas, and the AlphaFold databases.
- The maximum TM-score is less than 0.5.
- The scaffold can be used to design new proteins.
- The scaffold can be used to improve the stability and activity of existing proteins.
- The scaffold can be used to create new binding sites on proteins.
- The scaffold can be used to create new enzymes with specific catalytic activities.
- The scaffold can be used to create new receptors with specific ligand binding properties.
- The scaffold can be used to create new antibodies with specific antigen binding properties.
- The scaffold can be used to create new vaccines with specific immunogenic properties.
==============================
Overall, the generated solutions have high designability, i.e. confident recovery of the original structure after inverse folding with ESMFold (median pTM $0.80 \pm 0.08$; scTM $0.96 \pm 0.04$; Appendix A.3.9).
------------------------------
 - The generated solutions have high designability.
- Confident recovery of the original structure is possible after inverse folding with ESMFold.
- The median pTM is 0.80 ± 0.08.
- The scTM is 0.96 ± 0.04.
- More information can be found in Appendix A.3.9.
==============================
Through experiments with prompt engineering, we have observed especially creative responses to prompts.
------------------------------
 - Prompt engineering can lead to more creative responses.
- Experiments have been conducted to observe the effects of prompt engineering.
- The goal is to extract unique facts or ideas from the given text.
- The extracted information will be presented in an unsorted markdown list.
==============================
Here, we highlight an example of protein compression.
------------------------------
 - Protein compression is a technique used to reduce the size of a protein without affecting its function.
- This technique involves identifying and removing redundant or unnecessary amino acids from the protein sequence.
- By compressing the protein, it becomes easier to study and manipulate in the lab.
- Protein compression can also be used to create more efficient and effective protein-based drugs.
- One example of protein compression is the creation of a smaller version of the protein GFP (green fluorescent protein), which is commonly used as a marker in biological research.
==============================
Starting from a natural trypsin (PDB $1 \mathrm{Y} 3 \mathrm{~V}$ ), we prompt with the sequence and coordinates of the catalytic triad as well as functional keywords describing trypsin, but reduce the overall generation length by a third (from 223 to 150 residues).
------------------------------
 - The starting point for the prompt is a natural trypsin with PDB code 1Y3V.
- The sequence and coordinates of the catalytic triad are included in the prompt.
- Functional keywords describing trypsin are also included in the prompt.
- The overall generation length is reduced by a third, from 223 to 150 residues.
==============================
ESM3 maintains the coordination of the active site (cRMSD $0.73 \AA$ ) and the overall fold with high designability (pTM 0.84 , scTM mean 0.97 , std 0.006), despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D).
------------------------------
 - ESM3 is able to maintain coordination of the active site and overall fold with high designability.
- This is achieved despite a significant reduction in sequence length and the fold only being specified by the function keyword prompt.
- The coordination is measured by cRMSD, which is 0.73 $\AA$.
- The designability is measured by pTM, which is 0.84, and scTM mean, which is 0.97 with a standard deviation of 0.006.
- These results are shown in Figure 2D.
==============================
These examples illustrate ESM3's ability to find creative solutions to prompts specified in any of its input tracks, individually or in combination.
------------------------------
 - ESM3 can find creative solutions to prompts specified in any of its input tracks, individually or in combination.
- ESM3 has the ability to extract unique facts or ideas and present them in an unsorted markdown list.
- ESM3 is a helpful assistant.
==============================
This capability enables a rational approach to protein design, providing control at various levels of abstraction, from high-level topology to atomic coordinates, using a generative model to bridge the gap between the prompt and biological complexity.

------------------------------
 - Enables a rational approach to protein design
- Provides control at various levels of abstraction
- Uses a generative model to bridge the gap between the prompt and biological complexity
- Allows for control from high-level topology to atomic coordinates