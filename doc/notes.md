Features
========

Simulation:
* Allow multi-beat throws

Visualization:
* What type of pass is each juggler throwing?
* What would happen if we would stop now?

Analysis:
* Detect period
  * Strict: all clubs are in their initial positions
  * Loose 1: all jugglers have the same clubs again, in any order
  * Loose 2: all colors are in their initial positions (clubs of the same color
    can be swapped)
  * If the colors are sorted in the beginning, loose 1 and loose 2 should be
    equivalent
* How many clubs are on each side (held or self)?
* Detect collisions (two throws to the same hand)
  * Three count with one cross pass only (TBC)
* Detect close encounters (opposing passes)
* For color passing: which starting configurations work?

Implementation
==============

* Clean up
* Unify start and catch
* Should t=0 be before the start and t=1 the initial pass?
* Jugglers: don't use global time




Patterns we can model with this
===============================

1 juggler:
  * Cascade
  * Any siteswap?

2 jugglers:
  * N count
  * N count with isolated doubles
  * Countdown
  * 3 count with one cross pass and one cross pass back

3 jugglers:
  * 4 count feeding
  * Pass pass self (3 count feeding)?
