# Infraestrutura de Hardware

## Controlador de CI de Processador

O Controlador de CI de Processador é um módulo de hardware que atua como um encapsulador ao redor do núcleo do processador, permitindo o controle sobre ele, monitorando o barramento de memória e gerenciando sinais como clock, reset e halt.

A ideia principal é ser capaz de controlar diferentes tipos de processadores sem precisar interceptar sinais internos, como feito em trabalhos anteriores. Dessa forma, o controlador pode ser usado com qualquer processador que siga a ISA RISC-V, sem a necessidade de modificar o RTL do processador.

[Repositório no Github](https://github.com/LSC-Unicamp/processor-ci-controller)

## Módulos do Projeto

O controlador é dividido em vários módulos, cada um responsável por realizar uma função específica. Entre os módulos existentes, os principais são:

![Diagrama com os módulos](assets/controlador-riscv.svg)

### Interpretador

O interpretador é responsável por receber instruções enviadas pelo software de teste e emitir comandos para outros módulos. Esses comandos podem envolver tarefas como leitura e escrita na memória, fornecer N ciclos de clock ao processador, etc.

### Módulo de Comunicação

O módulo de comunicação atua como a ponte entre a máquina hospedeira que executa o software de teste e o controlador. É responsável por implementar o protocolo a ser utilizado, que pode ser UART, SPI ou PCIe.

### Controlador de Clock

O controlador de clock gerencia o sinal de clock fornecido ao processador. Ele tem a capacidade de fornecer um número específico de pulsos e/ou dividir a frequência do clock.

### Controlador de Memória

O controlador de memória fornece uma interface de acesso à memória tanto para o controlador quanto para o processador, gerenciando a prioridade com que cada um pode interagir com a memória.

## Placas FPGA Atualmente Suportadas

- Digilent Nexys 4 DDR
- Tang nano 20k
- Colorlight i9
- Digilent Arty A7 100T
- Xilinx VC709
- Cyclone 10 GX (Em progresso)

<img src="/assets/nexys4ddr.jpg" alt="Nexys 4 DDR" width="200px">
<img src="/assets/tangnano20k.jpg" alt="Tang nano 20k" width="200px">
<img src="/assets/colorlighti9.jpg" alt="Colorlight i9" width="200px">
<img src="/assets/artya7100t.jpg" alt="Digilent Arty A7 100T" width="200px">
<img src="/assets/vc709.jpg" alt="Xilinx VC709" width="200px">