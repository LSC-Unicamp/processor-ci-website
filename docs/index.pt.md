# CI de Processador

O campo da Arquitetura de Computadores está entrando em um período de renascimento, caracterizado pelo surgimento de hardware específico para domínios, medidas de segurança aprimoradas, Arquiteturas de Conjunto de Instruções (ISA) abertas e metodologias de desenvolvimento ágeis.

Essa era transformadora exige ferramentas e metodologias inovadoras para enfrentar esses desafios de forma eficaz, promovendo a inovação na resolução de problemas antigos. A adoção generalizada de ISAs abertas, reforçada pelo processador RISC-V, marca um marco histórico nas indústrias de software e hardware, possibilitando diversas implementações do mesmo modelo de hardware. No entanto, o cenário dos projetos de processadores é vasto e variado, abrangendo diferentes linguagens de descrição, ferramentas, metodologias de design e ambientes alvo, como ASICs, simulações e FPGAs. Essa diversidade é evidente apenas no site do RISC-V, que lista 17 implementações distintas começando com a letra A.

Embora se antecipe uma futura consolidação das principais implementações, os esforços atuais estão focados em atender a restrições de design específicas relacionadas a área, consumo de energia e desempenho. Uma base comum entre essas implementações variadas pode ser seus protocolos de teste. Apesar da existência de vários programas críticos e estratégias de verificação para RISC-V, falta um recurso unificado que consolide esses elementos, então grandes indústrias dependem de seus frameworks internos para reutilização e consolidação de casos de teste, enquanto novos participantes precisam construir toda a infraestrutura do zero.

Estamos trabalhando em uma abordagem inovadora que envolve um ambiente de Integração Contínua (CI) e um conjunto de FPGAs de vários fabricantes como uma estratégia de verificação padronizada para processadores RISC-V de código aberto. Nossa configuração atual inclui FPGAs da Intel, AMD, Lattice e Gowin, integrados com um sistema que se conecta diretamente ao repositório do GitHub para buscar automaticamente cada novo commit em um processador, facilitando um fluxo contínuo de CI em diferentes plataformas FPGA. Enxergamos algumas vantagens-chave dessa abordagem:

1. uma metodologia de inicialização rápida para novos participantes;
2. uma forma de incluir rapidamente novos testes de software e hardware que avaliem diferentes processadores;
3. uma maneira bem conhecida de verificar e avaliar a maturidade do processador na mesma infraestrutura; e
4. uma oportunidade para coletar, estudar e pesquisar vários designs distintos que abrangem um amplo espectro no espaço de design de processadores.

O Processor CI é uma framework de código aberto que fornece um conjunto de ferramentas para facilitar a verificação de processadores em um ambiente de integração contínua com o auxílio de FPGAs.