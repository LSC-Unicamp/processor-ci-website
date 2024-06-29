# Processor CI

The field of Computer Architecture is entering a renaissance period, characterized by the emergence of domain-specific hardware, enhanced security measures, open Instruction Set Architectures (ISA), and agile development methodologies. This transformative era demands novel tools and methodologies to address these challenges effectively, fostering innovation in solving long-standing issues. The widespread adoption of open ISAs, enhanced by the RISC-V processor, marks a historic milestone in the software and hardware industries, enabling diverse implementations of the same hardware blueprint. However, the landscape of processor designs is vast and varied, encompassing different description languages, tools, design methodologies, and target environments such as ASICs, simulations, and FPGAs. This diversity is evident only from the RISC-V website, which lists 17 distinct implementations beginning with letter A. Although future consolidation of key implementations is anticipated, current efforts are focused on meeting specific design constraints related to area, power, and performance. A common foundation across these varied implementations could be their testing protocols. Despite the existence of several critical programs and verification strategies for RISC-V, a unified resource that consolidates these elements is lacking, so large-scale industries rely on their internal frameworks for test case reuse and consolidation, while entrant actors need to construct all infrastructure from scratch. 

We are working on a novel approach that involves a Continuous Integration (CI) environment and a suite of FPGAs from various manufacturers as a standardized verification strategy for open source RISC-V processors. Our current setup includes FPGAs from Intel, AMD, Lattice, and Gowin, integrated with a system that connects directly to the GitHub repository to automatically fetch each new commit in a processor, facilitating a seamless CI flow across different FPGA platforms. We envision some key advantages of such approach:

1.  a fast startup methodology for entrants;
2.  a way to quickly include new software and hardware tests that evaluate against several distinct processors;
3.  a well-known way to check and evaluate processor maturity at the same infrastructure; and
4.  an opportunity to collect, study, and research multiple distinct designs that reach a broad spectrum on the design space of processors.

The Processor CI is an open-source framework that provides a set of tools to facilitate the verification of processors in a continuous integration environment with the assistance of FPGAs.

## Advantages

- Faster
- Less invasive to the processor core
- Hardware testing
- Completely open-source