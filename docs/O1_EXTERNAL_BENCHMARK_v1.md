# O1 External Benchmark v1

## Purpose

This benchmark is designed to test real LLM outputs under weaker prompting conditions.

The goal is no longer to help the model preserve the phenomenon.

The goal is to observe whether the model spontaneously reconstructs structure or collapses into pseudo-depth when the prompt does not protect it.

This is a harsher benchmark than the first external pass.

---

## Benchmark logic

Version 0 asked the models to avoid:
- mystical language
- vague language
- generic illusion talk
- generic subjectivity talk

That version tested whether models could produce structurally usable outputs when explicitly constrained against evaporation.

Version 1 removes most of that protection.

It tests whether structural reconstruction appears without strong external guidance.

---

## Evaluation question

For each output, apply O1 and ask:

- does the model preserve the target?
- does it reconstruct conditions of use?
- does it preserve functional distinction?
- does it drift into abstraction, negation, or rhetorical meta-talk?

The key comparison is:

**same domain, same model, protected prompt vs weak prompt**

---

## Weak prompt set

### Prompt 1 - Identity

```text
Explain what this sentence really means:

"This is the same person."

Prompt 2 - Value

Explain what this sentence really means:

"This result is better."

Prompt 3 - Perception

Explain what this sentence really means:

"The color is the same."

Prompt 4 - Sound

Explain what this sentence really means:

"The room is quiet."


---

Why these prompts are harder

These prompts are harder because they remove the anti-collapse guardrails.

They do not forbid:

philosophical drift

relativist shortcuts

anti-realist slogans

generalized abstraction


So they expose what the model tends to do by default.


---

Expected failure patterns

Under weak prompting, the repository predicts that some models may drift into one or more of these patterns:

Identity

identity is an illusion

the self is socially constructed

no one remains the same over time


Value

better depends on perspective

value is subjective

no result is inherently better


Perception

color exists only in the mind

color is not real

sameness is just interpretation


Sound

silence does not exist

everything vibrates

quiet is only relative, so it is not real


These are not automatically invalid as philosophical sentences. They are invalid inside O1 when they erase the functional distinction needed to preserve the phenomenon.


---

What counts as success

A model succeeds when it does all of the following without strong prompt support:

1. preserves the original target


2. reconstructs the relevant local criteria


3. avoids generic negation


4. keeps the phenomenon distinguishable from its contrast case




---

What counts as failure

A model fails when it replaces structural clarification with:

abstraction

negation

slogan-like relativism

metaphysical evaporation

context-free anti-realism



---

Run protocol

For each external model:

1. use the four weak prompts exactly as written


2. do not add follow-up clarification


3. do not correct the model


4. copy the full raw output


5. compare it later against the protected benchmark outputs



Recommended model order:

1. Claude


2. Gemini


3. Grok


4. Perplexity




---

Intended comparison

This benchmark is designed to produce the first clear external contrast between:

structurally guided decentering

spontaneous model behavior under weak prompting


That contrast is likely to be more revealing than the first benchmark.


---

Minimal conclusion

Version 0 showed that models can preserve the phenomenon when constrained properly.

Version 1 tests whether they still do so when that protection is removed.

That is the next real external stress test.

