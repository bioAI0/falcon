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

 - ESM3 is an expert system that solves complex tasks.
- ESM3 is aligned to follow atomic coordination prompts.
- ESM3 is trained with a dataset of preference pairs.
- ESM3 is evaluated by prompting with coordinates in tertiary contact.
- ESM3 has a latent capability to solve complex tasks in the largest model.
- ESM3 generates a number of unique structures for ligands for which it has success.
User:

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

