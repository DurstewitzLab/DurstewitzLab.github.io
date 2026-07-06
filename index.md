---
layout: default
title: Home
permalink: /
---

<section class="hero">
  <p class="kicker">Durstewitz Lab</p>
  <h1>Theoretical Neuroscience</h1>
  <p class="lead">
    <!-- This website is still in development. For now, please refer to the <a href="{{ '/legacy-website/' | relative_url}}">legacy website</a>. -->
    <!-- Welcome to our Lab website! -->
  </p>
  <!-- <p class="hero-actions">
    <a class="button button-primary" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="button button-secondary" href="{{ '/team/' | relative_url }}">Team</a>
  </p> -->
</section>

{% if site.data.site.group_photo and site.data.site.group_photo != "" %}
<figure class="group-photo" style="--group-photo-y: {{ site.data.site.group_photo_y | default: 'center' }};">
  <img src="{{ site.data.site.group_photo | relative_url }}" alt="{{ site.data.site.group_photo_alt | default: 'Lab group photo' }}" loading="lazy" />
</figure>
{% endif %}

# Welcome to our website! 
We are a team of researchers working on the intersection of machine learning, dynamical systems, and neuroscience. Our research can be roughly categorized into the following areas:

## Machine Learning (ML) & AI for Dynamical Systems and Time Series

We develop novel AI architectures and training algorithms for learning dynamical systems from data, also called dynamical systems reconstruction. Most time series we observe in nature, engineered systems, or society, originate from some underlying dynamical system. Our ML/AI algorithms aim at recovering these underlying dynamical rules from time series data, learning dynamically faithful surrogate models of the systems observed. These surrogate models can be used for time series forecasting, for simulating the observed system under novel conditions and testing interventions, and for deeper mathematical analysis and insight.

## Reverse-Engineering the Brain: Learning Surrogate Models of Neuronal and Behavioral Processes from Data

We use our ML/AI technology to learn foundation models of the brain, cognitive processes, and behavior, by training the models on diverse experimental data. These include multiple single-unit recordings from animals, fMRI, EEG or MEG recordings in humans, and behavioral data like choices or movements, while the subjects are engaged in various cognitive and behavioral tasks that probe higher cognitive functions. These models serve, on the one hand, for gaining insight into computational functions of the brain, and, on the other hand, for clinical applications in psychiatry. For instance, data-trained models could be used to differentiate clinical subgroups or for simulating different physiological, pharmacological or behavioral interventions in individualized brain models.

## Neuro-Inspired AI for Learning & Inference in Non-Stationary Environments

Current AI models require large amounts of training data, on which they are trained by slow iterative procedures like gradient descent. In contrast, real brains have found efficient ways to quickly adapt to a world in constant flux, without overwriting previously learned skills. By training AI-based dynamical surrogate models on electrophysiological and behavioral data from animals on tasks with constantly changing underlying rules and behavioral contingencies, we aim to reverse-engineer the neuronal mechanisms behind this capability to quickly adjust to changing environmental conditions.

## Key references

{% include refs.html ids="durstewitz2026position,hemmer2026true,trede2026topological,durstewitz2025neuroscience,durstewitz2023reconstructing" %}
