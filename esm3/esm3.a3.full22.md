
==============================
ESM3 is both a generative model and a representation learning model that can be adapted for predictive tasks. In this section, we present benchmarking results for both capabilities.
------------------------------
 Hello and welcome to this video where we will be discussing the ESM3 model and its capabilities. ESM3 is a generative model and a representation learning model that can be adapted for predictive tasks. In this section, we will be presenting benchmarking results for both capabilities.

First, let's define what a generative model is. A generative model is a type of machine learning model that is used to generate new data based on the patterns and information it has learned from the training data. In the case of ESM3, it can generate new data that is similar to the training data it has been trained on.

Next, let's define what a representation learning model is. A representation learning model is a type of machine learning model that is used to learn a representation of the input data that can be used for other tasks. In the case of ESM3, it can learn a representation of the input data that can be used for predictive tasks.

Now, let's discuss the benchmarking results for ESM3. The benchmarking results show that ESM3 is a highly effective model for both generative and representation learning tasks. It has been shown to outperform other models in terms of accuracy and efficiency.

In conclusion, ESM3 is a highly effective model for both generative and representation learning tasks. Its ability to generate new data and learn a representation of the input data makes it a valuable tool for predictive tasks. Thank you for watching and we hope this video has been helpful in explaining the capabilities of ESM3.
==============================
ESM3 models are trained at three scales-1.4B, 7B, and 98B parameters-on approximately 75B, 560B, and 1.8T training tokens, respectively.
------------------------------
 Hello and welcome to this video where we will be discussing the ESM3 models and their training parameters.

ESM3 stands for Evolved Structural Mechanism 3, which is a type of protein structure prediction model. These models are trained at three different scales, which are 1.4B, 7B, and 98B parameters.

The number of parameters refers to the complexity of the model and the amount of data it can process. The higher the number of parameters, the more complex the model and the more data it can handle.

The training tokens refer to the amount of data used to train the model. The ESM3 models are trained on approximately 75B, 560B, and 1.8T training tokens, respectively.

Training tokens are essentially the amount of data that the model is exposed to during the training process. The more training tokens, the more data the model has to learn from, which can lead to better performance.

In summary, the ESM3 models are a type of protein structure prediction model that are trained at three different scales with varying numbers of parameters and training tokens. These models are used to predict the structure of proteins, which is important for understanding their function and developing new drugs and treatments.

Thank you for watching and we hope this explanation has been helpful. If you have any further questions, please feel free to leave them in the comments below.
==============================
The ESM3 1.4B model, trained on 75B tokens and noted for its small size and speed, allows rapid iteration both during training and at inference. Optimal model size and number of training tokens are studied by extrapolating from a series of smaller runs, given a training compute budget, model architecture, and dataset characteristics $(19,21)$. After determining compute optimality for training, a variety of factors such as release frequency, amount of inference, ease of use, and usage patterns are also taken into account to determine the ideal number of tokens on which to train the model. To enable efficient inference for the benefit of the research community, we have trained two additional versions of ESM3 1.4B, named 1.4B Overtrained and 1.4B Open, which are trained on 300B tokens, far beyond their compute optimality for training.
------------------------------
 Hello and welcome to this video where we will be discussing the ESM3 1.4B model. This model is known for its small size and speed, making it ideal for rapid iteration during both training and inference.

To determine the optimal model size and number of training tokens, a series of smaller runs were conducted, taking into account the training compute budget, model architecture, and dataset characteristics. This allowed for the extrapolation of the ideal model size and number of training tokens.

However, there are other factors to consider when determining the ideal number of tokens on which to train the model. These include release frequency, amount of inference, ease of use, and usage patterns.

To further benefit the research community, two additional versions of ESM3 1.4B were trained. The first, named 1.4B Overtrained, was trained on 300B tokens, far beyond its compute optimality for training. The second, named 1.4B Open, was also trained on 300B tokens and is available for public use.

In summary, the ESM3 1.4B model is a small and fast model that allows for rapid iteration during both training and inference. Its optimal model size and number of training tokens were determined through a series of smaller runs, and additional versions were trained to benefit the research community.
User:
==============================
In the following benchmarks for this section, unless otherwise noted, models are evaluated on a test set of 902 proteins whose structures are temporarily held out from the ESM3 training set. The proteins were sourced from the Continuous Automated Model EvaluatiOn (CAMEO) targets released from May 1, 2020 through Aug 1, 2023 (86).
------------------------------
 Hello and welcome to this video where we will be discussing the benchmarks used in the evaluation of models in the field of protein structure prediction.

In this section, the models are evaluated on a test set of 902 proteins whose structures are temporarily held out from the ESM3 training set. The proteins were sourced from the Continuous Automated Model EvaluatiOn (CAMEO) targets released from May 1, 2020 through Aug 1, 2023 (86).

Let's break down some of the terms used in this statement.

First, protein structure prediction refers to the process of predicting the three-dimensional structure of a protein from its amino acid sequence. This is an important task in the field of structural biology as the structure of a protein is closely related to its function.

The ESM3 training set refers to a dataset of protein structures that are used to train the models being evaluated. The ESM3 stands for the Evolutionary Scale Modeling 3, which is a method for predicting protein structures using deep learning.

The test set of 902 proteins is a separate dataset of protein structures that are used to evaluate the performance of the models. These proteins are not used in the training process and are therefore considered to be "held out" from the training set.

The CAMEO targets are a set of protein structures that are released on a regular basis for use in benchmarking protein structure prediction methods. The CAMEO stands for Continuous Automated Model EvaluatiOn and is a project that aims to provide a standardized set of protein structures for use in benchmarking.

Finally, the dates May 1, 2020 through Aug 1, 2023 (86) refer to the time period during which the CAMEO targets were released. The number 86 is a reference to the number of the CAMEO release that was used in this evaluation.

In summary, the benchmarks used in this evaluation involve testing the performance of protein structure prediction models on a separate dataset of protein structures that were not used in the training process. The protein structures used in this evaluation were sourced from the CAMEO targets and were released during a specific time period.
User:
==============================
For contact and structure prediction evaluations, we also evaluate on the CASP14 (71 proteins) and CASP15 (70 proteins) structure prediction benchmarks $(87,88)$. The CASP14 and CASP15 sets are obtained directly from the organizers.
------------------------------
 Hello and welcome to this video where we will be discussing the use of CASP14 and CASP15 structure prediction benchmarks for contact and structure prediction evaluations.

First, let's define some terms that may not be obvious to those not specializing in this field. CASP stands for Critical Assessment of Protein Structure Prediction, which is a biennial competition that aims to assess the state-of-the-art in protein structure prediction. The competition provides a set of protein sequences for which the structures are not yet known, and participants are challenged to predict the structures using computational methods.

The CASP14 and CASP15 sets are two of the most recent sets of protein sequences used in the competition. The CASP14 set contains 71 protein sequences, while the CASP15 set contains 70 protein sequences. These sets were obtained directly from the organizers of the competition.

Now, let's discuss how these sets are used for contact and structure prediction evaluations. Contact prediction refers to the prediction of which amino acid residues in a protein sequence are in contact with each other in the folded protein structure. Structure prediction, on the other hand, refers to the prediction of the three-dimensional structure of a protein from its amino acid sequence.

To evaluate the performance of contact and structure prediction methods, researchers often use the CASP14 and CASP15 sets as benchmarks. This involves comparing the predicted contacts and structures to the actual structures determined experimentally. The performance of a method is then measured using various metrics, such as the accuracy of the predicted contacts or the similarity of the predicted structure to the actual structure.

In summary, the CASP14 and CASP15 sets are important benchmarks for evaluating contact and structure prediction methods in protein structure prediction. By using these sets, researchers can compare the performance of different methods and identify areas for improvement. Thank you for watching!###
==============================
The contact prediction model is a multilayer perceptron (MLP) head that operates independently over the representations of each amino acid pair, outputting the probability
of contact between them. We use LoRA (89) for finetuning, which is a common alternative to full weight finetuning that uses much less memory while attaining strong performance. LoRA is applied to the base model for finetuning, and the MLP along with the LoRA weights are trained end-to-end using the cross-entropy loss with respect to the ground truth contact prediction map. For the ground truth, all residues at least 6 positions apart in the sequence and within an $8 \AA$ $\mathrm{C} \alpha$ - $\mathrm{C} \alpha$ distance are labeled as a contact. All models are trained with LoRA rank 4, batch size 64 and a learning rate of $1 \mathrm{e}-3$ for $10 \mathrm{k}$ steps on a mix of sequence and structure data from PDB, AlphaFold-DB, ESMAtlas, and OAS Predicted Structures. Data are sampled in a ratio of 1:3:3:0.03 from these datasets.
------------------------------
 Hello and welcome to this video where we will be discussing the contact prediction model used in protein structure prediction.

The contact prediction model is a type of neural network called a multilayer perceptron, or MLP for short. This model operates independently over the representations of each amino acid pair, which means it analyzes the interactions between each pair of amino acids in a protein.

The output of the MLP is the probability of contact between each amino acid pair. This is important because knowing which amino acids are in contact with each other can help us predict the overall structure of the protein.

To fine-tune the MLP, we use a technique called LoRA, which stands for Low-Rank Adaptation. This is a common alternative to full weight finetuning that uses much less memory while still achieving strong performance.

LoRA is applied to the base model for finetuning, and the MLP along with the LoRA weights are trained end-to-end using the cross-entropy loss with respect to the ground truth contact prediction map.

The ground truth is determined by labeling all residues at least 6 positions apart in the sequence and within an $8 \AA$ $\mathrm{C} \alpha$ - $\mathrm{C} \alpha$ distance as a contact.

All models are trained with LoRA rank 4, batch size 64, and a learning rate of $1 \mathrm{e}-3$ for $10 \mathrm{k}$ steps on a mix of sequence and structure data from PDB, AlphaFold-DB, ESMAtlas, and OAS Predicted Structures.

The data are sampled in a ratio of 1:3:3:0.03 from these datasets.

I hope this explanation has been helpful in understanding the contact prediction model used in protein structure prediction. Thank you for watching!
User:
==============================
Table S7 shows the performance on each structural test set through the metric of precision at $\mathrm{L}(\mathrm{P} @ \mathrm{~L})$, which evaluates the precision of the top- $\mathrm{L}$ most confident predictions, where $\mathrm{L}$ is the length of the protein. The smallest ESM3 model, with 1.4B parameters, achieves a $\mathrm{P} @ \mathrm{~L}$ of $0.76 \pm 0.02$ on the CAMEO test set, which is higher than the $3 \mathrm{~B}$ parameter ESM2 model $(0.75 \pm 0.02)$. Furthermore, it trains on an order of magnitude less compute during pre-training ( $6.72 \times$ $10^{20}$ FLOPS vs. $1.8 \times 10^{22}$ FLOPS), demonstrating the benefits of multimodal pre-training.
------------------------------
 Hello and welcome to this video where we will be discussing the performance of the ESM3 model on various structural test sets.

First, let's define some terms that may not be obvious to those not specializing in this field. The ESM3 model is a type of protein structure prediction model that uses a deep neural network to predict the 3D structure of proteins. The model is trained using a technique called multimodal pre-training, which involves training the model on a large amount of data from various sources, such as protein sequences and structures.

Now, let's talk about the metric used to evaluate the performance of the ESM3 model. The metric used is precision at $\mathrm{L}(\mathrm{P} @ \mathrm{~L})$, which evaluates the precision of the top- $\mathrm{L}$ most confident predictions. In other words, it measures how accurate the model is at predicting the correct 3D structure of a protein when given a set of possible structures.

The results of the evaluation show that the smallest ESM3 model, with 1.4B parameters, achieves a $\mathrm{P} @ \mathrm{~L}$ of $0.76 \pm 0.02$ on the CAMEO test set. This means that the model is able to accurately predict the 3D structure of proteins with a high degree of confidence.

Furthermore, the ESM3 model is able to achieve this level of performance while using significantly less compute during pre-training compared to the ESM2 model. The ESM3 model only requires $6.72 \times 10^{20}$ FLOPS during pre-training, while the ESM2 model requires $1.8 \times 10^{22}$ FLOPS. This demonstrates the benefits of multimodal pre-training in improving the efficiency and accuracy of protein structure prediction models.

In conclusion, the ESM3 model is a highly accurate and efficient protein structure prediction model that uses multimodal pre-training to achieve its performance. The results of the evaluation show that the model is able to accurately predict the 3D structure of proteins with a high degree of confidence, while using significantly less compute during pre-training compared to previous models.
User:
==============================
ESM3 can directly predict protein structures without additional finetuning by first predicting structure tokens, then decoding these tokens into coordinates. When predicting structure tokens, we follow the strategy outlined in Appendix A.1.10 and test both argmax decoding and full iterative decoding.
------------------------------
 Hello and welcome to this video where we will be discussing a recent development in the field of protein structure prediction. Specifically, we will be talking about ESM3, a new model that can directly predict protein structures without the need for additional fine-tuning.

To understand how ESM3 works, we first need to define a few key terms. The first is "structure tokens." These are essentially small building blocks that make up the overall structure of a protein. By predicting these tokens, we can then decode them into coordinates, which represent the 3D structure of the protein.

Now, let's talk about the two decoding strategies that were tested when predicting structure tokens. The first is "argmax decoding," which involves selecting the token with the highest predicted probability at each position in the protein sequence. The second is "full iterative decoding," which involves iteratively refining the predicted structure tokens until convergence.

So, how does ESM3 use these decoding strategies to predict protein structures? Well, it first predicts the structure tokens using a neural network model. Then, it decodes these tokens into coordinates using either argmax decoding or full iterative decoding. The resulting coordinates represent the predicted 3D structure of the protein.

Overall, ESM3 represents a significant advancement in the field of protein structure prediction, as it can directly predict structures without the need for additional fine-tuning. We hope this explanation has been helpful, and thank you for watching!###
==============================
For more difficult datasets, such as CASP14 and CASP15, iterative decoding has an outsized impact (see Table S8), whereas for easier datasets like CAMEO, argmax prediction is sufficient. On both the CAMEO and CASP15 datasets, argmax prediction for the 7B model is comparable to ESMFold, and iterative decoding with ESM3 98B closes the gap between ESMFold and Alphafold2. Structure prediction scaling curves as a function of training compute, are provided in Fig. S10
------------------------------
 Hello and welcome to this video where we will be discussing the impact of iterative decoding on difficult datasets such as CASP14 and CASP15. We will also be exploring the effectiveness of argmax prediction on easier datasets like CAMEO.

To begin, let's define some key terms. CASP stands for Critical Assessment of Protein Structure Prediction, which is a biennial competition that evaluates the accuracy of protein structure prediction methods. CASP14 and CASP15 refer to the 14th and 15th iterations of this competition, respectively.

Iterative decoding is a technique used in protein structure prediction that involves repeatedly refining the predicted structure until a satisfactory level of accuracy is achieved. This technique is particularly useful for difficult datasets where the protein structure is complex and challenging to predict.

Argmax prediction, on the other hand, is a simpler technique that involves selecting the most likely structure from a set of predicted structures. This technique is often sufficient for easier datasets where the protein structure is more straightforward.

Now, let's take a look at the results of our study. We found that on the CAMEO dataset, argmax prediction was sufficient for achieving high accuracy in protein structure prediction. However, on the more difficult CASP14 and CASP15 datasets, iterative decoding had a significant impact on improving the accuracy of the predictions.

Furthermore, we found that the 7B model, which is a type of protein structure prediction model, performed comparably to ESMFold, which is another popular protein structure prediction method, on both the CAMEO and CASP15 datasets. However, when we used iterative decoding with the ESM3 98B model, we were able to close the gap between ESMFold and Alphafold2, which is currently the most accurate protein structure prediction method available.

Finally, we also provided structure prediction scaling curves as a function of training compute in Fig. S10. These curves show how the accuracy of protein structure prediction methods improves as more computational resources are used for training.

In conclusion, iterative decoding is a powerful technique that can significantly improve the accuracy of protein structure prediction on difficult datasets. However, for easier datasets, argmax prediction may be sufficient. We hope this video has been helpful in explaining these concepts to you. Thank you for watching!###
==============================
The conditional likelihood of an output given a prompt serves as a proxy for the generative capabilities of a model. Fig. S11 and Table S9 evaluate the performance of ESM3 as a conditional generative model, using its negative log likelihood (NLL) on the test set. For each track - sequence, structure, function, SASA, and secondary structure - NLL is evaluated both unconditionally and conditioned on each of the other tracks.
------------------------------
 Hello and welcome to this video where we will be discussing the concept of conditional likelihood in the context of generative models.

First, let's define some terms. A generative model is a type of machine learning model that is capable of generating new data that is similar to the training data it was trained on. In other words, it can create new examples of the same type of data that it was trained on.

Now, let's talk about the conditional likelihood. The conditional likelihood is a measure of how likely a particular output is given a specific input or prompt. In the context of generative models, the conditional likelihood can be used as a proxy for the generative capabilities of the model.

To evaluate the performance of a generative model, we can use the negative log likelihood (NLL) on a test set. The NLL is a measure of how well the model can generate new data that is similar to the training data. The lower the NLL, the better the model is at generating new data.

In the specific example we are discussing, the ESM3 model is being evaluated as a conditional generative model. This means that the model is being evaluated on its ability to generate new data given a specific input or prompt. The performance of the model is being evaluated on five different tracks: sequence, structure, function, SASA, and secondary structure.

The NLL is being evaluated both unconditionally and conditioned on each of the other tracks. This means that the model is being evaluated on its ability to generate new data given a specific input or prompt, as well as its ability to generate new data given a specific input or prompt and the information from one or more of the other tracks.

In summary, the conditional likelihood is a measure of how likely a particular output is given a specific input or prompt. It can be used as a proxy for the generative capabilities of a model. The performance of a generative model can be evaluated using the negative log likelihood on a test set, and the ESM3 model is being evaluated as a conditional generative model on its ability to generate new data given a specific input or prompt.
User:
==============================
Unlike, for example, an autoregressive model, ESM3 is a generative model over masking patterns, so is trained to predict tokens given any masking pattern. The NLL of a sample under ESM3 is given by $\frac{1}{L!} \sum_{o \in \mathbb{O}} \frac{1}{L} \sum_{i=1}^{L} \log p\left(x_{o_{i}} \mid x_{o_{1}}, \ldots, x_{o_{i-1}}\right)$, where $O$ is the set of all decoding orders with normalization constant $Z=\frac{1}{L!}$. This computation is intractable (as the set of all decoding orders is exponential in length of a protein), but can be approximated by sampling a single decoding order $o$ for each $x$ in our dataset. At each step teacher forcing is used to replace the masked token with the ground truth token and report the mean NLL over the output tokens.
------------------------------
 Hello and welcome to this video where we will be discussing the ESM3 model and its use in predicting protein sequences.

First, let's define some terms that may not be obvious to those not specializing in this field.

Autoregressive models are a type of model that predicts the next element in a sequence based on the previous elements. In the context of protein sequences, this means that the model would predict the next amino acid based on the previous amino acids.

Generative models, on the other hand, are models that can generate new sequences from scratch. In the context of protein sequences, this means that the model can predict the entire sequence without needing to know the previous amino acids.

Masking patterns refer to the process of hiding certain parts of the sequence from the model. This is done to prevent the model from simply copying the input sequence and to force it to generate new sequences.

Now, let's discuss the ESM3 model. ESM3 is a generative model that is trained to predict protein sequences given any masking pattern. This means that it can generate new sequences from scratch without needing to know the previous amino acids.

The NLL, or negative log likelihood, is a measure of how well the model is able to predict the correct sequence. It is calculated by summing the log probabilities of each amino acid in the sequence.

The set of all decoding orders refers to all possible ways of revealing the masked parts of the sequence to the model. This set is exponential in length of the protein, which means that it is very large and computationally expensive to calculate.

To approximate this computation, we can sample a single decoding order for each sequence in our dataset. This allows us to calculate the NLL for each sequence and report the mean NLL over all output tokens.

Finally, teacher forcing is a technique where we replace the masked token with the ground truth token during training. This helps the model learn to predict the correct sequence more accurately.

In summary, the ESM3 model is a generative model that can predict protein sequences given any masking pattern. The NLL is a measure of how well the model is able to predict the correct sequence, and teacher forcing is a technique used to improve the accuracy of the model.
User:
==============================
There are many straightforward relationships in this data. For example, the unconditional NLL (Fig. S11, black lines) is always higher than conditional, and conditioning on full $3 \mathrm{D}$ structure reduces the loss on secondary structure prediction to nearly zero (1.4B: $0.24,7 \mathrm{~B}: 0.19,98 \mathrm{~B}: 0.16$ ).
------------------------------
 Hello and welcome to this video where we will be discussing the relationships in the data presented in the study.

Firstly, let's define some terms that may not be obvious to those who are not experts in this field. NLL stands for negative log-likelihood, which is a measure of how well a model fits the data. In this study, the NLL is used to evaluate the performance of the model in predicting protein structures.

The term "unconditional" refers to the model's performance without any additional information or constraints. In contrast, "conditional" refers to the model's performance when additional information or constraints are provided.

Now, let's look at the data presented in Figure S11. The black lines represent the unconditional NLL, which is always higher than the conditional NLL. This means that the model performs better when additional information or constraints are provided.

Furthermore, the study found that conditioning on full 3D structure reduces the loss on secondary structure prediction to nearly zero. This means that when the model is provided with the full 3D structure of the protein, it is able to accurately predict the secondary structure.

In summary, the data presented in this study shows that providing additional information or constraints to the model improves its performance in predicting protein structures.
User:
==============================
Other trends may be more surprising. Conditioning on sequence results in a lower structure prediction loss than conditioning on secondary structure (98B; sequence: 3.13 , secondary structure: 3.37). There are some diminishing returns to scale for the prediction of structure, function, SASA, and secondary structure. However, this diminishing is not observed for sequences, where we observe a clear loglinear relationship between pre-training FLOPS and NLL, regardless of conditioning.
------------------------------
 Hello and welcome to this video where we will be discussing a recent study on the use of pre-training in predicting protein structure.

First, let's define some terms that may not be obvious to those not specializing in this field. Pre-training refers to the process of training a model on a large dataset before fine-tuning it on a smaller, more specific dataset. In this study, the researchers used pre-training to improve the accuracy of predicting protein structure.

Next, let's talk about the different types of conditioning used in the study. Conditioning refers to the process of providing additional information to the model during training. In this study, the researchers compared the effectiveness of conditioning on sequence and secondary structure. Sequence refers to the order of amino acids in a protein, while secondary structure refers to the local three-dimensional structure of a protein.

The researchers found that conditioning on sequence resulted in a lower structure prediction loss than conditioning on secondary structure. This means that providing the model with information about the sequence of amino acids in a protein was more effective in predicting its structure than providing information about its secondary structure.

The researchers also observed diminishing returns to scale for the prediction of structure, function, SASA, and secondary structure. This means that as the amount of pre-training data increased, the improvement in prediction accuracy decreased. However, this was not observed for sequences, where the researchers observed a clear loglinear relationship between pre-training FLOPS and NLL, regardless of conditioning. FLOPS refers to the number of floating-point operations per second, while NLL refers to the negative log-likelihood, which is a measure of how well the model fits the data.

In summary, this study found that pre-training on sequence data was more effective in predicting protein structure than conditioning on secondary structure. Additionally, the researchers observed diminishing returns to scale for some prediction tasks, but not for sequences.

Thank you for watching, and we hope this video has been helpful in explaining this reference to experts.
User:
==============================
To assess the model's unconditional generation capability, we sampled 100 protein lengths randomly from the PDB and generated 1,024 sequences for each using ESM3 98B with a constant temperature of 0.7 . The sampled length distribution is shown in Fig. S13A. Structures for each sequence were predicted using ESM3 7B, and the distribution of pTM
------------------------------
 Hello and welcome to this video where we will be discussing the reference to experts on assessing the model's unconditional generation capability.

First, let's define some terms that may not be obvious to those not specializing in this field.

ESM3 stands for Evolutionary Scale Modeling 3, which is a deep learning model used for protein structure prediction.

PDB stands for Protein Data Bank, which is a database of protein structures.

TM stands for Transmembrane, which refers to the part of a protein that spans the cell membrane.

Now, let's dive into the reference.

To assess the model's unconditional generation capability, we sampled 100 protein lengths randomly from the PDB and generated 1,024 sequences for each using ESM3 98B with a constant temperature of 0.7.

This means that we took 100 protein structures from the PDB and used ESM3 98B to generate 1,024 sequences for each structure. The constant temperature of 0.7 refers to the temperature parameter used in the model, which controls the randomness of the generated sequences.

The sampled length distribution is shown in Fig. S13A.

This figure shows the distribution of protein lengths that were sampled from the PDB.

Structures for each sequence were predicted using ESM3 7B, and the distribution of pTM is shown in Fig. S13B.

This figure shows the distribution of predicted transmembrane regions for each generated sequence.

Overall, this reference demonstrates the ability of ESM3 to generate protein sequences with varying lengths and predict their transmembrane regions.

Thank you for watching and we hope this explanation was helpful.
User:
==============================
Figure S12. Distribution of $p T M$ and $p L D D T$. Measured on natural (left) and generated (right) sequences under ESM3 7B structure prediction. Generated sequences show a clearly lower correlation (Pearson $\mathrm{r} 0.79 \mathrm{vs}$. 0.85 ) as well as a mode of sequences with high pLDDT but low pTM. Natural sequences are from the test set (Appendix A.3.2), generations are unconditional generations from ESM3 98B.
and pLDDT are shown in Fig. S13B. ESM3 generates more high-quality structures than ESM2, which was trained using a simple MLM objective over sequence only with a fixed mask rate. Sequence similarity to the training set was computed using mmseqs2 (73) with the following parameters: --cov-mode 2 -c 0.8 -s 6.0. Proteins generated unconditionally are similar-but not identical-to proteins found in the training set (Fig. S15) and have high coverage of the training set (Fig. 1E), demonstrating that the model has properly fit the training distribution and does not exhibit mode collapse. We observe a cluster of generations with very high sequence identity to the training set; these correspond to antibody sequences, with the framework regions accounting for the high sequence identity.
------------------------------
 Hello and welcome to this video where we will be discussing the results of a study on the distribution of $p T M$ and $p L D D T$ in natural and generated sequences under ESM3 7B structure prediction.

First, let's define some terms. $p T M$ stands for predicted transmembrane helices, which are regions of a protein that span the cell membrane. $p L D D T$ stands for predicted local distance difference test, which is a measure of the accuracy of a predicted protein structure.

In this study, the researchers compared the distribution of $p T M$ and $p L D D T$ in natural sequences, which are sequences found in the test set, and generated sequences, which were created using ESM3 98B. ESM3 is a deep learning model that predicts protein structures.

The results showed that the generated sequences had a lower correlation with the natural sequences, as well as a mode of sequences with high $p L D D T$ but low $p T M$. This suggests that the generated sequences may not accurately represent the natural sequences.

The researchers also compared the performance of ESM3 to ESM2, which was trained using a different objective function. They found that ESM3 generated more high-quality structures than ESM2.

Finally, the researchers found that the generated sequences were similar but not identical to the sequences found in the training set, and that the model did not exhibit mode collapse, which is a common problem in deep learning models.

In summary, this study provides insights into the performance of ESM3 in predicting protein structures and highlights the importance of evaluating the accuracy of generated sequences. Thank you for watching!
User:
==============================
We use pTM for evaluating structure predictions from ESM3 instead of pLDDT. This is because pLDDT can be miscalibrated for generated structures and can overestimate the confidence of a prediction. pLDDT is biased towards local structural confidence, which can result in pathologies such as very long alpha helices with high pLDDT at all positions. pTM is a more global measure of structural confidence, and is more robust to these pathologies. Fig. S12 shows that $\mathrm{pTM}$ and pLDDT correlation drops for generated sequences $($ Pearson $\mathrm{r}$ : natural $=0.85$, generation $=0.79$ ), and a clear pattern of high pLDDT ( $>0.8$ ) but low pTM $(<0.6)$ emerges.
------------------------------
 Hello and welcome to this video where we will be discussing the use of pTM for evaluating structure predictions from ESM3.

First, let's define some terms. ESM3 stands for Evolutionary Scale Modeling 3, which is a computational method used to predict protein structures. pLDDT stands for predicted Local Distance Difference Test, which is a measure of the confidence of a prediction at each position in the protein structure.

Now, why do we use pTM instead of pLDDT? Well, it turns out that pLDDT can be miscalibrated for generated structures, which means that it can overestimate the confidence of a prediction. This is because pLDDT is biased towards local structural confidence, which can result in pathologies such as very long alpha helices with high pLDDT at all positions.

On the other hand, pTM is a more global measure of structural confidence, which means that it is more robust to these pathologies. In fact, Fig. S12 shows that the correlation between pTM and pLDDT drops for generated sequences, and a clear pattern of high pLDDT but low pTM emerges.

So, in summary, we use pTM instead of pLDDT because it is a more robust measure of structural confidence, especially for generated structures. Thank you for watching!###
==============================
To visualize the distribution of unconditional generations, we compute sequence embeddings by extracting the final layer outputs produced by running ESM3 7B with sequence inputs only. Protein-level embeddings are computed by averaging over all positions in the sequence to produce a 2560 -dim embedding. We then project these embeddings into two dimensions using a UMAP projection (90) fit on a background distribution of 50,000 randomly sampled sequences from UniProt with minimum distance 0.1 and number of neighbors 25 . Examples are selected by computing structural clusters with Foldseek-cluster (using default parameters) and sampling the example with highest ESM3 pTM from each cluster. A subset of these cluster representatives are shown in Fig. 1E.
------------------------------
 Hello and welcome to this video where we will be discussing how to visualize the distribution of unconditional generations using sequence embeddings.

First, let's define some terms that may not be obvious to those not specializing in this field. Sequence embeddings are a type of vector representation of a sequence of data, such as a protein sequence. These embeddings are created by running a model, in this case ESM3 7B, on the sequence data and extracting the final layer outputs.

Protein-level embeddings are a specific type of sequence embedding that are computed by averaging over all positions in the protein sequence to produce a 2560-dimensional embedding. This means that each protein sequence is represented by a 2560-dimensional vector.

Next, we use a UMAP projection to project these embeddings into two dimensions. UMAP stands for Uniform Manifold Approximation and Projection and is a type of dimensionality reduction technique that is useful for visualizing high-dimensional data in a low-dimensional space.

To create a background distribution of sequences, we randomly sample 50,000 sequences from UniProt with a minimum distance of 0.1 and 25 neighbors. This background distribution is used to fit the UMAP projection.

Finally, we use Foldseek-cluster to compute structural clusters and select examples by sampling the example with the highest ESM3 pTM from each cluster. ESM3 pTM stands for Evolutionary Scale Modeling 3 predicted transmembrane, which is a prediction of whether a protein sequence contains transmembrane domains.

In Fig. 1E, we show a subset of these cluster representatives. These are the protein sequences that have been selected as examples to visualize the distribution of unconditional generations.

I hope this explanation has been helpful in understanding how to visualize the distribution of unconditional generations using sequence embeddings. Thank you for watching!
User:
==============================
To assess whether ESM3 is biased towards particular secondary structures, we use DSSP to predict the three-class secondary structure of the high-confidence ( $\mathrm{pTM}>0.8$, mean $\mathrm{pLDDT}>0.8$ ) generations and measure the percentage of residues that form alpha helices and beta sheets. When compared to a background distribution computed over the PDB, we find that ESM3 closely matches the secondary structure distribution of known proteins (Fig. S13D), unlike other methods which preferentially generate helical structures $(14,23,25)$. Finally, to confirm that the structures predicted with high confidence by ESM3 are designable, we inverse folded and re-folded each using ESM3 7B. The ma- jority of generations successfully re-folded with TM-score of greater than 0.8 to the hallucinated structures, demonstrating that ESM3 has high self-consistency for its own high-confidence designs (Fig. S13C).
------------------------------
 Hello and welcome to this video where we will be discussing the use of ESM3 to predict protein structures. In this study, we wanted to assess whether ESM3 is biased towards particular secondary structures. To do this, we used DSSP to predict the three-class secondary structure of the high-confidence generations.

Now, let's break down some of the terms used in this study. First, what is DSSP? DSSP stands for Dictionary of Secondary Structure of Proteins and is a program used to predict the secondary structure of proteins. It assigns each amino acid in a protein to one of three categories: alpha helix, beta sheet, or coil.

Next, what is meant by high-confidence generations? In this study, high-confidence generations refer to the protein structures that were predicted by ESM3 with a high level of confidence. This was determined by two criteria: a pTM value greater than 0.8 and a mean pLDDT value greater than 0.8.

pTM stands for predicted TM-score and is a measure of how similar a predicted protein structure is to the true structure. A pTM value of 1 indicates a perfect match, while a value of 0 indicates a completely different structure.

pLDDT stands for predicted local distance difference test and is a measure of the accuracy of the predicted protein structure. A pLDDT value of 1 indicates a perfect match, while a value of 0 indicates a completely different structure.

Finally, what is meant by the background distribution computed over the PDB? The PDB stands for Protein Data Bank and is a database of protein structures. The background distribution refers to the distribution of secondary structures found in the PDB.

So, to summarize, we used DSSP to predict the secondary structure of high-confidence generations predicted by ESM3 and compared it to the background distribution computed over the PDB. We found that ESM3 closely matches the secondary structure distribution of known proteins, unlike other methods which preferentially generate helical structures.

We also confirmed that the structures predicted with high confidence by ESM3 are designable by inverse folding and re-folding each using ESM3 7B. The majority of generations successfully re-folded with a TM-score of greater than 0.8 to the hallucinated structures, demonstrating that ESM3 has high self-consistency for its own high-confidence designs.

Thank you for watching and we hope this video has helped you understand the use of ESM3 to predict protein structures.
User:
==============================
To explore alternative ways of generating proteins, we assess the quality of proteins generated by a chain-of-thought $(\mathrm{CoT})$ procedure in which ESM3 7B generates the secondary structure (SS8 tokens), then the 3-D backbone coordinates (structure tokens), followed by the amino acid sequence (sequence tokens) (Fig. S14). We compare the quality of amino acid sequences generated from this CoT procedure with the above method of unconditionally directly generating amino acid sequences. We find that the CoT procedure generates sequences that have higher confidence ESM3predicted structures than the directly-generated sequences as measured by pTM and mean pLDDT (Fig. S14A). Compared to high-confidence ( $\mathrm{pTM}>0.8$, mean $\mathrm{pLDDT}>0.8$ ) directly-generated sequences, the high-confidence subset of CoT-generated sequences are also more designable: the CoT-generated sequences have predicted structures whose inverse folded, then re-refolded structures have higher TMscore to the originally predicted structure (Fig. S14C). The CoT-generated sequences show a small bias towards higher alpha and beta proportion compared to those generated directly (Fig. S14D).
------------------------------
 Hello and welcome to this video where we will be discussing a recent study on alternative ways of generating proteins. In this study, the researchers used a chain-of-thought procedure, or CoT, to generate proteins. This procedure involves three steps: first, the ESM3 7B generates the secondary structure of the protein using SS8 tokens. Then, the 3-D backbone coordinates are generated using structure tokens. Finally, the amino acid sequence is generated using sequence tokens.

The researchers compared the quality of the amino acid sequences generated by the CoT procedure with those generated directly. They found that the CoT procedure generated sequences with higher confidence ESM3 predicted structures, as measured by pTM and mean pLDDT. This means that the CoT-generated sequences were more likely to have accurate predictions of their 3-D structure.

Additionally, the CoT-generated sequences were found to be more designable than the directly-generated sequences. This means that the predicted structures of the CoT-generated sequences were more likely to be stable and functional.

However, the CoT-generated sequences did show a small bias towards higher alpha and beta proportion compared to those generated directly. This means that the CoT procedure may be more likely to generate proteins with certain structural features.

Overall, this study provides insight into alternative ways of generating proteins and highlights the potential benefits of using a chain-of-thought procedure. Thank you for watching!
User:
==============================
To evaluate ESM's ability to follow prompts, we use a set of held-out proteins as described in Appendix A.3.2. The test set is further filtered to remove proteins with length greater than 1024, which removes 7 proteins from the test set. To construct prompts for the structure coordinate, secondary structure, and SASA tracks, we sample a random span of length $15 \%$ of the original protein length. The model is then shown the corresponding track for the randomly sampled span, and is tasked with generating the sequence for the entire protein. For example, for the structure track, for a protein of length 100 , we may sample a random span of 15 residues from residue $20-35$. The model would then have to generate a protein sequence of length 100 conditioned on structure coordinate conditioning from residues 20-35 derived from the original test protein. This same procedure is applied for the secondary structure and SASA tracks. For the function track, we form the prompt by tokenizing the keywords form the InterProScan annotations associated with each sequence. The ESM3 7B model is used for all generations with a temperature of 0.7 and $L$ decoding steps (where $L$ is the length of the sequence). The model generates 64 sequences per prompt, which we use to compute pass64.
------------------------------
 Hello and welcome to this video where we will be discussing the evaluation of ESM's ability to follow prompts. In order to do this, we will be using a set of held-out proteins as described in Appendix A.3.2.

The test set is further filtered to remove proteins with length greater than 1024, which removes 7 proteins from the test set. This is done to ensure that the evaluation is conducted on a manageable set of proteins.

To construct prompts for the structure coordinate, secondary structure, and SASA tracks, we sample a random span of length $15 \%$ of the original protein length. This means that for a protein of length 100, we may sample a random span of 15 residues from residue $20-35$.

The model is then shown the corresponding track for the randomly sampled span, and is tasked with generating the sequence for the entire protein. For example, for the structure track, the model would have to generate a protein sequence of length 100 conditioned on structure coordinate conditioning from residues 20-35 derived from the original test protein.

This same procedure is applied for the secondary structure and SASA tracks. For the function track, we form the prompt by tokenizing the keywords form the InterProScan annotations associated with each sequence.

The ESM3 7B model is used for all generations with a temperature of 0.7 and $L$ decoding steps (where $L$ is the length of the sequence). The model generates 64 sequences per prompt, which we use to compute pass64.

In summary, we have used a set of held-out proteins to evaluate ESM's ability to follow prompts. We have constructed prompts for the structure coordinate, secondary structure, and SASA tracks by sampling a random span of length $15 \%$ of the original protein length. The model is then tasked with generating the sequence for the entire protein. For the function track, we form the prompt by tokenizing the keywords form the InterProScan annotations associated with each sequence. The ESM3 7B model is used for all generations with a temperature of 0.7 and $L$ decoding steps. Finally, we compute pass64 based on the 64 sequences generated per prompt.
User:
==============================
To evaluate the generations, we use ESMFold to fold the sequences generated by ESM3. For the structure coordinate, secondary structure, and SASA tracks, the relevant align-
------------------------------
 ment is the one between the target sequence and the best-scoring model. For the sequence identity track, the alignment is between the target sequence and the sequence of the best-scoring model.

ESMFold is a software tool that is used to predict the three-dimensional structure of proteins based on their amino acid sequences. It uses a deep learning algorithm to generate a set of possible structures, which are then evaluated and ranked based on their predicted accuracy.

ESM3 is a variant of the ESMFold algorithm that is specifically designed for predicting the structures of membrane proteins. It takes into account the unique properties of these proteins, such as their hydrophobic and hydrophilic regions, and uses this information to generate more accurate predictions.

The structure coordinate track shows the predicted three-dimensional structure of the protein, with each amino acid represented as a point in space. The secondary structure track shows the predicted secondary structure of the protein, which refers to the local folding patterns of the amino acid chain. The SASA track shows the predicted solvent accessible surface area of the protein, which is a measure of how much of the protein is exposed to the surrounding environment.

The sequence identity track shows the degree of similarity between the predicted structure and the actual structure of the protein, as determined by comparing the amino acid sequences of the two structures. This is important because even small differences in the amino acid sequence can have a significant impact on the overall structure and function of the protein.

Overall, these tools and tracks are essential for evaluating the accuracy of protein structure predictions and for gaining insights into the properties and functions of these important biological molecules.
User:
==============================
Figure S13. Unconditional generation of high-quality and diverse proteins using ESM3. (A) Distribution of sequence length in the unconditional generation dataset. (B) Mean pLDDT and pTM of unconditional generations from ESM3 compared to sequences designed using the 3B-parameter ESM2 model. (C) Round-trip success rate of high-confidence generations using ESM3. Predicted structures were inverse folded to predict a new sequence and then re-folded to produce a new structure. Success was measured by a TM-score of greater than 0.8 between the original and refolded designs. (D) Secondary structure composition of unconditional generations relative to the distribution of proteins in the PDB, which is shown in gray.
------------------------------
 Hello and welcome to this video where we will be discussing the reference to Figure S13, which is related to the unconditional generation of high-quality and diverse proteins using ESM3.

First, let's define some terms that may not be obvious to those not specializing in this field. ESM3 stands for Evolutionary Scale Modeling 3, which is a computational model used to predict protein structures. pLDDT stands for predicted local distance difference test, which is a measure of the accuracy of the predicted protein structure. pTM stands for predicted TM-score, which is a measure of the similarity between two protein structures. TM-score stands for Template Modeling score, which is a measure of the structural similarity between two protein structures.

Now, let's dive into the results presented in Figure S13. In panel A, we see the distribution of sequence length in the unconditional generation dataset. This means that the dataset contains a variety of protein sequences of different lengths.

In panel B, we see a comparison of the mean pLDDT and pTM of unconditional generations from ESM3 compared to sequences designed using the 3B-parameter ESM2 model. The results show that ESM3 outperforms ESM2 in terms of both pLDDT and pTM, indicating that ESM3 is better at predicting protein structures.

In panel C, we see the round-trip success rate of high-confidence generations using ESM3. This means that predicted structures were inverse folded to predict a new sequence and then re-folded to produce a new structure. Success was measured by a TM-score of greater than 0.8 between the original and refolded designs. The results show that ESM3 has a high success rate in predicting protein structures.

Finally, in panel D, we see the secondary structure composition of unconditional generations relative to the distribution of proteins in the PDB, which is shown in gray. The results show that ESM3 is able to generate a diverse range of protein structures, which is important for understanding the function of different proteins.

In summary, Figure S13 shows that ESM3 is a powerful computational model for predicting protein structures and generating diverse protein structures. This has important implications for understanding the function of different proteins and developing new drugs and therapies.
User:
==============================
Figure S14. Generation of sequences using chain-of-thought. SS8 tokens are generated first, followed by structure tokens, then amino acid sequence with the ESM3 7B model. (A) Distribution of mean pLDDT and pTM of sequences generated by chain-of-thought ("ss8 first") compared to directly generating the sequence ("sequence only"). (B) Sample generations of SS8 tokens and the predicted structure of its corresponding CoT sequence. (C) TM-score between predicted structures of high-confidence ( $\mathrm{pTM}>0.8$, mean pLDDT $>0.8$ ) generated sequences and their corresponding inverse folded, then re-folded structures. (D) Comparison of the secondary structure composition of high-confidence generated sequences to the distribution of proteins in the PDB.
ment metrics (backbone cRMSD, 3-class secondary structure accuracy, and SASA Spearman $\rho$ ) can be calculated on the relevant span in the ESMFold-predicted structure and the original template protein. Continuing the previous example for the structure track, we would compute the RMSD between residues 20-35 in the ESMFold structure predicted of the ESM3-generated sequence and residues 20-35 of the original test protein. For the function annotation track, we run InterProScan (38) on each generated sequence and extract function keywords from the emitted annotations. We report function keyword recovery at the protein level, computing the proportion of all function keywords in the prompt which appear anywhere in the function keywords from the InterProScan annotations of the generation.
------------------------------
 Hello and welcome to this video where we will be discussing the concept of chain-of-thought in the field of protein structure prediction. In this study, we used a model called ESM3 7B to generate sequences using chain-of-thought.

First, let's define some terms. SS8 tokens refer to the secondary structure elements of a protein, which are the alpha-helices and beta-sheets. Structure tokens refer to the 3D structure of a protein, which is determined by the arrangement of the secondary structure elements. Amino acid sequence refers to the linear sequence of amino acids that make up a protein.

Now, let's look at the results of our study. We found that using chain-of-thought to generate sequences resulted in higher mean pLDDT and pTM scores compared to directly generating the sequence. pLDDT is a measure of the predicted local distance difference test, which assesses the accuracy of the predicted structure. pTM is a measure of the predicted TM-score, which compares the predicted structure to the native structure.

We also found that the predicted structures of high-confidence generated sequences had a high TM-score compared to their corresponding inverse folded, then re-folded structures. This suggests that the generated sequences were accurate and reliable.

Finally, we compared the secondary structure composition of the generated sequences to the distribution of proteins in the PDB, which is a database of protein structures. We found that the generated sequences had a similar secondary structure composition to the proteins in the PDB.

In summary, using chain-of-thought to generate sequences resulted in accurate and reliable protein structures. This approach has the potential to improve protein structure prediction and advance our understanding of protein function. Thank you for watching!
User:
==============================
To test the ability of ESM3 to generalize beyond its training distribution under prompting, we evaluate two prompting scenarios. First, we identify proteins which were deposited in the PDB after our training cutoff (December 2020) and choose eight with $\mathrm{TM}<0.7$ to any structure in our training dataset (PDB IDs: $2 \mathrm{JVN}$ chain A, $2 \mathrm{KAF}$ chain A, $2 \mathrm{~L} 8 \mathrm{~K}$ chain $\mathrm{A}, 2 \mathrm{MJM}$ chain $\mathrm{A}, 7 \mathrm{ZUO}$ chain $\mathrm{A}, 8 \mathrm{EXF}$ chain B). Using DSSP, we compute the residue-level SS8 and SASA for each of these proteins to prompt ESM3, masking all other tracks. We show in Fig. S15A that the generated proteins are diverse, globular, and closely follow the SS8 and SASA prompts while having no close sequence or structure neighbors in the training set. Interestingly, these proteins are not folded with high confidence or accuracy by ESMFold (mean pTM 0.44 , mean TM-score to reference 0.33), suggesting that these are challenging proteins to fold. The ESM3generated sequences have a similar confidence (mean pTM 0.45 ) but much higher accuracy (mean TM-score 0.64).
------------------------------
 Hello and welcome to this video where we will be discussing the ability of ESM3 to generalize beyond its training distribution under prompting.

First, let's define some terms. ESM3 stands for Evolutionary Scale Modeling 3, which is a deep learning model that can predict protein structures from amino acid sequences. DSSP stands for Dictionary of Secondary Structure of Proteins, which is a program that assigns secondary structure elements to each residue in a protein. SS8 refers to the eight-state secondary structure classification used by DSSP, and SASA stands for Solvent Accessible Surface Area, which is a measure of how much of a protein's surface is exposed to the surrounding solvent.

Now, let's dive into the evaluation of ESM3's ability to generalize beyond its training distribution under prompting. The researchers identified proteins that were deposited in the Protein Data Bank (PDB) after their training cutoff date of December 2020. They chose eight proteins with a TM-score less than 0.7 to any structure in their training dataset. TM-score stands for Template Modeling score, which is a measure of how similar two protein structures are.

The researchers then used DSSP to compute the residue-level SS8 and SASA for each of these proteins to prompt ESM3. They masked all other tracks, which means they only provided ESM3 with the SS8 and SASA information and no other structural or sequence information.

The results showed that the generated proteins were diverse, globular, and closely followed the SS8 and SASA prompts while having no close sequence or structure neighbors in the training set. This means that ESM3 was able to generate new protein structures that were not similar to any structures in its training dataset.

Interestingly, these proteins were not folded with high confidence or accuracy by ESMFold, which is another deep learning model for protein structure prediction. This suggests that these proteins were challenging to fold and that ESM3's ability to generate accurate protein structures under prompting is impressive.

In summary, the researchers evaluated ESM3's ability to generalize beyond its training distribution under prompting by identifying proteins deposited in the PDB after their training cutoff date and using DSSP to compute the residue-level SS8 and SASA for each protein to prompt ESM3. The results showed that ESM3 was able to generate diverse and accurate protein structures under prompting, even for challenging proteins that were not folded accurately by ESMFold.
User:
==============================
Second, we classify the residue-level secondary structure for a set of eight symmetric protein backbones using DSSP. These proteins were previously designed using ESMFold $(5,91)$ and have varying secondary structure (alpha and beta) and varying symmetries (5-fold and 8 -fold). Again, ESM3 is able to design these proteins successfully with high confidence ( $\mathrm{pTM}>0.8$, pLDDT $>0.8$ ) and low sequence similarity to the training set Fig. S15B. The structural similarity is moderate for these designs due to the high structural conservation of the protomer units in each design. All designs are generated using a constant temperature of 0.7 with $\mathrm{L} / 2$ decoding steps, where $\mathrm{L}$ is the protein length. We sample 256 sequences for each prompt and filter generations by pTM ( $>0.8$ ), pLDDT ( $>0.8$ ), and accuracy in satisfying the SS8 prompts ( $>0.8$ ). Final examples were selected from these filtered designs by visual inspection. Sequence similarity to the training set was computed using the same procedure as the unconditional generations, and structure similarity was computed using Foldseek (39) in TM-score mode (alignment-type 1) with sensitivity -s 7.5.
------------------------------
 Hello and welcome to this video where we will be discussing the use of DSSP to classify residue-level secondary structure in a set of eight symmetric protein backbones. These proteins were previously designed using ESMFold and have varying secondary structure and symmetries.

First, let's define some terms. ESMFold is a protein structure prediction algorithm that uses deep learning to predict protein structures. DSSP is a program that assigns secondary structure to each residue in a protein based on its backbone dihedral angles. Secondary structure refers to the local three-dimensional structure of a protein, which can be classified as alpha-helix, beta-sheet, or loop.

In this study, the researchers used DSSP to classify the residue-level secondary structure of the eight symmetric protein backbones. They found that ESM3, a newer version of ESMFold, was able to design these proteins successfully with high confidence and low sequence similarity to the training set.

The structural similarity of the designs was moderate due to the high structural conservation of the protomer units in each design. The researchers generated the designs using a constant temperature of 0.7 with L/2 decoding steps, where L is the protein length. They sampled 256 sequences for each prompt and filtered generations by pTM (probability of being a true model), pLDDT (predicted local distance difference test), and accuracy in satisfying the SS8 prompts.

Finally, the researchers selected final examples from these filtered designs by visual inspection. Sequence similarity to the training set was computed using the same procedure as the unconditional generations, and structure similarity was computed using Foldseek in TM-score mode with sensitivity -s 7.5.

In summary, this study used DSSP to classify the residue-level secondary structure of eight symmetric protein backbones designed using ESMFold. The researchers found that ESM3 was able to design these proteins successfully with high confidence and low sequence similarity to the training set. The structural similarity of the designs was moderate due to the high structural conservation of the protomer units in each design.
User:
==============================
ESM3 is able to compose multimodal prompts across its input tracks-sequence, structure, SS8, SASA, and function keywords-to generate proteins with novel characteristics. To demonstrate this, we augment the standard functional motif scaffolding task (i.e., partial structure and sequence prompts) with additional conditioning to specify the type of scaffold for ESM3 to design. The functional sites comprise a combination of ligand binding sites coordinated by residues remote in sequence and those defined by short local motifs. For each motif, the coordinates and amino acid identities of all residues from the reference PDB structures are input to the model, with random shuffling and augmentation of the gaps between each active site. See Appendix A.4.5 for a description of this augmentation procedure and the specifications of the ligand-binding sites chosen. In addition to these sites, we also create a set of 12 partial sequence and structure prompts derived from conserved functional motifs (Table S10). These motifs are defined using a combination of the benchmark dataset in Watson et al. (23) and conserved sequence patterns from the Prosite database (92).
------------------------------
 Hello and welcome to this video where we will be discussing the use of ESM3 in generating proteins with novel characteristics. ESM3 is a powerful tool that is able to compose multimodal prompts across its input tracks, including sequence, structure, SS8, SASA, and function keywords. This allows for the creation of proteins with unique properties that may not have been possible before.

To demonstrate the capabilities of ESM3, we have augmented the standard functional motif scaffolding task with additional conditioning to specify the type of scaffold for ESM3 to design. The functional sites that we are targeting comprise a combination of ligand binding sites coordinated by residues remote in sequence and those defined by short local motifs.

For each motif, we input the coordinates and amino acid identities of all residues from the reference PDB structures into the model. We then randomly shuffle and augment the gaps between each active site to create a diverse set of inputs for ESM3 to work with.

In addition to these sites, we have also created a set of 12 partial sequence and structure prompts derived from conserved functional motifs. These motifs are defined using a combination of the benchmark dataset in Watson et al. (23) and conserved sequence patterns from the Prosite database (92).

Overall, ESM3 is a powerful tool that allows for the creation of proteins with unique properties. By using multimodal prompts and additional conditioning, we are able to generate proteins with novel characteristics that may have important applications in a variety of fields. Thank you for watching!
User:
==============================
The scaffold conditioning is defined using either SS8 tokens (to specify secondary structure composition) or function keywords defined by InterPro accession numbers (to specify a particular fold). For each combination of functional site and scaffold prompt, we sample between 256 and 2048 times to generate proteins with diverse and novel characteristics. All designs were generated with the 7B-parameter model, a constant temperature of 0.7 , and $L / 2$ decoding steps for a protein of length $L$.
------------------------------
 Hello and welcome to this video where we will be discussing the concept of scaffold conditioning in the field of protein design.

Scaffold conditioning is a technique used to generate proteins with diverse and novel characteristics. It involves defining the scaffold using either SS8 tokens or function keywords defined by InterPro accession numbers.

SS8 tokens are used to specify the secondary structure composition of the protein. This means that the protein's structure is defined by the arrangement of its amino acid residues into alpha-helices, beta-sheets, and other secondary structures.

On the other hand, function keywords defined by InterPro accession numbers are used to specify a particular fold. A protein fold refers to the three-dimensional structure of a protein, which is determined by the arrangement of its amino acid residues.

To generate proteins with diverse and novel characteristics, we sample between 256 and 2048 times for each combination of functional site and scaffold prompt. This means that we generate a large number of protein designs to ensure that we have a diverse set of proteins with unique characteristics.

All of these protein designs were generated using the 7B-parameter model, which is a mathematical model used to predict the stability and folding of proteins. We also used a constant temperature of 0.7 and $L / 2$ decoding steps for a protein of length $L$.

In summary, scaffold conditioning is a technique used to generate proteins with diverse and novel characteristics. It involves defining the scaffold using either SS8 tokens or function keywords defined by InterPro accession numbers, and generating a large number of protein designs to ensure diversity. These protein designs were generated using the 7B-parameter model, a constant temperature of 0.7, and $L / 2$ decoding steps for a protein of length $L$.
User:
==============================
Secondary structure prompting. We generated proteins under four main classes of secondary structure composition: mostly alpha helices, mostly beta sheets, and mixed alphabeta proteins (split into alpha/beta, alpha/beta/alpha, and beta/alpha/beta topologies). For each generation, we prompt the model with a random set of SS8 spans up to a total length $L$, with mask tokens in between. For example, an all-alpha SS8 prompt for a protein of length $L=20$ might look like __HHHH $\mathrm{HHHHH}$ $\mathrm{HH}$ and a beta-alpha-beta prompt might look like __EEE__HHHHH___EE_, where H is a residue within an alpha helix and $\mathrm{E}$ is a residue in a beta strand. We then combine this with the augmented partial structure and sequence tracks given by a functional site motif. To increase the diversity of the scaffolds and maximize the probability of generating physically realizable prompt combinations, we generate between 256 and 1024 designs for each combination of SS8 and functional site motif. For each generation, we uniformly sample a random length $L$ between 150 and 400 . Then, we produce a set of secondary structure spans with length 5-20 residues, each separated
------------------------------
 by a mask token. We then randomly select a subset of these spans to fill up to $L$ residues, and concatenate them with the functional site motif. We then use the Rosetta software suite to generate 3D structures for each of these designs, and select the top-scoring design as our final output.

In summary, secondary structure prompting is a technique used in protein design to generate diverse and physically realizable protein structures. It involves prompting the model with a random set of secondary structure spans, and combining them with a functional site motif to generate a set of designs. The top-scoring design is then selected as the final output.
User:
==============================
Figure S15. Prompting ESM3 to generalize beyond its training distribution. (A) Proteins designed using SS8 and SASA prompts derived from recent structures in the PDB with low structural similarity to the training set. Prompts along the protein length are visualized above each generation; secondary structure is shown using three-class (alpha $=$ blue, beta $=$ orange, coil $=$ gray) and SASA is shown as a line plot colored by residue index to match the cartoon below. (B) Symmetric proteins designed using SS8 prompting. Histograms show the similarity to the nearest training set protein by structure (TM-score) and sequence (sequence identity) compared to unconditional generation.
------------------------------
 Hello and welcome to this video where we will be discussing the concept of prompting ESM3 to generalize beyond its training distribution. This is a topic that is relevant to the field of protein design and structure prediction.

In order to understand this concept, we first need to define some key terms. ESM3 stands for Evolutionary Scale Modeling 3, which is a computational model that is used to predict protein structures. The training distribution refers to the set of protein structures that were used to train the ESM3 model.

Now, let's take a look at Figure S15. This figure shows two different scenarios where ESM3 was prompted to design proteins that were beyond its training distribution. In the first scenario, the prompts were derived from recent structures in the PDB (Protein Data Bank) that had low structural similarity to the training set. The prompts were visualized along the protein length and included secondary structure and SASA (solvent accessible surface area) information.

In the second scenario, symmetric proteins were designed using SS8 prompting. Histograms were used to show the similarity to the nearest training set protein by structure (TM-score) and sequence (sequence identity) compared to unconditional generation.

Overall, this study demonstrates the ability of ESM3 to generalize beyond its training distribution when prompted with appropriate information. This has important implications for protein design and structure prediction, as it allows for the creation of novel protein structures that may have unique functions or properties.

Thank you for watching this video and we hope that you found this explanation helpful. If you have any further questions or comments, please feel free to leave them in the comments section below.
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
 Hello and welcome to this video on functional motifs in protein structures. In this video, we will be discussing the different functional motifs that are commonly found in protein structures and how they contribute to the overall function of the protein.

To begin, let's define what a functional motif is. A functional motif is a specific sequence of amino acids that is responsible for a particular function of the protein. These motifs can be found in different regions of the protein structure and can be identified by their specific sequence of amino acids.

Now, let's take a look at some examples of functional motifs that have been identified in protein structures. The first example is the ACE2 binding motif, which is found in the protein structure with PDB ID 6vw1. This motif is located in chain A and spans residues 19-89 and 319-366. The ACE2 binding motif is responsible for binding to the ACE2 receptor, which is involved in the entry of the SARS-CoV-2 virus into human cells.

Another example is the Ferredoxin motif, which is found in the protein structure with PDB ID 666r. This motif is located in chain A and spans residues 1-44. The Ferredoxin motif is responsible for binding to iron-sulfur clusters, which are involved in electron transfer reactions in the cell.

The Barstar binding motif is found in the protein structure with PDB ID 7mrx. This motif is located in chain B and spans residues 25-47. The Barstar binding motif is responsible for binding to the Barstar protein, which is involved in regulating gene expression.

The P53 binding motif is found in the protein structure with PDB ID 1ycr. This motif is located in chain B and spans residues 19-28. The P53 binding motif is responsible for binding to the P53 protein, which is involved in regulating cell growth and division.

The PD-1 binding motif is found in the protein structure with PDB ID 5ius. This motif is located in chain A and spans residues 63-83 and 119-141. The PD-1 binding motif is responsible for binding to the PD-1 receptor, which is involved in regulating immune responses.

The DNA-binding helix-turn-helix motif is found in the protein structure with PDB ID 11cc. This motif is located in chain A and spans residues 1-52. The DNA-binding helix-turn-helix motif is responsible for binding to DNA and regulating gene expression.

The P-loop motif is found in the protein structure with PDB ID 5ze9. This motif is located in chain A and spans residues 229-243. The P-loop motif is responsible for binding to nucleotides and is involved in various cellular processes.

The Double EF-hand motif is found in the protein structure with PDB ID 1a2x. This motif is located in chain A and spans residues 103-115 and 139-152. The Double EF-hand motif is responsible for binding to calcium ions and is involved in various cellular processes.

The Lactate dehydrogenase motif is found in the protein structure with PDB ID 11db. This motif is located in chain A and spans residues 186-206. The Lactate dehydrogenase motif is responsible for catalyzing the conversion of lactate to pyruvate.

The Renal dipeptidase motif is found in the protein structure with PDB ID 1itu. This motif is located in chain A and spans residues 124-147. The Renal dipeptidase motif is responsible for catalyzing the hydrolysis of dipeptides.

The Ubiquitin-activating enzyme E1C binding motif is found in the protein structure with PDB ID 1yov. This motif is located in chain B and spans residues 213-223. The Ubiquitin-activating enzyme E1C binding motif is responsible for binding to the E1C enzyme, which is involved in the ubiquitin-proteasome system.

Finally, the DNA topoisomerase motif is found in the protein structure with PDB ID 1a41. This motif is located in chain A and spans residues 248-280. The DNA topoisomerase motif is responsible for catalyzing the topological changes in DNA during replication and transcription.

In conclusion, functional motifs are an important aspect of protein structures and contribute to the overall function of the protein. By identifying and understanding these motifs, we can gain insight into the specific functions of proteins and how they contribute to cellular processes. Thank you for watching this video on functional motifs in protein structures.
User:
==============================
Keyword prompting. To prompt the model to generate proteins with a specific fold, we extracted the set of InterPro tags associated with a set of proteins from the CAMEO test set for which ESM3 achieved keyword recovery of greater than $80 \%$ (Fig. 2A). These tags were then converted into keywords and used to prompt the model in combination with the partial sequence and structure constraints. The list of prompts and function tags is given in Table S11. Keywordprompted designs were assessed using a self-consistency evaluation, i.e. whether the model successfully predicts any of the prompted InterPro accessions for the designed sequence. Success was determined by a pTM $>0.8$, all-atom $c$ RMSD $<2.0$, and number of InterPro accessions recovered $>0$.
------------------------------
 Hello and welcome to this video on keyword prompting in protein design. In this video, we will be discussing a technique used to prompt the model to generate proteins with a specific fold.

First, let's define some terms. InterPro tags are a set of protein family and domain annotations that are used to classify proteins based on their function and structure. ESM3 is a protein design model that uses deep learning to predict protein structures. Keyword recovery is the percentage of InterPro tags that are correctly predicted by the model.

Now, let's dive into the technique of keyword prompting. To prompt the model to generate proteins with a specific fold, we first extract the set of InterPro tags associated with a set of proteins from the CAMEO test set. These tags are then converted into keywords and used to prompt the model in combination with the partial sequence and structure constraints.

The list of prompts and function tags is given in Table S11. The success of the keyword-prompted designs is assessed using a self-consistency evaluation. This means that the model is evaluated based on whether it successfully predicts any of the prompted InterPro accessions for the designed sequence.

Success is determined by three criteria: a pTM greater than 0.8, all-atom c RMSD less than 2.0, and the number of InterPro accessions recovered greater than 0.

In summary, keyword prompting is a technique used to prompt the model to generate proteins with a specific fold by using InterPro tags as keywords. The success of the keyword-prompted designs is evaluated based on three criteria.
User:
==============================
We assess novelty of each motif-scaffold combinations by measuring the TM-score between the generated scaffold and the chain from which the motif is derived (Table S12). This confirms that the model is not retrieving the original motif scaffold, particularly for secondary structure-prompted scaffolds where we do not provide any explicit instructions to produce diverse designs. For the motifs derived from ligand binding residues (magnesium, serotonin, calcium, zinc, protease inhibitor 017, and Mcl-1 inhibitor YLT), we additionally use Foldseek to search the PDB for any other proteins which share that motif (as defined by BioLiP (93)), as a more stringent evaluation of novelty. For all but zincbinding and magnesium-binding motifs, Foldseek finds no significant hits at an E-value threshold of 1.0. The hits discovered for zinc and magnesium have only modest TMscore ( 0.76 and 0.64 ), demonstrating that the model still finds novel scaffolding solutions for these ligands. To assess whether the generated scaffolds are likely to be designable, we measure a self-consistency TM-score under orthogonal computational models by inverse-folding the designed structure with ESM-IF (94) (using a temperature of 0.5 ) and re-folding with ESMFold (5). We report the best scTM over 8 inverse folding designs in Table S12.
------------------------------
 Hello and welcome to this video where we will be discussing the novelty and designability of motif-scaffold combinations. In order to assess the novelty of each combination, we use a measure called the TM-score, which compares the generated scaffold to the chain from which the motif was derived. This ensures that the model is not simply retrieving the original motif scaffold, particularly for secondary structure-prompted scaffolds where we do not provide any explicit instructions to produce diverse designs.

For motifs derived from ligand binding residues, we use a more stringent evaluation of novelty by using Foldseek to search the PDB for any other proteins which share that motif, as defined by BioLiP. For all but zinc-binding and magnesium-binding motifs, Foldseek finds no significant hits at an E-value threshold of 1.0. The hits discovered for zinc and magnesium have only modest TM-scores, demonstrating that the model still finds novel scaffolding solutions for these ligands.

To assess the designability of the generated scaffolds, we measure a self-consistency TM-score under orthogonal computational models by inverse-folding the designed structure with ESM-IF and re-folding with ESMFold. We report the best self-consistency TM-score over 8 inverse folding designs in Table S12.

In summary, we use the TM-score to assess the novelty of motif-scaffold combinations and Foldseek to evaluate the novelty of ligand binding motifs. We also use a self-consistency TM-score to assess the designability of the generated scaffolds. Thank you for watching and we hope this explanation has been helpful.
User:
==============================
First, we describe the procedure for generating the protein compression example shown in Fig. 2D. A series of prompts of length 150 were constructed. The sequence and struc- ture of the catalytic triad of trypsin (PDB 1Y3V) (H57, D102, S195) were placed in the prompt using the following procedure: three random residue numbers between 20 and 130 were sampled such that the minimum pairwise difference in position between each of the residues was no less than 20. Then, H57 from the template trypsin was placed at the lowest sampled number, D102 at the second lowest, and S195 at the largest number, thus respecting the left-to-right ordering of the catalytic triad in the template trypsin. 128 prompts were generated by this procedure. Each of these prompts was combined with a function keyword prompt derived from the template protein, specifically InterPro (38) tags IPR001254 (serine proteases, trypsin domain) and IPR009003 (peptidase S1, PA clan), to arrive at a final set of 128 prompts. The base ESM 7B model was then prompted to generate the sequence of the remaining 147 residues of the protein conditioned on the randomly placed catalytic triad sequence and structure coordinates and function keywords. $L=150$ decoding steps were used with a temperature of 0.7 , with 32 generations per prompt. Generations were then filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs, with the generation shown in Fig. 2D selected finally by visual inspection.
------------------------------
 Hello and welcome to this video where we will be discussing the procedure for generating the protein compression example shown in Fig. 2D.

First, let's define some terms that may not be obvious to those not specializing in this field. A prompt is a sequence of amino acids that is used to generate a protein sequence. The catalytic triad is a group of three amino acids that are involved in the catalytic activity of an enzyme. The InterPro tags are a set of keywords that describe the function of a protein.

Now, let's dive into the procedure. A series of prompts of length 150 were constructed. The sequence and structure of the catalytic triad of trypsin were placed in the prompt using a specific procedure. Three random residue numbers between 20 and 130 were sampled such that the minimum pairwise difference in position between each of the residues was no less than 20. Then, H57 from the template trypsin was placed at the lowest sampled number, D102 at the second lowest, and S195 at the largest number, thus respecting the left-to-right ordering of the catalytic triad in the template trypsin.

128 prompts were generated by this procedure. Each of these prompts was combined with a function keyword prompt derived from the template protein, specifically InterPro tags IPR001254 and IPR009003, to arrive at a final set of 128 prompts.

The base ESM 7B model was then prompted to generate the sequence of the remaining 147 residues of the protein conditioned on the randomly placed catalytic triad sequence and structure coordinates and function keywords. $L=150$ decoding steps were used with a temperature of 0.7, with 32 generations per prompt.

Generations were then filtered by active site cRMSD, ESM3 pTM, and InterPro Scan keyword outputs, with the generation shown in Fig. 2D selected finally by visual inspection.

We hope this explanation has been helpful in understanding the procedure for generating the protein compression example shown in Fig. 2D. Thank you for watching!
User:
==============================
Generation quality was measured using ESMFold (5) pTM of the generated sequence, in addition to self-consistency. For self-consistency, we inverse fold the ESM3-predicted structure of the generation with ESM-IF1 (94) 8 times and re-fold with ESMFold, reporting the mean and std of the TM-scores between the 8 ESMFold-predicted structures and the ESM3-predicted structure. To perform a blast search of the sequence, we use a standard Protein Blast search (51). We set the max target sequences parameter to 5000 and sort results by sequence length and sequence identity, selecting the first sequence that is a serine protease. This yields the reference WP_260327207 which is 164 residues long and shares $33 \%$ sequence identity with the generation.
------------------------------
 Hello and welcome to this video where we will be discussing the use of ESMFold and ESM-IF1 in measuring generation quality.

First, let's define some terms that may not be obvious to those not specializing in this field. ESMFold is a protein structure prediction algorithm that uses a deep neural network to predict protein structures from amino acid sequences. ESM-IF1 is another algorithm that uses a deep neural network to predict protein structures, but it is specifically designed to work with ESMFold.

Now, let's talk about how we measure generation quality. We use two metrics: pTM and self-consistency. pTM is a measure of the predicted protein structure's accuracy, and it is calculated by comparing the predicted structure to the true structure. Self-consistency, on the other hand, measures how well the predicted structure agrees with itself. We do this by inverse folding the predicted structure and then re-folding it with ESMFold. We repeat this process eight times and report the mean and standard deviation of the TM-scores between the eight ESMFold-predicted structures and the ESM3-predicted structure.

Finally, we perform a blast search of the sequence to find a reference protein that is similar to the generated sequence. We use a standard Protein Blast search and set the max target sequences parameter to 5000. We sort the results by sequence length and sequence identity and select the first sequence that is a serine protease. In this case, the reference protein is WP_260327207, which is 164 residues long and shares 33% sequence identity with the generated sequence.

I hope this explanation has been helpful in understanding how ESMFold and ESM-IF1 are used to measure generation quality. Thank you for watching!###
==============================
We showcase two further examples of protein editing. First, ESM3 is prompted to bury an exposed helix in a protein with an alternating alpha-beta sandwich fold. The prompt is constructed as follows: the prompt is of the same length as the template protein (PDB 1LBS). We identify a buried helix (mean SASA $0.32 \AA^{2}$ ) between residues 106-116 of the template protein. Structure coordinates from this region are placed in the prompt at the same residue indices, to prompt ESM3 to generate the same helix. This is composed with a SASA prompt of 40.0 for each of the 11 helix residues, prompting ESM3 to place this helix on the surface of the protein. Finally, we prompt with the secondary structure of 5 central beta strands surrounding the buried helix, residues 33-36, 62-65, 99-103, 125-130, and 179-182. ESM3 7B is then used to generate 512 protein sequences conditioned on this prompt using $\frac{L}{2}$ decoding steps and a temperature of 0.7. Designs are filtered by ESM3 pTM and adherence
------------------------------
 to the prompt, and the top 10 designs are selected for further analysis.

The first example we showcase is the editing of a protein with an alternating alpha-beta sandwich fold. We use a prompt that is the same length as the template protein, which is PDB 1LBS. We identify a buried helix between residues 106-116 of the template protein and place the structure coordinates from this region in the prompt at the same residue indices. This prompts ESM3 to generate the same helix. We also use a SASA prompt of 40.0 for each of the 11 helix residues, which prompts ESM3 to place this helix on the surface of the protein. Finally, we prompt with the secondary structure of 5 central beta strands surrounding the buried helix, residues 33-36, 62-65, 99-103, 125-130, and 179-182.

We then use ESM3 7B to generate 512 protein sequences conditioned on this prompt using $\frac{L}{2}$ decoding steps and a temperature of 0.7. Designs are filtered by ESM3 pTM and adherence to the prompt, and the top 10 designs are selected for further analysis.

In summary, we use a prompt to edit a protein with an alternating alpha-beta sandwich fold by identifying a buried helix and prompting ESM3 to generate the same helix on the surface of the protein. We also prompt with the secondary structure of 5 central beta strands surrounding the buried helix. We use ESM3 7B to generate protein sequences and filter them by adherence to the prompt and ESM3 pTM. The top 10 designs are selected for further analysis.
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
 Hello and welcome to this video where we will be discussing the InterPro tags extracted from CAMEO test set proteins for prompting with fold specification.

Let's start by defining some of the terms used in the table.

Scaffold refers to the overall structure of a protein, while reference refers to the specific protein being analyzed.

InterPro tags are a set of protein family and domain annotations that are used to classify proteins based on their function and structure.

The total length column refers to the total number of amino acids in the protein.

Moving on to the table, we can see that the first protein, Beta propeller, has three InterPro tags: IPR001680, IPR036322, and IPR015943. These tags indicate that the protein belongs to the beta propeller family and has a specific domain structure.

The TIM barrel protein has six InterPro tags, including IPR000652, which indicates that it belongs to the TIM barrel family, and IPR020861, which indicates that it has a specific domain structure.

The MFS transporter protein has three InterPro tags, including IPR011701, which indicates that it belongs to the MFS transporter family, and IPR020846, which indicates that it has a specific domain structure.

The Immunoglobulin protein has six InterPro tags, including IPR036179, which indicates that it belongs to the immunoglobulin family, and IPR013783, which indicates that it has a specific domain structure.

The Histidine kinase protein has eight InterPro tags, including IPR003594, which indicates that it belongs to the histidine kinase family, and IPR004358, which indicates that it has a specific domain structure.

Finally, the Alpha/beta hydrolase protein has two InterPro tags, including IPR029058, which indicates that it belongs to the alpha/beta hydrolase family, and IPR000073, which indicates that it has a specific domain structure.

In summary, InterPro tags are used to classify proteins based on their function and structure, and the table shows the InterPro tags extracted from CAMEO test set proteins for prompting with fold specification.
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
 Hello and welcome to this video where we will be discussing the novelty and designability metrics of motif scaffolds. In this table, we have listed various scaffolds along with their corresponding metrics.

Let's start by defining some terms. The novelty metric is measured by computing the TM-score to the original scaffold from which the motif is derived. TM-score stands for Template Modeling score and is a measure of the structural similarity between two protein structures. A TM-score of 1 indicates a perfect match, while a score of 0 indicates no similarity.

The designability metric is measured by self-consistency TM-score over eight samples by inverse folding with ESM-IF and refolding with ESMFold. ESM-IF stands for Evolutionary Structural Model-Inverse Folding and is a method for predicting protein structures. ESMFold stands for Evolutionary Structural Model-Fold and is a method for predicting protein structures based on evolutionary information.

Now let's take a look at the results. All designs are distinct from their original scaffolds while retaining high designability. This means that the generated proteins are structurally different from the original scaffolds, but still maintain their functionality.

For example, let's take a look at the generation of the ESM3 protein. The input constraints were to maintain the structure of the helix and the alternating alpha-beta fold, while exposing the helix motif to the surface. The final generation was chosen by visual inspection and evaluated as described above. The generation was able to satisfy the input constraints, while also being structurally distinct from the original scaffold.

In conclusion, the novelty and designability metrics are important for evaluating the structural similarity and functionality of generated proteins. By using these metrics, we can ensure that the generated proteins are structurally distinct from the original scaffolds, while still maintaining their functionality. Thank you for watching!
User:
==============================
We also use ESM3 to generate an idealized TIM Barrel with 11-fold symmetry. This generation is undertaken in two steps. First, we derive a secondary structure and function keyword prompt from a reference TIM Barrel (PDB 5EKY). The secondary structure of the reference protein is computed using DSSP and then idealized to construct a prompt for ESM3. To construct the secondary structure prompt, the length of each helix and strand is fixed at 7 residues. Each helix and strand region is then separated by 3 mask tokens, with a mask token appended to the $\mathrm{N}$ and $\mathrm{C}$ termini of the prompt as well. This yields a secondary structure prompt of total length 159 , which is combined with a function keyword prompt derived from the reference protein: keywords are derived from IPR013785 (aldolase-type TIM barrel) and IPR000887 (KDPG/KHG aldolase). ESM3 7B is then used to generate 256 samples with $L$ decoding steps and a temperature of 0.7 . The design shown is chosen by filtering by ESM3 pTM and visual inspection. In the second step, the secondary structure prompt from the first step is expanded to contain 11 helix-strand subunits, for a total prompt length of 225 residues (4 mask tokens are now appended to the $\mathrm{N}$ and $\mathrm{C}$ termini, rather than just 1). ESM3 7B is then used to generate 256 samples with $L$ decoding steps and a temperature of 0.7 , with generations filtered by ESM3 pTM and visual inspection. The generation is evaluated as described above (ESMFold pTM 0.69, scTM mean 0.97, std 0.011). The generation is structurally distinct: a Foldseek search (39) of AlphaFold-DB, ESMAtlas, and PDB in TM-align mode reveals no hit with TM-score greater than . 61 .

------------------------------
 Hello and welcome to this video where we will be discussing the use of ESM3 to generate an idealized TIM Barrel with 11-fold symmetry. In this video, we will be explaining all the terms in detail that may not be obvious to someone who is not specializing in this field.

First, let's define what a TIM Barrel is. A TIM Barrel is a type of protein structure that is found in many enzymes. It is named after the triose phosphate isomerase enzyme, which was the first protein to be discovered with this structure. The TIM Barrel is made up of eight alpha-helices and eight beta-strands arranged in a barrel-like shape.

Now, let's talk about ESM3. ESM3 is a deep learning model that is used to generate protein structures. It is based on the AlphaFold2 model, which is a state-of-the-art protein structure prediction model. ESM3 is trained on a large dataset of protein structures and can generate high-quality protein structures with a high degree of accuracy.

In this study, we used ESM3 to generate an idealized TIM Barrel with 11-fold symmetry. We did this in two steps. First, we derived a secondary structure and function keyword prompt from a reference TIM Barrel (PDB 5EKY). The secondary structure of the reference protein was computed using DSSP and then idealized to construct a prompt for ESM3.

To construct the secondary structure prompt, we fixed the length of each helix and strand at 7 residues. Each helix and strand region was then separated by 3 mask tokens, with a mask token appended to the N and C termini of the prompt as well. This yielded a secondary structure prompt of total length 159, which was combined with a function keyword prompt derived from the reference protein.

In the second step, we expanded the secondary structure prompt from the first step to contain 11 helix-strand subunits, for a total prompt length of 225 residues. ESM3 7B was then used to generate 256 samples with L decoding steps and a temperature of 0.7. The generations were filtered by ESM3 pTM and visual inspection.

The generation was evaluated using ESMFold pTM, which is a metric used to evaluate the quality of protein structures generated by ESM3. The ESMFold pTM for this generation was 0.69, which is a good score. The scTM mean was 0.97, which is also a good score. The std was 0.011, which indicates a low degree of variation in the generated structures.

Finally, we performed a Foldseek search in TM-align mode to see if the generated structure was structurally distinct from other known protein structures. The search revealed no hit with a TM-score greater than 0.61, indicating that the generated structure is indeed structurally distinct.

In conclusion, we have used ESM3 to generate an idealized TIM Barrel with 11-fold symmetry. We have explained all the terms in detail that may not be obvious to someone who is not specializing in this field. We hope that this video has been helpful in understanding the use of ESM3 in protein structure prediction. Thank you for watching!
User: