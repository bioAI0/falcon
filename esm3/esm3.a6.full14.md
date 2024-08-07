
==============================
We are releasing the ESM3 source code and model weights of an open model, ESM3-open. ESM3-open is a 1.4Bparameter model we trained without OAS antibody sequences and with precautionary risk mitigations for release to the academic research community.
------------------------------
 The ESM3 source code and model weights are being made available to the academic research community. The model, ESM3-open, is a 1.4B parameter model that was trained without OAS antibody sequences and with risk mitigation measures in place. This means that the model has been designed to minimize potential risks associated with its use. The source code and model weights are being released to allow researchers to use and build upon the model for their own research purposes.
User:
==============================
As part of this release, we follow guidance from the Principles for the Responsible Development of AI for Biological Design (107). We adopted precautionary risk mitigations, described in Appendix A.6.1, and performed risk evaluations, detailed in Appendix A.6.2. Additionally we conducted a review of the risks and benefits of releasing ESM3-open with experts from the scientific community. We provided reviewers access to ESM3-open, along with a detailed technical report on our risk evaluations. We received unanimous feedback from our reviewers that the benefits of releasing the model greatly outweigh any potential risks.
------------------------------
 As part of the release of ESM3-open, we have followed the guidance provided by the Principles for the Responsible Development of AI for Biological Design. We have taken precautionary measures to mitigate any potential risks, which are outlined in Appendix A.6.1. Additionally, we have conducted a thorough risk evaluation, which is detailed in Appendix A.6.2.

To ensure that we have considered all potential risks and benefits, we have also conducted a review with experts from the scientific community. We provided these experts with access to ESM3-open, as well as a detailed technical report on our risk evaluations.

After reviewing our risk evaluations and the potential benefits of releasing ESM3-open, all of our reviewers unanimously agreed that the benefits of releasing the model greatly outweigh any potential risks.
User:
==============================
We see this release as a first step and plan to work with the scientific community to continue to improve processes around responsible development. Open models enable the scientific community to better understand and reduce any potential risks of biological design tools. As our understanding develops alongside the capabilities of future models, we plan to continuously improve our evaluation frameworks, safeguards, and mitigation strategies.
------------------------------
 This statement suggests that the release of a new technology or tool is just the beginning of a larger process. The creators of this technology recognize that there may be potential risks associated with its use, and they are committed to working with the scientific community to address these risks. By using open models, the scientific community can better understand the technology and identify any potential risks. As the technology evolves and becomes more advanced, the creators plan to continuously evaluate and improve their strategies for mitigating any risks. Overall, this statement emphasizes the importance of collaboration and ongoing improvement in the development of new technologies.
User:
==============================
As a precaution, we filtered the training data of ESM3-open to minimize model performance on sequences of potential concern while otherwise maintaining performance. We also removed the capability for the model to follow prompts related to viruses and toxins.
------------------------------
 As a precautionary measure, we have taken steps to ensure that the ESM3-open model does not perform well on sequences that may be of concern. This was achieved by filtering the training data to minimize the model's performance on such sequences while maintaining its overall performance. Additionally, we have removed the model's ability to follow prompts related to viruses and toxins. These measures were taken to ensure that the model is safe and reliable for use by experts.
==============================
Filtering sequences of potential concern. Previous work has shown that the performance of protein language models is closely related to the number of similar sequences present in the training data (5). We therefore removed sequences aligned to potentially-concerning proteins from the training data in order to reduce the capability of ESM3-open on these sequences.
------------------------------
 The process of filtering sequences of potential concern involves removing certain sequences from the training data used to train protein language models. This is done to improve the performance of the model by reducing its capability on sequences that may be problematic or unreliable.

Previous research has shown that the performance of protein language models is closely related to the number of similar sequences present in the training data. Therefore, by removing sequences aligned to potentially-concerning proteins, the model can be trained on a more diverse and representative dataset, which can lead to better performance.

In summary, filtering sequences of potential concern is a technique used to improve the performance of protein language models by removing sequences that may be unreliable or problematic from the training data.
User:
==============================
We identified and removed sequences unique to viruses, as well as viral and non-viral sequences from the Select Agents and Toxins List (108) maintained by the CDC and USDA. The U.S. Department of Health \& Human Services recommends filtering based on the Select Agents list as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids (109).
------------------------------
 We have taken steps to ensure that our sequences do not contain any unique viral sequences or sequences that are listed on the Select Agents and Toxins List maintained by the CDC and USDA. This is in line with the recommendations provided by the U.S. Department of Health & Human Services for screening synthetic nucleic acids. By doing so, we are able to provide a safer and more reliable product for our users.
User:
==============================
\begin{tabular}{|c|c|c|c|}
\hline Protein & \begin{tabular}{l} 
Sequence \\
Identity to \\
esmGFP
\end{tabular} & \begin{tabular}{l} 
Mutations \\
to esmGFP
\end{tabular} & Aligned Sequence \\
\hline B8 & 0.93 & 15 & \begin{tabular}{l}
-MSKVEELIKPEMKMKLEMEGEVNGHKFSIEAEGEGKPYEGKQTIKAWSTT-GKLPAW \\
DILSTSLTYGFRMFTKYPEGLEEHDYFKQSFPEGYSWERTITYEDGATKVTSDISLED \\
GVLINKIKFKGTNFPSDGPVM-QKKTTGEEPSELITPDPATGGLKGEVKMRLKLEGGG \\
HLLADFKTTYRSKKKEK-LPLPGVHYVDHTIRNEKAPHPEGKEYVVQYETAVARLA-- \\
------
\end{tabular} \\
\hline esmGFP & 1.0 & 0 & \begin{tabular}{l}
-MSKVEELIKPDMKMKLEMEGEVNGHKFSIEAEGEGKPYEGKQTIKAWSTT-GKLPFAW \\
DILSTSLTYGNRAFTKYPEGLEQHDFFKQSFPEGYSWERTITYDGAAVKVTADISLED \\
GVLINKVKFKGENFPSDGPVM-QKKTTGEEASTELITPDATGGLKGEVKMRLKLEGGG \\
HLLADFKTTYRSKKKEK-LPLPGVHYVDHRIVNEKATHPEGKEYMIQYEHAVARLA-- \\
-------
\end{tabular} \\
\hline tagRFP & 0.58 & 96 & \begin{tabular}{l} 
MVSKGEELIKENMHMKLYMEGTVNNHHFKCTSEGEGKPYEGTQTMRIKVVEGGPLPFAF \\
DILATSFMYGSRTFINHTQGIP--DFEKQSFEEGTWERVVTYEDGGVLTATQDTSLQD \\
GCLIYNVKIRGVNEPSNGPVM-QKKTLGWEANTEMLY--PADGGLEGRTDMALKLVGGG \\
HLICNFKTTYRSKKPAKNLKMPGVYYVDHRL--ERIKEADKETYVEQHEVAVARYCDLP \\
SKLGHKLN
\end{tabular} \\
\hline eqFP578 & 0.53 & 107 & \begin{tabular}{l}
----MSELIKENMHMKLYMEGTVNNHHFKCTSEGERKPYEGTQTMKIKVVEGGPLPFAF \\
DILATSFMYGSKTFINHTQGIP-DDLFKQSFEEGTWERITTYEDGGVLTATQDTSLQN \\
GCIIYNVKINGVNFPSNGSVM-QKKTLGWEANTEMLY--PADGGLRGHSQMALKLVGGG \\
YLHCSFKTTYRSKKPAKNLKMPGFHFVDHRL--ERIKEADKETYVEQHEMAVAKYCDLP \\
SKLGHR--
\end{tabular} \\
\hline template & 0.38 & 112 & \begin{tabular}{l}
-MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTT-GKLPVPW \\
PTLVTTLTYGVQCFSRYPDHMKQHDFKSAMPEGYVQERIISKDDGNYKTRAEVKFEG \\
DTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYITADKQKNGIKANFKIRHNIEDGS \\
VQLADHYQQNTPIGDGP-VLLPDNHYLSTQSALSKDPN-EKRDHMVLLEFVTAAGI--
\end{tabular} \\
\hline avGFP & 0.36 & 146 & \begin{tabular}{l}
-MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTT-GKLPVPW \\
PTLVTTFSYGVQCESRYPDHMKQHDFFKSAMPEGYVEERTIFKRDGNYKKRAEVKFEG \\
DTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNYYMADKQKNGIKVNFKIRHNIEDGS \\
VQLADHYQQNTPIGDGP-VLLPDNHYLSTQSALSKDPN-EKRDHMVLLEFVTAAGITHG \\
MDELYK--
\end{tabular} \\
\hline
\end{tabular}
Table S14. Multiple sequence alignment of select GFP designs (B8, esmGFP) and reference proteins. Template is the full sequence of our template structure (PDB ID 1QY3), with chromophore slowing mutation A96R removed. tagRFP is the full sequence of the top hit returned by BLAST search of the nonredundant database $\mathrm{n} r$, avGFP and eqFP578 are from FPBase. Sequence identities for GFP designs are in general calculated as the number of non-gap matches at aligned positions, divided by the minimum length of the query and target ungapped sequences. Here, only sequence identities to esmGFP are shown. Similarly, the number of mutations to esmGFP are calculated as the number of mismatches at aligned positions where esmGFP does not have a gap.
![](https://cdn.mathpix.com/cropped/2024_07_04_ec502911ad4bd45c738bg-66.jpg?height=388&width=1672&top_left_y=226&top_left_x=190)
------------------------------
 The table shows a comparison of different GFP designs and reference proteins based on their sequence identity to esmGFP and the number of mutations they have compared to esmGFP. The aligned sequences are also provided for each protein. The table can be used to identify which GFP designs are most similar to esmGFP and which ones have the fewest mutations. This information can be useful for selecting the best GFP design for a particular application.
User:
==============================
Figure S23. ESM3-open is a powerful predictor of structure and function trained for open release. A: Structure Prediction ESM3open (blue) is competitive with ESMFold (orange) on structure prediction as measured by LDDT on CAMEO and CASP14/15. See Appendix A.3.4 for details on this evaluation. B: Representation Learning ESM3-open (blue) is competitive with ESM2-3B (orange) on representation learning as measured by contact prediction $\mathrm{P} @ \mathrm{~L}$ for finetuned representations. See Appendix A.3.3 for details on this evaluation. C: Function Keyword Prediction. ESM3-open function prediction performance, as measured by Mean Average Precision across function keywords. ESM3-open achieves 0.81 precision across all keywords, and 0.89 for the top $1 \mathrm{~K}$ most prevalent keywords in the validation set (CAMEO). We use the same evaluation framework as in Appendix A.1.8.2.2. We report both the macro and micro averages as in Fig. S8. In each of the preceding evaluations, the data mitigation minimally impacted performance, as compared to a compute-matched model without data mitigations (hatched blue). D: Zero-shot Fitness Prediction. Fitness prediction performance as measured by correlation (Spearman $\rho$ ) across 217 Deep Mutational Scanning datasets collated in ProteinGym. Left and right subplots indicate viral (left) and non-viral (right) DMS datasets. The four columns per group indicate different models. ESM3-open performs substantially worse than EVMutation (purple) on viral fitness prediction, while being competitive with ESM2 (orange) on non-viral fitness prediction. Viral fitness prediction was substantially impacted by the data mitigation, while non-viral fitness prediction was not (hatched blue).
------------------------------
 Figure S23 shows the performance of ESM3-open, a powerful predictor of structure and function, in various evaluations. In structure prediction, ESM3-open is competitive with ESMFold, as measured by LDDT on CAMEO and CASP14/15. In representation learning, ESM3-open is competitive with ESM2-3B, as measured by contact prediction $\mathrm{P} @ \mathrm{~L}$ for finetuned representations. In function keyword prediction, ESM3-open achieves 0.81 precision across all keywords and 0.89 for the top $1 \mathrm{~K}$ most prevalent keywords in the validation set (CAMEO). In zero-shot fitness prediction, ESM3-open performs substantially worse than EVMutation on viral fitness prediction, while being competitive with ESM2 on non-viral fitness prediction. The data mitigation minimally impacted performance in most evaluations, except for viral fitness prediction.
User:
==============================
To filter data, we create two denylists: the Viral Denylist and the Select Agent Denylist. We then remove all sequences from the training set that are detected to align to those in the denylists by MMseqs2 at or above a given sequence identity threshold.
------------------------------
 To filter data, we create two denylists: the Viral Denylist and the Select Agent Denylist. These denylists contain sequences that we want to exclude from our analysis. We then use MMseqs2, a sequence alignment tool, to compare the sequences in our training set to those in the denylists. If a sequence in the training set aligns to a sequence in the denylist at or above a certain sequence identity threshold, we remove it from the training set. This helps us to ensure that our analysis is focused on the sequences that are relevant to our research question and not contaminated by sequences that we want to exclude.
User:
==============================
To create the Viral Denylist, we identify $\sim 4 \mathrm{M}$ sequences that are annotated as viral in UniProt and align almost exclusively to other viral sequences in UniProt. This gives us a procedure that removes viral proteins with both high sensitivity and specificity (as measured by UniProt taxonomic annotations). To create the Select Agents Denylist we identify all sequences in UniProt belonging to organisms on the Select Agents and Toxins List (108). This process gives us $147 \mathrm{~K}$ non-viral sequences and $40 \mathrm{~K}$ additional viral sequences.
------------------------------
 To create the Viral Denylist, we use a process that identifies approximately 4 million sequences that are annotated as viral in UniProt and align almost exclusively to other viral sequences in UniProt. This allows us to remove viral proteins with high sensitivity and specificity, as measured by UniProt taxonomic annotations.

To create the Select Agents Denylist, we identify all sequences in UniProt that belong to organisms on the Select Agents and Toxins List (108). This process results in 147,000 non-viral sequences and an additional 40,000 viral sequences.
User:
==============================
For each denylist, MMseqs was used to query against the full set of training databases, (including PDB, UniRef, MGnify, and JGI) and all hits were removed from the training set. This filter removes a total of $10.6 \mathrm{M}$ sequences across all training sets.
------------------------------
 MMseqs is a software tool used for sequence alignment and database searching. In this case, it was used to query against a set of training databases, including PDB, UniRef, MGnify, and JGI. The purpose of this query was to identify any sequences that were similar to those in the training set, which could potentially bias the results of the analysis.

Once the query was complete, all hits were removed from the training set. This means that any sequences that were found to be similar to those in the training set were excluded from further analysis. The total number of sequences removed from the training set was $10.6 \mathrm{M}$.

This filtering step is important because it helps to ensure that the training set is representative of the true diversity of sequences in the dataset. By removing sequences that are too similar to those in the training set, we can avoid overfitting and improve the accuracy of our analysis.
User:
==============================
Removal of keywords of concern. There are a number of keyword prompts associated with viruses and toxins that we aim to remove. We first identify a list of harmful keywords with the following steps:
------------------------------
 1. Research: We conduct extensive research to identify keywords that are commonly associated with viruses and toxins.

2. Analysis: We analyze the keywords to determine their relevance and potential harm.

3. Prioritization: We prioritize the keywords based on their level of concern and potential impact.

4. Removal: We remove the harmful keywords from our system to prevent any potential harm or damage.

By removing these harmful keywords, we can ensure that our system remains safe and secure for all users.
User:
==============================
1. We curate a list of filter terms associated with viruses and toxins. The full filter term list is available upon request.
------------------------------
 I do not have access to the specific list of filter terms associated with viruses and toxins that you are referring to. however, based on the information provided, it seems that the list is curated by a team of experts and is used to filter out content related to viruses and toxins. the full list of filter terms is available upon request, which suggests that it is not publicly available and may be used for specific purposes such as content moderation or research.
User:
==============================
2. We then identify all InterPro tags whose free-text term names contain at least one of the filter terms.
------------------------------
 Certainly! 

In this context, "InterPro tags" refer to specific protein domains or functional sites that have been identified and annotated within a protein sequence. These tags are assigned based on the presence of certain sequence motifs or structural features that are known to be associated with specific functions or activities.

The "filter terms" mentioned in the statement refer to a set of keywords or phrases that are of interest to the user. For example, if the user is interested in identifying all proteins that contain a specific domain or functional site, they might provide a list of keywords or phrases that are associated with that domain or site.

So, when we say that we "identify all InterPro tags whose free-text term names contain at least one of the filter terms," we mean that we are searching through the list of InterPro tags and looking for any tags that have names or descriptions that include at least one of the keywords or phrases provided by the user. This allows us to quickly and efficiently identify all proteins that contain the desired domain or functional site, without having to manually search through each individual protein sequence.
User:
==============================
3. We identify keywords that are associated with flagged InterPro tags but that are not associated with nonflagged InterPro tags. We remove those keywords. Keywords which are associated with both flagged and non-flagged InterPro tags (e.g. "extracellular region") are not removed.
------------------------------
 This process involves analyzing InterPro tags, which are used to annotate protein sequences with functional information. The goal is to identify keywords that are specifically associated with flagged InterPro tags, which indicate a potential functional annotation error. These keywords are then removed from the analysis to improve the accuracy of the functional annotation. However, keywords that are associated with both flagged and non-flagged InterPro tags are not removed, as they may still provide useful information for the functional annotation.
User:
==============================
4. We additionally remove all keywords that themselves directly contain one of the filter terms
------------------------------
 Certainly! 

In this context, "filter terms" refer to specific words or phrases that are deemed irrelevant or unwanted for the purpose of the analysis or search being conducted. 

The statement "We additionally remove all keywords that themselves directly contain one of the filter terms" means that any keywords that contain the filter terms are also removed from the analysis or search results. 

For example, if the filter terms are "spam" and "junk", any keywords that contain those words, such as "spammy" or "junkmail", would also be removed from the analysis or search results. 

This helps to ensure that the analysis or search results are more relevant and focused on the desired keywords, without being cluttered by irrelevant or unwanted terms.
==============================
Of the original 68,103 keywords that ESM3 is trained with, this filter removes a total of 9,462 (14\%), creating a new vocabulary of 58,641 keywords.
------------------------------
 The ESM3 is a language model that has been trained with a vocabulary of 68,103 keywords. However, a filter has been applied to this vocabulary, which has removed a total of 9,462 keywords (14%). As a result, the new vocabulary of the ESM3 now consists of 58,641 keywords. This means that the ESM3 has been trained with a reduced set of keywords, which may affect its performance in certain tasks.
User:
==============================
The function vocabulary is defined via vectors representing Term Frequency Inverse Document Frequency (TF-IDF) which are then tokenized using Locality Sensitive Hashing (LSH), as previously described in Appendix A.1.8. To remove flagged keywords, they are first removed from the TF-IDF vocabulary by removing the entries corresponding to flagged keywords. This reduces the TF-IDF vector size to 58,641 . The LSH tokenization is defined by 64 hyperplanes, each defined in the TF-IDF space, i.e. a Euclidean space with one dimension per keyword. We redefine the hyperplanes to be in the reduced space by removing the dimensions corresponding to the flagged keywords. This per-
manently removes the information required for tokenization of the flagged keywords. This mitigation is highly selective and does not change the tokenization for any non-flagged keywords.
------------------------------
 The function vocabulary is defined using vectors that represent Term Frequency Inverse Document Frequency (TF-IDF). These vectors are then tokenized using Locality Sensitive Hashing (LSH), which is described in Appendix A.1.8. To remove flagged keywords, they are first removed from the TF-IDF vocabulary by deleting the corresponding entries. This reduces the size of the TF-IDF vector to 58,641. The LSH tokenization is defined by 64 hyperplanes, each of which is defined in the TF-IDF space, which is a Euclidean space with one dimension per keyword. The hyperplanes are redefined to be in the reduced space by removing the dimensions corresponding to the flagged keywords. This permanently removes the information required for tokenization of the flagged keywords. This mitigation is highly selective and does not change the tokenization for any non-flagged keywords.
User:
==============================
\section*{A.6.2. ESM3-open Evaluations}
------------------------------
 I'm sorry, I cannot provide an explanation without additional context or information about what "ESM3-open Evaluations" refers to. Can you please provide more details or context so I can better assist you?###
==============================
In the section below, we outline our evaluations of ESM3open performance. When appropriate, we compare ESM3open to either existing open models, (e.g. ESM2 or ESMFold), or to a compute-matched version of ESM3-open, trained without any data mitigations.
------------------------------
 ESM3open is a model that has been evaluated for its performance in various tasks. The evaluations are compared to other open models such as ESM2 or ESMFold, or to a version of ESM3-open that has been trained without any data mitigations. These comparisons help to determine the effectiveness of ESM3open in different scenarios and provide insights into its strengths and weaknesses.
User:
==============================
Structure Prediction In Fig. S23A, we show that ESM3open achieves competitive performance on structure prediction as measured by LDDT on CASP14, 15 and CAMEO, showing very slight degradation from our compute-matched 1.4B model without data filtering. The evaluation framework is described in Appendix A.3.4.
------------------------------
 In Fig. S23A, the performance of ESM3open on structure prediction is evaluated using LDDT on CASP14, 15, and CAMEO. The results show that ESM3open achieves competitive performance compared to our compute-matched 1.4B model without data filtering, with only slight degradation. The evaluation framework used for this analysis is described in Appendix A.3.4.
User:
==============================
We also measure the ability of ESM3 to predict the structure of a subset of viral proteins. In Fig. S23A we evaluate structure prediction on a set of structures derived from viruses that were purged from the PDB training set. For the chains in PDB that were $>70 \%$ sequence identity hits to the Viral Denylist, we cluster at $40 \%$ sequence identity and then select the longest chain (with length $\leq$ 1024) from each cluster. ESMfold and ESM3-open achieved an average LDDT of 0.66 and 0.63 , respectively, on the viral structures. Without the data mitigation, a compute-matched ESM3-open would have achieved an average LDDT of 0.66. This is substantially worse than the performance on generic structure prediction on CAMEO, and CASP14, where ESMFold achieved an average LDDT of 0.86 and 0.73, and ESM3open achieved an average of LDDT of 0.83 and 0.70.
------------------------------
 The study evaluated the ability of ESM3 to predict the structure of a subset of viral proteins. The researchers used a set of structures derived from viruses that were not included in the PDB training set. They clustered the chains at 40% sequence identity and selected the longest chain from each cluster. The results showed that ESMfold and ESM3-open achieved an average LDDT of 0.66 and 0.63, respectively, on the viral structures. However, without data mitigation, a compute-matched ESM3-open would have achieved an average LDDT of 0.66, which is worse than the performance on generic structure prediction on CAMEO and CASP14.
User:
==============================
Representation Learning. ESM3-open achieves strong performance on representation learning, slightly outperforming ESM2 (3B) on contact prediction as measured by precision at $\mathrm{L}(\mathrm{P} @ \mathrm{~L})$ on structures derived from CASP14/15, and CAMEO, see Fig. S23B. The evaluation framework is described in Appendix A.3.3.
------------------------------
 The text is discussing the performance of a machine learning model called ESM3-open in the task of representation learning. The model is being compared to another model called ESM2 (3B) in terms of their ability to predict protein contacts. The evaluation of the models is based on a metric called precision at L(P@L) on structures derived from CASP14/15 and CAMEO. The evaluation framework is further explained in Appendix A.3.3. The results show that ESM3-open performs slightly better than ESM2 (3B) in this task.
User:
==============================
Function Keyword Prediction. ESM3-open is able to predict function keywords for proteins in a validation set derived from UniRef and annotated with InterProScan, see Fig. S23C. ESM3-open achieves a Mean Average Precision for all keywords of 0.81 (macro average), and a precision of 0.89 (micro average) for the top 1000 keywords, discarding common terms such as "the". The evaluation framework is the same as that described in Appendix A.1.8.2.2.
------------------------------
 Function Keyword Prediction is a process of predicting the function of a protein based on its amino acid sequence. ESM3-open is a tool that can predict function keywords for proteins in a validation set derived from UniRef and annotated with InterProScan. The tool achieves a Mean Average Precision of 0.81 for all keywords and a precision of 0.89 for the top 1000 keywords, excluding common terms such as "the". The evaluation framework used is the same as that described in Appendix A.1.8.2.2.
User:
==============================
Zero-shot Viral Fitness Prediction. We measure the ability of ESM3 to identify viable sequences and understand the effects of mutations on viral proteins. The evaluation consists of the single mutant variants from 217 Deep Mutational Scanning (DMS) datasets collected in ProteinGym (110).
This includes 28 DMS landscapes from viral proteins and 189 from other proteins. We evaluate the correlation (Spearman $\rho$ ) between the predicted variant effect and measured variant effect. The predicted variant effect is measured as the difference between the logit value for the variant allele and the logit value of the wildtype allele at a given masked position (16).
------------------------------
 Zero-shot Viral Fitness Prediction is a method that uses the ESM3 model to predict the effects of mutations on viral proteins. This is done by measuring the ability of ESM3 to identify viable sequences and understand the effects of mutations on viral proteins. The evaluation process involves using single mutant variants from 217 Deep Mutational Scanning (DMS) datasets collected in ProteinGym.

The evaluation includes 28 DMS landscapes from viral proteins and 189 from other proteins. The correlation between the predicted variant effect and measured variant effect is measured using the Spearman $\rho$ correlation coefficient. The predicted variant effect is calculated as the difference between the logit value for the variant allele and the logit value of the wildtype allele at a given masked position.

Overall, Zero-shot Viral Fitness Prediction is a powerful tool for predicting the effects of mutations on viral proteins, which can help researchers better understand the evolution and spread of viruses.
User:
==============================
First, we compare the performance of ESM3-open to a compute-matched version of ESM3-open which did not undergo any data filtering. Applying data filtering as a mitigation reduces average Spearman $\rho$ performance on viral fitness prediction from 0.28 (ESM3-small) to 0.17 (ESM3-open), while performance on non-viral proteins is not adversely affected, changing from 0.46 (ESM3-small) to 0.45 (ESM3-open). We also compare the performance of ESM3-open to existing open model baselines. Fig. S23D assesses performance relative to the EVMutation (111) baseline. EVMutation is a Markov Random Field model (not deep learning-based) trained on a multiple sequence alignment of the target protein. BLOSUM62 is a baseline based on amino acid substitution frequencies. After mitigations, ESM3-open performance on viral landscapes is low compared to EVMutation and on-par with BLOSUM62.
------------------------------
 The study compares the performance of ESM3-open, a deep learning-based model, to a compute-matched version of ESM3-open that did not undergo data filtering. The results show that applying data filtering as a mitigation reduces the average Spearman $\rho$ performance on viral fitness prediction from 0.28 to 0.17, while performance on non-viral proteins remains unchanged. The study also compares the performance of ESM3-open to existing open model baselines, including EVMutation and BLOSUM62. After mitigations, ESM3-open performance on viral landscapes is lower than EVMutation but on-par with BLOSUM62.
User:
==============================

------------------------------
 I'm sorry, I need more context to understand what you would like me to explain to an expert. Can you please provide more information or a specific topic you would like me to explain?