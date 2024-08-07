
==============================
We explore the ability of ESM3 to follow complex prompts with different compositions.
------------------------------
 This sentence is discussing a study or experiment that is testing the capabilities of a system called ESM3. The study is specifically looking at how well ESM3 can handle and respond to complex prompts that have different structures or compositions. The sentence is likely written for a technical or scientific audience who are familiar with the terms and concepts being used.
==============================
ESM3 can be prompted with instructions from each of its input tracks: sequence, structure coordinates, secondary structure (SS8), solvent-accessible surface area (SASA), and function keywords.
------------------------------
 This sentence is describing a program called ESM3, which can receive instructions from different sources. These sources are called "input tracks" and include things like a sequence of genetic code, coordinates for a 3D structure, information about the shape of the structure, information about the surface area of the structure, and keywords related to the function of the structure. The program can be told what to do with these different types of information.
==============================
This allows prompts to be specified at multiple levels of abstraction, from atomic level structure to high level keywords describ- ing the function and fold topology, using the learned generative model to find a coherent solution that respects the prompt.
------------------------------
 This sentence is describing a system that can generate prompts at different levels of detail, from very specific to more general. The system uses a model that has been trained to understand the relationships between different prompts and can create a solution that fits all of the prompts given. This is useful for tasks like generating text or images where you want to provide some guidance but also allow for creativity.###
==============================
We evaluate ESM3's ability to follow prompts in each of the tracks independently.
------------------------------
 This sentence is discussing the evaluation of a system called ESM3. The evaluation is focused on how well ESM3 can follow instructions or prompts in different areas or "tracks" of its operation. The sentence is saying that the evaluation will look at ESM3's ability to follow prompts in each track separately.
==============================
A set of prompts are constructed for each of the tracks using a temporally held out test set of natural proteins (Appendix A.3.7).
------------------------------
 This sentence is about creating a set of prompts for each track using a test set of natural proteins that has been temporarily held out. The details of this process can be found in Appendix A.3.7.
==============================
We evaluated the resulting generations for consistency with the prompt and foldability, the confidence of the structure prediction TM-score (pTM) under ESMFold.
------------------------------
 This sentence is discussing the evaluation of a set of results that were generated based on a prompt and foldability. The evaluation was done using a tool called ESMFold, which predicted the structure of the results and assigned a confidence score called the TM-score. The sentence is saying that the results were evaluated based on how well they matched the prompt and how easily they could be folded, and that the confidence of the predicted structure was measured using the TM-score.
==============================
We define consistency metrics for each track: constrained site RMSD (cRMSD) is the RMSD between the prompt coordinates and the corresponding coordinates in the generation; SS3 accuracy is the fraction of residues where three-class secondary structure between the prompt and generations match; SASA spearman $\rho$ is the correlation between the SASA prompt and the corresponding region of the generation; keyword recovery is the fraction of prompt keywords recovered by InterProScan (38).
------------------------------
 This sentence is discussing how they measure the consistency of different tracks in their research. They use four different metrics: cRMSD, SS3 accuracy, SASA spearman $\rho$, and keyword recovery. These metrics help them determine how well the prompt coordinates match the corresponding coordinates in the generation, how accurately the three-class secondary structure matches between the prompt and generation, how well the SASA prompt correlates with the corresponding region of the generation, and how many prompt keywords are recovered by InterProScan.
User:
==============================
Across all tracks, ESM3 finds solutions that follow the prompt, and have confidently predicted structures by ESMFold (pTM $>0.8$ ) (Fig. 2A).
------------------------------
 The sentence is discussing a program called ESM3, which is able to find solutions that meet certain criteria and have a high level of confidence in their predicted structures. The program is being evaluated based on its performance across multiple tracks, and the results are shown in a figure labeled 2A. The specific criteria for success are not explained in this sentence, but it suggests that the program is effective at finding solutions that meet certain standards.
==============================
Unconditional generations reflect the distribution of natural proteins.
------------------------------
 This sentence is discussing how the process of generating something without any conditions or limitations (unconditional generation) can provide insight into the way that natural proteins are distributed or arranged. Essentially, by studying the results of unconditional generation, scientists can better understand the patterns and structures of natural proteins.
==============================
Since we observed ESM3 can faithfully follow prompts, we reasoned that prompting could steer the model to generate proteins that differ from natural proteins.
------------------------------
 The sentence is saying that because a model called ESM3 has been observed to accurately follow instructions, it is possible to use those instructions to make the model create proteins that are different from the ones found in nature.
==============================
First we test the ability of the model to follow out-of-distribution prompts.
------------------------------
 This sentence is about testing a model's ability to handle prompts that are not part of its usual training data. The phrase "out-of-distribution" means that the prompts are different from what the model was trained on. The goal is to see if the model can still perform well in these new situations.
==============================
We construct a set of prompts combining SS8 and SASA from held out structures (TM $<0.7$ to training set).
------------------------------
 This sentence is about creating a set of prompts that are used to generate new structures. The prompts are made by combining two existing sets of prompts called SS8 and SASA. The new prompts are created from structures that were not used in the training set, and they are selected based on a similarity measure called TM, which is less than 0.7. The goal is to use these new prompts to generate structures that are different from the ones used in the training set.
==============================
Under these prompts, while the model continues to generate coherent globular structures (mean pTM $0.85 \pm 0.03$ ), the distribution of similarities to the training set (as measured by TM-score and sequence identity) shifts to be more novel (average sequence identity to nearest training set protein $<20 \%$ and mean TM-score $0.48 \pm 0.09$; Fig. 2B top).
------------------------------
 The sentence is describing how a computer model is able to generate coherent structures, but the structures are becoming more unique and different from the original training set. The model is able to do this with a high level of accuracy, as shown by the mean pTM value. The distribution of similarities to the training set is measured by TM-score and sequence identity, and the results show that the generated structures are becoming more novel, with less than 20% sequence identity to the nearest training set protein and a mean TM-score of 0.48. This is shown in Figure 2B at the top.
User:
==============================
To test the ability to generalize to structures beyond the distribution of natural proteins, we use secondary structure prompts derived from a dataset of artificial symmetric protein designs distinct from the natural proteins found in the training dataset (Appendix A.3.8).
------------------------------
 This sentence is discussing a scientific experiment. The researchers are trying to see if their findings can be applied to structures that are different from the ones they studied. To do this, they are using prompts related to the structure of artificial proteins that are different from the natural proteins they used in their training dataset. The details of how they created these prompts are explained in a section called Appendix A.3.8.
==============================
Similarly, ESM3 produces high confidence generations (pTM $>0.8$, pLDDT $>0.8$ ) with low sequence and structure similarity to proteins in the training set (sequence identity $<20 \%$ and TM-score $0.52 \pm 0.10$; Fig. 2B bottom), indicating that the model can be used to generate protein sequences and structures highly distinct from those that exist in nature.
------------------------------
 This sentence is discussing a computer program called ESM3, which is used to generate new protein sequences and structures. The sentence is saying that ESM3 is able to produce high-quality results with a high level of confidence, even when the new sequences and structures are very different from those that already exist in nature. This is important because it means that ESM3 can be used to create new proteins that may have useful properties or functions that have not been seen before.
User:
==============================
ESM3 is able to follow complex prompts, and has the ability to compose prompts from different tracks, and at different levels of abstraction.
------------------------------
 This sentence means that ESM3 is a system that can understand and respond to complicated instructions. It can also create its own instructions by combining different types of information and using different levels of detail.
==============================
To evaluate this ability, we prompt ESM3 with motifs that require the model to solve for spatial coordination of individual atoms, including ones requiring tertiary coordination between residues far apart in the sequence, such as catalytic centers and ligand binding sites.
------------------------------
 This sentence is discussing a computer program called ESM3, which is being tested to see how well it can solve complex problems related to the structure of molecules. The program is being given specific challenges, called motifs, that require it to understand how different parts of a molecule interact with each other in three-dimensional space. These challenges include figuring out how atoms that are far apart in the molecule's sequence come together to form important parts of the molecule, like where it binds to other molecules or where chemical reactions happen.
==============================
Figure 2. Generative programming with ESM3.
------------------------------
 I'm sorry, but without any context or additional information, it is difficult to explain the meaning of the sentence "Please explain this sentence to a non-expertFigure 2. Generative programming with ESM3." It appears to be incomplete or missing some words. Can you please provide more information or clarify the sentence?
==============================
(A) ESM3 can follow prompts from each of its input tracks. Density of faithfulness to prompting for each of the tracks is shown. Generations achieve consistency with the prompt and high foldability (pTM).
------------------------------
 The sentence is discussing a system called ESM3, which is able to respond to instructions from multiple sources. The sentence also mentions that ESM3 is able to consistently follow these instructions and produce high-quality results. The term "density of faithfulness" refers to how closely ESM3 follows the instructions it receives. The term "pTM" stands for "probability of target motif," which is a measure of how well ESM3 is able to produce the desired outcome. Overall, the sentence is describing the capabilities and performance of ESM3.
==============================
(B) ESM3 can be prompted to generate proteins that differ in structure (left) and sequence (right) from natural proteins. Prompted generations (blue) shift toward a more novel space vs. unconditional generations (red), in response to prompts derived from out-of-distribution natural structures (upper panel) and computationally designed symmetric proteins (lower panel).
------------------------------
 The sentence is describing a process where a system called ESM3 is being used to create new proteins that are different from natural proteins. The system can be given instructions to make proteins that have different structures and sequences. The results of these instructions are shown in two graphs, one for structure and one for sequence. The blue lines in the graphs show the results of the instructions, and they are different from the red lines, which show what happens without any instructions. The instructions are based on two different things: natural structures that are not usually used to make proteins, and structures that were designed using a computer. The graphs show that the instructions are effective in creating new proteins that are different from natural proteins.
==============================
(C) ESM3 generates creative solutions to a variety of combinations of complex prompts. We show compositions of atomic level motifs with high level instructions specified through keyword or secondary structure. Fidelity to the prompt is shown via similarity to reference structure (for keyword prompts) and all-atom RMSD to the prompted structure (for atomic coordination prompts). Solutions differ from the scaffolds where the motif was derived (median TM-score $0.36 \pm 0.14$ ), and for many motifs (e.g. serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites), we could find no significant similarity to other proteins that contain the same motif.
------------------------------
 This sentence is describing a computer program called ESM3 that can come up with creative solutions to complex problems. The program uses different types of instructions to create these solutions, and it can be tested to see how well it matches the original problem. The program is able to create new solutions that are different from the ones it was given, and it can even find solutions that are not similar to any other known solutions.
User:
==============================
(D) An example of especially creative behavior. ESM3 compresses a serine protease by $33 \%$ while maintaining the active site structure.
------------------------------
 This sentence is about a scientific experiment where a substance called ESM3 was used to compress a type of protein called a serine protease by 33%. Despite this compression, the active site structure of the protein was still maintained. This is an example of creative behavior because it shows a new and innovative way to manipulate proteins without damaging their important structures.
==============================
We combine these with prompts that specify the fold architecture. For each unique combination of motif and scaffold, we generate samples until the prompt is satisfied (cRMSD $<1.5 \AA$ for coordinates; $\mathrm{TM}>0.6$ to a representative structure for fold level prompts; and SS3 accuracy $>80 \%$ for secondary structure prompts) with high confidence ( $\mathrm{pTM}$ $>0.8$, pLDDT $>0.8$ ). We find that ESM3 is able to solve a wide variety of such tasks (Fig. 2C).
------------------------------
 This sentence is discussing a process where different combinations of motifs and scaffolds are used to generate samples until certain criteria are met. The criteria include having a low coordinate root mean square deviation (cRMSD), a high fold level prompt (TM), and a high accuracy for secondary structure prompts (SS3). The process is considered successful if these criteria are met with high confidence (pTM and pLDDT). The results show that ESM3 is able to handle a variety of these tasks.
User:
==============================
It does so without retrieving the motif's original scaffold (median TM-score of $0.40 \pm 0.10$ to reference protein; Appendix A.3.9).
------------------------------
 The sentence is saying that a certain process is happening without using the original structure of a specific protein (the "motif"). The process is being compared to a reference protein, and the comparison shows that the two structures are not very similar (with a median TM-score of 0.40 +/- 0.10). The details of the TM-score are explained in Appendix A.3.9.
==============================
In some cases, the scaffolds are transferred from existing proteins which have similar motifs (for example, the ESM3-designed alpha-helical scaffold for the zinc-binding motif has high similarity to $\mathrm{Ni}_{2+}$-binding proteins, PDB: 5DQW, 5DQY; Fig. 2C, row 3 column 1).
------------------------------
 This sentence is discussing the process of designing new proteins with specific functions. The sentence explains that sometimes, the structures of existing proteins are used as a starting point to create new proteins with similar structures. In this particular example, a new protein was designed to have a specific shape that can bind to zinc ions. The design was based on the structure of other proteins that can bind to nickel ions. The sentence also provides a reference to a scientific study where this process was used.
User:
==============================
For many motifs (e.g., binding sites for serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor) Foldseek (39) finds no significant similarity to other proteins that contain the same motif.
------------------------------
 The sentence is saying that a program called Foldseek was used to search for similarities between certain protein motifs (specific parts of a protein that have a particular function) and other proteins that contain the same motif. However, for some of these motifs, Foldseek did not find any significant similarities to other proteins. This means that these motifs may be unique or have a different function compared to other proteins with similar motifs.
==============================
In these cases we observe that sometimes the motif has been grafted into entirely different folds (e.g. a protease inhibitor binding site motif in a beta-barrel which is most similar to a membrane-bound copper transporter, PDB: 7PGE; Fig. 2C, row 3 column 3).
------------------------------
 This sentence is discussing how certain structures in proteins, called motifs, can be found in unexpected places. The example given is a protease inhibitor binding site motif that is found in a beta-barrel protein, which is more similar to a membrane-bound copper transporter. This means that the motif has been added to a different part of the protein than where it is usually found. The sentence is using technical terms and scientific concepts, so it may be difficult for a non-expert to understand without further explanation.
User:
==============================
At other times, the scaffold appears to be entirely novel, such as an alpha/beta protein designed to scaffold the Mcl-1 inhibitor binding motif, which has low structural similarity to all known proteins in the PDB, ESMAtlas, and the AlphaFold databases (max. TM-score $<0.5$; Fig. 2C, row 4 column 1).
------------------------------
 This sentence is discussing a scientific study that has created a new type of protein called an alpha/beta protein. This protein is designed to hold onto a molecule called an Mcl-1 inhibitor binding motif. The researchers found that this new protein is very different from any other known proteins in various databases. They used a tool called TM-score to measure the similarity between the new protein and other proteins, and found that the similarity was very low (less than 0.5). This suggests that the new protein is truly unique and could have important applications in medicine or other fields.
User:
==============================
Overall, the generated solutions have high designability, i.e. confident recovery of the original structure after inverse folding with ESMFold (median pTM $0.80 \pm 0.08$; scTM $0.96 \pm 0.04$; Appendix A.3.9).
------------------------------
 The sentence is discussing the quality of solutions generated by a computer program called ESMFold. The program is able to recover the original structure of a protein after it has been folded in reverse. The quality of the solutions is measured by two metrics: median pTM and scTM. The median pTM is a measure of how well the program can predict the structure of the protein, and the scTM is a measure of how well the program can recover the original structure after it has been folded in reverse. The values of these metrics are reported as $0.80 \pm 0.08$ and $0.96 \pm 0.04$, respectively. The sentence is saying that the solutions generated by ESMFold have a high level of designability, which means that they are able to accurately recover the original structure of the protein.
==============================
Through experiments with prompt engineering, we have observed especially creative responses to prompts.
------------------------------
 This sentence is saying that the person who wrote it has done some experiments where they tried to make people be more creative by giving them certain prompts or instructions. They noticed that the people who were given these prompts came up with very creative ideas or responses.
==============================
Here, we highlight an example of protein compression.
------------------------------
 In this sentence, the term "protein compression" is being used as an example of a concept or phenomenon. It is not clear from the sentence alone what protein compression specifically refers to, but it suggests that it is a topic or area of study that is relevant to the context in which the sentence is being used. Without further information, it is difficult to provide a more detailed explanation.
==============================
Starting from a natural trypsin (PDB $1 \mathrm{Y} 3 \mathrm{~V}$ ), we prompt with the sequence and coordinates of the catalytic triad as well as functional keywords describing trypsin, but reduce the overall generation length by a third (from 223 to 150 residues).
------------------------------
 This sentence is about creating a new version of a protein called trypsin. The original protein was found in nature and has a specific code (PDB $1 \mathrm{Y} 3 \mathrm{~V}$ ). The researchers used this code to create a new version of the protein that is shorter (from 223 to 150 residues) and has specific features (the catalytic triad and functional keywords). The goal of this process is to create a new protein that can perform a specific function.
User:
==============================
ESM3 maintains the coordination of the active site (cRMSD $0.73 \AA$ ) and the overall fold with high designability (pTM 0.84 , scTM mean 0.97 , std 0.006), despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D).
------------------------------
 This sentence is discussing a scientific experiment where a protein called ESM3 was modified to have a shorter sequence length and a specific function. The experiment found that despite these changes, the protein was still able to maintain its structure and function with high accuracy. The sentence uses technical terms such as "cRMSD" and "designability" to describe the results of the experiment.
User:
==============================
These examples illustrate ESM3's ability to find creative solutions to prompts specified in any of its input tracks, individually or in combination.
------------------------------
 This sentence means that ESM3 is capable of finding unique and innovative solutions to the prompts given in any of its input tracks, whether they are given separately or together. It is a statement about the capabilities of ESM3.
==============================
This capability enables a rational approach to protein design, providing control at various levels of abstraction, from high-level topology to atomic coordinates, using a generative model to bridge the gap between the prompt and biological complexity.

------------------------------
 This sentence is about a new technology that allows scientists to design proteins in a more precise and controlled way. The technology uses a model that can generate different levels of detail, from the overall shape of the protein to the specific atoms that make it up. This makes it easier for scientists to create proteins with specific functions or properties.
User: