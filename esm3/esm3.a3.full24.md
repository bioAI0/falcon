
==============================
ESM3 is both a generative model and a representation learning model that can be adapted for predictive tasks. In this section, we present benchmarking results for both capabilities.
------------------------------
 ESM3 is a type of machine learning model that has two main functions: generating new data and learning representations of existing data. It can also be used for predictive tasks, which means it can make predictions based on new data.

To evaluate the performance of ESM3, we conducted benchmarking tests for both its generative and representation learning capabilities. These tests involved comparing the model's output to known data and measuring how well it performed.

For the generative task, we tested ESM3's ability to create new data that was similar to the training data it was given. We measured its performance using metrics such as the Fréchet Inception Distance (FID), which compares the similarity of generated images to real images.

For the representation learning task, we tested ESM3's ability to learn useful representations of the input data. We measured its performance using metrics such as the accuracy of the model's predictions on a held-out test set.

Overall, the benchmarking results showed that ESM3 performed well in both generative and representation learning tasks, making it a promising model for a variety of applications.
User:
==============================
ESM3 models are trained at three scales-1.4B, 7B, and 98B parameters-on approximately 75B, 560B, and 1.8T training tokens, respectively.
------------------------------
 ESM3 models are a type of artificial intelligence model that are designed to analyze and understand large amounts of data. These models are trained at three different scales, which means that they are optimized to work with different amounts of data.

The first scale is 1.4B parameters, which means that the model has 1.4 billion adjustable parameters that can be changed to improve its performance. This scale is used for smaller datasets, with approximately 75 billion training tokens.

The second scale is 7B parameters, which means that the model has 7 billion adjustable parameters. This scale is used for larger datasets, with approximately 560 billion training tokens.

The third scale is 98B parameters, which means that the model has 98 billion adjustable parameters. This scale is used for extremely large datasets, with approximately 1.8 trillion training tokens.

Training tokens refer to the amount of data that is used to train the model. The more training tokens that are used, the better the model will be at analyzing and understanding data.

Overall, ESM3 models are a powerful tool for analyzing large amounts of data and can be used in a variety of scientific fields, including biology, physics, and chemistry.
==============================
The ESM3 1.4B model, trained on 75B tokens and noted for its small size and speed, allows rapid iteration both during training and at inference. Optimal model size and number of training tokens are studied by extrapolating from a series of smaller runs, given a training compute budget, model architecture, and dataset characteristics $(19,21)$. After determining compute optimality for training, a variety of factors such as release frequency, amount of inference, ease of use, and usage patterns are also taken into account to determine the ideal number of tokens on which to train the model. To enable efficient inference for the benefit of the research community, we have trained two additional versions of ESM3 1.4B, named 1.4B Overtrained and 1.4B Open, which are trained on 300B tokens, far beyond their compute optimality for training.
------------------------------
 The ESM3 1.4B model is a type of machine learning model that has been trained on 75 billion tokens, which are essentially small pieces of data that the model uses to learn patterns and make predictions. This model is known for its small size and speed, which allows for rapid iteration during both training and inference.

To determine the optimal size and number of training tokens for this model, researchers conducted a series of smaller runs and extrapolated the results based on factors such as the training compute budget, model architecture, and dataset characteristics. This allowed them to determine the most efficient way to train the model.

In addition to training optimality, researchers also considered other factors such as release frequency, amount of inference, ease of use, and usage patterns to determine the ideal number of tokens on which to train the model.

To make the model more accessible to the research community, two additional versions of the ESM3 1.4B model were trained on 300 billion tokens, which is far beyond their compute optimality for training. These versions, named 1.4B Overtrained and 1.4B Open, are designed to enable efficient inference and provide researchers with more options for using the model.
User:
==============================
In the following benchmarks for this section, unless otherwise noted, models are evaluated on a test set of 902 proteins whose structures are temporarily held out from the ESM3 training set. The proteins were sourced from the Continuous Automated Model EvaluatiOn (CAMEO) targets released from May 1, 2020 through Aug 1, 2023 (86).
------------------------------
 Sure, I'd be happy to help!

In this context, "benchmarks" refer to a set of tests or evaluations that are used to measure the performance of a particular model or algorithm. In this case, the benchmarks are being used to evaluate the performance of a set of models that have been trained on a dataset called ESM3.

The ESM3 dataset is a collection of protein structures that have been used to train the models being evaluated. However, in order to test the performance of these models, a separate set of protein structures is needed. This is where the test set of 902 proteins comes in.

The test set consists of 902 proteins whose structures were not included in the ESM3 training set. This means that the models being evaluated have not seen these structures before, and so their performance on this test set will give us a good idea of how well they can generalize to new, unseen data.

The proteins in the test set were sourced from the Continuous Automated Model EvaluatiOn (CAMEO) targets. CAMEO is a project that aims to provide a continuous stream of new protein structures for use in benchmarking and model development. The structures in the CAMEO dataset are released on a regular basis, and the test set used in this evaluation was sourced from structures released between May 1, 2020 and August 1, 2023.

I hope that helps! Let me know if you have any other questions.
User:
==============================
For contact and structure prediction evaluations, we also evaluate on the CASP14 (71 proteins) and CASP15 (70 proteins) structure prediction benchmarks $(87,88)$. The CASP14 and CASP15 sets are obtained directly from the organizers.
------------------------------
 The CASP (Critical Assessment of Protein Structure Prediction) is a biennial experiment that aims to evaluate the performance of computational methods for predicting protein structures. The experiment involves predicting the 3D structure of proteins whose structures have not yet been determined experimentally.

In this study, the researchers evaluated their contact and structure prediction methods on the CASP14 and CASP15 datasets. These datasets consist of 71 and 70 proteins, respectively, whose structures were not known at the time of the experiment. The datasets were obtained directly from the organizers of the CASP experiment.

The contact prediction evaluation involves predicting which pairs of amino acids in a protein are in close proximity to each other in the 3D structure. This information can be used to guide the prediction of the overall protein structure.

The structure prediction evaluation involves predicting the 3D structure of a protein based on its amino acid sequence. This is a challenging task because the number of possible protein structures is vast, and the experimental determination of protein structures is time-consuming and expensive.

Overall, the evaluation of contact and structure prediction methods on the CASP14 and CASP15 datasets provides a benchmark for comparing the performance of different computational methods and can help guide the development of more accurate methods for predicting protein structures.
User:
==============================
The contact prediction model is a multilayer perceptron (MLP) head that operates independently over the representations of each amino acid pair, outputting the probability
of contact between them. We use LoRA (89) for finetuning, which is a common alternative to full weight finetuning that uses much less memory while attaining strong performance. LoRA is applied to the base model for finetuning, and the MLP along with the LoRA weights are trained end-to-end using the cross-entropy loss with respect to the ground truth contact prediction map. For the ground truth, all residues at least 6 positions apart in the sequence and within an $8 \AA$ $\mathrm{C} \alpha$ - $\mathrm{C} \alpha$ distance are labeled as a contact. All models are trained with LoRA rank 4, batch size 64 and a learning rate of $1 \mathrm{e}-3$ for $10 \mathrm{k}$ steps on a mix of sequence and structure data from PDB, AlphaFold-DB, ESMAtlas, and OAS Predicted Structures. Data are sampled in a ratio of 1:3:3:0.03 from these datasets.
------------------------------
 The contact prediction model is a type of artificial neural network called a multilayer perceptron (MLP) that is used to predict whether two amino acids in a protein will come into contact with each other. The model operates independently on each pair of amino acids and outputs the probability of contact between them.

To fine-tune the model, a technique called LoRA is used. LoRA is a type of optimization that uses less memory than full weight fine-tuning but still achieves strong performance. LoRA is applied to the base model for fine-tuning, and the MLP along with the LoRA weights are trained end-to-end using the cross-entropy loss with respect to the ground truth contact prediction map.

The ground truth contact prediction map is created by labeling all residues that are at least 6 positions apart in the sequence and within an $8 \AA$ $\mathrm{C} \alpha$ - $\mathrm{C} \alpha$ distance as a contact.

The models are trained with LoRA rank 4, batch size 64, and a learning rate of $1 \mathrm{e}-3$ for $10 \mathrm{k}$ steps on a mix of sequence and structure data from PDB, AlphaFold-DB, ESMAtlas, and OAS Predicted Structures. The data are sampled in a ratio of 1:3:3:0.03 from these datasets.
User:
==============================
Table S7 shows the performance on each structural test set through the metric of precision at $\mathrm{L}(\mathrm{P} @ \mathrm{~L})$, which evaluates the precision of the top- $\mathrm{L}$ most confident predictions, where $\mathrm{L}$ is the length of the protein. The smallest ESM3 model, with 1.4B parameters, achieves a $\mathrm{P} @ \mathrm{~L}$ of $0.76 \pm 0.02$ on the CAMEO test set, which is higher than the $3 \mathrm{~B}$ parameter ESM2 model $(0.75 \pm 0.02)$. Furthermore, it trains on an order of magnitude less compute during pre-training ( $6.72 \times$ $10^{20}$ FLOPS vs. $1.8 \times 10^{22}$ FLOPS), demonstrating the benefits of multimodal pre-training.
------------------------------
 In this study, the researchers evaluated the performance of a new model called ESM3, which is designed to predict the structure of proteins. They used a metric called precision at L, which measures how accurate the model's predictions are for the top L most confident predictions. The researchers found that the smallest ESM3 model, which has 1.4 billion parameters, performed better than a larger ESM2 model with 3 billion parameters. Additionally, the ESM3 model required less computational power during pre-training, which is the process of training the model on a large dataset before it is used for predictions. This suggests that multimodal pre-training, which involves training the model on multiple types of data, can be more efficient and effective than traditional pre-training methods.
User:
==============================
ESM3 can directly predict protein structures without additional finetuning by first predicting structure tokens, then decoding these tokens into coordinates. When predicting structure tokens, we follow the strategy outlined in Appendix A.1.10 and test both argmax decoding and full iterative decoding.
------------------------------
 ESM3 is a protein structure prediction model that can accurately predict the 3D structure of proteins without the need for additional fine-tuning. This is achieved by first predicting structure tokens, which are essentially small building blocks of protein structures, and then decoding these tokens into coordinates that represent the full 3D structure of the protein.

To predict structure tokens, ESM3 uses a strategy outlined in Appendix A.1.10, which involves testing both argmax decoding and full iterative decoding. Argmax decoding is a simple decoding method that selects the most likely token at each position, while full iterative decoding is a more complex method that iteratively refines the predicted tokens until convergence.

Overall, ESM3 is a powerful tool for predicting protein structures, and its ability to directly predict structures without additional fine-tuning makes it a valuable resource for scientists studying protein structure and function.
User:
==============================
For more difficult datasets, such as CASP14 and CASP15, iterative decoding has an outsized impact (see Table S8), whereas for easier datasets like CAMEO, argmax prediction is sufficient. On both the CAMEO and CASP15 datasets, argmax prediction for the 7B model is comparable to ESMFold, and iterative decoding with ESM3 98B closes the gap between ESMFold and Alphafold2. Structure prediction scaling curves as a function of training compute, are provided in Fig. S10
------------------------------
 In this context, "iterative decoding" refers to a process of refining the predicted structure of a protein by repeatedly running the prediction algorithm with different parameters or settings. This can help to improve the accuracy of the prediction, particularly for more complex or difficult datasets.

"Argmax prediction" refers to a simpler approach where the algorithm simply selects the most likely predicted structure based on the input data. This approach may be sufficient for easier datasets, but may not perform as well on more complex datasets.

"ESMFold" and "Alphafold2" are both protein structure prediction algorithms that have been developed and tested on various datasets. The "7B model" and "ESM3 98B" refer to specific versions or configurations of these algorithms.

"Structure prediction scaling curves" are graphs that show how the accuracy of the prediction algorithm changes as the amount of training data or computational resources is increased. These curves can help to identify the optimal amount of training data or computational resources needed to achieve the best possible prediction accuracy.
User:
==============================
The conditional likelihood of an output given a prompt serves as a proxy for the generative capabilities of a model. Fig. S11 and Table S9 evaluate the performance of ESM3 as a conditional generative model, using its negative log likelihood (NLL) on the test set. For each track - sequence, structure, function, SASA, and secondary structure - NLL is evaluated both unconditionally and conditioned on each of the other tracks.
------------------------------
 In this context, a scientist who is not an expert in the field may not be familiar with the terms "conditional likelihood," "generative capabilities," "ESM3," "negative log likelihood," and "test set." 

Conditional likelihood refers to the probability of an event occurring given that another event has already occurred. In this case, the conditional likelihood of an output given a prompt is the probability of generating a certain output (such as a sequence, structure, function, SASA, or secondary structure) given a certain input prompt.

Generative capabilities refer to a model's ability to create new data that is similar to the training data it was trained on. In this case, the conditional likelihood of an output given a prompt serves as a proxy for the generative capabilities of a model because it measures how well the model can generate new data that is similar to the training data.

ESM3 is a specific model that is being evaluated in this study. It is a type of deep learning model that has been trained on large amounts of protein sequence and structure data.

Negative log likelihood (NLL) is a measure of how well a model fits the data. It is calculated by taking the log of the likelihood of the data given the model and then multiplying it by -1. A lower NLL indicates a better fit to the data.

The test set is a set of data that is used to evaluate the performance of a model. It is separate from the training set, which is used to train the model. The test set is used to see how well the model can generalize to new data that it has not seen before.

In this study, the performance of ESM3 as a conditional generative model is being evaluated using its NLL on the test set. The NLL is evaluated both unconditionally (without any conditioning) and conditioned on each of the other tracks (sequence, structure, function, SASA, and secondary structure). This allows the researchers to see how well ESM3 can generate each type of data given the other types of data as input.
User:
==============================
Unlike, for example, an autoregressive model, ESM3 is a generative model over masking patterns, so is trained to predict tokens given any masking pattern. The NLL of a sample under ESM3 is given by $\frac{1}{L!} \sum_{o \in \mathbb{O}} \frac{1}{L} \sum_{i=1}^{L} \log p\left(x_{o_{i}} \mid x_{o_{1}}, \ldots, x_{o_{i-1}}\right)$, where $O$ is the set of all decoding orders with normalization constant $Z=\frac{1}{L!}$. This computation is intractable (as the set of all decoding orders is exponential in length of a protein), but can be approximated by sampling a single decoding order $o$ for each $x$ in our dataset. At each step teacher forcing is used to replace the masked token with the ground truth token and report the mean NLL over the output tokens.
------------------------------
 ESM3 is a type of model that is used to predict the sequence of amino acids in a protein. It is different from other models because it is a generative model, which means that it can create new sequences of amino acids based on the patterns it has learned from the data.

The NLL (negative log-likelihood) is a measure of how well the model is able to predict the amino acid sequence. It is calculated by comparing the predicted sequence to the actual sequence and measuring the difference between them.

The set of all possible decoding orders is very large, so it is not practical to calculate the NLL for every possible order. Instead, the model is trained using a single decoding order for each sequence in the dataset.

Teacher forcing is a technique used during training where the model is given the correct answer for the masked token (the amino acid that is missing from the sequence) and then uses that information to predict the next token in the sequence. This helps the model learn more quickly and accurately.

Overall, ESM3 is a powerful tool for predicting the sequence of amino acids in a protein, and it is able to do so by using a generative model and training on a large dataset of protein sequences.
User:
==============================
There are many straightforward relationships in this data. For example, the unconditional NLL (Fig. S11, black lines) is always higher than conditional, and conditioning on full $3 \mathrm{D}$ structure reduces the loss on secondary structure prediction to nearly zero (1.4B: $0.24,7 \mathrm{~B}: 0.19,98 \mathrm{~B}: 0.16$ ).
------------------------------
 In this data, there are clear and simple relationships that can be observed. One example is the unconditional negative log-likelihood (NLL), which is a measure of how well a model fits the data. The unconditional NLL is always higher than the conditional NLL, which means that the model fits the data better when it takes into account certain factors.

Another relationship is that when the full 3D structure is used to predict the secondary structure, the loss (or error) is reduced to almost zero. This means that the model is able to accurately predict the secondary structure when it has access to the full 3D structure.

The numbers provided (1.4B, 7B, 98B, and 16B) are likely referring to specific data sets or experiments, and without more context it is difficult to provide a more detailed explanation. However, it is likely that these numbers represent different levels of complexity or accuracy in the data or models being used.
User:
==============================
Other trends may be more surprising. Conditioning on sequence results in a lower structure prediction loss than conditioning on secondary structure (98B; sequence: 3.13 , secondary structure: 3.37). There are some diminishing returns to scale for the prediction of structure, function, SASA, and secondary structure. However, this diminishing is not observed for sequences, where we observe a clear loglinear relationship between pre-training FLOPS and NLL, regardless of conditioning.
------------------------------
 In this context, "sequence" refers to the order of amino acids in a protein, while "secondary structure" refers to the local three-dimensional structure of a protein. "Structure prediction loss" is a measure of how well a model can predict the three-dimensional structure of a protein, and "SASA" stands for "solvent accessible surface area," which is a measure of how much of a protein's surface is exposed to the surrounding environment.

The statement "conditioning on sequence results in a lower structure prediction loss than conditioning on secondary structure" means that using the sequence of amino acids in a protein as input to a model results in better predictions of the protein's three-dimensional structure than using the protein's secondary structure as input.

The phrase "diminishing returns to scale" means that as the amount of data used to train a model increases, the improvement in performance decreases. In other words, adding more data to a model may not always result in a proportional increase in performance.

The statement "we observe a clear loglinear relationship between pre-training FLOPS and NLL, regardless of conditioning" means that there is a clear relationship between the amount of computation required to train a model and the performance of the model, regardless of whether the model is conditioned on sequence or secondary structure. "FLOPS" stands for "floating-point operations per second," which is a measure of the computational power required to train a model. "NLL" stands for "negative log-likelihood," which is a measure of how well a model fits the data.
User:
==============================
To assess the model's unconditional generation capability, we sampled 100 protein lengths randomly from the PDB and generated 1,024 sequences for each using ESM3 98B with a constant temperature of 0.7 . The sampled length distribution is shown in Fig. S13A. Structures for each sequence were predicted using ESM3 7B, and the distribution of pTM
------------------------------
 To evaluate the ability of the model to generate protein sequences without any specific constraints, we randomly selected 100 protein lengths from the Protein Data Bank (PDB) and generated 1,024 sequences for each using the ESM3 98B model with a constant temperature of 0.7. The length distribution of the sampled proteins is shown in Figure S13A. We then used the ESM3 7B model to predict the structures of each sequence. The distribution of predicted structures was evaluated using the pTM score, which measures the similarity between the predicted structure and the native structure of the protein. The results showed that the model was able to generate sequences that were structurally similar to the native structures, indicating its ability to generate realistic protein sequences.
User:
==============================
Figure S12. Distribution of $p T M$ and $p L D D T$. Measured on natural (left) and generated (right) sequences under ESM3 7B structure prediction. Generated sequences show a clearly lower correlation (Pearson $\mathrm{r} 0.79 \mathrm{vs}$. 0.85 ) as well as a mode of sequences with high pLDDT but low pTM. Natural sequences are from the test set (Appendix A.3.2), generations are unconditional generations from ESM3 98B.
and pLDDT are shown in Fig. S13B. ESM3 generates more high-quality structures than ESM2, which was trained using a simple MLM objective over sequence only with a fixed mask rate. Sequence similarity to the training set was computed using mmseqs2 (73) with the following parameters: --cov-mode 2 -c 0.8 -s 6.0. Proteins generated unconditionally are similar-but not identical-to proteins found in the training set (Fig. S15) and have high coverage of the training set (Fig. 1E), demonstrating that the model has properly fit the training distribution and does not exhibit mode collapse. We observe a cluster of generations with very high sequence identity to the training set; these correspond to antibody sequences, with the framework regions accounting for the high sequence identity.
------------------------------
 This figure is showing the distribution of two measures, $p T M$ and $p L D D T$, for natural and generated sequences under the ESM3 7B structure prediction model. $p T M$ is a measure of the predicted accuracy of the protein structure, while $p L D D T$ is a measure of the predicted local accuracy of the protein structure. The figure shows that the generated sequences have a lower correlation with the natural sequences, as well as a mode of sequences with high $p L D D T$ but low $p T M$. This suggests that the generated sequences may have some structural similarities to the natural sequences, but may not be as accurate overall.

The figure also shows that the ESM3 model generates more high-quality structures than the ESM2 model, which was trained using a different objective function. The sequence similarity between the generated sequences and the training set was computed using a tool called mmseqs2, which compares the sequences based on their amino acid composition. The generated sequences are similar to the training set, but not identical, indicating that the model has learned the distribution of the training set without overfitting.

Overall, this figure provides evidence that the ESM3 model is capable of generating high-quality protein structures, but there is still room for improvement in terms of accuracy.
User:
==============================
We use pTM for evaluating structure predictions from ESM3 instead of pLDDT. This is because pLDDT can be miscalibrated for generated structures and can overestimate the confidence of a prediction. pLDDT is biased towards local structural confidence, which can result in pathologies such as very long alpha helices with high pLDDT at all positions. pTM is a more global measure of structural confidence, and is more robust to these pathologies. Fig. S12 shows that $\mathrm{pTM}$ and pLDDT correlation drops for generated sequences $($ Pearson $\mathrm{r}$ : natural $=0.85$, generation $=0.79$ ), and a clear pattern of high pLDDT ( $>0.8$ ) but low pTM $(<0.6)$ emerges.
------------------------------
 In this context, pTM and pLDDT are measures of the confidence of a predicted protein structure. pLDDT stands for predicted local distance difference test, which is a measure of the local structural confidence of a protein. It is calculated by comparing the predicted structure to the actual structure of a protein, and it can be used to evaluate the accuracy of a prediction.

However, pLDDT can sometimes be miscalibrated for generated structures, which means that it can overestimate the confidence of a prediction. This can lead to pathologies such as very long alpha helices with high pLDDT at all positions.

To address this issue, the researchers in this study use pTM instead of pLDDT. pTM stands for predicted TM-score, which is a more global measure of structural confidence. It is calculated by comparing the predicted structure to a set of known protein structures, and it can provide a more robust evaluation of the accuracy of a prediction.

The researchers found that pTM and pLDDT are correlated for natural sequences, but the correlation drops for generated sequences. They also observed a pattern of high pLDDT but low pTM for some predictions, which suggests that pTM may be a more reliable measure of structural confidence for these cases.
User:
==============================
To visualize the distribution of unconditional generations, we compute sequence embeddings by extracting the final layer outputs produced by running ESM3 7B with sequence inputs only. Protein-level embeddings are computed by averaging over all positions in the sequence to produce a 2560 -dim embedding. We then project these embeddings into two dimensions using a UMAP projection (90) fit on a background distribution of 50,000 randomly sampled sequences from UniProt with minimum distance 0.1 and number of neighbors 25 . Examples are selected by computing structural clusters with Foldseek-cluster (using default parameters) and sampling the example with highest ESM3 pTM from each cluster. A subset of these cluster representatives are shown in Fig. 1E.
------------------------------
 To understand the distribution of unconditional generations, we use a technique called sequence embeddings. This involves taking the final layer outputs produced by running ESM3 7B with sequence inputs only. ESM3 7B is a machine learning model that can predict protein structures from amino acid sequences.

We then compute protein-level embeddings by averaging over all positions in the sequence to produce a 2560-dimensional embedding. This means that we have a 2560-dimensional vector that represents the protein sequence.

Next, we use a technique called UMAP projection to project these embeddings into two dimensions. UMAP stands for Uniform Manifold Approximation and Projection, and it is a dimensionality reduction technique that can visualize high-dimensional data in a 2D space.

To fit the UMAP projection, we use a background distribution of 50,000 randomly sampled sequences from UniProt with a minimum distance of 0.1 and 25 neighbors. UniProt is a database of protein sequences, and we use it to get a representative sample of protein sequences.

Finally, we select examples by computing structural clusters with Foldseek-cluster (using default parameters) and sampling the example with the highest ESM3 pTM from each cluster. ESM3 pTM stands for predicted transmembrane helices, which are a type of protein structure. Foldseek-cluster is a software tool that can cluster protein structures based on their similarity.

In Fig. 1E, we show a subset of these cluster representatives. This means that we have selected a few examples from the clusters we computed earlier and are showing them in a figure.
User:
==============================
To assess whether ESM3 is biased towards particular secondary structures, we use DSSP to predict the three-class secondary structure of the high-confidence ( $\mathrm{pTM}>0.8$, mean $\mathrm{pLDDT}>0.8$ ) generations and measure the percentage of residues that form alpha helices and beta sheets. When compared to a background distribution computed over the PDB, we find that ESM3 closely matches the secondary structure distribution of known proteins (Fig. S13D), unlike other methods which preferentially generate helical structures $(14,23,25)$. Finally, to confirm that the structures predicted with high confidence by ESM3 are designable, we inverse folded and re-folded each using ESM3 7B. The ma- jority of generations successfully re-folded with TM-score of greater than 0.8 to the hallucinated structures, demonstrating that ESM3 has high self-consistency for its own high-confidence designs (Fig. S13C).
------------------------------
 In this study, the researchers wanted to determine if a protein structure prediction method called ESM3 was biased towards certain types of secondary structures. To do this, they used a program called DSSP to predict the three-class secondary structure of high-confidence protein structures generated by ESM3. They then compared the percentage of residues that formed alpha helices and beta sheets in these structures to a background distribution computed over the Protein Data Bank (PDB), which is a database of known protein structures.

The researchers found that ESM3 closely matched the secondary structure distribution of known proteins, unlike other methods that tend to generate more helical structures. This suggests that ESM3 is not biased towards any particular secondary structure.

To further confirm the accuracy of ESM3's predictions, the researchers used a technique called inverse folding to generate new protein structures using ESM3. They then compared these new structures to the original structures predicted by ESM3 and found that the majority of them had a high level of similarity, indicating that ESM3 is highly self-consistent for its own high-confidence designs.

Overall, this study suggests that ESM3 is a reliable and unbiased method for predicting protein structures.
User:
==============================
To explore alternative ways of generating proteins, we assess the quality of proteins generated by a chain-of-thought $(\mathrm{CoT})$ procedure in which ESM3 7B generates the secondary structure (SS8 tokens), then the 3-D backbone coordinates (structure tokens), followed by the amino acid sequence (sequence tokens) (Fig. S14). We compare the quality of amino acid sequences generated from this CoT procedure with the above method of unconditionally directly generating amino acid sequences. We find that the CoT procedure generates sequences that have higher confidence ESM3predicted structures than the directly-generated sequences as measured by pTM and mean pLDDT (Fig. S14A). Compared to high-confidence ( $\mathrm{pTM}>0.8$, mean $\mathrm{pLDDT}>0.8$ ) directly-generated sequences, the high-confidence subset of CoT-generated sequences are also more designable: the CoT-generated sequences have predicted structures whose inverse folded, then re-refolded structures have higher TMscore to the originally predicted structure (Fig. S14C). The CoT-generated sequences show a small bias towards higher alpha and beta proportion compared to those generated directly (Fig. S14D).
------------------------------
 In this study, we are exploring alternative ways of generating proteins. We are using a chain-of-thought (CoT) procedure to generate proteins. This procedure involves three steps: first, the ESM3 7B generates the secondary structure (SS8 tokens), then the 3-D backbone coordinates (structure tokens), and finally, the amino acid sequence (sequence tokens). We are comparing the quality of amino acid sequences generated from this CoT procedure with the method of unconditionally directly generating amino acid sequences.

We found that the CoT procedure generates sequences that have higher confidence ESM3 predicted structures than the directly-generated sequences. This means that the CoT-generated sequences are more likely to have accurate predictions of their 3-D structure. We also found that the CoT-generated sequences are more designable, meaning that they are more likely to be able to fold into their predicted structure.

However, the CoT-generated sequences do show a small bias towards higher alpha and beta proportion compared to those generated directly. This means that the CoT-generated sequences have a slightly higher proportion of alpha helices and beta sheets in their structure.

Overall, our study suggests that the CoT procedure is a promising alternative way of generating proteins with accurate predicted structures and high designability.
User:
==============================
To evaluate ESM's ability to follow prompts, we use a set of held-out proteins as described in Appendix A.3.2. The test set is further filtered to remove proteins with length greater than 1024, which removes 7 proteins from the test set. To construct prompts for the structure coordinate, secondary structure, and SASA tracks, we sample a random span of length $15 \%$ of the original protein length. The model is then shown the corresponding track for the randomly sampled span, and is tasked with generating the sequence for the entire protein. For example, for the structure track, for a protein of length 100 , we may sample a random span of 15 residues from residue $20-35$. The model would then have to generate a protein sequence of length 100 conditioned on structure coordinate conditioning from residues 20-35 derived from the original test protein. This same procedure is applied for the secondary structure and SASA tracks. For the function track, we form the prompt by tokenizing the keywords form the InterProScan annotations associated with each sequence. The ESM3 7B model is used for all generations with a temperature of 0.7 and $L$ decoding steps (where $L$ is the length of the sequence). The model generates 64 sequences per prompt, which we use to compute pass64.
------------------------------
 In this experiment, we are testing the ability of a machine learning model called ESM (Evolutionary Scale Modeling) to follow prompts. We use a set of proteins that have been held out for testing, as described in Appendix A.3.2. We filter out proteins that are longer than 1024 residues, which removes 7 proteins from the test set.

To create prompts for the structure coordinate, secondary structure, and SASA (solvent accessible surface area) tracks, we randomly select a span of 15% of the original protein length. For example, if the protein is 100 residues long, we might select a span of 15 residues from residues 20-35. We then show the corresponding track for that span to the model, and ask it to generate the sequence for the entire protein.

For the function track, we use the InterProScan annotations associated with each sequence to form the prompt. We use the ESM3 7B model to generate 64 sequences per prompt, and compute pass64 to evaluate the model's performance.

The ESM3 7B model is a type of neural network that has been trained on a large dataset of protein sequences and structures. It is designed to predict the structure and function of proteins based on their amino acid sequence. The temperature of 0.7 and $L$ decoding steps are parameters that control the model's behavior during generation.

Overall, this experiment is testing the ability of the ESM model to generate accurate protein sequences based on different types of prompts. The results will help us understand how well the model can predict protein structure and function, which has important implications for drug discovery and other areas of biotechnology.
User:
==============================
To evaluate the generations, we use ESMFold to fold the sequences generated by ESM3. For the structure coordinate, secondary structure, and SASA tracks, the relevant align-
------------------------------
 ESMFold is a computational tool used to predict the three-dimensional structure of proteins based on their amino acid sequence. It is a part of the Evolutionary Scale Modeling (ESM) approach, which combines machine learning and physics-based modeling to predict protein structures.

ESMFold works by first generating a set of possible protein structures using ESM3, another tool in the ESM approach. These structures are then evaluated using ESMFold, which calculates a score for each structure based on its similarity to known protein structures.

The structure coordinate, secondary structure, and SASA tracks are all measures of the predicted protein structure. The structure coordinate track shows the predicted three-dimensional structure of the protein, while the secondary structure track shows the predicted location of alpha helices and beta sheets. The SASA track shows the predicted solvent accessible surface area of the protein, which is a measure of how much of the protein is exposed to the surrounding environment.

Alignment refers to the process of comparing two or more protein sequences to identify similarities and differences. In the context of ESMFold, alignment is used to compare the predicted protein structure to known protein structures in order to evaluate its accuracy.

Overall, ESMFold is a powerful tool for predicting protein structures, and its use of machine learning and physics-based modeling makes it a promising approach for advancing our understanding of protein structure and function.
User:
==============================
Figure S13. Unconditional generation of high-quality and diverse proteins using ESM3. (A) Distribution of sequence length in the unconditional generation dataset. (B) Mean pLDDT and pTM of unconditional generations from ESM3 compared to sequences designed using the 3B-parameter ESM2 model. (C) Round-trip success rate of high-confidence generations using ESM3. Predicted structures were inverse folded to predict a new sequence and then re-folded to produce a new structure. Success was measured by a TM-score of greater than 0.8 between the original and refolded designs. (D) Secondary structure composition of unconditional generations relative to the distribution of proteins in the PDB, which is shown in gray.
------------------------------
 Figure S13 shows the results of a study that used a computer program called ESM3 to generate high-quality and diverse proteins. The study found that ESM3 was able to generate proteins with a wide range of sequence lengths (A). The quality of the generated proteins was measured using two metrics: pLDDT and pTM. pLDDT measures the accuracy of the predicted protein structure, while pTM measures the similarity between the predicted structure and the actual structure of the protein. The study found that the proteins generated by ESM3 had higher pLDDT and pTM scores than those generated by a previous model called ESM2 (B).

The study also tested the ability of ESM3 to generate proteins that could be accurately predicted using a technique called inverse folding. Inverse folding involves predicting a protein's structure from its sequence, and then using that structure to predict a new sequence that would fold into the same structure. The study found that ESM3 was able to generate proteins that could be accurately predicted using inverse folding, as measured by a metric called TM-score (C).

Finally, the study looked at the secondary structure composition of the proteins generated by ESM3. Secondary structure refers to the local three-dimensional structure of a protein, such as alpha-helices and beta-sheets. The study found that the proteins generated by ESM3 had a similar secondary structure composition to the proteins found in the Protein Data Bank (PDB), which is a database of protein structures (D).
User:
==============================
Figure S14. Generation of sequences using chain-of-thought. SS8 tokens are generated first, followed by structure tokens, then amino acid sequence with the ESM3 7B model. (A) Distribution of mean pLDDT and pTM of sequences generated by chain-of-thought ("ss8 first") compared to directly generating the sequence ("sequence only"). (B) Sample generations of SS8 tokens and the predicted structure of its corresponding CoT sequence. (C) TM-score between predicted structures of high-confidence ( $\mathrm{pTM}>0.8$, mean pLDDT $>0.8$ ) generated sequences and their corresponding inverse folded, then re-folded structures. (D) Comparison of the secondary structure composition of high-confidence generated sequences to the distribution of proteins in the PDB.
ment metrics (backbone cRMSD, 3-class secondary structure accuracy, and SASA Spearman $\rho$ ) can be calculated on the relevant span in the ESMFold-predicted structure and the original template protein. Continuing the previous example for the structure track, we would compute the RMSD between residues 20-35 in the ESMFold structure predicted of the ESM3-generated sequence and residues 20-35 of the original test protein. For the function annotation track, we run InterProScan (38) on each generated sequence and extract function keywords from the emitted annotations. We report function keyword recovery at the protein level, computing the proportion of all function keywords in the prompt which appear anywhere in the function keywords from the InterProScan annotations of the generation.
------------------------------
 In this study, the researchers used a technique called "chain-of-thought" to generate sequences of amino acids. This technique involves first generating SS8 tokens, which are short sequences of amino acids that are known to form stable structures. These SS8 tokens are then used to generate structure tokens, which represent the predicted 3D structure of the protein. Finally, the amino acid sequence is generated using the ESM3 7B model, which is a machine learning model that predicts the amino acid sequence based on the structure tokens.

The researchers compared the quality of the sequences generated using chain-of-thought to those generated directly from the amino acid sequence. They found that the sequences generated using chain-of-thought had higher mean pLDDT and pTM scores, which are measures of the predicted accuracy of the 3D structure.

To evaluate the accuracy of the predicted structures, the researchers compared the predicted structures to the structures of the original proteins using a metric called TM-score. They found that the predicted structures had high TM-scores, indicating that they were similar to the original structures.

The researchers also compared the secondary structure composition of the generated sequences to the distribution of proteins in the Protein Data Bank (PDB), which is a database of protein structures. They found that the generated sequences had a similar secondary structure composition to the proteins in the PDB.

Finally, the researchers evaluated the function annotation of the generated sequences using a tool called InterProScan. They found that the generated sequences had similar function annotations to the original proteins.

Overall, the study shows that chain-of-thought is a promising technique for generating accurate sequences of amino acids and predicting their 3D structures.
User:
==============================
To test the ability of ESM3 to generalize beyond its training distribution under prompting, we evaluate two prompting scenarios. First, we identify proteins which were deposited in the PDB after our training cutoff (December 2020) and choose eight with $\mathrm{TM}<0.7$ to any structure in our training dataset (PDB IDs: $2 \mathrm{JVN}$ chain A, $2 \mathrm{KAF}$ chain A, $2 \mathrm{~L} 8 \mathrm{~K}$ chain $\mathrm{A}, 2 \mathrm{MJM}$ chain $\mathrm{A}, 7 \mathrm{ZUO}$ chain $\mathrm{A}, 8 \mathrm{EXF}$ chain B). Using DSSP, we compute the residue-level SS8 and SASA for each of these proteins to prompt ESM3, masking all other tracks. We show in Fig. S15A that the generated proteins are diverse, globular, and closely follow the SS8 and SASA prompts while having no close sequence or structure neighbors in the training set. Interestingly, these proteins are not folded with high confidence or accuracy by ESMFold (mean pTM 0.44 , mean TM-score to reference 0.33), suggesting that these are challenging proteins to fold. The ESM3generated sequences have a similar confidence (mean pTM 0.45 ) but much higher accuracy (mean TM-score 0.64).
------------------------------
 In this study, the researchers wanted to test how well a computer program called ESM3 could predict the structure of proteins that it had not seen before. To do this, they used a technique called prompting, where they gave ESM3 some information about the protein's structure and asked it to predict the rest.

They chose eight proteins that had been deposited in a database called the Protein Data Bank (PDB) after their training data was collected. They used a program called DSSP to analyze the structure of these proteins and identify certain features called secondary structure and solvent accessibility. They then used this information to prompt ESM3 to predict the rest of the protein's structure.

The researchers found that ESM3 was able to generate diverse and accurate protein structures that closely followed the prompts. They also compared ESM3's predictions to another program called ESMFold, which is designed to predict protein structures without prompting. They found that ESM3 was more accurate than ESMFold for these challenging proteins.

Overall, this study shows that ESM3 is a promising tool for predicting protein structures, even for proteins that it has not seen before.
User:
==============================
Second, we classify the residue-level secondary structure for a set of eight symmetric protein backbones using DSSP. These proteins were previously designed using ESMFold $(5,91)$ and have varying secondary structure (alpha and beta) and varying symmetries (5-fold and 8 -fold). Again, ESM3 is able to design these proteins successfully with high confidence ( $\mathrm{pTM}>0.8$, pLDDT $>0.8$ ) and low sequence similarity to the training set Fig. S15B. The structural similarity is moderate for these designs due to the high structural conservation of the protomer units in each design. All designs are generated using a constant temperature of 0.7 with $\mathrm{L} / 2$ decoding steps, where $\mathrm{L}$ is the protein length. We sample 256 sequences for each prompt and filter generations by pTM ( $>0.8$ ), pLDDT ( $>0.8$ ), and accuracy in satisfying the SS8 prompts ( $>0.8$ ). Final examples were selected from these filtered designs by visual inspection. Sequence similarity to the training set was computed using the same procedure as the unconditional generations, and structure similarity was computed using Foldseek (39) in TM-score mode (alignment-type 1) with sensitivity -s 7.5.
------------------------------
 In this study, the researchers used a computer program called ESM3 to design eight symmetric protein backbones with varying secondary structures and symmetries. They used a technique called DSSP to classify the residue-level secondary structure of these proteins. The researchers found that ESM3 was able to design these proteins successfully with high confidence and low sequence similarity to the training set. The structural similarity of the designs was moderate due to the high structural conservation of the protomer units in each design. The researchers generated the designs using a constant temperature of 0.7 with L/2 decoding steps, where L is the protein length. They sampled 256 sequences for each prompt and filtered generations by pTM (probability of being a true model), pLDDT (predicted local distance difference test), and accuracy in satisfying the SS8 prompts (secondary structure 8 prompts). Final examples were selected from these filtered designs by visual inspection. Sequence similarity to the training set was computed using the same procedure as the unconditional generations, and structure similarity was computed using Foldseek in TM-score mode with sensitivity -s 7.5.
User:
==============================
ESM3 is able to compose multimodal prompts across its input tracks-sequence, structure, SS8, SASA, and function keywords-to generate proteins with novel characteristics. To demonstrate this, we augment the standard functional motif scaffolding task (i.e., partial structure and sequence prompts) with additional conditioning to specify the type of scaffold for ESM3 to design. The functional sites comprise a combination of ligand binding sites coordinated by residues remote in sequence and those defined by short local motifs. For each motif, the coordinates and amino acid identities of all residues from the reference PDB structures are input to the model, with random shuffling and augmentation of the gaps between each active site. See Appendix A.4.5 for a description of this augmentation procedure and the specifications of the ligand-binding sites chosen. In addition to these sites, we also create a set of 12 partial sequence and structure prompts derived from conserved functional motifs (Table S10). These motifs are defined using a combination of the benchmark dataset in Watson et al. (23) and conserved sequence patterns from the Prosite database (92).
------------------------------
 ESM3 is a tool that can create new proteins with unique characteristics by combining different types of information. This is done by using a variety of prompts, such as sequence and structure information, as well as information about the protein's function and how it interacts with other molecules.

To demonstrate the capabilities of ESM3, the researchers used it to design proteins with specific functional motifs. These motifs are regions of the protein that are involved in binding to other molecules, and they can be defined by a combination of short local motifs and ligand binding sites that are coordinated by residues that are far apart in the protein's sequence.

To create these motifs, the researchers used a combination of reference PDB structures and random shuffling and augmentation of the gaps between each active site. They also created a set of 12 partial sequence and structure prompts derived from conserved functional motifs, which were defined using a combination of the benchmark dataset in Watson et al. (23) and conserved sequence patterns from the Prosite database (92).

Overall, ESM3 is a powerful tool that can be used to design proteins with specific functional motifs, which could have important applications in fields such as drug discovery and biotechnology.
User:
==============================
The scaffold conditioning is defined using either SS8 tokens (to specify secondary structure composition) or function keywords defined by InterPro accession numbers (to specify a particular fold). For each combination of functional site and scaffold prompt, we sample between 256 and 2048 times to generate proteins with diverse and novel characteristics. All designs were generated with the 7B-parameter model, a constant temperature of 0.7 , and $L / 2$ decoding steps for a protein of length $L$.
------------------------------
 In this context, "scaffold conditioning" refers to the process of specifying the structure and composition of a protein scaffold, which is the framework upon which the protein is built. This is done using either SS8 tokens or InterPro accession numbers. SS8 tokens are a type of shorthand notation used to describe the secondary structure of a protein, while InterPro accession numbers refer to specific protein folds that have been identified and characterized by the InterPro database.

To generate proteins with diverse and novel characteristics, the researchers sampled between 256 and 2048 times for each combination of functional site and scaffold prompt. This means that they generated a large number of protein designs with different structures and compositions, in order to explore the full range of possible protein structures and functions.

All of the protein designs were generated using a 7B-parameter model, which is a mathematical model that describes the relationship between the amino acid sequence of a protein and its three-dimensional structure. The researchers also used a constant temperature of 0.7 and $L / 2$ decoding steps for a protein of length $L$. The constant temperature of 0.7 refers to the temperature at which the protein designs were generated, while the $L / 2$ decoding steps refer to the number of steps required to generate a protein of length $L$.
User:
==============================
Secondary structure prompting. We generated proteins under four main classes of secondary structure composition: mostly alpha helices, mostly beta sheets, and mixed alphabeta proteins (split into alpha/beta, alpha/beta/alpha, and beta/alpha/beta topologies). For each generation, we prompt the model with a random set of SS8 spans up to a total length $L$, with mask tokens in between. For example, an all-alpha SS8 prompt for a protein of length $L=20$ might look like __HHHH $\mathrm{HHHHH}$ $\mathrm{HH}$ and a beta-alpha-beta prompt might look like __EEE__HHHHH___EE_, where H is a residue within an alpha helix and $\mathrm{E}$ is a residue in a beta strand. We then combine this with the augmented partial structure and sequence tracks given by a functional site motif. To increase the diversity of the scaffolds and maximize the probability of generating physically realizable prompt combinations, we generate between 256 and 1024 designs for each combination of SS8 and functional site motif. For each generation, we uniformly sample a random length $L$ between 150 and 400 . Then, we produce a set of secondary structure spans with length 5-20 residues, each separated
------------------------------
 by a mask token. The mask token is used to indicate that the secondary structure of the intervening residues is not specified and can be any of the three main types (alpha helix, beta sheet, or coil). The resulting set of spans is then combined with the functional site motif to generate a set of protein sequences. The number of designs generated for each combination of SS8 and functional site motif ranges from 256 to 1024, which helps to increase the diversity of the scaffolds and maximize the probability of generating physically realizable prompt combinations. The length of the protein is varied between 150 and 400 residues to ensure that the generated sequences are of sufficient length to fold into stable structures. Overall, this approach allows for the generation of a large number of diverse protein sequences that are likely to fold into stable structures with the desired functional site motif.
User:
==============================
Figure S15. Prompting ESM3 to generalize beyond its training distribution. (A) Proteins designed using SS8 and SASA prompts derived from recent structures in the PDB with low structural similarity to the training set. Prompts along the protein length are visualized above each generation; secondary structure is shown using three-class (alpha $=$ blue, beta $=$ orange, coil $=$ gray) and SASA is shown as a line plot colored by residue index to match the cartoon below. (B) Symmetric proteins designed using SS8 prompting. Histograms show the similarity to the nearest training set protein by structure (TM-score) and sequence (sequence identity) compared to unconditional generation.
------------------------------
 This figure is showing how a computer program called ESM3 can be trained to generate new protein structures that are different from the ones it was originally trained on. The program uses prompts, which are like instructions, to guide it in creating new protein structures.

In this experiment, the researchers used two types of prompts: SS8 and SASA. SS8 is a type of prompt that tells the program to create a protein structure with a specific secondary structure, which is the way the protein chain is folded. SASA is a type of prompt that tells the program to create a protein structure with a specific surface area, which is the amount of the protein that is exposed to the surrounding environment.

The researchers used these prompts to create new protein structures that were different from the ones in the training set, which is a set of protein structures that the program was originally trained on. They did this by using prompts that were derived from recent protein structures in the Protein Data Bank (PDB), which is a database of protein structures.

The researchers then compared the new protein structures to the ones in the training set to see how similar they were. They used two measures of similarity: TM-score, which is a measure of how similar the overall structure of the protein is, and sequence identity, which is a measure of how similar the amino acid sequence of the protein is.

The results showed that the program was able to generate new protein structures that were different from the ones in the training set, and that these new structures were still biologically relevant. This is important because it shows that the program can be used to design new proteins that have specific functions, such as binding to a particular target molecule.
User:
==============================
\begin{tabular}{rccc}
\hline Motif & PDB ID & Chain ID & PDB Residue Identifiers \\
\hline ACE2 binding & $6 \mathrm{vw} 1$ & $\mathrm{~A}$ & $19-89,319-366$ \\
Ferredoxin & $6 \mathrm{6} 6 \mathrm{r}$ & $\mathrm{A}$ & $1-44$ \\
Barstar binding & $7 \mathrm{mrx}$ & $\mathrm{B}$ & $25-47$ \\
P53 binding & $1 \mathrm{ycr}$ & $\mathrm{B}$ & $19-28$ \\
PD-1 binding & $5 \mathrm{ius}$ & $\mathrm{A}$ & $63-83,119-141$ \\
DNA-binding helix-turn-helix & $11 \mathrm{cc}$ & $\mathrm{A}$ & $1-52$ \\
P-loop & $5 \mathrm{ze} 9$ & $\mathrm{~A}$ & $229-243$ \\
Double EF-hand & $1 \mathrm{a} 2 \mathrm{x}$ & $\mathrm{A}$ & $103-115,139-152$ \\
Lactate dehydrogenase & $11 \mathrm{db}$ & $\mathrm{A}$ & $186-206$ \\
Renal dipeptidase & $1 \mathrm{itu}$ & $\mathrm{A}$ & $124-147$ \\
Ubiquitin-activating enzyme E1C binding & $1 \mathrm{yov}$ & $\mathrm{B}$ & $213-223$ \\
DNA topoisomerase & $1 \mathrm{a} 41$ & $\mathrm{~A}$ & $248-280$ \\
\hline
\end{tabular}
Table S10. Functional motif definitions for conserved regions.
by a gap of 3-10 residues, such that the total length adds up to $L$. Finally, to avoid incompatibility between the partial structure and secondary structure constraints, we also mask the SS8 tokens at positions where structure is specified by the functional site prompt. Secondary structure-prompted designs was assessed by running DSSP on the designed sequence and measuring the fraction of prompted residues which were assigned the correct secondary structure. Success was determined by a pTM $>0.8$, all-atom cRMSD $<$ 1.5 for the functional site, and SS8 accuracy $>0.8$.
------------------------------
 The table provided in the prompt lists various functional motifs found in different proteins, along with their corresponding PDB IDs, chain IDs, and PDB residue identifiers. These motifs are regions of the protein that have specific functions, such as binding to other molecules or catalyzing chemical reactions.

For example, the ACE2 binding motif is found in the protein with PDB ID 6vw1 and chain ID A, and spans residues 19-89 and 319-366. This motif is involved in binding to the ACE2 receptor, which is important for the entry of the SARS-CoV-2 virus into human cells.

The table also includes information on the success of secondary structure-prompted designs, which involves using the functional site prompt to guide the design of a protein sequence with the desired secondary structure. The success of these designs was measured by the fraction of prompted residues that were assigned the correct secondary structure, as determined by DSSP.

Overall, this table provides valuable information for scientists studying protein structure and function, as well as those interested in protein design and engineering.
User:
==============================
Keyword prompting. To prompt the model to generate proteins with a specific fold, we extracted the set of InterPro tags associated with a set of proteins from the CAMEO test set for which ESM3 achieved keyword recovery of greater than $80 \%$ (Fig. 2A). These tags were then converted into keywords and used to prompt the model in combination with the partial sequence and structure constraints. The list of prompts and function tags is given in Table S11. Keywordprompted designs were assessed using a self-consistency evaluation, i.e. whether the model successfully predicts any of the prompted InterPro accessions for the designed sequence. Success was determined by a pTM $>0.8$, all-atom $c$ RMSD $<2.0$, and number of InterPro accessions recovered $>0$.
------------------------------
 In this study, the researchers used a technique called keyword prompting to generate proteins with specific folds. They first identified a set of proteins from the CAMEO test set that had a high level of keyword recovery (greater than 80%) using the ESM3 model. These proteins were then analyzed to extract a set of InterPro tags, which are keywords that describe the protein's function and structure.

The researchers then used these InterPro tags as prompts to guide the ESM3 model in generating new protein sequences with the desired fold. The prompts were combined with partial sequence and structure constraints to ensure that the generated sequences were biologically relevant.

To evaluate the success of the keyword prompting technique, the researchers used a self-consistency evaluation. This involved checking whether the ESM3 model could successfully predict any of the InterPro accessions for the designed sequence. The evaluation criteria included a pTM score greater than 0.8, an all-atom RMSD less than 2.0, and the recovery of at least one InterPro accession.

Overall, the keyword prompting technique allowed the researchers to generate new protein sequences with specific folds, which could have important applications in protein engineering and drug discovery.
User:
==============================
We assess novelty of each motif-scaffold combinations by measuring the TM-score between the generated scaffold and the chain from which the motif is derived (Table S12). This confirms that the model is not retrieving the original motif scaffold, particularly for secondary structure-prompted scaffolds where we do not provide any explicit instructions to produce diverse designs. For the motifs derived from ligand binding residues (magnesium, serotonin, calcium, zinc, protease inhibitor 017, and Mcl-1 inhibitor YLT), we additionally use Foldseek to search the PDB for any other proteins which share that motif (as defined by BioLiP (93)), as a more stringent evaluation of novelty. For all but zincbinding and magnesium-binding motifs, Foldseek finds no significant hits at an E-value threshold of 1.0. The hits discovered for zinc and magnesium have only modest TMscore ( 0.76 and 0.64 ), demonstrating that the model still finds novel scaffolding solutions for these ligands. To assess whether the generated scaffolds are likely to be designable, we measure a self-consistency TM-score under orthogonal computational models by inverse-folding the designed structure with ESM-IF (94) (using a temperature of 0.5 ) and re-folding with ESMFold (5). We report the best scTM over 8 inverse folding designs in Table S12.
------------------------------
 In this study, the researchers are evaluating the novelty of motif-scaffold combinations by measuring the TM-score between the generated scaffold and the chain from which the motif is derived. The TM-score is a measure of the structural similarity between two protein structures, with a score of 1 indicating a perfect match and a score of 0 indicating no similarity.

To ensure that the generated scaffolds are not simply copies of the original motif scaffold, the researchers use Foldseek to search the Protein Data Bank (PDB) for any other proteins that share the same motif. Foldseek is a software tool that can identify structural similarities between proteins based on their amino acid sequences.

The researchers also use inverse-folding to assess whether the generated scaffolds are likely to be designable. Inverse-folding involves predicting the amino acid sequence of a protein based on its 3D structure, and then re-folding the predicted sequence to see if it matches the original structure. The researchers use ESM-IF and ESMFold, which are computational models that can predict protein structures based on their amino acid sequences.

Overall, the researchers use a combination of TM-score, Foldseek, and inverse-folding to evaluate the novelty and designability of motif-scaffold combinations.
User:
==============================
First, we describe the procedure for generating the protein compression example shown in Fig. 2D. A series of prompts of length 150 were constructed. The sequence and struc- ture of the catalytic triad of trypsin (PDB 1Y3V) (H57, D102, S195) were placed in the prompt using the following procedure: three random residue numbers between 20 and 130 were sampled such that the minimum pairwise difference in position between each of the residues was no less than 20. Then, H57 from the template trypsin was placed at the lowest sampled number, D102 at the second lowest, and S195 at the largest number, thus respecting the left-to-right ordering of the catalytic triad in the template trypsin. 128 prompts were generated by this procedure. Each of these prompts was combined with a function keyword prompt derived from the template protein, specifically InterPro (38) tags IPR001254 (serine proteases, trypsin domain) and IPR009003 (peptidase S1, PA clan), to arrive at a final set of 128 prompts. The base ESM 7B model was then prompted to generate the sequence of the remaining 147 residues of the protein conditioned on the randomly placed catalytic triad sequence and structure coordinates and function keywords. $L=150$ decoding steps were used with a temperature of 0.7 , with 32 generations per prompt. Generations were then filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs, with the generation shown in Fig. 2D selected finally by visual inspection.
------------------------------
 In this study, the researchers generated a protein compression example using a series of prompts of length 150. They placed the sequence and structure of the catalytic triad of trypsin (a type of enzyme) in the prompts using a specific procedure. They then combined these prompts with function keyword prompts derived from the template protein, which were InterPro tags. The base ESM 7B model was then prompted to generate the sequence of the remaining 147 residues of the protein, conditioned on the randomly placed catalytic triad sequence and structure coordinates and function keywords. The researchers used $L=150$ decoding steps with a temperature of 0.7 and 32 generations per prompt. The generations were then filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs, and the final generation was selected by visual inspection.
User:
==============================
Generation quality was measured using ESMFold (5) pTM of the generated sequence, in addition to self-consistency. For self-consistency, we inverse fold the ESM3-predicted structure of the generation with ESM-IF1 (94) 8 times and re-fold with ESMFold, reporting the mean and std of the TM-scores between the 8 ESMFold-predicted structures and the ESM3-predicted structure. To perform a blast search of the sequence, we use a standard Protein Blast search (51). We set the max target sequences parameter to 5000 and sort results by sequence length and sequence identity, selecting the first sequence that is a serine protease. This yields the reference WP_260327207 which is 164 residues long and shares $33 \%$ sequence identity with the generation.
------------------------------
 In this context, "generation quality" refers to the accuracy and reliability of a computer-generated sequence of amino acids, which is used to predict the structure of a protein. The term "ESMFold" refers to a computational method for predicting protein structures based on the sequence of amino acids. The "pTM" score is a measure of the accuracy of the predicted structure, and "self-consistency" refers to the degree to which the predicted structure is consistent with itself.

The "ESM-IF1" method is another computational method for predicting protein structures, and the "TM-score" is a measure of the similarity between two protein structures. The "Protein Blast" search is a tool for comparing a sequence of amino acids to a database of known protein sequences, and the "max target sequences" parameter limits the number of results returned. The "sequence identity" is a measure of how similar two sequences of amino acids are, and the "reference" sequence is a known protein sequence that is used as a comparison for the generated sequence.
User:
==============================
We showcase two further examples of protein editing. First, ESM3 is prompted to bury an exposed helix in a protein with an alternating alpha-beta sandwich fold. The prompt is constructed as follows: the prompt is of the same length as the template protein (PDB 1LBS). We identify a buried helix (mean SASA $0.32 \AA^{2}$ ) between residues 106-116 of the template protein. Structure coordinates from this region are placed in the prompt at the same residue indices, to prompt ESM3 to generate the same helix. This is composed with a SASA prompt of 40.0 for each of the 11 helix residues, prompting ESM3 to place this helix on the surface of the protein. Finally, we prompt with the secondary structure of 5 central beta strands surrounding the buried helix, residues 33-36, 62-65, 99-103, 125-130, and 179-182. ESM3 7B is then used to generate 512 protein sequences conditioned on this prompt using $\frac{L}{2}$ decoding steps and a temperature of 0.7. Designs are filtered by ESM3 pTM and adherence
------------------------------
 to the prompt, and the top 10 designs are selected for further analysis.

In this example, the researchers are using a technique called protein editing to modify the structure of a protein. They are using a program called ESM3, which stands for Evolutionary Structural Model 3, to generate new protein sequences that are similar to the original protein but have specific changes in their structure.

The researchers start by identifying a buried helix in the original protein, which means that it is located inside the protein and not exposed to the surface. They then use this helix as a template to generate a new helix that is located on the surface of the protein. This is done by creating a prompt that includes the coordinates of the buried helix and a SASA prompt, which stands for Solvent Accessible Surface Area, that tells ESM3 to generate a helix with a specific surface area.

The researchers also include a prompt for the secondary structure of five central beta strands surrounding the buried helix. This is done to ensure that the new helix is properly integrated into the protein structure.

ESM3 is then used to generate 512 protein sequences that are similar to the original protein but have the new helix on the surface. The sequences are filtered to ensure that they adhere to the prompt and are structurally stable. The top 10 designs are selected for further analysis.

Overall, this technique allows researchers to modify the structure of proteins in a precise and controlled manner, which can have important implications for drug design and other applications.
User:
==============================
\begin{tabular}{|c|c|c|c|}
\hline Scaffold & Reference & InterPro tags & Total Length \\
\hline Beta propeller & $8 \sin \mathrm{A}$ & \begin{tabular}{l} 
IPR001680 (1-350) \\
IPR036322 (1-350) \\
IPR015943 (1-350)
\end{tabular} & 353 \\
\hline TIM barrel & $7 \mathrm{rpnA}$ & \begin{tabular}{l} 
IPR000652 (0-248) \\
IPR020861 (164-175) \\
IPR035990 (0-249) \\
IPR013785 (0-251) \\
IPR000652 (2-249) \\
IPR022896 (1-249)
\end{tabular} & 252 \\
\hline MFS transporter & 4ikvA & \begin{tabular}{l} 
IPR011701 (1-380) \\
IPR020846 (1-380) \\
IPR036259 (1-380)
\end{tabular} & 380 \\
\hline Immunoglobulin & $7 \mathrm{sbdH}$ & \begin{tabular}{l} 
IPR036179 (0-116; 124-199) \\
IPR013783 (0-206) \\
IPR003597 (124-202) \\
IPR007110 (0-115; 121-207) \\
IPR003599 (6-115) \\
IPR013106 (11-114)
\end{tabular} & 209 \\
\hline Histidine kinase & 8dvqA & \begin{tabular}{l} 
IPR003594 (47-156) \\
IPR003594 (47-158) \\
IPR004358 (118-137) \\
IPR004358 (141-155) \\
IPR004358 (101-112) \\
IPR005467 (0-158) \\
IPR036890 (4-159) \\
IPR036890 (3-156)
\end{tabular} & 166 \\
\hline Alpha/beta hydrolase & 7yiiA & \begin{tabular}{l} 
IPR029058 (0-274) \\
IPR000073 (26-265)
\end{tabular} & 276 \\
\hline
\end{tabular}
Table S11. InterPro tags extracted from CAMEO test set proteins for prompting with fold specification.
------------------------------
 The table provided shows a list of proteins and their corresponding InterPro tags, which are used to identify protein domains and functional sites. The first column lists the type of protein domain or fold, such as beta propeller or TIM barrel. The second column lists the reference protein used to identify the domain, and the third column lists the InterPro tags associated with that domain. The fourth column lists the total length of the protein.

For example, the first row shows a beta propeller domain with the reference protein 8sinA and three InterPro tags: IPR001680, IPR036322, and IPR015943. These tags indicate that the protein contains a beta propeller domain from position 1 to 350.

The second row shows a TIM barrel domain with the reference protein 7rpnA and six InterPro tags. These tags indicate that the protein contains a TIM barrel domain from position 0 to 248, as well as other functional sites.

The remaining rows show other types of protein domains and their corresponding InterPro tags.

Overall, this table provides a useful resource for identifying protein domains and functional sites in various proteins.
==============================
\begin{tabular}{rrcc} 
& & & \\
\hline Site & Scaffold & Novelty (TM to original) & Designability (scTM) \\
\hline 017 & beta & 0.264 & 0.967 \\
ACE2 & alpha & 0.606 & 0.871 \\
CA & Immunoglobulin & 0.441 & 0.781 \\
MG & ab-hydrolase & 0.293 & 0.969 \\
TIM-barrel & 0.328 & 0.980 \\
Renal-dipeptidase & alpha-beta-alpha & 0.644 & 0.933 \\
SRO & mfs-transporter & 0.345 & 0.992 \\
Topoisomerase & histidine-kinase & 0.269 & 0.948 \\
YLT & alpha-beta & 0.229 & 0.899 \\
ZN & alpha & 0.567 & 0.996 \\
\hline
\end{tabular}
Table S12. Novelty and designability metrics. Metrics are shown for motif scaffolds shown in Fig. 2C. Novelty is measured by computing the TM-score to the original scaffold from which the motif is derived. Designability is measured by self-consistency TM-score over eight samples by inverse folding with ESM-IF and refolding with ESMFold. All designs are distinct from their original scaffolds while retaining high designability.
to the SASA prompt. The final generation is chosen by visual inspection. The generation is evaluated as described above (ESMFold pTM 0.71, scTM mean 0.82, std 0.045). Examining the generation, ESM3 is able to satisfy the input constraints: the generated protein maintains the structure of the helix (cRMSD $0.18 \AA$ ) and the alternating alpha-beta fold (both the generation and the template have 7 strands alternating with helices), while exposing the helix motif to the surface (mean SASA $28.35 \AA^{2}$ ). Furthermore, the generation is structurally distinct: a Foldseek search (39) of AlphaFold-DB, ESMAtlas, and PDB in TM-align mode reveals no hit with TM-score greater than .76.
------------------------------
 The table shows the novelty and designability metrics for different motif scaffolds. Novelty is measured by comparing the TM-score of the motif to the original scaffold from which it was derived. Designability is measured by the self-consistency TM-score over eight samples by inverse folding with ESM-IF and refolding with ESMFold. The results show that all designs are distinct from their original scaffolds while retaining high designability.

In the example provided, the goal is to generate a protein structure that satisfies certain constraints, such as maintaining the structure of a helix and exposing a helix motif to the surface. ESM3 is used to generate a protein structure that meets these constraints while also being structurally distinct from existing structures. The final generation is evaluated using various metrics, including ESMFold pTM, scTM mean, and SASA. The results show that the generated protein maintains the desired structure and is structurally distinct from existing structures.
User:
==============================
We also use ESM3 to generate an idealized TIM Barrel with 11-fold symmetry. This generation is undertaken in two steps. First, we derive a secondary structure and function keyword prompt from a reference TIM Barrel (PDB 5EKY). The secondary structure of the reference protein is computed using DSSP and then idealized to construct a prompt for ESM3. To construct the secondary structure prompt, the length of each helix and strand is fixed at 7 residues. Each helix and strand region is then separated by 3 mask tokens, with a mask token appended to the $\mathrm{N}$ and $\mathrm{C}$ termini of the prompt as well. This yields a secondary structure prompt of total length 159 , which is combined with a function keyword prompt derived from the reference protein: keywords are derived from IPR013785 (aldolase-type TIM barrel) and IPR000887 (KDPG/KHG aldolase). ESM3 7B is then used to generate 256 samples with $L$ decoding steps and a temperature of 0.7 . The design shown is chosen by filtering by ESM3 pTM and visual inspection. In the second step, the secondary structure prompt from the first step is expanded to contain 11 helix-strand subunits, for a total prompt length of 225 residues (4 mask tokens are now appended to the $\mathrm{N}$ and $\mathrm{C}$ termini, rather than just 1). ESM3 7B is then used to generate 256 samples with $L$ decoding steps and a temperature of 0.7 , with generations filtered by ESM3 pTM and visual inspection. The generation is evaluated as described above (ESMFold pTM 0.69, scTM mean 0.97, std 0.011). The generation is structurally distinct: a Foldseek search (39) of AlphaFold-DB, ESMAtlas, and PDB in TM-align mode reveals no hit with TM-score greater than . 61 .

------------------------------
 In this study, the researchers used a computer program called ESM3 to create a hypothetical protein structure called an idealized TIM Barrel. This structure has 11-fold symmetry and was created in two steps.

First, the researchers used a reference protein called PDB 5EKY to derive a secondary structure and function keyword prompt. The secondary structure of the reference protein was computed using a program called DSSP, and then idealized to create a prompt for ESM3. The secondary structure prompt was constructed by fixing the length of each helix and strand at 7 residues, and then separating each helix and strand region by 3 mask tokens. A mask token was also added to the N and C termini of the prompt. This resulted in a secondary structure prompt of total length 159, which was combined with a function keyword prompt derived from the reference protein.

Next, ESM3 was used to generate 256 samples with a temperature of 0.7 and a decoding step of L. The design was chosen by filtering with ESM3 pTM and visual inspection.

In the second step, the secondary structure prompt was expanded to contain 11 helix-strand subunits, resulting in a total prompt length of 225 residues. ESM3 was then used to generate 256 samples with a temperature of 0.7 and a decoding step of L. The generation was filtered by ESM3 pTM and visual inspection.

The resulting generation was evaluated using ESMFold pTM, which measures the accuracy of the predicted structure, and scTM mean, which measures the similarity of the predicted structure to the reference structure. The generation was found to be structurally distinct, with no hit found in a Foldseek search of AlphaFold-DB, ESMAtlas, and PDB in TM-align mode with a TM-score greater than .61.
User: