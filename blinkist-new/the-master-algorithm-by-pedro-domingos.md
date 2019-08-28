![The Master Algorithm](https://images.blinkist.com/images/books/57bc6f2e003a4b0003f1a92d/3_4/470.jpg)

# The Master Algorithm

## What’s in it for me? Understand how algorithms are changing the world.

One of the world’s greatest mysteries is how a pound of gray jelly in the head of a newborn can eventually produce a stream of consciousness, able to perceive the world and interact with it. Maybe more astounding is how little teaching the brain requires while it’s undergoing this transformation.

No machine in the history of mankind has a learning capacity comparable to the human brain. But things are changing. Our ability to create ever more sophisticated machines means that, in the future, they may be able to challenge the brain.

Machines may even surpass human ability. They can learn from the enormous amounts of data that we encounter and ignore every day. So let's put on our thinking caps and explore the fascinating world of algorithms and machine learning.

In these blinks, you’ll find out

- how machines will be able to learn without instruction in the future;
- why seeing patterns sometimes is a problem; and
- how an algorithm for winning Tetris could improve your route to work.

## Machine learning can solve important problems by looking at data and then finding an algorithm to explain it.

Have you ever been frustrated by recipes with imprecise instructions, like, “cook at medium heat for 15-20 minutes”? If so, you might be someone who prefers a good algorithm.

Unlike recipes, algorithms are sequences of precise instructions that produce the same result every time.

Though you might not be aware of their presence, algorithms are used everywhere. They schedule flights, route the packages you send and make sure factories run smoothly.

These standard algorithms are designed to accept information as an input, then perform a task and produce an output.

Let’s say an algorithm’s task is to give directions. When you input two points, the output would then be the shortest route between these two points.

But machine learning, or ML, algorithms are one step more abstract: they are algorithms that output other algorithms! Given lots of examples of input-output pairs to learn from, they find an algorithm that seems to turn the inputs into the outputs.

This comes in handy for finding algorithms for tasks that human programmers can’t precisely describe, such as reading someone’s handwriting. Like riding a bike, deciphering handwriting is something we do unconsciously. We would have trouble putting our process into words, let alone into an algorithm.

Thanks to machine learning, we don’t have to. We just give a machine learning algorithm lots of examples of handwritten text as input, and the meaning of the text as the desired output. The result will be an algorithm that can transform one into the other.

Once learned, we can then use that algorithm whenever we want to automatically decipher handwriting. And, indeed, that’s how the post office is able to read the zip code you write down on your packages.

What’s great is that ML algorithms like this one can be used for many different tasks, and solving emergent problems is only a matter of collecting enough data.

This means that the initial underlying algorithm is often the same and requires no adjustments in order to solve seemingly unrelated problems.

For example, you might think that making a medical diagnosis, filtering spam from your email and figuring out the best chess move might all need completely different algorithms. But, actually, with one ML algorithm and the right kind of data, you can solve all these problems.

## To avoid hallucinating patterns, learning algorithms need to be restricted and tested for validity.

To hallucinate is to see something that isn’t really there. Interestingly enough, hallucinations are a central problem in the world of algorithms. In 1998, a best-selling book, **The Bible Code**, claimed that the Bible contained hidden predictions that were revealed by selectively skipping certain lines and letters.

Critics disproved this assertion, however, by demonstrating that similar “patterns” could be found in **Moby Dick** and within Supreme Court rulings.

This is a good example of hallucinating patterns, which, in ML lingo, is the result of **overfitting**. Overfitting takes place when an algorithm is so powerful that it can “learn” anything. You see, when you throw enough computing power at a data set like the Bible, you will always find patterns because the computer can construct increasingly complex models until some arise. But the resulting model won’t work on any other data.

So, to get your algorithms under control, their power needs to be** bounded** by limiting their complexity.

With the right kind of limiting restrictions, you make sure the scope of your algorithm isn’t too big and ensure that the results are verifiable and consistent. If it’s too flexible, your algorithm can end up like **The Bible Code,** finding patterns in any given text or set of data.

But what if your algorithm discovers multiple patterns that explain the data you have but disagree on new data? Which result should you believe? And how can you be 100 percent sure your results aren’t just a fluke?

This is when **holdout** data comes in.

When you are preparing your original data set for the learning algorithm, it is important to divide it into a **training set**, which the algorithm uses to learn, and a **holdout set**, against which to test it.

This way you can double-check the results and confirm that the patterns found in the data are valid.

Ensuring the validity of the results is what an ML expert’s work is all about. Her job is to restrict the power of the algorithm by making sure the rules are not too flexible and that the results perform well against both the training-set data and the holdout-set data.

## Rules using deductive reasoning and decision trees can allow machines and algorithms to think logically.

Just as the medical world has specialists who have preferred ways of treating the body, the world of machine learning has specialized branches with their own perspectives and preferred style of algorithms.

**Symbolists**, for example, manipulate symbols and learn rules in order to create artificial intelligence (AI).

Symbolists are the oldest branch of the AI community; they’re rationalists who view the senses as unreliable, and therefore believe that all intelligence must be learned through logical methods.

For this reason, the symbolists’ preferred algorithm is **inverse deduction.**

Generally speaking, inverse deduction creates rules by linking separate statements, like this: If you provide two statements, such as “Napoleon is human” and “Therefore Napoleon is mortal,” the algorithm can arrive at broader statements, such as “Humans are mortal.”

While this kind of algorithm is good for data mining and sorting through relatively large amounts of data, such as medical records, it is costly and inefficient for truly massive databases because it has to consider all possible relationships between all variables in the data, which results in exponentially growing complexity.

So, to make this work less complex, you can use **decision trees** to find these rules.

As the name suggests, decision trees branch the data off into smaller sets. They do this by basically playing a game of 20 questions, with each question or rule further narrowing down the options and possibilities.

For example, if you wanted to come up with rules for sifting through medical records, you could use a decision tree. You’d start out with all of the records, but then, at the various branching points in the tree, you’d divide them into groups like “healthy,” “leukemia,” “lung cancer” and so forth. The ML algorithm would then find suitable rules that would also result in this division.

This method prevents overfitting by restricting the number of questions the decision tree asks, so that only the most widely applicable and general rules are applied.

Decision trees are used in software that make medical diagnoses by narrowing down someone’s symptoms. They were also used in an application that could predict the outcome of Supreme Court rulings with a 75-percent accuracy rate; the predictions from a panel of human experts had an accuracy rate of less than 60 percent.

In the next blink, we’ll see how to deal with data of a more difficult, and more human, sort – data that’s uncertain or even contradictory.

## You can prevent effective algorithms from overfitting by keeping models open and restricting assumptions.

**Bayesianism** is another popular branch of machine learning, and its followers are practically religious in their devotion.

Contrary to the rationalists, Bayesians are empiricists who believe that logical reasoning is flawed and that true intelligence comes from observation and experimentation.

Their algorithm of choice is called **Bayesian** **inference**, which works by keeping a number of different hypotheses or models open simultaneously. The degree to which we believe in any one of these hypotheses or models will vary depending on the evidence found in the data, as some will invariably receive more support than others.

This approach can also help provide a medical diagnosis. While remaining open to many hypothetical diseases and their symptoms, the algorithm can sift through the data of a patient’s record to make the best match. The more data the record provides, the more diseases the algorithm can rule out, until one hypothesis becomes the statistical winner.

Bayesian inference is a powerful algorithm, and it prevents overfitting by restricting assumptions about causes and events.

For example, if it is apparent that you have the flu but we want to find out if you also have a fever or a cough, we can categorize the flu as a cause and the fever or cough as events. The restricting assumption here is to assume that the two events do not influence each other, meaning that a cough does not affect your chances of also getting a fever.

By ignoring the possible connections between events, Bayesian inference avoids overfitting and becoming too powerful by strictly focusing on the connection between cause and effect.

Similar assumptions are used by voice-recognition software like Siri. When you say, “Call the police!” the Bayesian inference keeps options open and considers how likely it is that you might have said, “Call the please!”

But when checking its database of popular phrases, it is enough to look at the frequency of how often certain words follow one another. And, in this case, it is clear that “police” follows the word “the” far more often than “please.”

## Unsupervised learning algorithms are great at finding structure and meaning in raw data.

Have you ever noticed how you can hear when someone says your name, even if it’s said quietly and you’re surrounded by dozens of loudly talking people? We have an impressive ability to filter the information our ears pick up and focus on. Could an algorithm learn to do the same thing?

As a matter of fact, **unsupervised learning** is a category of algorithms that are designed to use raw and noisy data.

The algorithms in the previous blinks have all used data containing labeled examples to learn from, such as examples of correct diagnoses or emails that have been labeled as spam or non-spam.

However, **clustering algorithms** are one group of unsupervised learners that can discover categories from large amounts of raw data.

This is the kind of algorithm that can be used in image recognition or voice isolation software, which can identify a face or object among millions of pixels, or single out a voice in a noisy crowd.

These algorithms can find meaningful structures like these by reducing the dimensionality of the data by bringing the description of what you’re looking for down to its primary essentials.

Sketch artists, for instance, are able to reproduce faces with such accuracy because they memorize ten different variations of each facial feature – nose, eyes, ears and so on. This narrows their options down considerably, making it possible to produce a passable drawing based on a description alone. Similarly, facial recognition algorithms, after preprocessing all the different options, only need to compare a few hundred variables rather than a million pixels.

**Neural networks** are another effective way to crunch massive amounts of raw data.

While other algorithms process data sequentially, neural networks work like a brain and process multiple inputs at the same time.

One of the biggest neural networks ever created spent three days sifting through ten million randomly selected YouTube videos. And without being told what to look out for, the program learned to recognize human faces and, perhaps unsurprisingly, cats.

Now that you know about all these different algorithms, you’ve surely begun to wonder what would happen if they were all combined into a master algorithm. Well, let’s find out.

## There is no one perfect algorithm, and a unifying master algorithm is required to tackle the big problems.

So, with all these different algorithms, you might be asking, which one’s the best?

The truth is, there’s no such thing as a perfect algorithm; they all rely on different fundamental assumptions.

Remarkably, for every data set where an algorithm comes up with something useful, a devil’s advocate could use the same algorithm on another data set to show that everything it does is nonsensical. That’s why it’s important to make the right assumptions about the data you’re applying the algorithm to.

Luckily, this isn’t as big of an issue as it might seem.

The majority of the most difficult problems in computer science are fundamentally related and could be solved with one good algorithm.

Just consider some problems that have already been solved: Determining the shortest route to visit several cities, compressing data, controlling urban traffic flow, turning 2D images into 3D shapes, laying out components on a microchip and, last but not least, playing Tetris.

Discovering an efficient solution for one of these problems essentially solved them all.

It might be hard to believe that one algorithm can address so much, but it’s true and it’s considered one of the most fascinating insights in all of computer science.

Unfortunately, the most important problems facing humanity require much more capable algorithms than are currently available.

For example, in order to come up with a cure for cancer, the ultimate algorithm needs to incorporate all the previously acquired knowledge, plus be able to keep up with the quick rate at which new scientific discoveries are being published. On top of that, it would need to consider the relevance of all of this data and discern an overarching structure that no one has yet been able to see.

While this is currently beyond the capability of algorithms, progress is being made.

Take Adam, for instance – a research robot at the Institute of Biology in Manchester that has learned general knowledge about genetics and can suggest hypotheses. It can even design and carry out experiments as well as test and analyze their results!

## In modern business, finding the best algorithm and the best data is the key to success.

“Data is the new oil,” or at least so say the modern business prophets.

It’s hard to argue against, too, because, in the world of big business, many feel that the company with the best algorithms is the company that’s going to win.

In the pre-internet era, if a business had problems connecting with consumers, it could solve them with a physical solution, like coming up with a better ad campaign.

But with the internet came virtually unlimited consumer choice, and now the question is: How do you decide what to buy when there are 10 million options?

This is where machine learning comes in and helps narrow things down.

Amazon has led the race in offering intelligent suggestions on what products customers might like, and their service covers just about every market.

But the race is still on. And whoever has the best data can come up with the best algorithm, which is why data is a tremendous strategic asset. The average value of a user’s data trail for the online advertising industry is around $1,200 per year. Google’s data on you goes for about $20, while Facebook’s costs $5.

The business of buying data has become so big that experts believe **data unions **and **data banks **will eventually allow private citizens and companies to conduct fair negotiations about the use of their data.

Databanks could keep your information secure and also allow you to set the terms for when and how it is accessed. And a data union could operate like other worker unions, with like-minded people joining forces to ensure that information is being used fairly and accurately.

This kind of regulation could benefit everyone. It could help businesses, by improving their algorithms; you could get better purchase recommendations; and, with the extra security, more people might feel comfortable sharing their data to help advance medical and humanitarian causes.

## In the future, you’ll have a digital model of yourself to help make life easier.

Chances are you’ve been caught talking to yourself at one point or another. Well, if you’ve ever wished you could talk** back** to yourself, your dreams may soon come true.

By sharing all your data with the ultimate master learning algorithm you will end up with a pretty accurate digital model of yourself.

Imagine the master algorithm: Seeded with a database containing all general human knowledge, then personalized with all the data that you’ve collected over the course of your life, including emails, phone records, web searches, purchases, downloads, health records, GPS directions and so on and so on.

You could then download the learned-model digital version of yourself onto a flash drive, carry it with you in your pocket and use it like a personal butler to help you run your life.

With your very own digital you, little annoyances could be quickly dealt with, saving you time and hassle.

In addition to simple things like automated web searches and recommending new books and movies, it could also file your tax returns, pay your credit-card bills, sort your email, plan your vacations and, if you’re single, it could even set you up on dates.

Or, if you’re feeling introspective, you could set it to a conversation mode and have a chat with your digital model.

In a society where digital models are a common thing, it could even interact with the rest of the world on your behalf.

Imagine you are looking for a new job. After spending a second on LinkedIn, your model could apply for every suitable job available, including some perfect jobs you might have otherwise overlooked.

Those companies might have personal models as well, and your digital self could interact with them and provide you with a list of every company that agreed to a personal interview. All you’d have to do is confirm your appointment.

Your digital self will be like power steering: you’ll get where you want to go with less hassle and a fraction of the effort.

## Final summary

The key message in this book:

**Machine learning algorithms are universal problem solvers that need only a few assumptions and a whole lot of data to work their magic. Unifying the current branches of machine learning into one ultimate master algorithm would advance humanity like no other single event in history. Even as it stands today, advanced algorithms and access to personal data are already crucial for businesses to be competitive. **

Actionable advice:

**Be aware of your data trail.**

Every digital interaction has two levels, getting you what you want and teaching the computer a little bit more about yourself. The second one will be more important over the long-term, since it will be used both to serve you, by helping you perform tasks, and also to manipulate you, by showing you ads and recommendations likely to make you buy. So be aware. If you don't want a current internet session to influence your personalization, go to incognito mode. And if you don't want your kids to be shown YouTube suggestions and ads based on your history, make sure to use different accounts.

**Got feedback?**

We’d sure love to hear what you think about our content! Just drop an email to remember@blinkist.com with the title of this book as the subject line and share your thoughts!

**Suggested** **further** **reading: ******Superintelligence ******by Nick Bostrom**

**Superintelligence** (2014) investigates how creating a machine more intelligent than a human would change humanity. These blinks are full of facts, figures and studies from a variety of disciplines, resulting in a complex picture of the superintelligent future and how we might arrive there.
