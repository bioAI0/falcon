We sought to understand if the base pre-trained ESM3 model has sufficient biological fidelity to generate functional proteins.

We set out to create a functional green fluorescent protein (GFP) with low sequence similarity to existing ones.

We chose the functionality of fluorescence because it is difficult to achieve, easy to measure, and one of the most beautiful mechanisms in nature.

Responsible for the fluorescence of jellyfish and the vivid colors of coral (43), proteins in the GFP family are unique in their ability to form a fluorescent chromophore without cofactors or substrates (27).

This property allows the GFP sequence to be inserted into the genomes of other organisms to visibly label molecules, cellular structures, or processes, providing a foundational toolkit that has been broadly applied across the biosciences.

The GFP family has been the subject of decades of protein engineering efforts, but still the vast majority of functional variants have come from prospecting the natural world.

Rational design and machine learning-assisted highthroughput screening have yielded GFP sequences with improved properties-such as higher brightness or stability, or differently colored variants-that incorporated small numbers of mutations (typically 5 to 15 , out of the total 238 amino acid coding sequence) from the originating sequence.

Studies have shown that only a few random mutations reduces fluorescence to zero (44-46).

whereas in rare cases, leveraging high throughput experimentation, scientists have been able to introduce up to $40-50$ mutations i.e. a $20 \%$ difference in total sequence identity $(44,47,48)$ while retaining GFP fluorescence.

Generating a new GFP would require materialization of the complex biochemistry and physics that underlie its fluorescence.

In all GFPs, an autocatalytic process forms the chromophore from three key amino acids in the core of the protein.

The unique structure of GFP, a kinked central alpha helix surrounded by an eleven stranded beta barrel

Figure 4. Generating a new fluorescent protein with a chain of thought.

Figure 4 (A) We prompt ESM3 with the sequence and structure of residues required for forming and catalyzing the chromophore reaction, as well as the structure of part of the central alpha helix from a natural fluorescent protein (left). Through a chain of thought, ESM3 generates design candidates (right).

(B) ESM3 found a bright GFP distant from other known GFPs in two experiments. We measured fluorescence in E. coli lysate. Top row, photograph of plates. Bottom row, plate reader fluorescence quantification. Positive controls of known GFPs are marked with purple circles, negative controls with no GFP sequence or no E. Coli are marked with red circles. In the first experiment (left) we expressed designs with a range of sequence identities. A notable design with low sequence identity to known fluorescent proteins appears in the well labeled B8 (highlighted in a black circle bottom, white circle top). We continue the chain of thought from the protein in B8 for the second experiment (right). A bright design appears in the well labeled C10 (black circle bottom, white circle top) which we designate esmGFP.

(C) esmGFP exhibits fluorescence intensity similar to common GFPs. Normalized fluorescence is shown for a subset of proteins in experiment 2.

(D) Excitation and emission spectra for esmGFP overlaid on the spectra of EGFP.

(E) Two cutout views of the central alpha helix and the inside of the beta barrel of a predicted structure of esmGFP. The 96 mutations esmGFP has relative to its nearest neighbor, tagRFP, are shown in blue.

(F) Cumulative density of sequence identity between fluorescent proteins across taxa. esmGFP has the level of similarity to all other FPs that is typically found when comparing sequences across orders, but within the same class.

(G) Evolutionary distance by time in millions of years (MY) and sequence identities for three example anthozoa GFPs and esmGFP.

(H) Estimator of evolutionary distance by time (MY) from GFP sequence identity.

We estimate esmGFP is over 500 million years of natural evolution removed from the closest known protein.
with inward facing coordinating residues, enables this reaction (49).

Once formed, the chromophore must not just absorb light but also emit it in order to be fluorescent.

Light emission is highly sensitive to the local electronic environment of the chromophore.

For these reasons, obtaining a new functional GFP would require precise configuration of both the active site and the surrounding long range tertiary interactions throughout the beta barrel.

In an effort to generate new GFP sequences, we directly prompt the base pretrained 7B parameter ESM3 to generate a 229 residue protein conditioned on the positions Thr62, Thr65, Tyr66, Gly67, Arg96, Glu222, which are critical residues for forming and catalyzing the chromophore reaction (Fig. 4A).

We additionally condition on the structure of residues 58 through 71 from the experimental structure in 1QY3, which are known to be structurally important for the energetic favorability of chromophore formation (50).

Specifically, sequence tokens, structure tokens, and atomic coordinates of the backbone are provided at the input and generation begins from a nearly completely masked array of tokens corresponding to 229 residues, except for the token positions used for conditioning.

We generate designs using a chain-of-thought procedure as follows.

The model first generates structure tokens, effectively creating a protein backbone.

Backbones that have sufficiently good atomic coordination of the active site but differentiated overall structure from the 1QY3 backbone pass through a filter to the next step of the chain.

We add the generated structure to the original prompt to generate a sequence conditioned on the new prompt.

We then perform an iterative joint optimization, alternating between optimizing the sequence and the structure.

We reject chainsof-thought that lose atomic coordination of the active site (Appendix A.5.1).

We draw a computational pool of $10 \mathrm{~s}$ of thousands of candidate GFP designs from the intermediate and final points in the iterative joint optimization stage of the generation protocol.

We then bucket the designs by sequence similarity to known fluorescent proteins and filter and rank designs using a variety of metrics (details in Appendix A.5.1.5)

We performed a first experiment with 88 designs on a 96 well plate, with the top generations in each sequence similarity bucket.

Each generated protein was synthesized, expressed in E. coli, and measured for fluorescence activity at an excitation wavelength of $485 \mathrm{~nm}$ Fig. 4B left.

We measured brightness similar to positive controls from a number of designs that have higher sequence identity with naturally occurring GFPs.

We also identify a design in well B8 (highlighted in a black circle) with only $36 \%$ sequence identity to the 1QY3 sequence and $57 \%$ sequence identity to the nearest existing fluorescent protein, tagRFP.

This design was 50x less bright than natural GFPs and its chromophore matured over the course of a week, instead of in under a day, but it presents a signal of function in a new portion of sequence space that to our knowledge has not been found in nature or through protein engineering.

We continue the chain of thought starting from the sequence of the design in well B8 to generate a protein with improved brightness, using the same iterative joint optimization and ranking procedure as above.

We create a second 96 well plate of designs, and using the same plate reader assay we find that several designs in this cohort have a brightness in the range of GFPs found in nature.

The best design, located in well C10 of the second plate (Fig. 4B right), we designate esmGFP.

We find esmGFP exhibits brightness in the distribution of natural GFPs.

We evaluated the fluorescence intensity at 0 , 2 , and 7 days of chromophore maturation, and plot these measurements for esmGFP, a replicate of B8, a chromophore knockout of B8, along with three natural GFPs avGFP, cgreGFP, ppluGFP (Fig. 4C).

esmGFP takes longer to mature than the known GFPs that we measured, but achieves a comparable brightness after two days.

To validate that fluorescence was mediated by the intended Thr65 and Tyr66, we show that B8 and esmGFP variants where these residues were mutated to glycine lost fluorescence activity (Fig. S21).

Analysis of the excitation and emission spectra of esmGFP reveals that its peak excitation occurs at $496 \mathrm{~nm}$, which is shifted $7 \mathrm{~nm}$ relative to the $489 \mathrm{~nm}$ peak for EGFP, while both proteins emit at a peak of $512 \mathrm{~nm}$ (Fig. 4D).

The shapes of the spectra indicated a narrower full-widthhalf-maximum (FWHM) for the excitation spectrum of esmGFP (39mm for esmGFP vs $56 \mathrm{~nm}$ for EGFP), whereas the FWHM of their emission spectra were highly comparable ( $35 \mathrm{~nm}$ and $39 \mathrm{~nm}$, respectively).

Overall esmGFP exhibits spectral properties consistent with known GFPs.

We next sought to understand how the sequence and structure of esmGFP compares to known proteins.

A BLAST (51) search against the non-redundant protein sequences database and an MMseqs (52) search of ESM3's training set report the same top hit-tagRFP, which was also the nearest neighbor to B8-with $58 \%$ sequence identity, representing 96 mutations throughout the sequence.

tagRFP is a designed variant, and the closest wildtype sequence to esmGFP from the natural world is eqFP578, a red fluorescent protein, which differs from esmGFP by 107 sequence positions ( $53 \%$ identity).

Sequence differences between esmGFP and tagRFP occur throughout the structure (Fig. 4E) with 22 mutations occurring in the protein's interior, which is known to be intensely sensitive to mutations due to chromophore proximity and a high density of interactions (46).

Examination of a sequence alignment of 648 natural and designed GFP-like fluorescent proteins revealed that esmGFP
has the level of similarity to all other FPs that is typically found when comparing sequences across taxonomic orders, but within the same taxonomic class (Fig. 4F).

For example, the difference of esmGFP to other FPs is similar to level of difference between FPs belonging to the orders of scleractinia (stony corals) and actiniaria (sea anemones) both of which belong to the larger class anthozoa of marine invertebrates (Fig. 4G).

The closest FPs to esmGFP come from the anthozoa class (corals and anemones), average sequence identity $51.4 \%$, but esmGFP also shares some sequence identity with FPs from the hydrozoa (jellyfish) where the famous avGFP was discovered, average sequence identity $33.4 \%$ (Fig. S22).

We can draw insight from evolutionary biology on the amount of time it would take for a protein with similar sequence identity to arise through natural evolution.

In Fig. 4G we show esmGFP alongside three Anthozoan GFPs.

We use a recent time-calibrated phylogenetic analysis of the Anthozoans (53) that estimated the millions of years ago (MYA) to last common ancestors to estimate evolutionary time between each pair of these species.

Using a larger dataset of six Anthozoan GFPs and species for which we have accurate MYA to last common ancestors and GFP sequence identities, we construct a simple estimator that correlates sequence identity between FPs to MY of evolutionary time between the species (Fig. $4 \mathrm{H}$ ) to calibrate against natural evolution.

Based on this analysis we estimate esmGFP represents an equivalent of over 500 million years of evolution from the closest protein that has been found in nature.
