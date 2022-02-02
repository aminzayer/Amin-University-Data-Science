# ML-Coding-Practice-Example
What is Find-S Algorithm in Machine Learning?
In order to understand Find-S algorithm, you need to have a basic idea of the following concepts as well:

Concept Learning
General Hypothesis
Specific Hypothesis

## Learning algorithms used in Inductive Bias are -

### Rote-Learner:
Learning corresponds to storing each observed training example in memory.
Subsequent instances are classified by looking them up in the memory.
If the instance is found in memory, the stored classification is returned.
Otherwise, the system refuses to classify the new instance.
Inductive Bias: There is no inductive bias.
### Candidate-Elimination:
New instances are predicted/classified only in the case where all members of the current version space agree on the classification.
Otherwise, the system refuses to classify the new, instance.
Inductive Bias: The target concept can be represented in its hypothesis space.
### FIND-S:
This algorithm finds the most specific hypothesis consistent with training examples.
It then uses this hypothesis to classify all subsequent instances.
Inductive Bias: The target concept can be represented in its hypothesis space, and all instances are negative instances unless the opposite is entailed by its other knowledge.

## Description

## 1. Concept Learning 
Let’s try to understand concept learning with a real-life example. Most of human learning is based on past instances or experiences. For example, we are able to identify any type of vehicle based on a certain set of features like make, model, etc., that are defined over a large set of features.

These special features differentiate the set of cars, trucks, etc from the larger set of vehicles. These features that define the set of cars, trucks, etc are known as concepts.

Similar to this, machines can also learn from concepts to identify whether an object belongs to a specific category or not. Any algorithm that supports concept learning requires the following:

#### Training Data
#### Target Concept
#### Actual Data Objects

If you want to learn AI-ML in-depth, come to us and sign up for this Post Graduate Diploma Artificial Intelligence Online Course at Edureka.

## 2. General Hypothesis

Hypothesis, in general, is an explanation for something. The general hypothesis basically states the general relationship between the major variables. For example, a general hypothesis for ordering food would be I want a burger.

G = { ‘?’, ‘?’, ‘?’, …..’?’}

## 3. Specific Hypothesis

The specific hypothesis fills in all the important details about the variables given in the general hypothesis. The more specific details into the example given above would be I want a cheeseburger with a chicken pepperoni filling with a lot of lettuce. 
Course Curriculum
S = {‘Φ’,’Φ’,’Φ’, ……,’Φ’}

Now ,let’s talk about the Find-S Algorithm in Machine Learning.

The Find-S algorithm follows the steps written below:

Initialize ‘h’ to the most specific hypothesis.
The Find-S algorithm only considers the positive examples and eliminates negative examples. For each positive example, the algorithm checks for each attribute in the example. If the attribute value is the same as the hypothesis value, the algorithm moves on without any changes. But if the attribute value is different than the hypothesis value, the algorithm changes it to ‘?’.

Now that we are done with the basic explanation of the Find-S algorithm, let us take a look at how it works.

# How Does It Work?

![how it work pic](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/12/flow.png)


The process starts with initializing ‘h’ with the most specific hypothesis, generally, it is the first positive example in the data set.
We check for each positive example. If the example is negative, we will move on to the next example but if it is a positive example we will consider it for the next step.
We will check if each attribute in the example is equal to the hypothesis value.
If the value matches, then no changes are made.
If the value does not match, the value is changed to ‘?’.
We do this until we reach the last positive example in the data set.

 
## Limitations of Find-S Algorithm

There are a few limitations of the Find-S algorithm listed down below:

There is no way to determine if the hypothesis is consistent throughout the data.
Inconsistent training sets can actually mislead the Find-S algorithm, since it ignores the negative examples.
Find-S algorithm does not provide a backtracking technique to determine the best possible changes that could be done to improve the resulting hypothesis.

Now that we are aware of the limitations of the Find-S algorithm, let us take a look at a practical implementation of the Find-S Algorithm.

 
## Implementation of Find-S Algorithm

To understand the implementation, let us try to implement it to a smaller data set with a bunch of examples to decide if a person wants to go for a walk.

### The concept of this particular problem will be on what days does a person likes to go on walk.
Time	Weather	Temperature	Company	Humidity	Wind	Goes
Morning	Sunny	Warm	    Yes	Mild	Strong	Yes
Evening	Rainy	Cold	    No	Mild	Normal	No
Morning	Sunny	Moderate	Yes	Normal	Normal	Yes
Evening	Sunny	Cold	    Yes	High	Strong	Yes

Looking at the data set, we have six attributes and a final attribute that defines the positive or negative example. In this case, yes is a positive example, which means the person will go for a walk.

So now, the general hypothesis is:

h0 = {‘Morning’, ‘Sunny’, ‘Warm’, ‘Yes’, ‘Mild’, ‘Strong’}

This is our general hypothesis, and now we will consider each example one by one, but only the positive examples.

h1= {‘Morning’, ‘Sunny’, ‘?’, ‘Yes’, ‘?’, ‘?’}

h2 = {‘?’, ‘Sunny’, ‘?’, ‘Yes’, ‘?’, ‘?’}

We replaced all the different values in the general hypothesis to get a resultant hypothesis. Now that we know how the Find-S algorithm works, let us take a look at an implementation using Python.

## Inductive Bias in Machine Learning


Inductive bias refers to the restrictions that are imposed by the assumptions made in the learning method.

For example, assuming that the solution to the problem of road safety can be expressed as a conjunction of a set of eight concepts.

This does not allow for more complex expressions that cannot be expressed as conjunction.

This inductive bias means that there are some potential solutions that we cannot explore, and not contained within the version space we examine.

In order to have an unbiased learner, the version space would have to contain every possible hypothesis that could possibly be expressed.

The solution that the learner produced could never be more general than the complete set of training data.

In other words, it would be able to classify data that it had previously seen (as the rote learner could) but would be unable to generalize in order to classify new, unseen data.

The inductive bias of the candidate elimination algorithm is that it is only able to classify a new piece of data if all the hypotheses contained within its version space give data the same classification.

Hence, the inductive bias does not impose a limitation on the learning method.


## Getting Started

### Dependencies

* Python / Code Editor

## Help

List of projects
```
   Find-S Algorithm in Machine Learning
```

## Authors

Amin Zayeromali

![Profile views](https://visitor-badge.glitch.me/badge?page_id=aminzayer.aminzayer)

[![Github](https://img.shields.io/github/followers/aminzayer?label=Follow&style=social)](https://github.com/aminzayer)

Twitter: [@AminZayeromali](https://twitter.com/aminzayeromali)

Instagram: [aminzayer](https://www.instagram.com/aminzayer/)

Linkedin: [aminzayeromali](https://ir.linkedin.com/in/aminzayeromali)

Google Scolar: [Amin Zayeromali](https://scholar.google.com/citations?user=IDR8QvcAAAAJ&hl=en)

Email : [Amin {dot} zayeromali {At} gmail {dot} com](&#109;&#097;&#105;&#108;&#116;&#111;:&#097;&#109;&#105;&#110;&#046;&#122;&#097;&#121;&#101;&#114;&#111;&#109;&#097;&#108;&#105;&#064;&#103;&#109;&#097;&#105;&#108;&#046;&#099;&#111;&#109;)


<h2> Connect with me </h2>
<a href = 'https://www.linkedin.com/in/aminzayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/linked-in-alt.svg"/></a> 
<a href = 'https://twitter.com/AminZayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> 
<a href = 'https://aminzayer.ir/'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/portfolio.png"/></a> 
<a href = 'https://www.github.com/aminzayer'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>
<br>


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
