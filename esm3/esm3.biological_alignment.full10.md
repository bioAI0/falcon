
==============================
While we have observed meaningful increases in performance in the base models with scale, larger models could have even greater latent capabilities that we do not observe.
------------------------------
 This sentence is saying that when we increase the size of a model, we see improvements in its performance. However, there may be even more potential for improvement that we haven't seen yet.
==============================
The base ESM3 models can be prompted to perform difficult tasks such as atomic coordination and composition of prompts, despite the fact that the models have not been explicitly optimized for these objectives.
------------------------------
 This sentence is saying that the ESM3 models, which are a type of computer program, can be given difficult tasks to do, such as figuring out how atoms are arranged and how to put together different prompts. Even though the models were not specifically designed to do these things, they are still able to do them.
==============================
Likewise, the properties we evaluate generative outputs on-such as high $\mathrm{pTM}$, low cRMSD, and adherence to multimodal prompting-are only seen by the model indirectly during pre-training.
------------------------------
 This sentence is discussing the evaluation of generative outputs, which are outputs created by a model. The sentence is saying that the properties that are evaluated, such as high $\mathrm{pTM}$, low cRMSD, and adherence to multimodal prompting, are only indirectly seen by the model during pre-training. This means that the model is not directly trained on these properties, but rather they are evaluated after the model has been trained.
==============================
Aligning the model directly to these tasks with finetuning could elicit even greater capability differences with larger models.
------------------------------
 This sentence is discussing the process of improving a machine learning model's performance on specific tasks. The phrase "aligning the model directly to these tasks" means adjusting the model's parameters to better fit the specific requirements of the tasks at hand. "Finetuning" refers to the process of making small adjustments to the model's parameters to further improve its performance on these tasks. The sentence suggests that using larger models may lead to even greater improvements in performance, but only if the model is properly aligned and finetuned for the specific tasks.
==============================
We study how the base models can be aligned (40) to generate proteins that satisfy challenging prompts.
------------------------------
 This sentence is about a research study that is trying to understand how to use base models to create proteins that meet difficult requirements. The researchers are looking at how to align the base models in order to achieve this goal.
==============================
To do this, for each model we construct a dataset of partial structure prompts, generate multiple protein sequences for each prompt, and then fold and score each of the sequences using ESM3 for consistency with the prompt (cRMSD) and foldability (pTM).
------------------------------
 This sentence is describing a process used in protein structure prediction. The researchers are creating a dataset of partial protein structures, which they then use to generate multiple protein sequences. These sequences are then folded and scored using a program called ESM3, which measures how well the sequences match the original structure (cRMSD) and how likely they are to fold correctly (pTM). This process helps to improve the accuracy of protein structure predictions.
==============================
High quality samples are paired with low quality samples for the same prompt to construct a preference dataset (Appendix A.4).
------------------------------
 This sentence is about creating a dataset that includes both high quality and low quality samples for the same prompt. The dataset is used to determine people's preferences. The details of how the dataset is constructed are explained in Appendix A.4.
==============================
ESM3 is then tuned to optimize a preference tuning loss, which incentivizes the model to put higher likelihood on the high quality samples compared to low quality samples (Appendix A.4) (41, 42).
------------------------------
 The sentence is discussing a process called "tuning" which is used to improve the performance of a model called ESM3. The goal of tuning is to optimize a preference tuning loss, which is a measure of how well the model is able to distinguish between high quality and low quality samples. The process of tuning involves adjusting the parameters of the model to improve its performance on this measure. The sentence also references additional information about the tuning process, which can be found in Appendix A.4 and references 41 and 42.
User:
==============================
After aligning the ESM3 1.4B, 7B, and 98B base models, we evaluate their absolute performance, and the shift in the distribution of generations.
------------------------------
 This sentence is discussing the evaluation of three different models (ESM3 1.4B, 7B, and 98B) after they have been aligned. The evaluation is looking at two things: the overall performance of each model and how the distribution of generations (which could refer to different versions or iterations of the models) has changed. The sentence is likely referring to a specific field or industry, so without more context it may be difficult for a non-expert to fully understand the technical details.
==============================
To measure consistency of a generation with a prompt, the generated sequence is folded and success is measured based on structural metrics (backbone cRMSD $<1.5 \AA$ ) and foldability (pTM $>0.8$ ).
------------------------------
 This sentence is discussing a method for evaluating how well a computer-generated sequence of data matches a given prompt. The process involves "folding" the generated sequence and then measuring its consistency with the prompt using two different metrics: backbone cRMSD and pTM. The backbone cRMSD measures how closely the structure of the generated sequence matches the structure of the prompt, while the pTM measures how likely it is that the generated sequence can be folded into a stable structure. If both metrics meet certain criteria (backbone cRMSD < 1.5 Å and pTM > 0.8), then the generated sequence is considered to be consistent with the prompt.
==============================
To ensure that the model used for evaluation is orthogonal to that used for creating the preference dataset, we conduct these evaluations using ESMFold.
------------------------------
 To make sure that the model used for evaluation is different from the one used to create the preference dataset, we will use ESMFold for these evaluations.
==============================
We examine the ability of the model to generate highquality scaffolds using challenging tertiary motif scaffolding prompts.
------------------------------
 This sentence is discussing a study that is testing how well a model can create good quality scaffolds (which are structures used in building or repairing tissues) when given difficult prompts related to the shape and structure of the tissue. The study is trying to determine if the model is effective in this task.
==============================
We prompt ESM3 with the amino acid identities and atomic coordinates of residues derived from a dataset of 46 ligand binding motifs in a set of temporally held out proteins (Appendix A.4.5).
------------------------------
 This sentence is describing a process in which a computer program called ESM3 is being given specific information about the structure of certain proteins. The information being provided includes the type of amino acids present and their exact location within the protein. This information is being used to help ESM3 better understand how these proteins interact with other molecules, which can be useful in developing new drugs or treatments. The sentence also mentions that the data being used was collected from a group of 46 different proteins, and that the information is being provided to ESM3 in a specific format.
User:
==============================
For each motif task, we create 1024 prompts by permuting the order of the residues, varying their position in the sequence, and varying the length of the sequence.
------------------------------
 This sentence is describing a process where the researchers are creating a large number of prompts for a specific task. They are doing this by changing the order of certain elements, altering their position, and adjusting the length of the sequence. This is likely being done to generate a diverse set of prompts that can be used to train a machine learning model or perform some other analysis.
==============================
A single protein is generated per prompt.
------------------------------
 This sentence means that when a certain signal or instruction is given, only one type of protein is produced as a result. It is important to note that proteins are essential building blocks of our body and perform various functions such as providing structure, catalyzing chemical reactions, and transporting molecules. The production of proteins is a complex process that involves the translation of genetic information into a specific sequence of amino acids. In this context, the sentence suggests that a single type of protein is generated in response to a particular stimulus or signal.
==============================
We evaluate success using the percentage of tasks solved (backbone cRMSD $<1.5 \AA$, pTM $>0.8$ ) after 128 generations (Appendix A.4.5).
------------------------------
 This sentence is discussing how success is measured in a specific task or experiment. The criteria for success are based on two factors: backbone cRMSD and pTM. Backbone cRMSD refers to the root mean square deviation of the backbone atoms in a protein structure, which is a measure of how similar two structures are. pTM refers to the probability of a protein structure being in its native state, which is a measure of how stable and functional the protein is. The sentence states that success is evaluated based on whether these criteria are met after 128 generations, which likely refers to a simulation or experiment that involves evolving or optimizing protein structures. The Appendix A.4.5 is likely a reference to a section in a research paper or report that provides more details on the methodology and results of the experiment.
==============================
Preference tuned models solve double the atomic coordination tasks compared to base models (Fig.3A).
------------------------------
 This sentence is discussing the performance of two types of models: base models and preference tuned models. The sentence is saying that preference tuned models are able to solve twice as many atomic coordination tasks as base models. The figure mentioned in the sentence (Fig.3A) likely shows the results of a study or experiment that compared the performance of these two types of models.
User:
==============================
While the base models show differences in the fraction of tasks solved $(9.5 \%$ for 1.4B, $19.0 \%$ for 7B, 26.8\% for 98B; Fig.3A), a much larger capability difference is revealed through alignment $(9.5 \%$ to $18.8 \%, 19.0 \%$ to $37.4 \%, 26.8 \%$ to $65.5 \%$ for the 1.4B, 7B and 98B models, respectively).
------------------------------
 The sentence is discussing the performance of different models in solving tasks. The base models show some differences in the percentage of tasks they can solve, with the 1.4B model solving 9.5%, the 7B model solving 19.0%, and the 98B model solving 26.8%. However, when the models are aligned, there is a much larger difference in their capabilities. The 1.4B model's performance increases to 18.8%, the 7B model's performance increases to 37.4%, and the 98B model's performance increases to 65.5%. This means that the models are much more capable when they are aligned properly.
==============================
Preferencetuned models not only solve a greater proportion of tasks, but also find a greater number of solutions per task, as evaluated by the number of distinct structural clusters ( $\mathrm{TM}>0.8$ ) with backbone cRMSD $<1.5$ Åand pTM $>0.8$ (Fig.3B).
------------------------------
 This sentence is discussing the performance of "preferencetuned models" in solving tasks. The sentence states that these models not only solve a greater proportion of tasks, but also find a greater number of solutions per task. The performance of the models was evaluated using a specific metric, which is the number of distinct structural clusters with certain criteria. The criteria include having a backbone cRMSD (root mean square deviation) of less than 1.5 Å and a pTM (probability of true match) of greater than 0.8. The results of this evaluation are shown in Figure 3B.
User:
==============================
A shift in the distribution of ESMFold pTM and backbone cRMSD for each ligand binding motif is observed (Fig.3C; Fig.S17).
------------------------------
 This sentence is discussing a change in the distribution of two measurements, ESMFold pTM and backbone cRMSD, for a specific type of protein binding motif called a ligand binding motif. The change is shown in two figures, Fig.3C and Fig.S17. The sentence is likely from a scientific paper or report and is intended for an audience with some knowledge of protein structure and binding.
==============================
At the 98B scale, the finetuned model produces more distinct successful clusters than the base model on 37 of the 46 tested ligands, while the remaining 9 ligands were not solved by either the base or aligned model, indicating that alignment almost universally improves the faithfulness to the prompt and the foldability of the generated proteins.
------------------------------
 This sentence is discussing the results of an experiment where two different models were used to generate proteins. The "base model" was the original model, and the "finetuned model" was an improved version of the base model. The experiment tested the ability of these models to generate proteins that were similar to a specific target protein, called the "prompt." The results showed that the finetuned model was better at generating proteins that were similar to the prompt, and also had a higher chance of being "foldable," which means they could form a stable 3D structure. This was true for 37 out of the 46 tested proteins. However, for the remaining 9 proteins, neither model was able to generate a successful protein. Overall, the experiment suggests that using the finetuned model is a better approach for generating proteins that are similar to a specific target protein.
==============================
Compared to a supervised finetuning baseline, which only maximizes the likelihood of the positive examples, preference tuning leads to larger improvements at all scales (Appendix A.4.6).
------------------------------
 The sentence is discussing a comparison between two methods for improving a system's performance. The first method, called "supervised finetuning," focuses on improving the system's ability to recognize positive examples. The second method, called "preference tuning," is more effective at improving the system's performance overall, even at different levels of analysis. The details of this comparison can be found in Appendix A.4.6.
User:
==============================
Figure 3. The ability to solve complex tasks increases with scale through alignment. ESM3 is aligned to follow atomic coordination prompts with a dataset of preference pairs constructed from prompted generations, where positive samples with good scores for desired properties (high pTM, low cRMSD) are paired with negative samples with worse scores. The preference tuning loss encourages the model to put higher likelihood on the positive samples. After training, models are evaluated by prompting with coordinates in tertiary contact.
------------------------------
 This sentence is discussing a process called "alignment" in the context of a machine learning model called ESM3. The goal of this process is to improve the model's ability to solve complex tasks. To achieve this, the model is trained using a dataset of preference pairs, which are generated by prompting the model with atomic coordination prompts. The preference pairs consist of positive samples with good scores for desired properties and negative samples with worse scores. The model is then trained to put higher likelihood on the positive samples using a preference tuning loss. Finally, the model is evaluated by prompting it with coordinates in tertiary contact. Overall, this process helps the model to better understand complex tasks and improve its performance.###
==============================
(A) We show the effect of finetuning on the fraction of tasks solved with 128 generations (Pass@ 128). A large gap opens between the models with scale. The response to alignment shows a latent capability to solve complex tasks in the largest model. Error bars show 2 standard deviations.
------------------------------
 This sentence is discussing the results of an experiment where different models were tested on their ability to solve complex tasks. The researchers found that when they adjusted a certain parameter (finetuning), the models with a larger scale performed much better than the others. This difference was particularly noticeable when they looked at how many tasks were solved within a certain number of attempts (128 generations). The researchers also noticed that the largest model had a hidden ability to solve complex tasks, which was revealed when they aligned the data. The error bars show how much variation there was in the results.
==============================
(B) Number of distinct solutions (clustered at $\mathrm{TM}>0.8$ ) generated for each tertiary motif. After finetuning we often see a number of unique structures for ligands for which we have successes.
------------------------------
 The sentence is discussing the results of a scientific experiment or analysis. The phrase "tertiary motif" refers to a specific type of structure or pattern that is being studied. The phrase "distinct solutions" means that there are different possible outcomes or results that have been identified. The phrase "clustered at $\mathrm{TM}>0.8$ " means that these different outcomes are grouped together in a particular range of values. The phrase "finetuning" suggests that the experiment or analysis has been refined or improved in some way. The phrase "unique structures for ligands" means that there are different ways that certain molecules can be arranged or configured. The phrase "for which we have successes" means that these different arrangements have been successful in achieving some desired outcome or result. Overall, the sentence is describing the results of a scientific experiment or analysis that has identified different possible outcomes or solutions for a specific type of structure or pattern, and has refined the analysis to identify unique arrangements that have been successful in achieving a desired outcome.
==============================
(C) Densities of prompted generations are shown for the base model (left) and aligned model (right) at the 98B scale for a number of randomly selected ligands. After alignment, the fidelity to the prompt (cRMSD) and quality of generations (pTM) tends to improve meaningfully.
------------------------------
 The sentence is discussing the results of a study that used computer models to generate new versions of certain molecules called ligands. The study compared two different models: the "base model" and the "aligned model." The researchers looked at how well the new versions of the ligands matched the original prompt (the molecule they were trying to create a new version of) and how good the quality of the new versions was. They found that after using the aligned model, the new versions were more similar to the original prompt and of higher quality.
==============================
These results demonstrate that preference tuning extracts latent capability in the models.
------------------------------
 This sentence is saying that the results of a study or experiment show that a process called "preference tuning" can reveal hidden abilities or potential in certain models. In other words, by adjusting certain preferences or settings, the models can perform better or show new capabilities that were not previously apparent.
==============================
The capability of larger models to solve challenging tasks become far more apparent after alignment.
------------------------------
 This sentence is discussing the usefulness of larger models in solving difficult tasks. The phrase "after alignment" means that once the models are properly aligned or adjusted, their ability to handle complex tasks becomes much more noticeable. Essentially, the sentence is saying that larger models are better at solving tough problems, but this is only true if they are properly aligned.
==============================
Since alignment can be performed with arbitrary objectives, this is an indication of a general ability to respond to finetuning that greatly improves with scale.

------------------------------
 This sentence is saying that when something is aligned with different goals or purposes, it shows that it has a general ability to adapt and improve as it grows larger. The word "alignment" means to bring something into agreement or harmony with something else. The word "arbitrary" means that the goals or purposes can be chosen freely without any restrictions. The phrase "general ability" means that this adaptability is not specific to one particular situation or goal. The phrase "respond to finetuning" means that the thing being discussed can be improved or adjusted in small ways. The word "scale" means the size or extent of something. So, the sentence is saying that if something can be aligned with different goals and improve with small adjustments as it grows larger, it shows that it has a general ability to adapt and improve.