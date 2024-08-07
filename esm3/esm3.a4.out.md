 - A.4. Alignment
- A.4.1. Algorithm
- IRPO (Iterative Reasoning Preference Optimization) is an algorithm used for alignment
- IRPO combines supervised finetuning with contrastive learning from preference pairs
- IRPO operates on a dataset consisting of prompt and a pair of completions (preferred and not preferred)
- IRPO operates on two separate models: the reference model and the current model
- The reference model is the fixed base model of the same scale, and the current model is the model being optimized
- The IRPO loss contains two terms: $\mathcal{L}_{\text {NLL }}$ and $\mathcal{L}_{\text {DPO }}$
- $\mathcal{L}_{\text {NLL }}$ maximizes the $\log$ likelihood of the preferred example normalized by the length of the sequence
- $\mathcal{L}_{\text {DPO }}$ is the contrastive preference tuning term, which increases the difference in log likelihoods between the preferred and not preferred examples while staying close to the reference model.

 - The reference model is used to prevent overfitting to the preference dataset.
- There are two hyperparameters, $\alpha$ and $\beta$.
- $\alpha$ weights the relative importance of the supervised with the preference loss.
- $\beta$ controls how close we stay to the reference model.
- The loss is minimized with respect to the current model parameters $\theta$.
- ESM3 is a multi-modal model.
- The prompt can be any combination of the input tracks of (partial) sequence, structure, and function.
- The generation can be any of the output tracks.
- In the experiments, the amino-acid sequence is always generated.
- Computing the full likelihood of generating a sequence from a prompt is intractable.
- A surrogate is used to approximate the likelihood.
- The surrogate involves masking the generated sequence with a mask sampled from a linear noise schedule.
- The same mask is used to compute the likelihoods for the reference policy vs current policy, as well as for the preferred sample vs non preferred sample.
- ESM3 can be used for multimodal protein editing.
- ESM3 can expose a buried helix in a protein while maintaining the alternating alpha-beta sandwich fold of the protein.
User:

 - ESM3 is used in a two-step iterative edit.
- Secondary structure prompting and function prompting are used to idealize a reference TIM barrel.
- Secondary structure prompting is then used to increase the number of subunits in the TIM barrel from 8 to 11.
- The DPO term of the loss function can be rearranged to give insight into how it finetunes the model for the preference pairs.
- The softplus function is used in the loss function to approximate the hinge function.
- The loss function is in the linear regime when the log likelihood ratio is much greater than zero.
- The loss function is in the nonlinear regime when the log likelihood ratio is much less than zero.
User:

 - The loss function in Equation 6 is used to ensure that the model does not deviate too far from the reference model.
- The loss function in Equation 6 is used in ESM3 finetuning to increase the surrogate of the preferred pair over the non-preferred pair until the current model deviates too much from the reference model.
- The desired objectives for a generation in preference tuning are quality and correctness.
- Quality in preference tuning refers to the viability of the sequence to be a stable protein.
- Correctness in preference tuning refers to the extent to which the sequence follows the given prompt.
- Prompt consistency in preference tuning can be measured via constrained site RMSD (cRMSD).
- Sequence quality in preference tuning can be measured via predicted-TM (pTM) of a structure predictor on the generated sequence.
- Over-optimizing can occur when a model keeps improving a specific metric, but the actual property of interest stops correlating with the metric.
- Using orthogonal models to rank the training dataset vs. performing evaluation helps mitigate over-optimizing.
- Generations in preference tuning are evaluated according to cRMSD and pTM of ESM3 7B to maintain a consistent structure predictor across all datasets.
- After the preference tuning phase, the generations from the tuned models are evaluated with ESMFold.
User:

 - ESM3 models are trained with the IRPO loss on preconstructed training datasets.
- Each dataset has 16 generations for 30,000 prompts from the respective ESM3 model.
- Preference selection is determined via a threshold of metrics.
- A sample is considered "good" if it has ESM3 7B pTM $>0.8$ and backbone cRMSD to its structure prompt $<1.5 \AA$.
- Each "good" sample is paired with a "bad" sample to create a preference pair.
- To qualify as a "bad" sample, the generation must have a delta $\mathrm{pTM}=\mathrm{pTM}_{\text {good }}-\mathrm{pTM}_{\text {bad }}>=0.2$ and delta backbone $c R M S D=c R M S D_{\text {good }}-c^{2} M S D_{\text {bad }}<-2 \AA$.
- Structure prompts are composed of a variety of proteins adapted from the pre-training pipeline.
- $50 \%$ of the prompts are synthetic active sites, while the other $50 \%$ are structure coordinates randomly masked with a noise schedule.
- All of the structure prompts are derived from PDB structures with a temporal cutoff of before May 1st, 2020.
- The synthetic active sites are derived by finding sequences from PDB with coordinating residues.
- The remaining structure track prompts are masked according to a cosine noise schedule.
- $50 \%$ of the noise scheduled prompts are masked in completely random positions, and the other $50 \%$ are masked according to an autocorrelation mechanism that prefers sequentially masked positions.

 - Each model's training dataset consists of generations of its own reference model.
- For each prompt, we generate samples from the corresponding ESM3 model scale using iterative decoding with $L / 4$ steps, where $L$ is the length of the prompt.
- We anneal the temperature from 1.0 to 0.5 over the decoding steps.
- The evaluation dataset for atomic coordination tasks consists of 46 proteins with ligand binding sites from the Biolip dataset.
- The coordinating residues shown to the model are given by the ligand binding sites defined in the Biolip dataset.
- ESM3 is prompted with the sequence and coordinates of the residues for a particular ligand binding site.
- The total sequence length is sampled evenly to be 150, 250, or 350 residues.
- A contiguous span of coordinating residues is defined as prompt residues with fewer than 5 sequence positions between them.
- The order and distance between contiguous spans of residues is shuffled.
- A generation is considered a success if backbone cRMSD $<1.5 \AA$ and $\mathrm{pTM}>0.8$.
- A total of 1024 prompts are constructed for each ligand.
- Pass@ 128 is reported, which is an estimate for the fraction of ligands with at least one successful completion after 128 prompts per ligand.
User:

 - The success rate over 1024 prompts is used to estimate the performance of the model.
- The base model and finetuned model are visualized using randomly selected successful generations.
- Supervised finetuning is used to increase the likelihood of high quality samples without preference tuning loss.
- The 1.4B, 7B, and 98B models solve a certain percentage of atomic coordination tasks at 128 generations.
- Each IRPO model is trained for 1000 steps using RMSProp with different learning rates and gradient norms.
- The SFT baseline uses the same hyperparameters as the IRPO model, but with a different value for alpha.

