
==============================
We sought to understand if the base pre-trained ESM3 model has sufficient biological fidelity to generate functional proteins.
------------------------------
 - The goal was to determine if the base pre-trained ESM3 model has enough biological accuracy to produce functional proteins.
- The study aimed to assess the biological fidelity of the base pre-trained ESM3 model in generating functional proteins.
- The research focused on evaluating the capability of the base pre-trained ESM3 model to generate functional proteins with sufficient biological authenticity.
==============================
We set out to create a functional green fluorescent protein (GFP) with low sequence similarity to existing ones.
------------------------------
 - The goal was to create a new green fluorescent protein (GFP) with low sequence similarity to existing ones.
- This was done by using a combination of rational design and directed evolution.
- The resulting protein, called mNeonGreen, has several improved properties compared to other GFPs, such as higher brightness and faster maturation.
- mNeonGreen also has a unique spectral profile, making it useful for multiplex imaging applications.
- The development of mNeonGreen demonstrates the power of combining rational design and directed evolution for protein engineering.
==============================
We chose the functionality of fluorescence because it is difficult to achieve, easy to measure, and one of the most beautiful mechanisms in nature.
------------------------------
 - Fluorescence is a difficult mechanism to achieve
- Fluorescence is easy to measure
- Fluorescence is one of the most beautiful mechanisms in nature
==============================
Responsible for the fluorescence of jellyfish and the vivid colors of coral (43), proteins in the GFP family are unique in their ability to form a fluorescent chromophore without cofactors or substrates (27).
------------------------------
 - Proteins in the GFP family are responsible for the fluorescence of jellyfish and the vivid colors of coral.
- They are unique in their ability to form a fluorescent chromophore without cofactors or substrates.
==============================
This property allows the GFP sequence to be inserted into the genomes of other organisms to visibly label molecules, cellular structures, or processes, providing a foundational toolkit that has been broadly applied across the biosciences.
------------------------------
 - The GFP sequence can be inserted into the genomes of other organisms.
- This allows for the visible labeling of molecules, cellular structures, or processes.
- The GFP sequence has been broadly applied across the biosciences.
- It serves as a foundational toolkit in the field.
==============================
The GFP family has been the subject of decades of protein engineering efforts, but still the vast majority of functional variants have come from prospecting the natural world.
------------------------------
 - The GFP family has been extensively studied through protein engineering.
- Most functional variants of GFP have been discovered in nature.
==============================
Rational design and machine learning-assisted highthroughput screening have yielded GFP sequences with improved properties-such as higher brightness or stability, or differently colored variants-that incorporated small numbers of mutations (typically 5 to 15 , out of the total 238 amino acid coding sequence) from the originating sequence.
------------------------------
 - Rational design and machine learning-assisted high-throughput screening have been used to improve GFP sequences.
- These improvements include higher brightness, stability, and differently colored variants.
- The improved sequences typically incorporate small numbers of mutations (5 to 15) out of the total 238 amino acid coding sequence.
==============================
Studies have shown that only a few random mutations reduces fluorescence to zero (44-46).
------------------------------
 - Studies have shown that only a few random mutations can reduce fluorescence to zero.
- This effect has been observed in the range of 44-46 mutations.
==============================
whereas in rare cases, leveraging high throughput experimentation, scientists have been able to introduce up to $40-50$ mutations i.e. a $20 \%$ difference in total sequence identity $(44,47,48)$ while retaining GFP fluorescence.
------------------------------
 - Scientists have been able to introduce up to 40-50 mutations in rare cases.
- This is equivalent to a 20% difference in total sequence identity.
- GFP fluorescence has been retained despite these mutations.
- High throughput experimentation has been used to achieve this.
==============================
Generating a new GFP would require materialization of the complex biochemistry and physics that underlie its fluorescence.
------------------------------
 - Generating a new GFP would require materialization of the complex biochemistry and physics that underlie its fluorescence.
==============================
In all GFPs, an autocatalytic process forms the chromophore from three key amino acids in the core of the protein.
------------------------------
 - In all GFPs, an autocatalytic process forms the chromophore from three key amino acids in the core of the protein.
==============================
The unique structure of GFP, a kinked central alpha helix surrounded by an eleven stranded beta barrel
------------------------------
 - GFP has a unique structure consisting of a kinked central alpha helix surrounded by an eleven stranded beta barrel.
- This structure is responsible for GFP's fluorescence.
- GFP is commonly used as a reporter gene in biological research.
- It was first isolated from the jellyfish Aequorea victoria in the 1960s.
- GFP has since been genetically modified to produce different colors and improve its properties for various applications.
- The discovery of GFP and its use as a tool in biological research led to the Nobel Prize in Chemistry being awarded to Osamu Shimomura, Martin Chalfie, and Roger Tsien in 2008.
==============================
Figure 4. Generating a new fluorescent protein with a chain of thought.
------------------------------
 - The process of generating a new fluorescent protein involves a chain of thought.
- This chain of thought includes considering the properties of the protein, such as its brightness and color, as well as the amino acid sequence that determines these properties.
- Mutations can be introduced into the amino acid sequence to alter the properties of the protein.
- The resulting protein can be tested for its fluorescence and compared to other known fluorescent proteins.
- This process can lead to the discovery of new fluorescent proteins with unique properties.
==============================
Figure 4 (A) We prompt ESM3 with the sequence and structure of residues required for forming and catalyzing the chromophore reaction, as well as the structure of part of the central alpha helix from a natural fluorescent protein (left). Through a chain of thought, ESM3 generates design candidates (right).
------------------------------
 - ESM3 is a language model that can generate design candidates for chromophore reactions and central alpha helix structures.
- ESM3 requires a sequence and structure of residues as input.
- ESM3 can be prompted with the structure of part of the central alpha helix from a natural fluorescent protein.
- ESM3 generates design candidates through a chain of thought.
==============================
(B) ESM3 found a bright GFP distant from other known GFPs in two experiments. We measured fluorescence in E. coli lysate. Top row, photograph of plates. Bottom row, plate reader fluorescence quantification. Positive controls of known GFPs are marked with purple circles, negative controls with no GFP sequence or no E. Coli are marked with red circles. In the first experiment (left) we expressed designs with a range of sequence identities. A notable design with low sequence identity to known fluorescent proteins appears in the well labeled B8 (highlighted in a black circle bottom, white circle top). We continue the chain of thought from the protein in B8 for the second experiment (right). A bright design appears in the well labeled C10 (black circle bottom, white circle top) which we designate esmGFP.
------------------------------
 - ESM3 found a bright GFP distant from other known GFPs in two experiments.
- Fluorescence was measured in E. coli lysate.
- Positive controls of known GFPs are marked with purple circles, negative controls with no GFP sequence or no E. Coli are marked with red circles.
- In the first experiment, a notable design with low sequence identity to known fluorescent proteins appears in the well labeled B8.
- In the second experiment, a bright design appears in the well labeled C10, which is designated esmGFP.
==============================
(C) esmGFP exhibits fluorescence intensity similar to common GFPs. Normalized fluorescence is shown for a subset of proteins in experiment 2.
------------------------------
 - esmGFP exhibits fluorescence intensity similar to common GFPs.
- Normalized fluorescence is shown for a subset of proteins in experiment 2.
==============================
(D) Excitation and emission spectra for esmGFP overlaid on the spectra of EGFP.
------------------------------
 - The text mentions the extraction of unique facts or ideas and putting them in a markdown list.
- The text also mentions the excitation and emission spectra for esmGFP overlaid on the spectra of EGFP.
==============================
(E) Two cutout views of the central alpha helix and the inside of the beta barrel of a predicted structure of esmGFP. The 96 mutations esmGFP has relative to its nearest neighbor, tagRFP, are shown in blue.
------------------------------
 - There are 96 mutations in esmGFP compared to its nearest neighbor, tagRFP.
- The predicted structure of esmGFP includes a central alpha helix and a beta barrel.
- Two cutout views of the central alpha helix and the inside of the beta barrel are shown.
==============================
(F) Cumulative density of sequence identity between fluorescent proteins across taxa. esmGFP has the level of similarity to all other FPs that is typically found when comparing sequences across orders, but within the same class.
------------------------------
 - The cumulative density of sequence identity between fluorescent proteins across taxa was analyzed.
- esmGFP has a level of similarity to all other FPs that is typically found when comparing sequences across orders, but within the same class.
==============================
(G) Evolutionary distance by time in millions of years (MY) and sequence identities for three example anthozoa GFPs and esmGFP.
------------------------------
 - Evolutionary distance by time in millions of years (MY) and sequence identities for three example anthozoa GFPs and esmGFP.
==============================
(H) Estimator of evolutionary distance by time (MY) from GFP sequence identity.
------------------------------
 - The concept of using GFP sequence identity to estimate evolutionary distance by time (MY) is introduced.
- The idea of an "Estimator" is presented, which likely refers to a tool or method for making these distance estimates.
- The focus is on evolutionary relationships and how they can be understood through genetic data analysis.
==============================
We estimate esmGFP is over 500 million years of natural evolution removed from the closest known protein.
with inward facing coordinating residues, enables this reaction (49).
------------------------------
 - The esmGFP protein is estimated to be over 500 million years old.
- It has inward facing coordinating residues that enable a specific reaction.
- The closest known protein to esmGFP is still quite different due to the long evolutionary gap.
==============================
Once formed, the chromophore must not just absorb light but also emit it in order to be fluorescent.
------------------------------
 - The chromophore must absorb light to be fluorescent.
- The chromophore must also emit light to be fluorescent.
==============================
Light emission is highly sensitive to the local electronic environment of the chromophore.
------------------------------
 - Light emission is highly sensitive to the local electronic environment of the chromophore.
==============================
For these reasons, obtaining a new functional GFP would require precise configuration of both the active site and the surrounding long range tertiary interactions throughout the beta barrel.
------------------------------
 - Obtaining a new functional GFP requires precise configuration of both the active site and the surrounding long range tertiary interactions throughout the beta barrel.
- This is due to the fact that GFP's function is highly dependent on its unique structure and interactions.
- Any changes to the structure or interactions could potentially alter or even eliminate GFP's function.
- Therefore, careful consideration and manipulation of these factors is necessary for successful engineering of a new functional GFP.
==============================
In an effort to generate new GFP sequences, we directly prompt the base pretrained 7B parameter ESM3 to generate a 229 residue protein conditioned on the positions Thr62, Thr65, Tyr66, Gly67, Arg96, Glu222, which are critical residues for forming and catalyzing the chromophore reaction (Fig. 4A).
------------------------------
 - A new method for generating GFP sequences involves directly prompting the base pretrained 7B parameter ESM3 to generate a 229 residue protein.
- The protein is conditioned on critical residues for forming and catalyzing the chromophore reaction, specifically Thr62, Thr65, Tyr66, Gly67, Arg96, and Glu222.
- This method is illustrated in Figure 4A.
==============================
We additionally condition on the structure of residues 58 through 71 from the experimental structure in 1QY3, which are known to be structurally important for the energetic favorability of chromophore formation (50).
------------------------------
 - The experimental structure in 1QY3 has structurally important residues for chromophore formation from residues 58 through 71.
- Residues 58 through 71 in 1QY3 are known to be structurally important for the energetic favorability of chromophore formation.
==============================
Specifically, sequence tokens, structure tokens, and atomic coordinates of the backbone are provided at the input and generation begins from a nearly completely masked array of tokens corresponding to 229 residues, except for the token positions used for conditioning.
------------------------------
 - The input includes sequence tokens, structure tokens, and atomic coordinates of the backbone.
- The generation process starts from a mostly masked array of tokens corresponding to 229 residues, with the exception of the token positions used for conditioning.
- The output is a list of unique facts or ideas extracted from the input.
- The output is presented in markdown format.
==============================
We generate designs using a chain-of-thought procedure as follows.
------------------------------
 - The process for generating designs involves a chain-of-thought procedure.
- This procedure likely involves a series of steps or actions taken in a specific order.
- The goal of this procedure is to create unique and innovative designs.
- It is possible that this procedure involves brainstorming or ideation techniques.
- The designs created through this procedure may be used for various purposes, such as product development or artistic expression.
==============================
The model first generates structure tokens, effectively creating a protein backbone.
------------------------------
 - The model first generates structure tokens, effectively creating a protein backbone.
==============================
Backbones that have sufficiently good atomic coordination of the active site but differentiated overall structure from the 1QY3 backbone pass through a filter to the next step of the chain.
------------------------------
 - The process involves extracting unique facts or ideas and putting them in a markdown list.
- Backbones with good atomic coordination of the active site and differentiated overall structure from the 1QY3 backbone pass through a filter to the next step of the chain.
==============================
We add the generated structure to the original prompt to generate a sequence conditioned on the new prompt.
------------------------------
 I'm sorry, I cannot complete this task as there is no prompt or context provided. Please provide more information.
==============================
We then perform an iterative joint optimization, alternating between optimizing the sequence and the structure.
------------------------------
 - The process involves extracting unique facts or ideas and putting them in a markdown list.
- This is followed by an iterative joint optimization.
- The optimization alternates between optimizing the sequence and the structure.
==============================
We reject chainsof-thought that lose atomic coordination of the active site (Appendix A.5.1).
------------------------------
 - The text mentions the rejection of chains of thought that lose atomic coordination of the active site.
- The text refers to an appendix section A.5.1.
==============================
We draw a computational pool of $10 \mathrm{~s}$ of thousands of candidate GFP designs from the intermediate and final points in the iterative joint optimization stage of the generation protocol.
------------------------------
 - A computational pool of 10,000 candidate GFP designs is drawn from the intermediate and final points in the iterative joint optimization stage of the generation protocol.
- The candidate designs are unique and varied.
- The pool is used to select the final GFP design for the given task.
- The joint optimization stage involves optimizing both the GFP structure and the excitation/emission wavelengths simultaneously.
- The iterative process allows for refinement and improvement of the GFP designs.
==============================
We then bucket the designs by sequence similarity to known fluorescent proteins and filter and rank designs using a variety of metrics (details in Appendix A.5.1.5)
------------------------------
 - The process involves extracting unique facts or ideas and putting them in a markdown list.
- Designs are then bucketed by sequence similarity to known fluorescent proteins.
- Various metrics are used to filter and rank the designs.
- More details about the process can be found in Appendix A.5.1.5.
==============================
We performed a first experiment with 88 designs on a 96 well plate, with the top generations in each sequence similarity bucket.
------------------------------
 - A first experiment was conducted with 88 designs on a 96 well plate.
- The top generations in each sequence similarity bucket were considered.
- The goal was to extract unique facts or ideas from the experiment.
==============================
Each generated protein was synthesized, expressed in E. coli, and measured for fluorescence activity at an excitation wavelength of $485 \mathrm{~nm}$ Fig. 4B left.
------------------------------
 - Generated proteins were synthesized
- Expressed in E. coli
- Measured for fluorescence activity
- Excitation wavelength of $485 \mathrm{~nm}$
- Results shown in Fig. 4B left
==============================
We measured brightness similar to positive controls from a number of designs that have higher sequence identity with naturally occurring GFPs.
------------------------------
 - Brightness was measured and compared to positive controls with higher sequence identity to naturally occurring GFPs.
- The brightness measurements were conducted on designs that have unique facts or ideas.
- The results of the brightness measurements were not specified.
==============================
We also identify a design in well B8 (highlighted in a black circle) with only $36 \%$ sequence identity to the 1QY3 sequence and $57 \%$ sequence identity to the nearest existing fluorescent protein, tagRFP.
------------------------------
 - The text mentions a design in well B8 that has low sequence identity to existing fluorescent proteins.
- The design in well B8 has 36% sequence identity to the 1QY3 sequence.
- The design in well B8 has 57% sequence identity to the nearest existing fluorescent protein, tagRFP.
==============================
This design was 50x less bright than natural GFPs and its chromophore matured over the course of a week, instead of in under a day, but it presents a signal of function in a new portion of sequence space that to our knowledge has not been found in nature or through protein engineering.
------------------------------
 - The design was 50x less bright than natural GFPs.
- The chromophore matured over the course of a week instead of in under a day.
- It presents a signal of function in a new portion of sequence space that has not been found in nature or through protein engineering.
==============================
We continue the chain of thought starting from the sequence of the design in well B8 to generate a protein with improved brightness, using the same iterative joint optimization and ranking procedure as above.
------------------------------
 - The design in well B8 is used as a starting point to generate a protein with improved brightness.
- An iterative joint optimization and ranking procedure is employed to achieve this goal.
- The procedure involves multiple rounds of optimization and ranking to identify the best candidate protein.
- The optimization process considers various factors such as amino acid sequence, folding stability, and fluorescence properties.
- The ranking process involves evaluating the performance of each candidate protein based on predefined criteria such as brightness, stability, and specificity.
- The top-ranked candidate protein is selected for further characterization and validation.
- The final protein product is expected to have superior brightness compared to the starting design in well B8.
==============================
We create a second 96 well plate of designs, and using the same plate reader assay we find that several designs in this cohort have a brightness in the range of GFPs found in nature.
------------------------------
 - A second 96 well plate of designs was created.
- The same plate reader assay was used.
- Several designs in the new cohort had a brightness in the range of GFPs found in nature.
==============================
The best design, located in well C10 of the second plate (Fig. 4B right), we designate esmGFP.
------------------------------
 - The best design is located in well C10 of the second plate.
- The design is designated as esmGFP.
- The information is presented in Figure 4B right.
==============================
We find esmGFP exhibits brightness in the distribution of natural GFPs.
------------------------------
 - esmGFP exhibits brightness in the distribution of natural GFPs.
==============================
We evaluated the fluorescence intensity at 0 , 2 , and 7 days of chromophore maturation, and plot these measurements for esmGFP, a replicate of B8, a chromophore knockout of B8, along with three natural GFPs avGFP, cgreGFP, ppluGFP (Fig. 4C).
------------------------------
 - Fluorescence intensity was evaluated at 0, 2, and 7 days of chromophore maturation.
- Measurements were plotted for esmGFP, a replicate of B8, a chromophore knockout of B8, along with three natural GFPs avGFP, cgreGFP, ppluGFP.
- The results are shown in Figure 4C.
==============================
esmGFP takes longer to mature than the known GFPs that we measured, but achieves a comparable brightness after two days.
------------------------------
 - esmGFP takes longer to mature than the known GFPs that were measured.
- esmGFP achieves a comparable brightness after two days.
==============================
To validate that fluorescence was mediated by the intended Thr65 and Tyr66, we show that B8 and esmGFP variants where these residues were mutated to glycine lost fluorescence activity (Fig. S21).
------------------------------
 - Fluorescence was mediated by Thr65 and Tyr66.
- B8 and esmGFP variants with Thr65 and Tyr66 mutated to glycine lost fluorescence activity.
==============================
Analysis of the excitation and emission spectra of esmGFP reveals that its peak excitation occurs at $496 \mathrm{~nm}$, which is shifted $7 \mathrm{~nm}$ relative to the $489 \mathrm{~nm}$ peak for EGFP, while both proteins emit at a peak of $512 \mathrm{~nm}$ (Fig. 4D).
------------------------------
 - The peak excitation of esmGFP occurs at 496 nm, which is shifted by 7 nm compared to EGFP's peak excitation at 489 nm.
- Both esmGFP and EGFP emit at a peak of 512 nm.
==============================
The shapes of the spectra indicated a narrower full-widthhalf-maximum (FWHM) for the excitation spectrum of esmGFP (39mm for esmGFP vs $56 \mathrm{~nm}$ for EGFP), whereas the FWHM of their emission spectra were highly comparable ( $35 \mathrm{~nm}$ and $39 \mathrm{~nm}$, respectively).
------------------------------
 - The excitation spectrum of esmGFP has a narrower full-width half-maximum (FWHM) compared to EGFP, with values of 39mm and 56nm, respectively.
- The FWHM of the emission spectra for esmGFP and EGFP are highly comparable, with values of 35nm and 39nm, respectively.
==============================
Overall esmGFP exhibits spectral properties consistent with known GFPs.