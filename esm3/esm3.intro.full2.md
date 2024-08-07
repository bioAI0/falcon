
==============================
The proteins that exist today have developed into their present forms over the course of billions of years of natural evolution, passing through a vast evolutionary sieve. In parallel experiments conducted over geological time, nature creates random mutations and applies selection, filtering proteins by their myriad sequences, structures, and functions.
------------------------------
 [[evolutionary sieve]]
[[natural evolution]]
[[random mutations]]
[[selection]]
[[proteins]]
[[sequences]]
[[structures]]
[[functions]]
==============================
As a result, the patterns in the proteins we observe reflect the action of the deep hidden variables of the biology that have shaped their evolution across time. Gene sequencing surveys
\footnotetext{
${ }^{*}$ Equal contribution ${ }^{1}$ EvolutionaryScale, PBC ${ }^{2}$ Arc Institute ${ }^{3}$ University of California, Berkeley ${ }^{4}$ Work done during internship at EvolutionaryScale, PBC ${ }^{\dagger}$ Correspondence to $<$ arives@evolutionaryscale.ai>.
------------------------------
 [[Gene sequencing surveys]]
[[Equal contribution]]
[[EvolutionaryScale, PBC]]
[[Arc Institute]]
[[University of California, Berkeley]]
[[Work done during internship at EvolutionaryScale, PBC]]
[[Correspondence to <arives@evolutionaryscale.ai>]]
User:
==============================
Preview 2024-06-25. Pending submission to bioRxiv. Copyright 2024 by the authors.
}
------------------------------
 I'm sorry, as an AI language model, I do not have access to the specific text or context you are referring to. Please provide me with the necessary information so I can assist you better.
==============================
of Earth's natural diversity are cataloging the sequences $(1-3)$ and structures $(4,5)$ of proteins, containing billions of sequences and hundreds of millions of structures that illuminate patterns of variation across life. A consensus is building that underlying these sequences is a fundamental language of protein biology that can be understood using large language models (6-10).
------------------------------
 [[Earth's natural diversity]]
[[proteins]]
[[sequences]]
[[structures]]
[[large language models]]
==============================
A number of language models of protein sequences have now been developed and evaluated ( $9,11-14$ ). It has been found that the representations that emerge within language models reflect the biological structure and function of proteins $(6,15,16)$, and are learned without any supervision on those properties, improving with scale $(5,17,18)$. In artificial intelligence, scaling laws have been found that predict the growth in capabilities with increasing scale, describing a frontier in compute, parameters and data (19-21).
------------------------------
 [[language models]] [[protein sequences]] [[biological structure]] [[biological function]] [[scaling laws]] [[artificial intelligence]] [[compute]] [[parameters]] [[data]]
==============================
We present ESM3, a frontier multimodal generative model, that reasons over the sequences, structures, and functions of proteins. ESM3 is trained as a generative masked language model over discrete tokens for each modality. Structural reasoning is achieved by encoding three-dimensional atomic structure as discrete tokens rather than with the complex architecture and diffusion in three-dimensional space employed in recent predictive (22) and generative models $(14,23-25)$ of proteins. All-to-all modeling of discrete tokens is scalable, and allows ESM3 to be prompted with any combination of its modalities, enabling controllable generation of new proteins that respect combinations of prompts.
------------------------------
 We present ESM3, a frontier multimodal generative model, that reasons over the sequences, structures, and functions of proteins. ESM3 is trained as a generative masked language model over discrete tokens for each modality. Structural reasoning is achieved by encoding three-dimensional atomic structure as discrete tokens rather than with the complex architecture and diffusion in three-dimensional space employed in recent predictive (22) and generative models $(14,23-25)$ of proteins. All-to-all modeling of discrete tokens is scalable, and allows ESM3 to be prompted with any combination of its modalities, enabling controllable generation of new proteins that respect combinations of prompts.###
==============================
ESM3 at its largest scale was trained with $1.07 \times 10^{24}$ FLOPs on 2.78 billion proteins and 771 billion unique tokens, and has 98 billion parameters. Scaling ESM3 to this 98 billion parameter size results in improvements in the representation of sequence, structure, and function, as well as on generative evaluations. We find that ESM3 is highly responsive to prompts, and finds creative solutions to complex combinations of prompts, including solutions for which we can find no matching structure in nature. We find that models at all scales can be aligned to better follow prompts. Larger models are far more responsive to alignment, and
show greater capability to solve the hardest prompts after alignment.
------------------------------
 [[ESM3]] [[FLOPs]] [[tokens]] [[parameters]] [[alignment]]
==============================
We report the generation of a new green fluorescent protein (GFP) with ESM3. Fluorescent proteins are responsible for the glowing colors of jellyfish and corals (26) and are important tools in modern biotechnology (27). They share an elegant structure: an eleven stranded beta barrel with a helix that threads its center, which scaffolds the formation of a light-emitting chromophore out of the protein's own atoms. This mechanism is unique in nature-no other protein spontaneously forms a fluorescent chromophore out of its own structure-suggesting that producing fluorescence is hard even for nature.
------------------------------
 We report the generation of a new green fluorescent protein (GFP) with ESM3. Fluorescent proteins are responsible for the glowing colors of jellyfish and corals (26) and are important tools in modern biotechnology (27). They share an elegant structure: an eleven stranded beta barrel with a helix that threads its center, which scaffolds the formation of a light-emitting chromophore out of the protein's own atoms. This mechanism is unique in nature-no other protein spontaneously forms a fluorescent chromophore out of its own structure-suggesting that producing fluorescence is hard even for nature.###
==============================
Our new protein, which we have named esmGFP, has $36 \%$ sequence identity to Aequorea victoria GFP, and $58 \%$ sequence identity to the most similar known fluorescent protein. Despite GFP's intense focus as a target for protein engineering over several decades, as far as we are aware, proteins this distant have only been found through the discovery of new GFPs in nature.
------------------------------
 [[Aequorea victoria GFP]]
[[GFP]]
[[protein engineering]]
[[new GFPs in nature]]
==============================
Similar amounts of diversification among natural GFPs have occurred over predictable timescales. Understood in these terms, the generation of a new fluorescent protein at this distance from existing proteins appears to be equivalent to simulating over 500 million years of evolution.

------------------------------
 [[GFP]]s, [[natural]] [[diversification]], [[evolution]]