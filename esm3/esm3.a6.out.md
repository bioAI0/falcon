 - ESM3-open is a 1.4B parameter model trained without OAS antibody sequences.
- ESM3-open is an open model.
- ESM3-open was trained with precautionary risk mitigations.
- ESM3-open underwent risk evaluations.
- ESM3-open underwent a review of risks and benefits with experts from the scientific community.
- ESM3-open received unanimous feedback that the benefits of releasing the model outweigh any potential risks.
- ESM3-open is a first step towards responsible development.
- Open models enable the scientific community to better understand and reduce potential risks of biological design tools.
- ESM3-open underwent filtering of sequences of potential concern.
- ESM3-open had the capability to follow prompts related to viruses and toxins removed.
- ESM3-open's performance on sequences of potential concern was minimized while maintaining performance.
- ESM3-open's performance is closely related to the number of similar sequences present in the training data.
- ESM3-open's training data was filtered to minimize model performance on sequences of potential concern.
User:

 - The authors identified and removed sequences unique to viruses, as well as viral and non-viral sequences from the Select Agents and Toxins List.
- The U.S. Department of Health \& Human Services recommends filtering based on the Select Agents list as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to filter sequences.
- The authors used the Select Agents and Toxins List to identify and remove sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique to viruses and non-viral sequences as part of their Screening Framework Guidance for Providers and Users of Synthetic Nucleic Acids.
- The authors used the Select Agents and Toxins List to identify and remove sequences unique to viruses and non-viral sequences.
- The authors used the Select Agents and Toxins List to filter out sequences unique

 - The table contains information on multiple sequence alignment of select GFP designs and reference proteins.
- The sequence identities for GFP designs are calculated as the number of non-gap matches at aligned positions divided by the minimum length of the query and target ungapped sequences.
- The number of mutations to esmGFP are calculated as the number of mismatches at aligned positions where esmGFP does not have a gap.
- ESM3-open is a powerful predictor of structure and function trained for open release.
- ESM3-open is competitive with ESMFold on structure prediction as measured by LDDT on CAMEO and CASP14/15.
- ESM3-open is competitive with ESM2-3B on representation learning as measured by contact prediction $\mathrm{P} @ \mathrm{~L}$ for finetuned representations.
- ESM3-open is also competitive with ESM2-3B on function keyword prediction.
User:

 - ESM3-open achieves 0.81 precision across all keywords and 0.89 for the top $1 \mathrm{~K}$ most prevalent keywords in the validation set (CAMEO).
- ESM3-open performs substantially worse than EVMutation (purple) on viral fitness prediction, while being competitive with ESM2 (orange) on non-viral fitness prediction.
- Viral fitness prediction was substantially impacted by the data mitigation, while non-viral fitness prediction was not.
- To filter data, two denylists are created: the Viral Denylist and the Select Agent Denylist.
- The Viral Denylist is created by identifying $\sim 4 \mathrm{M}$ sequences that are annotated as viral in UniProt and align almost exclusively to other viral sequences in UniProt.
- The Select Agent Denylist is created by identifying all sequences in UniProt belonging to organisms on the Select Agents and Toxins List (108).
- For each denylist, sequences are removed from the training set that are detected to align to those in the denylists at or above a given sequence identity threshold.
User:

 - MMseqs was used to query against the full set of training databases, including PDB, UniRef, MGnify, and JGI.
- All hits were removed from the training set.
- A total of $10.6 \mathrm{M}$ sequences were removed across all training sets.
- A list of harmful keywords associated with viruses and toxins was curated.
- InterPro tags containing at least one of the filter terms were identified.
- Keywords associated with flagged InterPro tags but not non-flagged InterPro tags were removed.
- Keywords containing one of the filter terms were also removed.
- A total of 9,462 (14\%) keywords were removed from the original 68,103 keywords.
- The TF-IDF vocabulary was reduced to 58,641 keywords.
- The LSH tokenization was redefined in the reduced space by removing the dimensions corresponding to the flagged keywords.
- This permanently removes the information required for tokenization of the flagged keywords.
User:

 - ESM3-open achieves competitive performance on structure prediction as measured by LDDT on CASP14, 15 and CAMEO.
- ESM3-open achieves strong performance on representation learning, slightly outperforming ESM2 (3B) on contact prediction as measured by precision at $\mathrm{L}(\mathrm{P} @ \mathrm{~L})$ on structures derived from CASP14/15, and CAMEO.
- ESM3-open is able to predict function keywords for proteins in a validation set derived from UniProt.
- ESM3-open achieves an average LDDT of 0.63 on a set of structures derived from viruses that were purged from the PDB training set.
- ESM3-open achieves an average LDDT of 0.83 and 0.70 on CASP14 and CAMEO, respectively, without data mitigation.
- ESM3-open achieves an average LDDT of 0.66 on the viral structures without data mitigation.
- ESM3-open achieves an average LDDT of 0.70 on CASP14 and CAMEO with data mitigation.
- ESM3-open achieves an average LDDT of 0.66 on the viral structures with data mitigation.
- ESM3-open achieves an average LDDT of 0.86 and 0.73 on CASP14 and CAMEO, respectively, with data mitigation.
- ESM3-open achieves an average LDDT of 0.83 and 0.70 on CASP14 and CAMEO, respectively, without data mitigation.
- ESM3-open achieves an average LDDT of 0.66 on the viral structures without data mitigation.
- ESM3-open achieves an average LDDT of 0.70 on CASP14 and CAMEO with data mitigation.
- ESM3-open achieves an average LDDT of 0.66 on the viral structures with data mitigation.
- ESM3-open achieves an average LDDT of 0.86 and 0.73 on CASP14 and CAMEO, respectively, with data mitigation.
User:

 - ESM3-open achieves a Mean Average Precision of 0.81 for all keywords.
- ESM3-open has a precision of 0.89 for the top 1000 keywords.
- The evaluation framework is the same as that described in Appendix A.1.8.2.2.
- ESM3 is evaluated for its ability to identify viable sequences and understand the effects of mutations on viral proteins.
- The evaluation consists of the single mutant variants from 217 Deep Mutational Scanning datasets.
- The predicted variant effect is measured as the difference between the logit value for the variant allele and the logit value of the wildtype allele at a given masked position.
- ESM3-open is compared to a compute-matched version of ESM3-open which did not undergo any data filtering.
- Applying data filtering as a mitigation reduces average Spearman $\rho$ performance on viral fitness prediction from 0.28 to 0.17.
- ESM3-open performance on non-viral proteins is not adversely affected by data filtering.
- ESM3-open is compared to existing open model baselines.
- ESM3-open performance on viral landscapes is low compared to EVMutation and on-par with BLOSUM62 after mitigations.

