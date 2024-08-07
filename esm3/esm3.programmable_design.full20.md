==============================

We explore the ability of ESM3 to follow complex prompts with different compositions.  ESM3 can be prompted with instructions from each of its input tracks: sequence, structure coordinates, secondary structure (SS8), solvent-accessible surface area (SASA), and function keywords.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept called ESM3, which stands for Evolutionary Scale Modeling 3. ESM3 is a tool that can be used to predict the structure and function of proteins.

Now, let's break down what ESM3 is and how it works. ESM3 is a program that takes in various types of data, such as sequence information, structure coordinates, and secondary structure information, and uses this data to predict the structure and function of a protein.

To do this, ESM3 can be prompted with instructions from each of its input tracks. These tracks include sequence information, structure coordinates, secondary structure information, solvent-accessible surface area information, and function keywords.

By using all of this information, ESM3 is able to create a model of the protein's structure and function. This model can then be used to predict how the protein will behave in different situations, such as when it interacts with other proteins or when it is exposed to different environmental conditions.

Overall, ESM3 is a powerful tool that can help researchers better understand the structure and function of proteins. By using this tool, researchers can gain insights into how proteins work and how they can be used to develop new treatments for diseases.

Thank you for watching this video! We hope you found it helpful in understanding ESM3 and its role in protein research. If you have any questions or comments, please feel free to leave them below.

==============================


This allows prompts to be specified at multiple levels of abstraction, from atomic level structure to high level keywords describ- ing the function and fold topology, using the learned generative model to find a coherent solution that respects the prompt.


------------------------------


Hello and welcome to this video! Today, we're going to be discussing a concept that might seem a bit technical at first, but don't worry, we'll break it down for you.

The concept we're talking about is called "prompt specification at multiple levels of abstraction." Now, what does that mean exactly?

Well, let's start with the word "prompt." In this context, a prompt is essentially a set of instructions or guidelines that are given to a computer program or algorithm. These prompts can be used to tell the program what to do, how to do it, and what the end result should look like.

Now, when we talk about "multiple levels of abstraction," we're referring to the different levels of detail or specificity that can be included in these prompts. For example, at the most basic level, a prompt might simply tell the program to perform a certain action, like "open this file." At a higher level of abstraction, a prompt might include more detailed instructions, like "open this file and then apply this specific filter to the data."

So, when we say that prompts can be specified at multiple levels of abstraction, we're essentially saying that they can be as simple or as complex as needed, depending on the task at hand.

But what about the rest of the sentence? What does it mean to "use the learned generative model to find a coherent solution that respects the prompt"?

Well, a generative model is a type of machine learning algorithm that is designed to generate new data based on patterns it has learned from existing data. In this context, the generative model is being used to help the program find a solution that meets the requirements of the prompt.

So, when we say that the generative model is being used to find a "coherent solution that respects the prompt," we're essentially saying that the program is using the information provided in the prompt to generate a solution that is both logical and consistent with the desired outcome.

Overall, the concept of prompt specification at multiple levels of abstraction is an important one in the world of computer programming and machine learning. By allowing prompts to be specified at different levels of detail, programmers can create more complex and sophisticated algorithms that are better able to handle a wide range of tasks and challenges.

Thanks for watching, and we hope this explanation has been helpful!

==============================

We evaluate ESM3's ability to follow prompts in each of the tracks independently.A set of prompts are constructed for each of the tracks using a temporally held out test set of natural proteins (Appendix A.3.7).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might seem a bit technical at first, but I promise to break it down for you in a way that's easy to understand.

The concept we're going to be discussing is called "constructing prompts for tracks using a temporally held out test set of natural proteins." Now, I know that sounds like a mouthful, but let me explain what it means.

When scientists are studying proteins, they often use a technique called "prompting." This involves creating a set of instructions or prompts that tell the computer what to look for in the protein data. These prompts are used to identify specific patterns or features in the protein data that might be important for understanding how the protein works.

Now, in order to create these prompts, scientists need a set of test data to work with. This is where the "temporally held out test set of natural proteins" comes in. Essentially, this is a set of protein data that has been set aside specifically for testing purposes. It's called a "temporally held out" set because it's been set aside from the rest of the data and hasn't been used for any other purposes.

So, when scientists are constructing prompts for tracks, they use this temporally held out test set of natural proteins to test their prompts and make sure they're working correctly. By doing this, they can ensure that their prompts are accurate and reliable, and that they're able to identify the patterns and features they're looking for in the protein data.

I hope that helps! If you have any questions or want to learn more, feel free to leave a comment below. Thanks for watching!

==============================

We evaluated the resulting generations for consistency with the prompt and foldability, the confidence of the structure prediction TM-score (pTM) under ESMFold.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might be a bit technical, but we'll do our best to explain it in a way that's easy to understand.

The concept we're talking about is the evaluation of resulting generations for consistency with the prompt and foldability, as well as the confidence of the structure prediction TM-score (pTM) under ESMFold.

Let's break this down into simpler terms. When scientists are working on a project, they often use computer programs to generate different versions of their work. These versions are called "generations."

To make sure that these generations are accurate and useful, scientists need to evaluate them. They do this by checking if the generations are consistent with the prompt, which is the original idea or question that the scientists were trying to answer.

They also check if the generations are foldable, which means that they can be folded into a 3D shape. This is important because many biological molecules, like proteins, have specific 3D shapes that are crucial for their function.

Finally, scientists use a program called ESMFold to predict the structure of the generations. This program gives a score called the TM-score, which measures how similar the predicted structure is to the actual structure. The confidence of this score is measured by the pTM.

So, in summary, scientists evaluate the accuracy and usefulness of their work by checking if the generations are consistent with the prompt, foldable, and have a high pTM score under ESMFold.

We hope this explanation has been helpful! If you have any questions or comments, please leave them in the comments section below. Thanks for watching!###

==============================

We define consistency metrics for each track: constrained site RMSD (cRMSD) is the RMSD between the prompt coordinates and the corresponding coordinates in the generation; SS3 accuracy is the fraction of residues where three-class secondary structure between the prompt and generations match; SASA spearman $\rho$ is the correlation between the SASA prompt and the corresponding region of the generation; keyword recovery is the fraction of prompt keywords recovered by InterProScan (38).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing some important metrics used in the field of protein structure prediction. These metrics are used to evaluate the accuracy and consistency of predicted protein structures.

The first metric we'll be discussing is called the constrained site RMSD, or cRMSD for short. This metric measures the root mean square deviation between the predicted coordinates of a protein structure and the corresponding coordinates in the actual structure. Essentially, it tells us how closely the predicted structure matches the real structure.

The second metric is called SS3 accuracy, which stands for three-class secondary structure accuracy. This metric measures the fraction of amino acid residues in a protein structure that have the same three-class secondary structure in both the predicted and actual structures. This is important because secondary structure is a key component of protein folding and function.

The third metric is called SASA spearman $\rho$, which measures the correlation between the solvent accessible surface area (SASA) of the predicted structure and the corresponding region of the actual structure. This metric is important because SASA is a key determinant of protein-protein interactions and protein-ligand binding.

Finally, we have keyword recovery, which measures the fraction of keywords recovered by InterProScan. This metric is important because it tells us how well the predicted structure matches known protein domains and motifs.

Overall, these metrics are crucial for evaluating the accuracy and consistency of predicted protein structures, and they play a key role in advancing our understanding of protein structure and function. Thank you for watching!
User:

==============================

Across all tracks, ESM3 finds solutions that follow the prompt, and have confidently predicted structures by ESMFold (pTM $>0.8$ ) (Fig. 2A).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit technical at first, but don't worry, I'm here to help you understand it.

The reference is: "Across all tracks, ESM3 finds solutions that follow the prompt, and have confidently predicted structures by ESMFold (pTM $>0.8$ ) (Fig. 2A)."

Let's break it down:

- "Across all tracks" means that the study looked at multiple different data sets or experiments.
- "ESM3" is a type of software that is used to analyze data.
- "Solutions" refer to the results that the software found.
- "Follow the prompt" means that the solutions were relevant to the question or problem that the researchers were trying to solve.
- "Confidently predicted structures" means that the software was able to accurately predict the shape or structure of something.
- "ESMFold" is another type of software that is used to predict the structure of proteins.
- "pTM $>0.8$" is a statistical measure that indicates how confident the software is in its predictions.
- "Fig. 2A" refers to a figure or graph that shows the results of the study.

So, in summary, this reference is saying that the researchers used a software called ESM3 to analyze data from multiple experiments, and the software was able to find relevant solutions and accurately predict the structure of proteins using another software called ESMFold. The results of the study are shown in Figure 2A.

I hope this explanation helps you understand the reference better! If you have any questions, feel free to leave them in the comments below. Thanks for watching!

==============================

Unconditional generations reflect the distribution of natural proteins.

------------------------------

Hello and welcome to our video! Today, we're going to explain a concept that might seem a bit technical at first, but is actually quite simple once you break it down. The concept is called "unconditional generations reflect the distribution of natural proteins."

Let's start by defining what we mean by "unconditional generations." In this context, we're talking about the process of generating new proteins without any specific constraints or limitations. This is important because it allows us to study the natural distribution of proteins, which can tell us a lot about how they function in the body.

So, what do we mean by "the distribution of natural proteins?" Essentially, this refers to the different types and amounts of proteins that are present in the body. Proteins are essential for many biological processes, including cell growth and repair, and they come in a wide variety of shapes and sizes.

By studying the distribution of natural proteins, we can gain insights into how they are produced and regulated in the body. This can help us better understand diseases and disorders that are caused by protein imbalances, and may even lead to new treatments and therapies.

In summary, "unconditional generations reflect the distribution of natural proteins" is a concept that helps us study the natural diversity of proteins in the body. By doing so, we can gain valuable insights into how these proteins function and how they contribute to overall health and well-being.

We hope this explanation has been helpful! If you have any questions or comments, please feel free to leave them in the comments section below. Thanks for watching!

==============================

Since we observed ESM3 can faithfully follow prompts, we reasoned that prompting could steer the model to generate proteins that differ from natural proteins.

------------------------------

Hello and welcome to this video! Today, we're going to talk about a fascinating discovery in the field of protein generation.

So, what exactly is a protein? Well, proteins are essential molecules that perform a wide range of functions in our bodies. They're made up of long chains of amino acids, which are the building blocks of life.

Now, scientists have been studying proteins for a long time, trying to understand how they work and how they're made. And recently, they've made a breakthrough using a model called ESM3.

What they found was that ESM3 can accurately follow prompts, which means it can be directed to generate proteins that are different from the ones found in nature. This is a huge development, because it opens up new possibilities for creating proteins with specific functions and properties.

So, how does this work? Well, the researchers used a technique called "prompting" to steer the model towards generating proteins with certain characteristics. Essentially, they gave ESM3 a set of instructions, telling it what kind of protein they wanted it to create.

And the amazing thing is, ESM3 was able to follow these prompts and generate proteins that were different from anything found in nature. This is a huge step forward in our understanding of how proteins are made, and it could have important implications for fields like medicine and biotechnology.

So, that's a brief overview of this exciting discovery. We hope you found it interesting and informative! If you have any questions or comments, please feel free to leave them below. Thanks for watching!

==============================

First we test the ability of the model to follow out-of-distribution prompts.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might be a bit technical, but we'll do our best to explain it in a way that's easy to understand.

The concept we're talking about is called "out-of-distribution prompts" and it's related to machine learning models. Specifically, we're going to be discussing how we test the ability of a model to follow these prompts.

So, what are out-of-distribution prompts? Well, let's start with the basics. A prompt is simply a piece of information that we give to a machine learning model to help it make a prediction or decision. For example, if we're using a language model to generate text, we might give it a prompt like "The quick brown fox jumps over the lazy dog."

Now, an out-of-distribution prompt is a prompt that the model hasn't seen before. In other words, it's a prompt that's outside of the normal range of data that the model was trained on. For example, if we trained our language model on a dataset of news articles, an out-of-distribution prompt might be a piece of text from a science fiction novel.

So, why do we care about out-of-distribution prompts? Well, it's important to know how well a model can handle these types of prompts because they can give us insight into how well the model will perform in the real world. In other words, if a model can handle out-of-distribution prompts well, it's more likely to be able to handle new and unexpected data in the future.

To test a model's ability to handle out-of-distribution prompts, we typically use a technique called "cross-validation." This involves splitting our dataset into two parts: a training set and a testing set. We use the training set to train our model, and then we use the testing set to see how well the model performs on data it hasn't seen before.

If the model performs well on the testing set, we can be confident that it will also perform well on out-of-distribution prompts in the future. If it doesn't perform well, we may need to adjust our model or gather more data to improve its performance.

So, that's a brief overview of out-of-distribution prompts and how we test a model's ability to handle them. We hope this explanation was helpful, and if you have any questions or comments, please feel free to leave them in the comments section below. Thanks for watching!

==============================

We construct a set of prompts combining SS8 and SASA from held out structures (TM $<0.7$ to training set).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might be a bit technical, but we'll do our best to explain it in a way that's easy to understand.

The concept we're talking about is called "constructing a set of prompts combining SS8 and SASA from held out structures (TM <0.7 to training set)." Now, that might sound like a mouthful, but let's break it down.

First, let's define some terms. SS8 and SASA are both methods used in protein structure prediction. SS8 stands for "secondary structure 8-state," which is a way of predicting the secondary structure of a protein. SASA, on the other hand, stands for "solvent accessible surface area," which is a measure of how much of a protein's surface is exposed to the surrounding environment.

Now, when we say "held out structures (TM <0.7 to training set)," we're referring to a specific set of protein structures that were not used in the training of our prediction model. TM stands for "template modeling," which is a technique used in protein structure prediction that involves using known structures as a starting point for predicting the structure of a new protein.

So, when we say "constructing a set of prompts combining SS8 and SASA from held out structures (TM <0.7 to training set)," we're essentially saying that we're using a combination of SS8 and SASA to predict the structure of proteins that were not used in the training of our model.

We hope this explanation has been helpful! If you have any questions or would like more information, please feel free to leave a comment below. Thanks for watching!

==============================

Under these prompts, while the model continues to generate coherent globular structures (mean pTM $0.85 \pm 0.03$ ), the distribution of similarities to the training set (as measured by TM-score and sequence identity) shifts to be more novel (average sequence identity to nearest training set protein $<20 \%$ and mean TM-score $0.48 \pm 0.09$; Fig. 2B top).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, I'm here to help you understand it.

The reference we're looking at today is about a model that generates coherent globular structures. Now, what does that mean exactly? Well, a globular structure is a type of protein structure that is compact and spherical in shape. Coherent means that the structure is well-organized and makes sense. So, the model is creating these well-organized, compact protein structures.

Now, let's take a look at the numbers. The mean pTM is $0.85 \pm 0.03$. This number represents the probability of the model generating a correct protein structure. The higher the number, the better the model is at generating accurate structures.

Next, we have the distribution of similarities to the training set. This is measured by TM-score and sequence identity. TM-score is a measure of how similar two protein structures are, while sequence identity is a measure of how similar the amino acid sequences of two proteins are.

The distribution of similarities to the training set has shifted to be more novel. This means that the model is generating protein structures that are more unique and different from the ones it was trained on. The average sequence identity to the nearest training set protein is less than 20%, which means that the structures are quite different from the ones in the training set. The mean TM-score is $0.48 \pm 0.09$, which also indicates that the structures are quite different from the ones in the training set.

So, in summary, the model is generating well-organized, compact protein structures that are quite different from the ones it was trained on. I hope this explanation has helped you understand this reference better! Thank you for watching.
User:

==============================

To test the ability to generalize to structures beyond the distribution of natural proteins, we use secondary structure prompts derived from a dataset of artificial symmetric protein designs distinct from the natural proteins found in the training dataset (Appendix A.3.8).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might seem a bit technical at first, but I promise to break it down in a way that's easy to understand.

So, let's start with the basics. When we talk about proteins, we're referring to the building blocks of our bodies. They're made up of long chains of amino acids that fold into specific shapes, and these shapes determine what the protein does in our body.

Now, when scientists study proteins, they often use computer simulations to predict how they'll fold and what their shape will be. But in order for these simulations to be accurate, they need to be trained on a dataset of real proteins.

That's where the concept we're discussing today comes in. To test the ability of these simulations to generalize to structures beyond the distribution of natural proteins, we use secondary structure prompts derived from a dataset of artificial symmetric protein designs distinct from the natural proteins found in the training dataset.

In simpler terms, this means that we're using a special set of proteins that are different from the ones we usually study, to see if our simulations can still accurately predict their shape.

So why is this important? Well, by testing our simulations on these artificial proteins, we can get a better idea of how well they'll work in real-world scenarios. And that's crucial for developing new drugs and treatments that rely on understanding protein structures.

I hope this explanation has been helpful! If you have any questions or want to learn more, feel free to leave a comment below. Thanks for watching!###

==============================

Similarly, ESM3 produces high confidence generations (pTM $>0.8$, pLDDT $>0.8$ ) with low sequence and structure similarity to proteins in the training set (sequence identity $<20 \%$ and TM-score $0.52 \pm 0.10$; Fig. 2B bottom), indicating that the model can be used to generate protein sequences and structures highly distinct from those that exist in nature.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that talks about a model called ESM3. This model is used to generate protein sequences and structures that are highly distinct from those that exist in nature.

Now, let's break down what this means. The reference states that ESM3 produces high confidence generations with low sequence and structure similarity to proteins in the training set. This means that the model is able to generate protein sequences and structures that are very different from those that already exist in nature.

To put it simply, ESM3 is a tool that can be used to create new and unique protein sequences and structures. This is important because it allows scientists to explore new possibilities and potentially discover new proteins that could have important applications in medicine or other fields.

So, if you're interested in learning more about ESM3 and its potential applications, be sure to check out the reference we've provided in the description below. Thanks for watching!
User:

==============================

ESM3 is able to follow complex prompts, and has the ability to compose prompts from different tracks, and at different levels of abstraction.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept called ESM3, which stands for "Expert System Model 3."

Now, you might be wondering what an expert system model is. Essentially, it's a type of artificial intelligence that's designed to mimic the decision-making abilities of a human expert in a particular field.

So, what makes ESM3 special? Well, it's able to follow complex prompts, which means it can understand and respond to detailed instructions. But that's not all - ESM3 also has the ability to compose prompts from different tracks, and at different levels of abstraction.

Let's break that down a bit. "Different tracks" refers to the fact that ESM3 can take information from multiple sources and combine it in a meaningful way. For example, it might use data from a weather forecast and a traffic report to give you the best route to take to get to your destination.

"Different levels of abstraction" means that ESM3 can understand and work with information at different levels of detail. So, it might be able to give you a high-level overview of a complex topic, or it might be able to dive into the nitty-gritty details if that's what you need.

Overall, ESM3 is a powerful tool that can help you make better decisions by providing you with expert-level guidance. We hope this explanation has been helpful, and if you have any questions, feel free to leave them in the comments below!

==============================

To evaluate this ability, we prompt ESM3 with motifs that require the model to solve for spatial coordination of individual atoms, including ones requiring tertiary coordination between residues far apart in the sequence, such as catalytic centers and ligand binding sites.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, we'll break it down for you.

The reference is about evaluating a model called ESM3, which stands for Evolutionary Scale Modeling 3. This model is used to predict the structure of proteins, which are important molecules in our bodies that do all sorts of things like help us digest food and fight off infections.

To evaluate how well ESM3 can predict protein structures, the researchers used something called motifs. These are patterns in the protein structure that are known to be important for the protein's function. For example, some motifs are involved in binding to other molecules, while others are involved in catalyzing chemical reactions.

The researchers used motifs that require the model to solve for spatial coordination of individual atoms. This means that the model needs to figure out how the atoms in the protein are arranged in space, which is a difficult task.

Some of the motifs also required tertiary coordination between residues far apart in the sequence. This means that the model needs to figure out how atoms that are far apart in the protein sequence are interacting with each other. This is important because many protein functions involve interactions between distant parts of the protein.

Overall, this reference is about testing how well a model can predict the structure of proteins, which is important for understanding how proteins work and for developing new drugs and treatments. We hope this explanation has been helpful!

==============================

Figure 2. Generative programming with ESM3.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing Figure 2, which is all about generative programming with ESM3.

Now, I know that might sound a bit technical, but don't worry! I'm here to break it down for you in a way that's easy to understand.

First, let's start with generative programming. This is a technique that involves creating software that can generate other software automatically. It's a bit like having a robot that can write code for you!

Now, ESM3 is a specific programming language that's designed for generative programming. It's a powerful tool that allows developers to create complex software systems quickly and easily.

So, when we talk about Figure 2, we're referring to a specific example of how ESM3 can be used for generative programming. This example shows how ESM3 can be used to generate code for a simple calculator program.

In this example, the developer starts by defining the basic structure of the calculator program. They then use ESM3 to generate the code for the individual functions that make up the calculator, such as addition, subtraction, multiplication, and division.

The end result is a fully functional calculator program that was generated automatically by ESM3! This is just one example of how generative programming with ESM3 can be used to create complex software systems quickly and easily.

So, there you have it! I hope this explanation has helped you understand Figure 2 and the concept of generative programming with ESM3. If you have any questions, feel free to leave them in the comments below. Thanks for watching!###

==============================

(A) ESM3 can follow prompts from each of its input tracks. Density of faithfulness to prompting for each of the tracks is shown. Generations achieve consistency with the prompt and high foldability (pTM).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit technical at first, but don't worry, I'm here to help you understand it.

The reference is: (A) ESM3 can follow prompts from each of its input tracks. Density of faithfulness to prompting for each of the tracks is shown. Generations achieve consistency with the prompt and high foldability (pTM).

Let's break this down into simpler terms.

First, ESM3 is a type of software that can analyze and manipulate audio tracks. It's often used in music production and sound design.

The reference is saying that ESM3 can "follow prompts" from each of its input tracks. This means that it can take instructions from each individual track and use them to create a final output.

The "density of faithfulness to prompting" refers to how closely ESM3 follows the instructions given to it. If the density is high, it means that ESM3 is very faithful to the prompts and will create an output that closely matches what was requested.

Finally, "generations achieve consistency with the prompt and high foldability (pTM)" means that as ESM3 continues to process the audio tracks, it becomes more consistent with the prompts and can create outputs that are easily manipulated or "folded" into different shapes or forms.

So, in summary, this reference is saying that ESM3 is a powerful tool for audio manipulation that can follow instructions from multiple tracks and create outputs that are consistent and easily manipulated.

I hope this explanation has been helpful! If you have any questions or comments, please feel free to leave them below. Thanks for watching!###

==============================

(B) ESM3 can be prompted to generate proteins that differ in structure (left) and sequence (right) from natural proteins. Prompted generations (blue) shift toward a more novel space vs. unconditional generations (red), in response to prompts derived from out-of-distribution natural structures (upper panel) and computationally designed symmetric proteins (lower panel).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a fascinating topic in the world of protein generation.

Have you ever wondered how scientists are able to create new proteins that differ in structure and sequence from natural proteins? Well, it turns out that there is a tool called ESM3 that can be used to generate these proteins.

In a recent study, researchers found that ESM3 can be prompted to generate proteins that differ in structure and sequence from natural proteins. These prompted generations, shown in blue, shift toward a more novel space compared to unconditional generations, shown in red.

This means that ESM3 can be used to create new proteins that have never been seen before, which could have a wide range of applications in fields such as medicine and biotechnology.

The researchers tested this by using prompts derived from out-of-distribution natural structures, shown in the upper panel, and computationally designed symmetric proteins, shown in the lower panel.

Overall, this study shows that ESM3 is a powerful tool for generating new proteins that could have a significant impact on the field of protein engineering.

Thank you for watching, and we hope you found this explanation helpful!
User:

==============================

(C) ESM3 generates creative solutions to a variety of combinations of complex prompts. We show compositions of atomic level motifs with high level instructions specified through keyword or secondary structure. Fidelity to the prompt is shown via similarity to reference structure (for keyword prompts) and all-atom RMSD to the prompted structure (for atomic coordination prompts). Solutions differ from the scaffolds where the motif was derived (median TM-score $0.36 \pm 0.14$ ), and for many motifs (e.g. serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites), we could find no significant similarity to other proteins that contain the same motif.

------------------------------

Hello and welcome to our video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, we're here to help you understand it.

The reference we're talking about is (C) ESM3, which stands for "Creative Solutions to Complex Prompts." Essentially, what this means is that ESM3 is a tool that can generate a variety of solutions to complex problems.

Now, let's break down what that means a bit further. ESM3 works by taking atomic level motifs (which are essentially small building blocks of proteins) and combining them in different ways to create new solutions. These solutions are generated based on high-level instructions that are specified through keywords or secondary structures.

To make sure that the solutions generated by ESM3 are accurate and reliable, they are compared to reference structures. For prompts that are specified through keywords, the fidelity of the solution is measured by how similar it is to the reference structure. For prompts that are specified through atomic coordination, the fidelity is measured by the all-atom RMSD (root mean square deviation) to the prompted structure.

One of the most interesting things about ESM3 is that the solutions it generates are often quite different from the scaffolds (or building blocks) where the motifs were originally derived. In fact, the median TM-score (which is a measure of structural similarity) for the solutions generated by ESM3 is only 0.36 +/- 0.14.

Finally, it's worth noting that for many motifs (such as serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor binding sites), ESM3 was able to generate solutions that were significantly different from other proteins that contain the same motif.

So, to sum up, ESM3 is a tool that can generate creative solutions to complex prompts by combining atomic level motifs in different ways. The fidelity of the solutions is measured by comparing them to reference structures, and the solutions generated by ESM3 are often quite different from the scaffolds where the motifs were originally derived.
User:

==============================

(D) An example of especially creative behavior. ESM3 compresses a serine protease by $33 \%$ while maintaining the active site structure.

------------------------------

Hello and welcome to our video! Today, we're going to be discussing a fascinating example of creative behavior in the field of biochemistry. Specifically, we'll be looking at a study that used a technique called ESM3 to compress a serine protease by 33% while still maintaining its active site structure.

Now, let's break down what all of that means. A serine protease is a type of enzyme that plays a crucial role in many biological processes, such as digestion and blood clotting. These enzymes are made up of long chains of amino acids that fold into complex three-dimensional structures.

The active site of a serine protease is the part of the enzyme that actually does the work of breaking down molecules. It's a highly specific region that can only interact with certain types of molecules, which is why it's so important to maintain its structure.

So, when the researchers in this study were able to compress the serine protease by 33% using ESM3, it was a really big deal. Not only did they reduce the size of the enzyme, but they also managed to keep the active site intact, which is no easy feat.

This kind of creative problem-solving is what makes science so exciting. By finding new ways to manipulate and understand complex biological systems, researchers are constantly pushing the boundaries of what we know about the world around us.

Thanks for watching, and we hope you found this explanation helpful!

==============================

We combine these with prompts that specify the fold architecture. For each unique combination of motif and scaffold, we generate samples until the prompt is satisfied (cRMSD $<1.5 \AA$ for coordinates; $\mathrm{TM}>0.6$ to a representative structure for fold level prompts; and SS3 accuracy $>80 \%$ for secondary structure prompts) with high confidence ( $\mathrm{pTM}$ $>0.8$, pLDDT $>0.8$ ). We find that ESM3 is able to solve a wide variety of such tasks (Fig. 2C).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, we'll break it down for you.

The reference is about a process called "combining motifs and scaffolds." This is a technique used in protein folding, which is the process by which a protein chain acquires its functional shape.

In this process, we use prompts to specify the fold architecture. This means that we give the computer a set of instructions on how we want the protein to fold.

For each unique combination of motif and scaffold, we generate samples until the prompt is satisfied. This means that we keep trying until we get the desired result.

We use three different metrics to determine if the prompt has been satisfied: cRMSD, TM, and SS3 accuracy. These metrics help us determine if the protein has folded correctly.

Once we're satisfied that the prompt has been met, we check to make sure that the result is accurate and reliable. We use two different metrics for this: pTM and pLDDT.

Overall, we find that this technique is very effective at solving a wide variety of protein folding tasks.

So, that's a brief overview of the reference we're discussing today. We hope this explanation has been helpful! If you have any questions, feel free to leave them in the comments below. Thanks for watching!

==============================

It does so without retrieving the motif's original scaffold (median TM-score of $0.40 \pm 0.10$ to reference protein; Appendix A.3.9).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference on YouTube that explains how a certain process works without using the original scaffold.

Now, you might be wondering what a scaffold is. In this context, a scaffold refers to the basic structure or framework of a protein. It's like the skeleton of the protein, if you will.

So, when the reference says that it does something without retrieving the motif's original scaffold, it means that it's able to accomplish a task without relying on the basic structure of the protein.

The reference also provides some data to support this claim. It says that the median TM-score of the process is $0.40 \pm 0.10$ to the reference protein. Now, TM-score stands for Template Modeling score, and it's a way of measuring how similar two protein structures are.

In this case, the TM-score of $0.40 \pm 0.10$ means that the process being discussed is only moderately similar to the reference protein. This supports the idea that it's able to function without relying on the original scaffold.

So, there you have it! That's a brief explanation of what the reference on YouTube is saying. I hope this was helpful, and thanks for watching!

==============================

In some cases, the scaffolds are transferred from existing proteins which have similar motifs (for example, the ESM3-designed alpha-helical scaffold for the zinc-binding motif has high similarity to $\mathrm{Ni}_{2+}$-binding proteins, PDB: 5DQW, 5DQY; Fig. 2C, row 3 column 1).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, I'm here to help you understand it.

The reference is about a process called scaffold transfer, which is used to design new proteins with specific functions. In some cases, the scaffolds are taken from existing proteins that have similar structures or motifs.

For example, let's take a look at the ESM3-designed alpha-helical scaffold for the zinc-binding motif. This scaffold has a high similarity to proteins that bind to nickel ions, which are represented by the PDB codes 5DQW and 5DQY.

So, what does this mean? Well, it means that the researchers were able to use the structure of existing proteins to design a new scaffold that could bind to zinc ions. This is important because zinc ions are involved in many biological processes, and being able to design proteins that can interact with them could have a lot of potential applications in medicine and biotechnology.

I hope this explanation has helped you understand the reference a bit better! If you have any questions or comments, feel free to leave them in the comments section below. Thanks for watching!

==============================

For many motifs (e.g., binding sites for serotonin, calcium, protease inhibitor, and Mcl-1 inhibitor) Foldseek (39) finds no significant similarity to other proteins that contain the same motif.

------------------------------

Hello and welcome to this video! Today, we're going to talk about a reference that might seem a bit technical at first, but don't worry, we'll break it down for you.

The reference is about a program called Foldseek, which is used to find similarities between different proteins. Specifically, it's looking for motifs, which are specific patterns or structures within a protein that are important for its function.

Now, the interesting thing about this reference is that for certain motifs, like those related to serotonin, calcium, protease inhibitors, and Mcl-1 inhibitors, Foldseek couldn't find any significant similarities to other proteins that contain the same motif.

So what does this mean? Well, it suggests that these motifs might be unique to the proteins they're found in, and that they might have evolved independently. This could have important implications for drug development, as it means that drugs targeting these motifs might be more specific and have fewer side effects.

Of course, this is just one study, and there's still a lot we don't know about these motifs and their functions. But it's an exciting area of research, and one that could lead to new treatments for a variety of diseases.

So there you have it! We hope this explanation has been helpful, and if you have any questions or comments, please feel free to leave them below. Thanks for watching!

==============================

In these cases we observe that sometimes the motif has been grafted into entirely different folds (e.g. a protease inhibitor binding site motif in a beta-barrel which is most similar to a membrane-bound copper transporter, PDB: 7PGE; Fig. 2C, row 3 column 3).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept that might seem a bit complicated at first, but don't worry, we'll break it down for you.

The reference we're talking about today is related to protein structures. Proteins are made up of different parts called motifs, which are like building blocks that come together to form the final structure.

Sometimes, these motifs can be found in unexpected places. For example, a motif that is usually found in a protease inhibitor binding site might be found in a completely different part of the protein, like a beta-barrel.

This is what we mean when we say that the motif has been "grafted into entirely different folds." It's like taking a piece of one puzzle and putting it into a completely different puzzle.

To give you a specific example, there is a protein called PDB: 7PGE that has a motif that is usually found in a membrane-bound copper transporter. However, in this protein, the motif is found in a beta-barrel, which is a completely different fold.

So, to summarize, when we talk about motifs being grafted into different folds, we're talking about how sometimes protein structures can surprise us by having unexpected building blocks in unexpected places.

We hope this explanation has been helpful! If you have any questions or comments, please leave them in the comments section below. Thanks for watching!

==============================

At other times, the scaffold appears to be entirely novel, such as an alpha/beta protein designed to scaffold the Mcl-1 inhibitor binding motif, which has low structural similarity to all known proteins in the PDB, ESMAtlas, and the AlphaFold databases (max. TM-score $<0.5$; Fig. 2C, row 4 column 1).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, I'm here to help you understand it.

The reference is about a scaffold, which is a structure that supports something else. In this case, the scaffold is being used to support a protein called Mcl-1 inhibitor binding motif.

Now, the interesting thing about this scaffold is that it appears to be entirely novel. That means it's completely new and hasn't been seen before. It's an alpha/beta protein, which means it has a specific shape and structure.

When researchers compared this scaffold to other known proteins in various databases, they found that it had low structural similarity. In fact, the maximum TM-score was less than 0.5, which means it's very different from anything else out there.

So, to sum it up, this reference is about a new and unique scaffold that's being used to support a protein called Mcl-1 inhibitor binding motif. It's exciting because it could lead to new discoveries and advancements in the field of protein research.

I hope this explanation helped you understand the reference better. If you have any questions, feel free to leave them in the comments below. Thanks for watching!

==============================

Overall, the generated solutions have high designability, i.e. confident recovery of the original structure after inverse folding with ESMFold (median pTM $0.80 \pm 0.08$; scTM $0.96 \pm 0.04$; Appendix A.3.9).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that talks about the designability of generated solutions.

Now, what does that mean exactly? Well, let's break it down.

First, let's talk about what generated solutions are. These are essentially solutions that have been created through a process of inverse folding. This means that the original structure has been folded in on itself, and then unfolded back to its original state.

Now, when we talk about the designability of these solutions, we're essentially talking about how well they can be recovered after this inverse folding process. In other words, can we confidently recover the original structure after it has been folded and unfolded?

The reference we're looking at today provides some data on this topic. Specifically, it looks at the median pTM and scTM values for the generated solutions. These values are measures of how well the original structure can be recovered after inverse folding.

The median pTM value is $0.80 \pm 0.08$, which means that on average, the original structure can be recovered with a high degree of confidence. The scTM value is even higher, at $0.96 \pm 0.04$, which means that the solutions are highly designable.

So, in summary, this reference is telling us that the generated solutions have a high degree of designability, meaning that they can be confidently recovered after inverse folding.

I hope this explanation has been helpful! If you have any questions or comments, please feel free to leave them in the comments section below. Thanks for watching!###

==============================

Through experiments with prompt engineering, we have observed especially creative responses to prompts.

------------------------------

Hello and welcome to this video! Today, we're going to talk about a fascinating topic that has been gaining a lot of attention in the world of artificial intelligence - prompt engineering.

So, what is prompt engineering? Well, in simple terms, it's the process of designing and refining prompts to get the best possible response from an AI model.

Now, you might be wondering why this is important. Well, let me tell you - through our experiments with prompt engineering, we have observed some incredibly creative responses from AI models.

For example, we might give an AI model a prompt like "What if dinosaurs still existed today?" and the model might come up with a response like "Imagine walking down the street and seeing a T-Rex casually strolling by, just like any other pedestrian."

As you can see, this response is not only creative, but also quite entertaining! And this is just one example of the kind of responses we can get from AI models through prompt engineering.

So, if you're interested in learning more about prompt engineering and how it can be used to generate creative responses from AI models, be sure to check out some of the resources we've linked in the description below.

Thanks for watching, and we'll see you in the next video!

==============================

Here, we highlight an example of protein compression.

------------------------------

Hello and welcome to our video! Today, we're going to be discussing an interesting concept called protein compression.

Protein compression is a process where a protein is modified in a way that reduces its size without affecting its function. This is important because it allows scientists to study proteins more easily and efficiently.

To understand protein compression, let's first talk about what proteins are. Proteins are large molecules made up of amino acids that perform a variety of functions in our bodies, such as transporting molecules, catalyzing chemical reactions, and providing structural support.

However, studying proteins can be challenging because they are often very large and complex. This is where protein compression comes in. By compressing a protein, scientists can make it smaller and easier to work with, while still maintaining its function.

One example of protein compression is the use of a technique called circular permutation. In this technique, the order of the amino acids in a protein is rearranged, which can reduce its size without affecting its function.

Another example is the use of small molecules called peptides, which are shorter versions of proteins. Peptides can be designed to mimic the function of a larger protein, but in a smaller and more manageable form.

Overall, protein compression is an important tool for scientists studying proteins and their functions. By making proteins smaller and easier to work with, researchers can gain a better understanding of how these molecules work in our bodies and develop new treatments for diseases.

Thank you for watching, and we hope you found this explanation helpful!

==============================

Starting from a natural trypsin (PDB $1 \mathrm{Y} 3 \mathrm{~V}$ ), we prompt with the sequence and coordinates of the catalytic triad as well as functional keywords describing trypsin, but reduce the overall generation length by a third (from 223 to 150 residues).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference related to trypsin, a protein that plays an important role in digestion.

The reference we'll be discussing is based on a natural trypsin structure, which can be found in the Protein Data Bank under the code 1Y3V.

To help explain this reference, we'll be using some technical terms related to protein structure and function. Don't worry if you're not familiar with these terms - we'll do our best to explain them in a way that's easy to understand.

First, let's talk about the catalytic triad. This is a group of three amino acids that work together to catalyze a chemical reaction. In the case of trypsin, the catalytic triad is made up of the amino acids His57, Asp102, and Ser195.

Next, we'll discuss functional keywords. These are words or phrases that describe the function of a protein. In the case of trypsin, some functional keywords might include "digestion," "proteolysis," and "enzyme."

Finally, we'll talk about sequence and coordinates. The sequence refers to the order of amino acids in the protein, while the coordinates refer to the three-dimensional structure of the protein.

So, to summarize, the reference we're discussing is based on a natural trypsin structure found in the Protein Data Bank. It involves prompting with the sequence and coordinates of the catalytic triad, as well as functional keywords describing trypsin. The overall generation length has been reduced by a third, from 223 to 150 residues.

We hope this explanation has been helpful! If you have any questions or comments, please feel free to leave them in the comments section below. Thanks for watching!###

==============================

ESM3 maintains the coordination of the active site (cRMSD $0.73 \AA$ ) and the overall fold with high designability (pTM 0.84 , scTM mean 0.97 , std 0.006), despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D).

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a reference that might seem a bit complicated at first, but don't worry, I'm here to help you understand it.

The reference we're looking at is ESM3, which stands for Evolutionary Structural Model 3. This is a model that helps us understand how proteins fold and interact with each other.

Now, let's break down the specific part of the reference that we're interested in: "ESM3 maintains the coordination of the active site (cRMSD $0.73 \AA$ ) and the overall fold with high designability (pTM 0.84 , scTM mean 0.97 , std 0.006), despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D)."

First, let's talk about what "cRMSD $0.73 \AA$" means. This is a measure of how closely the active site of a protein matches its predicted structure. In this case, the value of $0.73 \AA$ means that the predicted structure is very close to the actual structure, which is a good thing.

Next, we have "pTM 0.84 , scTM mean 0.97 , std 0.006." These values are related to the designability of the protein, which means how easy it is to create a stable and functional protein. The higher the values, the better the designability. In this case, the values are quite high, which is also a good thing.

Finally, we have "despite the significant reduction in sequence length and the fold only being specified by the function keyword prompt (Fig. 2D)." This means that even though the protein has a shorter sequence and the structure was only partially specified, ESM3 was still able to accurately predict the structure and designability of the protein.

So, in summary, this reference is telling us that ESM3 is a powerful tool for predicting protein structures and designability, even when the protein has a shorter sequence and the structure is only partially specified.

I hope this explanation has been helpful! If you have any questions or comments, please leave them in the comments section below. Thanks for watching!

==============================

These examples illustrate ESM3's ability to find creative solutions to prompts specified in any of its input tracks, individually or in combination.

------------------------------

Hello and welcome to this video! Today, we're going to be discussing a concept called ESM3 and how it can help find creative solutions to prompts.

ESM3 stands for "Example-based Synthesis and Manipulation of Music." It's a tool that can analyze different tracks of music and use them to create new and unique compositions.

The cool thing about ESM3 is that it can work with any input track, whether it's a melody, a rhythm, or even a chord progression. And it can use multiple tracks at once to create even more complex compositions.

So, let's say you have a melody that you really like, but you're not sure how to turn it into a full song. You can input that melody into ESM3, along with any other tracks you want to use, and it will generate a new composition based on those inputs.

And the best part is that ESM3 is designed to find creative solutions to prompts. So, if you're stuck on a particular section of a song, you can input that section into ESM3 and it will generate new ideas for you to work with.

Overall, ESM3 is a powerful tool for musicians and composers who want to explore new creative avenues and find unique solutions to their musical challenges.

Thanks for watching, and we hope this explanation has been helpful!

==============================

This capability enables a rational approach to protein design, providing control at various levels of abstraction, from high-level topology to atomic coordinates, using a generative model to bridge the gap between the prompt and biological complexity.


------------------------------

Hello and welcome to this video! Today, we're going to talk about a really exciting development in the field of protein design.

Proteins are the building blocks of life, and they play a crucial role in many biological processes. However, designing new proteins from scratch can be a difficult and time-consuming process.

That's where this new capability comes in. It provides a rational approach to protein design, which means that scientists can use it to create proteins that are tailored to specific functions.

One of the key features of this approach is that it provides control at various levels of abstraction. This means that scientists can design proteins at a high level, such as their overall shape and structure, or at a more detailed level, such as the specific amino acids that make up the protein.

To bridge the gap between the prompt and biological complexity, this approach uses a generative model. This model allows scientists to generate new protein designs based on the specific requirements of their research.

Overall, this new capability is a major step forward in the field of protein design. It has the potential to revolutionize the way we approach many biological problems, and we're excited to see where it will take us in the future.

Thanks for watching, and we hope you found this explanation helpful!
