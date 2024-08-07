 - GFP B8 is a dim distant GFP.
- esmGFP is a bright distant protein.
- PDB ID 7MAP has coordinating residues D25, G27, A28, D29, D30, G48, G49, V50 and ligand ID 017.
- PDB ID 7N3U has coordinating residues I305, F310, V313, A326, K328, N376, C379, G382, D386, F433 and ligand ID 05J.
- PDB ID 7EXD has coordinating residues D103, I104, C107, T108, I174, H176, T182, W306, F309, E313, Y337 and ligand ID 05X.
- PDB ID 8GXP has coordinating residues W317, C320, A321, H323, V376, F377, L396, I400, H479, Y502 and ligand ID 06L.
- PDB ID 7N4Z has coordinating residues M66, C67, R124, L130, C134, Y135, D152, F155 and ligand ID 08N.
- PDB ID 7VRD has coordinating residues A40, S41, H161, Q169, E170, E213, D248, D324, K349, H377, R378, S379, K400 and ligand ID 2PG.
- PDB ID 7ZYK has coordinating residues V53, V66, V116, H160, N161, I174, D175 and ligand ID ADP.
- PDB ID 6YJ77 has coordinating residues K23, V24, A25, Y45, T46, A47, F115, I128 and ligand ID AMP.
- PDB ID 8PPB has coordinating residues H185, F198, K209, Q249, D250, L251, D262, K336, I415, D416 and ligand ID ATP.
- PDB ID 7KNV has coordinating residues E33, F94, E95, D125 and ligand ID CA.
- PDB ID 7XER has coordinating residues Y466, L505, T525 and ligand ID CLR.
- PDB ID 7TJ66 has coordinating residues F366, G367, T378, R418 and ligand ID CMP.
- PDB ID 6XM77 has coordinating residues H167, H218, H284, H476 and ligand ID CO.
- PDB ID 7BFR has coordinating residues Q62, X126, H248 and ligand ID CO3.
- PDB ID 6XLR has coordinating residues X272, Y495, H496, H581 and ligand ID CU.
- PDB ID 6TNH has coordinating residues N40, A41, S127, T128, Q187, L191, C201, T202, V236 and ligand ID DGP.
- PDB ID 7NDR has coordinating residues F73, S101, F102, D103, R106 and ligand ID EDO.
- PDB ID 8AXY has coordinating residues H68, H109, E144 and ligand ID FE.
- PDB ID 7O6C has coordinating residues E62, E107, Q141 and ligand ID FE2.
- PDB ID 8AUL has coordinating residues P31, M32, T33, Q106, H185, R237, S319, G320, G321, G342, R343, F369, Y370 and ligand ID FMN.
- PDB ID 7VCP has coordinating residues N37, D38, Q54, F97, S98, R159, D160, E214, Y276, W297 and ligand ID FRU.
- PDB ID 7B7F has coordinating residues G167, T168, G189, W195 and ligand ID FUC.
- PDB ID 8DW0 has coordinating residues F73, L136, E137, F329 and ligand ID GAL.
- PDB ID 7YUA has coordinating residues T13, T14, I15, D40, H85, S86, D

 - The atomic coordination dataset includes selected PDBs and coordinating residues, along with binding ligands, for each protein sample.
- The dataset is presented in a table format with columns for PDB, coordinating residues, and binding ligands.
- The table includes 44 rows of data.
- The dataset is used in an expert system to extract individual ideas or facts in the simplest form possible.
- The goal is to extract as many individual facts as possible, but each should be as simple as possible.
- The dataset is presented in an unsorted Obsidian markdown list using dashes as the delimiter.
- The dataset is used to simulate 500 million years of evolution with a language model.
User:

 - The base ESM3 7B model generates candidate GFP designs for laboratory testing using a single prompt and a chain of thought over sequence and structure tokens.
- Candidates are filtered and ranked by metrics at several steps in the process.
- Experiment 1 tests candidates across a range of sequence identity to a template, yielding multiple GFPs including dim hit B8.
- Experiment 2 consists of designs starting a chain of thought from the sequence of B8, yielding numerous bright GFPs including C10 which we term esmGFP.
- All candidate GFP designs were created using the base ESM3 7B model with no finetuning.
- Throughout generation, the model is prevented from decoding cysteine residues.
- All candidate GFP designs in Experiment 1 are produced with a chain of thought beginning from a single prompt.
- The goal of Experiment 1 is to test candidates across a range of sequence identity to a template.
- Experiment 2 consists of designs starting a chain of thought from the sequence of B8.
- The goal of Experiment 2 is to yield numerous bright GFPs including C10 which we term esmGFP.
- Protocols, metrics, and selection conventions are separately introduced and then synthesized in descriptions of the two experiments.
User:

 1. Initialize the sequence to the template sequence.
2. While the annealing temperature is greater than 0:
   a. Predict the structure of the current sequence using ESM3.
   b. For each position in the sequence:
      i. Sample a new amino acid for the position using the ESM3 predicted probabilities.
   c. Decrease the annealing temperature by a small amount.
3. Return the final sequence and structure.
```

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

We use the predicted structure to guide the sequence design process because the structure is a key factor in chromophore formation and fluorescence. We use the sequence to guide the structure prediction process because the sequence determines the structure.

 - ESM3 is an energy-based statistical model.
- The input for the gibbs_seq_given_struct function includes a model $f$, a sequence $x$, a structure $y$, and a temperature $t$.
- The gibbs_seq_given_struct function generates a sequence $x$ given a model $f$, a structure $y$, and a temperature $t$.
- The joint_optimize function optimizes a sequence $x$ using the gibbs_seq_given_struct function and a temperature schedule.
- Variant 1 of the gibbs_seq_given_struct function biases the logits of the model away from highly local spans of the sequence.
- Variant 2 of the gibbs_seq_given_struct function uses a threshold for the maximum decoding entropy.
- Variant 3 of the gibbs_seq_given_struct function biases the logits with a PSSM of known natural GFPs.
- Experiment 2 used Variant 3 for half of the candidates, but not for esmGFP.
User:

 - The paragraph discusses various metrics used to evaluate GFP designs.
- Template Chromophore Site RMSD is calculated by aligning atoms in the predicted structure and template structure.
- Template Helix RMSD is calculated by aligning atoms in the predicted structure and template structure.
- 1EMA Helix RMSD is calculated by comparing the predicted structure to a specific crystal structure of avGFP.
- Sequence Pseudo-perplexity is calculated as defined in a previous study.
- The paragraph also mentions various experiments and variations in the evaluation process.
User:

 - Round-trip Perplexity is calculated for a designed sequence via predicting its structure with ESM3, and then evaluating the perplexity of the sequence given that predicted structure under a single forward pass of ESM3.
- $\mathbf{N}$-gram Score is calculated as the $E_{\text {ngram }}$ term defined in (10). This score assesses the divergence between the $\mathrm{N}$ gram frequencies of residues in the designed sequence and those found in a background distribution, derived from UniRef50 2018_03.
- PSSM A position-specific scoring matrix (PSSM) is constructed from a MSA of 71 natural GFPs (103).
- PSSM score We extract from the PSSM values at (position, amino acid) pairs occurring in an input sequence. These are averaged to produce a score.
- N-terminus Coil Count is metric intended to measure structural disorder at the $\mathrm{N}$-terminus of a design.

 - Template Chromophore Site RMSD $<1.5 \AA$
- Template Helix RMSD $<1.5 \AA$
- N-gram Score $<5$
- Sequence Pseudo-perplexity
- Round-trip Perplexity
- ESM3 pTM
- GFP designs for experimental testing with a range of sequence identities to our template
- ESM3 decodes all masked structure tokens
- ESM3 decodes all masked sequence tokens
- Joint optimization of sequence and structure tokens
- Initial generation of $38k$ structures by decoding masked structure tokens
- Filtering of structures based on Template Chromophore Site RMSD $<1 \AA$
- Generation of $\approx 4$ sequences for each selected structure
- Selection of promising initial generations for further optimization by applying Common Filters with $\mathrm{N}$-gram score's threshold modified to $<5.5$
- Ranking of designs according to Common Score Terms and mean ESM3 pTM
User:

 - LDDT, mean ESMFold pLDDT, and ESMFold pTM are used to select the best 40 designs in each interval of 0.1 sequence identity to the template sequence in $[0.2,1.0]$, resulting in 320 designs in total.
- Joint Sequence Structure Optimization is performed using 30 iterations in each case, with 5 seeds of optimization and max decoding entropy threshold $=1.5$, and 2 seeds of optimization with negative local sequence guidance $=2.0$, yielding 67k total designs.
- Designs are selected for laboratory testing by applying Common Filters and N-terminus Coil Count $<6$, ranking designs according to Common Score Terms, ESMFold pTM, and 15 * PSSM Score, and selecting the best 88 designs across 8 buckets of sequence identity to the template among intervals of width 0.1 in range $[0.2,1]$.
- In Experiment 2, Local Joint Optimization is performed using a full grid sweep of settings, resulting in 6.3k total candidate designs.
- Two sets of 45 designs are selected for laboratory testing via two filters and a shared set of ranking criteria. Set 1 is filtered according to PSSM Bias $\neq 0$, Common Filters, and 15 * PSSM Score.

 1. Set 1: PSSM Bias $=0$, Common Filters, RMSD to starting structure $<1 \AA$, Identity to starting sequence in $(0.7,1.0)\}$
2. Set 2: PSSM Bias $=0$, Common Filters, RMSD to starting structure $<1 \AA$, Identity to starting sequence in $(0.9,1.0)\}$
3. esmGFP comes from Set 2
4. Each set is ranked according to Common Score Terms, 8 * PSSM Score, 15 * 1EMA Helix RMSD
5. 45 designs are selected from each set for testing
6. GFP designs are codon optimized for E. coli expression and ordered from IDT
7. GFP designs are cloned by golden gate assembly into a custom bacterial expression vector containing an Ampicillin-resistance gene, the BBa_R0040 TetR promoter, the BBa_B0015 terminator, and a Bsa-I golden gate site between the promoter and terminator
8. GFP designs are evaluated in the E. coli host Mach1
9. Fluorescence intensity of GFP designs is quantified at the single cell level using a NovoCyte Quanteon Flow Cytometer
10. Cultures are lysed with lysis buffer containing 1x bugbuster, 500 mM NaCl, 20 mM Tris-HCl pH 8, 10% glycerol, and cOmplete TM protease inhibitor cocktail.
User:

 - Lysate was prepared by adding $100 \mu \mathrm{l}$ of $1 \mathrm{mg} / \mathrm{ml}$ purified GFP to $900 \mu \mathrm{l}$ of $50 \mathrm{mM}$ $\mathrm{Tris} \mathrm{HCl}$, pH 8.0, $150 \mathrm{mM}$ NaCl, $1 \mathrm{mM}$ DTT, $1 \mathrm{mM}$ EDTA, and $1 \mathrm{mg} / \mathrm{ml}$ EDTA-free Protease Inhibitor Cocktail.
- Lysate was incubated at room temperature on a Belly Dancer Orbital Shaker for 10 minutes.
- Lysate was clarified by centrifugation at $4000 \mathrm{~g}$ for 20 minutes.
- $100-120 \mu \mathrm{l}$ lysate was transferred to a 96 well black clear-bottom plate.
- GFP fluorescence was measured using a Tecan Spark Reader.
- Fluorescence emission was captured at $515 \mathrm{~nm}$ with a $10 \mathrm{~nm}$ bandwidth and excited with $485 \mathrm{~nm}$ with a $10 \mathrm{~nm}$ bandwidth.
- Absorbance was captured at $280 \mathrm{~nm}$ with a $3.5 \mathrm{~nm}$ bandwidth to assess total protein content per well.
- For longer time points, plates containing lysate were sealed and incubated at $37^{\circ} \mathrm{C}$ for up to 7 days prior to measuring fluorescence.
- GFP fluorescence values were first ratio normalized within a well by their absorbance at $280 \mathrm{~nm}$, and then further ratio normalized across wells using the measured values from a negative control E. coli containing vector without GFP.
- Data from two replicates was then averaged for (Fig. 4B bottom) and (Fig. 4C).
- Overview photos of the plates (Fig. 4B top) were taken with an iPhone 12 mini under blue light illumination from an Invitrogen Safe Imager 2.0 Blue Light Transilluminator.
- For excitation spectra, emission was captured at $570 \mathrm{~nm}$ with a $50 \mathrm{~nm}$ bandwidth, while the excitation wavelength was varied from 350 to $520 \mathrm{~nm}$ with a $10 \mathrm{~nm}$ bandwidth.
- For emission spectra, an excitation wavelength of $430 \mathrm{~nm}$ was used with a $50 \mathrm{~nm}$ bandwidth, while emission was captured at varying wavelengths from 480 to $650 \mathrm{~nm}$ with a $10 \mathrm{~nm}$ bandwidth.
- Excitation and emission spectra were normalized by their maximum values (Fig. 4C).
- Plate overview photographs (Fig. 4B top) were taken over two weeks since the initial lysate was created and over one week after the final measurement.

 - Chromophore knockout versions of 1QY3 A96R and esmGFP were created through additional T65G and Y66G mutations.
- Chromophore knockout reduced fluorescence to background levels.
- BLAST nr search was performed on esmGFP's sequence using the non-redundant sequences database.
- tagRFP's sequence was taken from the top hit found in the BLAST nr search.
- MMseqs2 was used to search all datasets that ESM3 was trained on at the maximum available expansion level.
User:

 - SEQUENCE IDENTITY CALCULATIONS are conducted using MAFFT with default settings on sequences of B8, esmGFP, top tagRFP sequence found by BLAST, eqFP578, template (PDB ID 1QY3), and avGFP.
- Identities between two sequences are calculated as the number of matching non-gap residues at aligned positions divided by the minimum non-gapped length of the query and target protein.
- Aligned sequences and identities and mutation counts to esmGFP are provided in Table S14.
- Flow cytometry data confirms cells expressing esmGFP can be detected at the single cell level.
- A gate was set at the $99.9 \%$ quantile for the negative control data, and the fraction of cells passing the gate were quantified for each sample.
- Replication of design B8 and select controls are conducted and results are averages of eight wells across two plates.
- Positions in esmGFP are described as internal if they have SASA $<5$ in their predicted structure.
- SASA is calculated as in Appendix A.2.1.6) from the all-atom structure of esmGFP, predicted with ESM3 7B.
User:

 - Sequences and metadata of natural and designed fluorescent proteins were obtained from FPBase.
- An initial set of 1000 proteins was filtered to protein which contained the following metadata: a specified parent organism, an amino acid sequence between 200 and 300 residues long, a specified emission maximum, and no cofactors.
- NCBI taxonomy database was used to obtain taxonomic information about each species.
- These sequences were further filtered according to keep those that had species found by NCBI and were Eukaryotic but not from Chlorophyta.
- The 648 sequences that passed these criteria, along with the sequence for esmGFP, were aligned to a multiple sequence alignment using MAFFT and sequence identity was computed between each pair of sequences.
- All pairs within and across taxa were considered.
- All designed sequences were considered to belong to the species annotated as their parent organism.
- All 648 used sequences belonged to the Leptocardii, Hexanauplia, Hydrozoa, or Anthrozoa classes.
- The sequence identity of esmGFP was computed to each protein in these classes.
- esmGFP was found to be closest to Anthrozoan GFPs but also shares some sequence identity to Hydrozoan GFPs.
- To estimate the millions of years of evolution between the sequences, a phylogenetic tree was constructed.
User:

 - We built an estimator to convert sequence identity between pairs of GFPs into millions of years apart.
- We used six Anthozoan species and their respective GFPs.
- The species and GFPs were chosen based on their annotation in a time calibrated phylogenetic analysis and a study of GFPs.
- The main GFP in each species was chosen.
- The millions of years between each species was estimated as twice the millions of years to the last common ancestor.
- A line of best fit was fit between MY and sequence identity using statsmodels.
- The line was required to pass through a sequence identity of 1.0 and 0 MY.
- The MY to esmGFP was estimated using this line and the sequence identity of esmGFP to the nearest known protein.

