UniRef release 2023_02 is downloaded and parsed from the official UniRef website (71). MGnify90 version 2023_02 is downloaded and parsed from MGnify (35). All nonrestricted studies available in JGI on July 31st, 2023 are downloaded and concatenated into the JGI dataset (72). OAS, which includes over a billion antibody sequences from 80 studies, is downloaded and clustered at $95 \%$ sequence identity (36).

In all cases, data is clustered with mmseqs2 (73), with flags --kmer-per-seq 100 --cluster-mode 2 --cov-mode 1 -c 0.8 --min-seq-id $<$ seqid>.

In order to do cluster expansion, we separately cluster the dataset at the two levels, and perform a join to determine cluster member and cluster center based on IDs. We first sample a cluster center at the lower level, and then sample a sequence within the cluster at the higher level. As an example, for expansion of UniRef70 at $90 \%$, we first cluster UniRef at $70 \%$ sequence similarity using mmseqs linclust. Then, we cluster it separately at $90 \%$. Since each UniRef90 cluster center is by definition a UniRef70 cluster member, we filter out UniRef70 for all cluster members that are in the UniRef90 clusters. We can then drop all cluster centers without any members, which may occur due to the nondeterminism of clustering. This allows us to sample a UniRef70 center, and then a member within that cluster, of which each are $90 \%$ sequence similarity apart. For ease of dataloading, we additionally limit the number of data points within a cluster to 20 .

As data augmention we train a 200M parameter inverse folding model and use it to create additional training examples.

The inverse folding model uses the geometric attention layer for structure conditioning and output projection head for the sequence logits as ESM3. Unlike ESM3 the transformer stack alternates between blocks with geometric attention and standard attention. The model is trained on the sequence and structure pairs in PDB, AlphaFold-DB, and ESMAtlas, with the single training task of (and loss computed on) predicting sequence at the output given structure at the input. Model architecture and training methodology is otherwise substantially similar to ESM3.

This model is used to generate additional sequences corresponding to each structure in the training data for ESM3 ( 5 sequences per structure for ESMAtlas and AlphaFold$\mathrm{DB}, 64$ sequences per structure for the $\mathrm{PDB})$. When training ESM3, with $50 \%$ probability the original sequence and structure pair is presented to the model as a training example. The other $50 \%$ of the time one of these 5 sequences is paired with the structure as the training example seen by ESM3.

Functional labels are obtained from InterPro (38) and InterProScan (74), both version 95.0. All annotations for UniProtKB were downloaded from the InterPro website via the 'protein2ipr.dat.gz' file. InterProScan was applied to the entirety of MGnify 90 with flags --goterms --iprlookup --pathways --disable-precalc. The resultant values are taken as ground truth functional labels for model training.

We use all PDB chains, clustered by unique PDB ID and entity ID within the PDB structure. We filter to all structures deposited before May 1, 2020, determined by X-ray crystallography, and better than $9 \AA$ resolution. (37)

AlphaFoldDB is downloaded as the $v 4$ version specified on their website (4). We notice that structures with high pLDDT are disproportionately alpha helices. Therefore, we ensure globularity by measuring the number of long range ( $>12$ sequence distance) contacts in the chain. If this value is $<0.5 \mathrm{~L}$ with an $\mathrm{L}$ length protein, we omit it from our training set. We also filter out all proteins $<0.7$ pLDDT.

ESMAtlas is downloaded as version v0 and v2023_02. Similarly we use $\mathrm{a}<0.7$ pLDDT filter. We use a $0.7 \mathrm{pTM}$ cutoff as well to enforce globularity. High pTM structures tends to be more compact.

Structural data also includes any functional labels that exist for the corresponding sequence.

For solvent accessibility surface area, we use the ShrakeRupley rolling probe algorithm as implemented in biotite (75). This generates a set of real numbers, or a nan value when structural coordinates are not provided. Similarly, SS8 labels are generated using the mkdssp tool (76) and taken as ground truth labels.

In both cases, we use the set of high quality predicted structures in AlphaFoldDB and ESMAtlas. We split our datasets into structural and sequence data. Structural data is shown separately in order to weight the ratios of structural data (mostly synthetic) properly with the amount of sequence data (mostly real).

An oversight was that we did not manage to apply these augmentations to PDB. However, since PDB constituted a relatively small portion of our training data, and these structural conditioning tasks did not depend on precise sidechain positions, we reasoned that high confidence synthetic structures would perform equally well and annotation of PDB was not necessary.

We keep track of validation set performance on a set of held out sequences from each training set, UniRef, MGnify, and JGI. In order to properly hold out a sufficiently diverse set of validation proteins, we first sample 25000 proteins from each set. Then we use mmseqs easy-search to filter out proteins from this set with a $70 \%$ sequence identity threshold. We choose the set of proteins from our training set to be the "query" set, and the set of validation proteins as our "target" set for mmseqs. We use the flags --alignment-mode 3 -c 0.8 \{cov-mode 0 --max-seqs 300 --max-accept 3 --start-sens 2 -s 7 --sens-steps 3.

This query is designed such that early stopping in mmseqs will not affect if we find a hit in the "query" training set.

Train purges are run to generate a list of blacklisted UniRef, MGnify, and JGI IDs, which are removed from the training set.

The dataset counts in Table S3 are computed after limiting the large clusters to 20 . The number of tokens are computed by multiplying the number of sequences with the average length of the dataset.

In order to compute the approximate number of sequences and tokens seen during training, we first compute the number of times the dataset is repeated at the cluster level. Given the the number of repeats, we know the expected number of unique samples seen when sampling with replacement is $n\left(1-\left(1-\frac{1}{n}\right)^{k}\right)$ with a cluster of size $n$ and $k$ items selected. Computing this on the size of each cluster and number of dataset repeats results in the approximate number of tokens we present as presented in Table S4. Our largest model is trained on all of this data, while our smaller models use a portion of it depending on the model's token budget.

In the masked generative framework, corruption is applied to each input to the model. To enable generation, the amount of noise applied to an input is sampled from a distribution with probability mass on all values between 0 and 1 .

We select various noise schedules for different tracks with several goals in mind. First, ESM3 should see all combinations of tracks as input and output, enabling it to generate and predict based on arbitrary inputs. Second, ESM3 should maintain a balance of strong representation learning and high quality generations. Third, the type of inputs provided should be representative of what users would like to prompt the model with.
In initial experimentation, we found that a fixed $15 \%$ noise schedule led to poor generation results, while a linear noise schedule where probability of each mask rate was constant led to good generation but poor representation learning results. We find a good trade-off between representation learning and generation by sampling the noise schedule from a mixture distribution. $80 \%$ of the time, the mask rate is sampled from a $\beta(3,9)$ distribution with mean mask rate $25 \%$. $20 \%$ of the time, the mask rate is sampled from a uniform distribution, resulting in an average overall mask rate of $30 \%$.

The noise schedules applied to each input are listed in Table S6. For the structure coordinate track, we also modify the noise to be applied as span dropping, as opposed to i.i.d over the sequence with $50 \%$ probability. This ensures that the model sees contiguous regions of masked and provided coordinates, which better mimics the types of inputs users may provide.

Along with applying noise to each track, we want to ensure ESM3 is able to perform well when some tracks are not provided at all (e.g. to perform structure prediction when no structure is provided as input). We enable this by wholly dropping out some tracks with varying probabilities, listed in Table S6.

We apply gaussian noise with standard deviation 0.1 to all coordinates the model takes as input.

An interesting use case of generative protein models involves conditioning on key structural information, such as an active site, and generating the sequence and structure of a protein that contains this information. It is possible to define an atomic coordination task as 3 residues which are mutually in contact in structure space ( $C \alpha-C \alpha$ distance $<6 \AA$ ), but are distant in sequence space ( $\geq 10$ positions apart) (23). Training on this conditioning may enable the model to better perform the type of atomic coordination required for active site sampling.

While this task will be sampled with some probability under the standard noise schedules, we also manually sample the task with $5 \%$ probability whenever a structure is available. If the task is sampled and a valid atomic coordination triplet is found, the structure coordinates for that triplet are shown to the model. For each residue in the triplet, the adjacent residues are also independently shown with $50 \%$ probability, which leads to a total size of between 3 and 9 residues. All other structure coordinates are masked. Normal masking is applied to the other tracks.

Predicting and generating binding interfaces is another important task for generative protein models. To help with this capability, we add computational data augmentation that simulates the binding interface task.

We define a tertiary interface as one involving a long range contact $(C \alpha-C \alpha$ distance $<8 \AA, \geq 24$ sequence positions). When this task is sampled ( $5 \%$ probability whenever a structure is present), a long range contact is found, then the chain is split into two chains, each containing one side of the contact interface. Suppose the contacting positions are given by the indices $i, j$. Then the first chain will contain residues between [RANDINT $(1, i-3)$, RANDINT $(i+3, j-15)$ ], while the second chain will contain residues between [RANDINT $(i+15, j-3)$, RANDINT $(j+15, L)$ ]. This ensures there is always a residue gap between the two pseudochains. A chainbreak token "-" is inserted to represent the residue gap.

To encourage the model to learn to represent residue gaps using the chainbreak token, we introduce a task which randomly splits a single chain into multiple subchains.

First, a number of chains to sample is sampled from a geometric distribution with probability 0.9 , up to a maximum of 9 possible chains. If the number of chains sampled is 1 , no additional transformations are applied. A minimum separation of 10 residues between chains is defined. Sequence lengths of the chains along with gaps are sampled from a dirichlet distribution to maintain identically distributed sequence lengths for each chain. This transformation is applied to all samples.

In the case that multiple chains are provided to the model from either the interface sampling or pseudo-multimer augmentation tasks, we mask the geometric attention layer to prevent the model from attending to cross-chain coordinates. This simulates tasks where the structure of individual chains is known, but the interface is unknown.

We train all models using AdamW optimizer (77), with the following hyperparameters: $\beta_{1}=0.9, \beta_{2}=0.95$. We use a weight decay of 0.01 and gradient clipping of 1.0. We employ $5 \mathrm{~K}$ to $20 \mathrm{~K}$ warmup steps until reaching the maximum learning rate, and utilize a cosine decay scheduler to decay LR to $10 \%$ of the maximum learning rate by the end of training.

Our training codebase uses Pytorch. We use Pytorch's FSDP (78) implementation for data parallelism. We also use custom components from the TransformerEngine (79) library.

We have made several optimizations to increase the training speed of our models. For multi-head attention uses, we use the memory efficient implementation from the xformers library (80). We also save activations that are expensive to compute during training when necessary. We employ mixed precision training, utilizing FP8, BF16, and FP32 as needed based on accuracy requirements and kernel availability throughout our network.

Scaling ESM3 to 98 billion parameters with its novel architecture, multi-modal inputs, and low precision computation requirements poses significant training stability challenges. Our model is significantly deeper than its NLP counterparts, and literature has shown that deeper networks are harder to train due to attention collapse (81).

We observed training instability early in the architectural innovation phase, which we addressed through several changes. We apply layer normalization to the query and key vectors within the attention mechanism (82). We observe longer warm up helps (83). Another source of instability is the masking rate in pre-training tasks. We found that a very high masking rate is more likely to cause training divergences than a lower one, especially early in the training. Choosing a masking schedule biased towards lower mask rates improved both performance and training stability. Interestingly, the introduction of conditioning from other modalities also improves training stability, perhaps suggesting that stability is related to the degree of underspecification of a task.

An incorrectly set learning rate is another source of instability. To ensure the right balance between learning effectiveness and stability, we optimized the learning rate on smaller models and scaled it according to best practices as outlined in $(84,85)$. We find empirically that the initialization has a small effect on model stability, and the majority of stabilization can be gained from simply scaling the learning rate at the appropriate rate. By applying the rules in both width $-\mu \mathrm{P}$ and depth $-\mu \mathrm{P}$, we can simply scale the learning rate inversely proportional to the square root of the number of parameters, and find this results in stable training.

Following these modifications, we successfully trained our 98-billion-parameter model without any issues related to training instability.

We stage training to alter dataset composition, train on longer contexts that would be too expensive for the entire pre-training, or introduce features such as the taxonomy track (A.1.9.2.
