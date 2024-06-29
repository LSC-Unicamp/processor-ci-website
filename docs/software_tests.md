# Software Tests

The software infrastructure can be split into the software stack for the Processor CI, which comprises of the Jenkins framework and the synthesis and compiler toolsets. The second part is the software tests, which are the tests that are run on the Processor CI to verify the processor's correctness.

## Jenkins infrastructure

We use out-of the shelf Jenkins to run the tests. The Jenkins server is responsible for running the tests, managing the test results, and providing a web interface for the user to interact with the tests.

Our key goal is to include new processors by adding their github repository to the Jenkins server. This way, the system fetchs the processor design for every commit and run the tests.

As coleteral, we also provide a stamp of pass/fail on tests to be included in the github project.

We use multiple FPGA hardware and, consequently, we use distinct synthesis and configuration tools. We try to keep all those tools updated to the last version that support our hardware infrastructure. We also use the YoSys synthesis tool to synthesize the processor design and, in the future, we plan to explore ASIC synthesis flows.

## Processor CI Tests

To control and validate the processor infrastructure, we use the the hardware infrastructure to run a set of software that we collect from all processors we agregate in the system and add to them some of our own software desigend to increase the software complexity by using more and more instruction from the ISA.

The future goal is to split all tests into requirements and provide badges for each of the RISC-V extensions as a way to partially validate the processor.

[Github repository](https://github.com/LSC-Unicamp/riscv-isa-ci-tests)

### Processor CI Interface

For each hardware feature we add to our FPGA, we add specifically designed software commands, configurations and checks to work on the processor CI. This way, we can test the processor in a more complex way, by using the hardware features in a more complex way, but share these infrastrucutre among multiple processors to reduce the effort of adding new processors to the CI.

[Github repository](https://github.com/LSC-Unicamp/riscv-isa-ci)