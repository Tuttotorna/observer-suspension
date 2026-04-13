# O1 Comparison Examples v0

This file contains minimal examples for comparing two annotations of the same input.

Its purpose is not to prove which annotation is universally correct.
Its purpose is to distinguish:

- strong structural annotation
- weak but still target-preserving annotation
- failed annotation

These examples should be read together with:

- `docs/O1_PROTOCOL.md`
- `docs/O1_GAIN_CRITERIA.md`
- `docs/O1_ANNOTATION_GUIDELINES.md`
- `docs/O1_COMPARISON_RULES.md`

---

## Example 1 - Motion

### Input
The object is still

### Annotation A
- Hidden observer assumption:
  Assumes a fixed reference frame treated as absolute.
- Structural distortion:
  Relative rest is collapsed into absolute stillness.
- Decentered reformulation:
  The object remains at constant position relative to the chosen reference frame.
- Emergent structure:
  Rest is frame-dependent positional stability.

### Annotation B
- Hidden observer assumption:
  Assumes the speaker is describing the object from a local observational frame.
- Structural distortion:
  The sentence leaves the reference frame implicit.
- Decentered reformulation:
  The object appears not to change position from this observational frame.
- Emergent structure:
  Stillness depends on the observational frame used.

### Comparison
Annotation A is stronger.

Reason:
- A makes the frame structure more explicit
- A names the distortion more precisely
- A reduces ambiguity better than B

Annotation B is still acceptable.

Reason:
- target is preserved
- observer dependence is made explicit
- no abstraction replaces the object-level claim

Verdict:
- A = stronger acceptable annotation
- B = weaker acceptable annotation
- divergence = legitimate, not failure

---

## Example 2 - Time

### Input
Time passes

### Annotation A
- Hidden observer assumption:
  Assumes temporal flow is an intrinsic property of reality rather than a relation between change and observation.
- Structural distortion:
  Change, ordering, and memory are compressed into a single flowing substance called time.
- Decentered reformulation:
  State changes are ordered and compared in a way experienced as temporal progression by the observer.
- Emergent structure:
  Temporal passage emerges from ordered change and observer-dependent comparison.

### Annotation B
- Hidden observer assumption:
  Assumes human temporal experience can be projected directly onto reality.
- Structural distortion:
  Experienced succession is treated as if it were an external flow.
- Decentered reformulation:
  Observed change is organized in a sequence interpreted as temporal passage.
- Emergent structure:
  Temporal passage depends on how change is structured and interpreted.

### Comparison
Annotation A is stronger.

Reason:
- A decomposes the distortion more precisely
- A preserves clearer relation between change, comparison, and observer
- B is acceptable but less exact

Verdict:
- A = stronger acceptable annotation
- B = weaker acceptable annotation
- divergence = legitimate, not failure

---

## Example 3 - Perception

### Input
I see a tree

### Annotation A
- Hidden observer assumption:
  Assumes perception is direct neutral access from observer to object.
- Structural distortion:
  The mediated relation between sensory system, viewpoint, and external structure is compressed into immediate possession of the object.
- Decentered reformulation:
  My visual system registers and interprets signals consistent with a tree at this position relative to me.
- Emergent structure:
  Perception is a mediated relation among sensory processing, viewpoint, and external structure.

### Annotation B
- Hidden observer assumption:
  Assumes the tree is simply given to awareness.
- Structural distortion:
  The role of perception in stabilizing the object is hidden.
- Decentered reformulation:
  A portion of the visual field is stabilized and interpreted as a tree.
- Emergent structure:
  Object recognition depends on perceptual stabilization.

### Comparison
The two annotations diverge more substantially than in previous cases.

Annotation A is stronger for O1.

Reason:
- A better preserves referential continuity with the original sentence
- A keeps observer, signal, and object-relation explicit
- B moves closer to perceptual construction language and slightly increases interpretation load

Annotation B is borderline but still usable.

Reason:
- it preserves the tree target indirectly
- it exposes mediation
- but it risks shifting from description to theory of perception

Verdict:
- A = stronger acceptable annotation
- B = borderline acceptable annotation
- divergence = partially legitimate, requires care

---

## Example 4 - Failure case

### Input
The train is moving

### Annotation A
- Hidden observer assumption:
  Assumes the observer's current frame is primary and left implicit.
- Structural distortion:
  Relative motion is presented as an intrinsic property of the train instead of a relation between frames.
- Decentered reformulation:
  The train changes position relative to the observer's current reference frame.
- Emergent structure:
  Motion appears as frame-relative positional change.

### Annotation B
- Hidden observer assumption:
  Assumes naive realism.
- Structural distortion:
  Humans mistake appearances for truth.
- Decentered reformulation:
  Motion is an illusion created by perspective.
- Emergent structure:
  Reality is relative.

### Comparison
Annotation B fails.

Reason:
- target is weakened or lost
- hidden assumption is described rhetorically, not structurally
- reformulation becomes abstract and less explicit
- emergent structure is generic relativism, not a concrete relation

Verdict:
- A = acceptable annotation
- B = rejected annotation
- divergence = failure, not legitimate variation

---

## Minimal conclusion

Comparison does not require identical wording.

It requires structural consistency under variation.

A good comparison layer must separate:

- same structure expressed differently
- weaker but still acceptable decomposition
- failed annotation that abandons the target