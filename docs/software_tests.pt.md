# Testes de Software

A infraestrutura de software pode ser dividida em duas partes: a pilha de software para o Processor CI, que inclui o framework Jenkins e as ferramentas de síntese e compilação; e a segunda parte, que são os testes de software executados no Processor CI para verificar a correção do processador.

## Infraestrutura Jenkins

Usamos o Jenkins disponível no mercado para executar os testes. O servidor Jenkins é responsável por rodar os testes, gerenciar os resultados dos testes e fornecer uma interface web para o usuário interagir com os testes.

Nosso objetivo principal é incluir novos processadores adicionando seu repositório do GitHub ao servidor Jenkins. Dessa forma, o sistema busca o design do processador para cada commit e executa os testes.

Como adicional, também fornecemos uma marcação de aprovação/reprovação nos testes para serem incluídos no projeto do GitHub.

Usamos múltiplos hardwares FPGA e, consequentemente, utilizamos ferramentas distintas de síntese e configuração. Tentamos manter todas essas ferramentas atualizadas para a versão mais recente que suporta nossa infraestrutura de hardware. Também usamos a ferramenta de síntese YoSys para sintetizar o design do processador e, no futuro, planejamos explorar fluxos de síntese ASIC.

## Testes do Processor CI

Para controlar e validar a infraestrutura do processador, utilizamos a infraestrutura de hardware para rodar um conjunto de software que coletamos de todos os processadores que agregamos ao sistema e adicionamos a eles alguns de nossos próprios softwares projetados para aumentar a complexidade do software, utilizando cada vez mais instruções da ISA.

O objetivo futuro é dividir todos os testes em requisitos e fornecer distintivos para cada uma das extensões RISC-V como uma forma de validar parcialmente o processador.

[Repositório no Github](https://github.com/LSC-Unicamp/processor-ci-tests)

### Interface do Processor CI

Para cada recurso de hardware que adicionamos ao nosso FPGA, incluímos comandos de software, configurações e verificações especificamente projetados para funcionar no Processor CI. Dessa forma, podemos testar o processador de uma maneira mais complexa, utilizando os recursos de hardware de forma mais sofisticada, mas compartilhando essa infraestrutura entre múltiplos processadores para reduzir o esforço de adicionar novos processadores ao CI.

[Repositório no Github](https://github.com/LSC-Unicamp/processor-ci)