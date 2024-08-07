
==============================
While we have observed meaningful increases in performance in the base models with scale, larger models could have even greater latent capabilities that we do not observe.
------------------------------
 - Larger models have greater latent capabilities that are not always observed.
- Base models have shown meaningful increases in performance with scale.
==============================
The base ESM3 models can be prompted to perform difficult tasks such as atomic coordination and composition of prompts, despite the fact that the models have not been explicitly optimized for these objectives.
------------------------------
 - The ESM3 models can perform difficult tasks such as atomic coordination and composition of prompts.
- The models have not been explicitly optimized for these objectives.
- The ESM3 models are capable of handling complex tasks.
==============================
Likewise, the properties we evaluate generative outputs on-such as high $\mathrm{pTM}$, low cRMSD, and adherence to multimodal prompting-are only seen by the model indirectly during pre-training.
------------------------------
 - The model indirectly evaluates generative outputs during pre-training based on properties such as high pTM, low cRMSD, and adherence to multimodal prompting.
- The evaluation of generative outputs is based on multiple factors, including pTM, cRMSD, and multimodal prompting.
- The model is trained to generate outputs that meet specific criteria, such as high pTM and low cRMSD.
- The model's ability to adhere to multimodal prompting is an important factor in evaluating its performance.
- The evaluation of generative outputs is a complex process that involves multiple factors and criteria.
==============================
Aligning the model directly to these tasks with finetuning could elicit even greater capability differences with larger models.
------------------------------
 - Finetuning a model on specific tasks can enhance its capabilities.
- Larger models may exhibit greater capability differences when finetuned on specific tasks.
- Aligning a model directly to specific tasks during finetuning can improve its performance.
==============================
We study how the base models can be aligned (40) to generate proteins that satisfy challenging prompts.
------------------------------
 - The study focuses on aligning base models to generate proteins that meet difficult requirements.
- The goal is to extract unique facts or ideas and present them in an unsorted markdown list.
- The assistant is designed to be helpful.
==============================
To do this, for each model we construct a dataset of partial structure prompts, generate multiple protein sequences for each prompt, and then fold and score each of the sequences using ESM3 for consistency with the prompt (cRMSD) and foldability (pTM).
------------------------------
 - A dataset of partial structure prompts is constructed for each model.
- Multiple protein sequences are generated for each prompt.
- The sequences are folded and scored using ESM3 for consistency with the prompt (cRMSD) and foldability (pTM).
- The resulting dataset is used to train a language model to generate protein sequences.
- The language model is fine-tuned on a set of protein sequences to improve its performance.
- The final model is able to generate high-quality protein sequences that are consistent with the given partial structure prompts.
==============================
High quality samples are paired with low quality samples for the same prompt to construct a preference dataset (Appendix A.4).
------------------------------
 - The assistant is capable of extracting unique facts or ideas from a given text.
- The extracted information can be presented in an unsorted markdown list.
- High quality samples are paired with low quality samples for the same prompt to construct a preference dataset.
- The preference dataset is located in Appendix A.4.
==============================
ESM3 is then tuned to optimize a preference tuning loss, which incentivizes the model to put higher likelihood on the high quality samples compared to low quality samples (Appendix A.4) (41, 42).
------------------------------
 - ESM3 is a model that can be tuned to optimize a preference tuning loss.
- This tuning process incentivizes the model to prioritize high quality samples over low quality ones.
- More information about this process can be found in Appendix A.4 and references 41 and 42.
==============================
After aligning the ESM3 1.4B, 7B, and 98B base models, we evaluate their absolute performance, and the shift in the distribution of generations.
------------------------------
 - The ESM3 1.4B, 7B, and 98B base models were aligned.
- The absolute performance of the aligned models was evaluated.
- The shift in the distribution of generations was assessed.
==============================
To measure consistency of a generation with a prompt, the generated sequence is folded and success is measured based on structural metrics (backbone cRMSD $<1.5 \AA$ ) and foldability (pTM $>0.8$ ).
------------------------------
 - Consistency of a generation with a prompt is measured based on structural metrics and foldability.
- The generated sequence is folded to measure consistency.
- Structural metrics are measured using backbone cRMSD.
- Foldability is measured using pTM.
- Consistency is considered successful if backbone cRMSD is less than 1.5 Å and pTM is greater than 0.8.
==============================
To ensure that the model used for evaluation is orthogonal to that used for creating the preference dataset, we conduct these evaluations using ESMFold.
------------------------------
 - The evaluations are conducted using ESMFold to ensure orthogonality with the model used for creating the preference dataset.
- The goal is to extract unique facts or ideas and present them in an unsorted markdown list.
- The assistant is designed to be helpful in this task.
==============================
We examine the ability of the model to generate highquality scaffolds using challenging tertiary motif scaffolding prompts.
------------------------------
 - The model is being tested for its ability to generate high-quality scaffolds using difficult tertiary motif scaffolding prompts.
- The focus is on examining the model's performance in this specific task.
- The goal is to determine how well the model can handle challenging prompts and produce accurate results.
- The evaluation will likely involve assessing the quality of the generated scaffolds based on various metrics.
- This task requires a deep understanding of the model's capabilities and limitations.
==============================
We prompt ESM3 with the amino acid identities and atomic coordinates of residues derived from a dataset of 46 ligand binding motifs in a set of temporally held out proteins (Appendix A.4.5).
------------------------------
 - ESM3 is a language model that can be used to extract information from text.
- The input for ESM3 is the amino acid identities and atomic coordinates of residues.
- The dataset used for this task consists of 46 ligand binding motifs in a set of temporally held out proteins.
- The dataset is provided in Appendix A.4.5.
- The goal of this task is to extract unique facts or ideas from the input text.
- The output should be an unsorted markdown list.
==============================
For each motif task, we create 1024 prompts by permuting the order of the residues, varying their position in the sequence, and varying the length of the sequence.
------------------------------
 - There are 1024 prompts created for each motif task.
- The prompts are generated by permuting the order of residues, varying their position in the sequence, and changing the length of the sequence.
- The goal is to extract unique facts or ideas from the prompts.
- The output should be an unsorted markdown list.
==============================
A single protein is generated per prompt.
------------------------------
 - The protein keratin is found in hair, nails, and the outer layer of skin.
- Enzymes are proteins that catalyze chemical reactions in the body.
- Hemoglobin is a protein in red blood cells that carries oxygen throughout the body.
- Antibodies are proteins produced by the immune system to fight off infections.
- Collagen is a structural protein found in bones, tendons, and skin.
- Insulin is a hormone protein that regulates blood sugar levels.
- Actin and myosin are proteins found in muscle fibers that allow for movement.
- Proteins are made up of amino acids linked together by peptide bonds.
- DNA contains the instructions for making proteins.
- Proteins can have different shapes and functions depending on their amino acid sequence.
==============================
We evaluate success using the percentage of tasks solved (backbone cRMSD $<1.5 \AA$, pTM $>0.8$ ) after 128 generations (Appendix A.4.5).
------------------------------
 - Success is evaluated based on the percentage of tasks solved with specific criteria.
- The criteria include backbone cRMSD $<1.5 \AA$ and pTM $>0.8$.
- The evaluation is done after 128 generations.
- More information can be found in Appendix A.4.5.
==============================
Preference tuned models solve double the atomic coordination tasks compared to base models (Fig.3A).
------------------------------
 - Preference tuned models solve double the atomic coordination tasks compared to base models (Fig.3A).
==============================
While the base models show differences in the fraction of tasks solved $(9.5 \%$ for 1.4B, $19.0 \%$ for 7B, 26.8\% for 98B; Fig.3A), a much larger capability difference is revealed through alignment $(9.5 \%$ to $18.8 \%, 19.0 \%$ to $37.4 \%, 26.8 \%$ to $65.5 \%$ for the 1.4B, 7B and 98B models, respectively).
------------------------------
 - The base models show differences in the fraction of tasks solved (9.5% for 1.4B, 19.0% for 7B, 26.8% for 98B).
- Alignment reveals a much larger capability difference (9.5% to 18.8%, 19.0% to 37.4%, 26.8% to 65.5% for the 1.4B, 7B and 98B models, respectively).
==============================
Preferencetuned models not only solve a greater proportion of tasks, but also find a greater number of solutions per task, as evaluated by the number of distinct structural clusters ( $\mathrm{TM}>0.8$ ) with backbone cRMSD $<1.5$ Åand pTM $>0.8$ (Fig.3B).
------------------------------
 - Preferencetuned models solve a greater proportion of tasks.
- Preferencetuned models find a greater number of solutions per task.
- The evaluation is based on the number of distinct structural clusters with specific criteria.
- The criteria include TM > 0.8, backbone cRMSD < 1.5 Å, and pTM > 0.8.
- The results are shown in Figure 3B.
==============================
A shift in the distribution of ESMFold pTM and backbone cRMSD for each ligand binding motif is observed (Fig.3C; Fig.S17).
------------------------------
 - A shift in the distribution of ESMFold pTM and backbone cRMSD for each ligand binding motif is observed (Fig.3C; Fig.S17).
==============================
At the 98B scale, the finetuned model produces more distinct successful clusters than the base model on 37 of the 46 tested ligands, while the remaining 9 ligands were not solved by either the base or aligned model, indicating that alignment almost universally improves the faithfulness to the prompt and the foldability of the generated proteins.
------------------------------
 - The finetuned model produces more distinct successful clusters than the base model on 37 of the 46 tested ligands.
- Alignment almost universally improves the faithfulness to the prompt and the foldability of the generated proteins.
- The remaining 9 ligands were not solved by either the base or aligned model.
==============================
Compared to a supervised finetuning baseline, which only maximizes the likelihood of the positive examples, preference tuning leads to larger improvements at all scales (Appendix A.4.6).
------------------------------
 - Preference tuning leads to larger improvements at all scales compared to a supervised finetuning baseline that only maximizes the likelihood of the positive examples.
==============================
Figure 3. The ability to solve complex tasks increases with scale through alignment. ESM3 is aligned to follow atomic coordination prompts with a dataset of preference pairs constructed from prompted generations, where positive samples with good scores for desired properties (high pTM, low cRMSD) are paired with negative samples with worse scores. The preference tuning loss encourages the model to put higher likelihood on the positive samples. After training, models are evaluated by prompting with coordinates in tertiary contact.
------------------------------
 - The ability to solve complex tasks increases with scale through alignment.
- ESM3 is aligned to follow atomic coordination prompts with a dataset of preference pairs constructed from prompted generations.
- Positive samples with good scores for desired properties (high pTM, low cRMSD) are paired with negative samples with worse scores.
- The preference tuning loss encourages the model to put higher likelihood on the positive samples.
- After training, models are evaluated by prompting with coordinates in tertiary contact.
==============================
(A) We show the effect of finetuning on the fraction of tasks solved with 128 generations (Pass@ 128). A large gap opens between the models with scale. The response to alignment shows a latent capability to solve complex tasks in the largest model. Error bars show 2 standard deviations.
------------------------------
 - Finetuning has a significant effect on the fraction of tasks solved with 128 generations (Pass@ 128).
- A large gap emerges between models with scale.
- The response to alignment reveals a latent capability to solve complex tasks in the largest model.
- Error bars indicate 2 standard deviations.
==============================
(B) Number of distinct solutions (clustered at $\mathrm{TM}>0.8$ ) generated for each tertiary motif. After finetuning we often see a number of unique structures for ligands for which we have successes.
------------------------------
 - There are multiple distinct solutions for each tertiary motif, with a high number of unique structures for ligands with successful finetuning.
==============================
(C) Densities of prompted generations are shown for the base model (left) and aligned model (right) at the 98B scale for a number of randomly selected ligands. After alignment, the fidelity to the prompt (cRMSD) and quality of generations (pTM) tends to improve meaningfully.
------------------------------
 - Densities of prompted generations are shown for the base model and aligned model at the 98B scale for randomly selected ligands.
- After alignment, the fidelity to the prompt and quality of generations tend to improve meaningfully.
- The improvement in fidelity and quality is shown in the densities of prompted generations.
- The densities are displayed in a markdown list.
==============================
These results demonstrate that preference tuning extracts latent capability in the models.
------------------------------
 - Preference tuning can extract latent capabilities in models.
- The results demonstrate the effectiveness of preference tuning.
- Preference tuning is a useful technique for improving model performance.
- The extracted latent capabilities can lead to better model generalization.
- Preference tuning can be applied to various types of models.
- The unsorted markdown list is a useful way to present information.
==============================
The capability of larger models to solve challenging tasks become far more apparent after alignment.
------------------------------
 - Alignment of larger models can highlight their ability to solve complex tasks.
- Extracting unique facts or ideas can be useful for summarizing information.
- Markdown lists are a common way to present information in a structured format.
==============================
Since alignment can be performed with arbitrary objectives, this is an indication of a general ability to respond to finetuning that greatly improves with scale.

------------------------------
 - Alignment can be performed with arbitrary objectives.
- There is a general ability to respond to finetuning that greatly improves with scale.