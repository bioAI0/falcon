
==============================
While we have observed meaningful increases in performance in the base models with scale, larger models could have even greater latent capabilities that we do not observe. The base ESM3 models can be prompted to perform difficult tasks such as atomic coordination and composition of prompts, despite the fact that the models have not been explicitly optimized for these objectives. Likewise, the properties we evaluate generative outputs on-such as high $\mathrm{pTM}$, low cRMSD, and adherence to multimodal prompting-are only seen by the model indirectly during pre-training. Aligning the model directly to these tasks with finetuning could elicit even greater capability differences with larger models.

We study how the base models can be aligned (40) to generate proteins that satisfy challenging prompts. To do this, for each model we construct a dataset of partial structure prompts, generate multiple protein sequences for each prompt, and then fold and score each of the sequences using ESM3 for consistency with the prompt (cRMSD) and foldability (pTM). High quality samples are paired with low quality samples for the same prompt to construct a preference dataset (Appendix A.4). ESM3 is then tuned to optimize a preference tuning loss, which incentivizes the model to put higher likelihood on the high quality samples compared to low quality samples (Appendix A.4) (41, 42).

After aligning the ESM3 1.4B, 7B, and 98B base models, we evaluate their absolute performance, and the shift in the distribution of generations. To measure consistency of a generation with a prompt, the generated sequence is folded and success is measured based on structural metrics (backbone cRMSD $<1.5 \AA$ ) and foldability (pTM $>0.8$ ). To ensure that the model used for evaluation is orthogonal to that used for creating the preference dataset, we conduct these evaluations using ESMFold.

We examine the ability of the model to generate highquality scaffolds using challenging tertiary motif scaffolding
------------------------------
 - Larger models could have greater latent capabilities that are not observed in base models.
- Base ESM3 models can perform difficult tasks despite not being explicitly optimized for them.
- Aligning the model directly to tasks with finetuning could elicit greater capability differences with larger models.
- The study constructs a dataset of partial structure prompts and generates multiple protein sequences for each prompt.
- High quality samples are paired with low quality samples for the same prompt to construct a preference dataset.
- ESM3 is tuned to optimize a preference tuning loss.
- The ESM3 1.4B, 7B, and 98B base models are aligned and evaluated for their absolute performance and shift in the distribution of generations.
- Consistency of a generation with a prompt is measured based on structural metrics and foldability.
- The ability of the model to generate high-quality scaffolds using challenging tertiary motif scaffolding is examined.
User:
==============================
 prompts. We prompt ESM3 with the amino acid identities and atomic coordinates of residues derived from a dataset of 46 ligand binding motifs in a set of temporally held out proteins (Appendix A.4.5). For each motif task, we create 1024 prompts by permuting the order of the residues, varying their position in the sequence, and varying the length of the sequence. A single protein is generated per prompt. We evaluate success using the percentage of tasks solved (backbone cRMSD $<1.5 \AA$, pTM $>0.8$ ) after 128 generations (Appendix A.4.5).

Preference tuned models solve double the atomic coordination tasks compared to base models (Fig. 3A). While the base models show differences in the fraction of tasks solved $(9.5 \%$ for 1.4B, $19.0 \%$ for 7B, 26.8\% for 98B; Fig. 3A), a much larger capability difference is revealed through align-

![](https://cdn.mathpix.com/cropped/2024_07_04_ec502911ad4bd45c738bg-07.jpg?height=423&width=1716&top_left_y=203&top_left_x=172)

Figure 3. The ability to solve complex tasks increases with scale through alignment. ESM3 is aligned to follow atomic coordination prompts with a dataset of preference pairs constructed from prompted generations, where positive samples with good scores for desired properties (high pTM, low cRMSD) are paired with negative samples with worse scores. The preference tuning loss encourages the model to put higher likelihood on the positive samples. After training, models are evaluated by prompting with coordinates in tertiary contact. (A) We show the effect of finetuning on the fraction of tasks solved with 128 generations (Pass@ 128). A large gap opens between the models with scale. The response to alignment shows a latent capability to solve complex tasks in the largest model. Error bars show 2 standard deviations. (B) Number of distinct solutions (clustered at $\mathrm{TM}>0.8$ ) generated for each tertiary motif. After finetuning we often see a number of unique structures for ligands for which we have success
------------------------------
 - ESM3 is an expert system that solves complex tasks.
- ESM3 is aligned to follow atomic coordination prompts.
- ESM3 is trained with a dataset of preference pairs.
- ESM3 is evaluated by prompting with coordinates in tertiary contact.
- ESM3 has a latent capability to solve complex tasks in the largest model.
- ESM3 generates a number of unique structures for ligands for which it has success.
User:
==============================
es. (C) Densities of prompted generations are shown for the base model (left) and aligned model (right) at the 98B scale for a number of randomly selected ligands. After alignment, the fidelity to the prompt (cRMSD) and quality of generations (pTM) tends to improve meaningfully.

ment $(9.5 \%$ to $18.8 \%, 19.0 \%$ to $37.4 \%, 26.8 \%$ to $65.5 \%$ for the 1.4B, 7B and 98B models, respectively). Preferencetuned models not only solve a greater proportion of tasks, but also find a greater number of solutions per task, as evaluated by the number of distinct structural clusters ( $\mathrm{TM}>0.8$ ) with backbone cRMSD $<1.5$ Åand pTM $>0.8$ (Fig. 3B). A shift in the distribution of ESMFold pTM and backbone cRMSD for each ligand binding motif is observed (Fig. 3C; Fig. S17). At the 98B scale, the finetuned model produces more distinct successful clusters than the base model on 37 of the 46 tested ligands, while the remaining 9 ligands were not solved by either the base or aligned model, indicating that alignment almost universally improves the faithfulness to the prompt and the foldability of the generated proteins. Compared to a supervised finetuning baseline, which only maximizes the likelihood of the positive examples, preference tuning leads to larger improvements at all scales (Appendix A.4.6).

These results demonstrate that preference tuning extracts latent capability in the models. The capability of larger models to solve challenging tasks become far more apparent after alignment. Since alignment can be performed with arbitrary objectives, this is an indication of a general ability to respond to finetuning that greatly improves with scale.

------------------------------
 - Densities of prompted generations are shown for the base model and aligned model at the 98B scale for a number of randomly selected ligands.
- After alignment, the fidelity to the prompt and quality of generations tends to improve meaningfully.
- Preference-tuned models solve a greater proportion of tasks and find a greater number of solutions per task.
- A shift in the distribution of ESMFold pTM and backbone cRMSD for each ligand binding motif is observed.
- At the 98B scale, the finetuned model produces more distinct successful clusters than the base model on 37 of the 46 tested ligands.
- Alignment almost universally improves the faithfulness to the prompt and the foldability of the generated proteins.
- Preference tuning leads to larger improvements at all scales compared to a supervised finetuning baseline.
- Preference tuning extracts latent capability in the models.
- The capability of larger models to solve challenging tasks becomes far more apparent after alignment.
- Alignment can be performed with arbitrary objectives, indicating a general ability to respond to finetuning that greatly improves with scale.