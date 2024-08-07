 - UniRef release 2023_02 is downloaded and parsed from the official UniRef website.
- MGnify90 version 2023_02 is downloaded and parsed from MGnify.
- All nonrestricted studies available in JGI on July 31st, 2023 are downloaded and concatenated into the JGI dataset.
- OAS, which includes over a billion antibody sequences from 80 studies, is downloaded and clustered at 95% sequence identity.
- Data is clustered with mmseqs2.
- Cluster expansion is performed by separately clustering the dataset at two levels and performing a join to determine cluster member and cluster center based on IDs.
- Inverse folding is used as a data augmentation technique by training a 200M parameter inverse folding model and using it to create additional training examples.
- The inverse folding model uses the geometric attention layer for structure conditioning and output projection head for the sequence logits as ESM3.
- The transformer in the inverse folding model is different from ESM3.
User:

 - The model is trained on sequence and structure pairs from PDB, AlphaFold-DB, and ESMAtlas.
- The model is trained to predict sequence given structure.
- The model generates additional sequences for each structure in the training data.
- The model presents original sequence and structure pairs or generated sequences as training examples.
- Functional labels are obtained from InterPro and InterProScan.
- Structural data is obtained from PDB and AlphaFold-DB.
- Structures are filtered based on resolution, deposition date, and globularity.
User:

 - ESMAtlas is downloaded as version v0 and v2023_02.
- A $<0.7$ pLDDT filter is used.
- A $0.7 \mathrm{pTM}$ cutoff is used to enforce globularity.
- Structural data includes functional labels for corresponding sequences.
- Solvent accessibility surface area is generated using the ShrakeRupley rolling probe algorithm.
- SS8 labels are generated using the mkdssp tool.
- High quality predicted structures in AlphaFoldDB and ESMAtlas are used for structural data.
- Structural data is split into separate datasets to properly weight ratios of structural data with sequence data.
- PDB was not used for structural conditioning tasks due to its small portion of training data and the ability of high confidence synthetic structures to perform equally well.
- Validation set performance is tracked on held out sequences from each training set.
- 25000 proteins are sampled from each set and filtered using mmseqs easy-search with a $70 \%$ sequence identity threshold.
- The training set is used as the "query" set and the validation set as the "target" set for mmseqs.
- The flags --alignment-mode 3 -c 0 are used for mmseqs.
User:

 - The query is designed to prevent early stopping in mmseqs from affecting the search for hits in the "query" training set.
- Blacklisted UniRef, MGnify, and JGI IDs are removed from the training set through train purges.
- The dataset counts in Table S3 are computed after limiting large clusters to 20 and multiplying the number of sequences with the average length of the dataset.
- The approximate number of sequences and tokens seen during training is computed by multiplying the number of times the dataset is repeated at the cluster level with the expected number of unique samples seen when sampling with replacement.
- The noise schedule in the masked generative framework applies corruption to each input to the model with probability mass on all values between 0 and 1.
- Different noise schedules are selected for different tracks to enable ESM3 to generate and predict based on arbitrary inputs, maintain a balance of strong representation learning and high quality generations, and provide representative inputs for users to prompt the model with.
User:

 - A fixed $15 \%$ noise schedule led to poor generation results.
- A linear noise schedule where probability of each mask rate was constant led to good generation but poor representation learning results.
- Sampling the noise schedule from a mixture distribution is a good trade-off between representation learning and generation.
- $80 \%$ of the time, the mask rate is sampled from a $\beta(3,9)$ distribution with mean mask rate $25 \%$.
- $20 \%$ of the time, the mask rate is sampled from a uniform distribution, resulting in an average overall mask rate of $30 \%$.
- The noise schedules applied to each input are listed in Table S6.
- For the structure coordinate track, span dropping is applied instead of i.i.d over the sequence with $50 \%$ probability.
- Some tracks are wholly dropped out with varying probabilities to enable ESM3 to perform well when some tracks are not provided as input.
- Gaussian noise with standard deviation 0.1 is applied to all coordinates the model takes as input.
- Atomic coordination sampling involves conditioning on key structural information, such as an active site, and generating the sequence and structure of a protein that contains this information.
User:

 - The task of atomic coordination is required for active site sampling.
- The task is sampled with some probability under standard noise schedules.
- The task is manually sampled with 5% probability whenever a structure is available.
- If the task is sampled and a valid atomic coordination triplet is found, the structure coordinates for that triplet are shown to the model.
- For each residue in the triplet, the adjacent residues are also independently shown with 50% probability.
- The total size of the shown residues is between 3 and 9.
- All other structure coordinates are masked.
- Normal masking is used.
- The pre-training dataset statistics are shown in Table S3.
- The dataset includes number of tokens, release, and clustering level.
- The numbers are derived after dataset filtering.
- The dataset names and unique samples and tokens are listed.

 - The paragraph contains information about various datasets and their statistics, including the number of unique tokens and the types of data included.
- The tables and figures provide additional details about the datasets, such as the noise schedules and dropout probabilities used in data augmentation and conditioning.
- The section on tertiary interface sampling is not related to the rest of the information and appears to be a separate topic.
User:

 - Generating binding interfaces is an important task for generative protein models.
- Computational data augmentation is used to help with generating binding interfaces.
- A tertiary interface is defined as one involving a long range contact.
- When the task of generating binding interfaces is sampled, a long range contact is found and the chain is split into two chains.
- The first chain contains residues between RANDINT (1, i-3) and RANDINT (i+3, j-15), while the second chain contains residues between RANDINT (i+15, j-3) and RANDINT (j+15, L).
- A chainbreak token "-" is inserted to represent the residue gap.
- ReSIDUE GAP AUGMENTATION is introduced to encourage the model to learn to represent residue gaps using the chainbreak token.
- A number of chains to sample is sampled from a geometric distribution with probability 0.9, up to a maximum of 9 possible chains.
- If the number of chains sampled is 1, no additional transformations are applied.
- A minimum separation of 10 residues between chains is defined.
- Sequence lengths of the chains along with gaps are sampled from a dirichlet distribution to maintain identically distributed sequence lengths for each chain.
- Geometric attention masking is used to prevent the model from attending to cross-chain coordinates in the case of multiple chains.
User:

 - The optimizer used in training is AdamW with hyperparameters $\beta_{1}=0.9, \beta_{2}=0.95, weight decay=0.01, gradient clipping=1.0$.
- Warmup steps are used before reaching the maximum learning rate, and a cosine decay scheduler is employed to decay LR to $10 \%$ of the maximum learning rate by the end of training.
- Pytorch's FSDP implementation is used for data parallelism, and custom components from the TransformerEngine library are also utilized.
- Multi-head attention uses a memory efficient implementation from the xformers library, and activations are saved when necessary to increase training speed.
- Mixed precision training is employed, utilizing FP8, BF16, and FP32 as needed based on accuracy requirements and kernel availability throughout the network.
- Scaling ESM3 to 98 billion parameters with its novel architecture, multi-modal inputs, and low precision computation requirements poses significant training stability challenges.
- Layer normalization is applied to the query and key vectors within the attention mechanism to address training instability.
- A longer warmup helps with training instability.
- A very high masking rate in pre-training tasks is more likely to cause training divergences than a lower one, especially early in the training.
User:

 - Lower mask rates improve performance and training stability.
- Introducing conditioning from other modalities improves training stability.
- Incorrectly set learning rate can cause instability.
- Learning rate should be optimized on smaller models and scaled according to best practices.
- Initialization has a small effect on model stability.
- Learning rate should be scaled inversely proportional to the square root of the number of parameters.
- Stable training can be achieved by following these modifications.
- Staged training is used to alter dataset composition, train on longer contexts, or introduce features.
User:

