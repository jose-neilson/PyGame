**ANO 2026** 

## **Linguagem de Programação Aplicada** 

**Prof. Jadson de Araujo Almeida** 

Linguagem de Programação Aplicada 

## **OBJETIVO DO TRABALHO** 

Utilizando como referência as aulas da disciplina, você aluno deve **desenvolver um demo de jogo utilizando a linguagem Python** . 

O jogo não precisa estar completo, mas como toda versão demo, **deve ser jogável** possuindo: **controle do jogador + desafio + condição de vitória + condição de derrota.** É obrigatório que seja um **jogo 2D** , não pode ser um jogo via console (cmd). 

Todos os assets como imagem e som podem ser adquiridos na internet e não necessitam ser criados por você. Porém, o código produzido deve ser seu. Todos os detalhes, incluindo o tema do seu jogo, são decisões suas. 

Você aluno está autorizado a utilizar bibliotecas ou APIs que achar necessárias. 

**Seu projeto não pode ser uma cópia completa de outro projeto** . Isso é, ele pode ser inspirado em um outro jogo, mas será verificado se todo o projeto é um copy/paste, podendo a nota ser zerada. 

Seu jogo precisa ter um menu e já na tela do menu você deve escrever em alguma parte dele os comandos de controle. Por exemplo: “Space – Saltar”. Ou “CTRL – Atirar” etc. 

O produto desta atividade será **um arquivo ZIP contendo o projeto compilado para windows (exe + assets)** , que deve ser anexado na entrega do Trabalho. 

2 

Linguagem de Programação Aplicada 

## **Como criar uma build (compilação) do python para windows?** 

Siga o guia em anexo na aula 7. 

Modo alternativo: 

1. Com o **Pycharm** : https://www.youtube.com/watch?v=cGSerUmK0CE 

2. Com o **VsCode** : https://www.youtube.com/watch?v=LocNiBP4ik8 

Dica 1: em caso de erro ao executar o exe, é possível verificar a mensagem de erro gerada. Para isso você deve executá-lo via CMD. 

Dica 2: os assets (imagens, sons etc.) não são compilados junto com o exe. Então eles devem ser copiados e colados junto ao projeto compilado, mantendo a hierarquia de pastas igual a hierarquia que está no seu projeto. 

## **ATENÇÃO: Uso de URL (erro frequente)** 

Sempre que uma URL é usada (por exemplo, para importar assets em um projeto), há duas formas de ser aplicada. 

   - Você pode assistir esse vídeo sobre o assunto: https://youtu.be/j_aGOFAvyPA 

   - Ou ler o texto abaixo. 

- 1) **Caminho absoluto** : inicia informando a unidade até o arquivo final, exemplo 

## **"C:\Pasta 1\Pasta 2\arquivo.extensão"** . 

Essa opção não é recomendada, pois se o seu projeto for ser executado em outra máquina, esse caminho não vai encontrar o arquivo. 

O exemplo abaixo mostra um caminho absoluto para o arquivo piso.png, utilizado no script aaaTeste.py. 

- 2) **Caminho relativo** : inicia informando o caminho com base na localização atual do 

script que está usando a URL. O exemplo abaixo mostra que o script aaaTeste.py 

3 

Linguagem de Programação Aplicada 

utiliza uma URL para carregar o arquivo piso.png. Como a URL não inicia informando a unidade do disco, ele vai ser lida como caminho relativo. 

Então como o script e a pasta imagens estão no mesmo nível hierárquico, o caminho 

relativo vai usar o caminho base do script e adicionar a ele o **"imagens/piso.png".** 

Mas e quando o nível hierárquico do arquivo está acima do script? Nesse caso, precisamos fazer o caminho voltar um nível hierárquico. Isso é feito igual no CMD, iniciando com 2 pontos. 

Veja esse exemplo abaixo, onde movi o script aaaTeste.py para a pasta code, então tive que mudar a URL para **"../imagens/piso.png".** 

Dessa forma o leitor vai voltar uma pasta acima do nível, saindo da pasta code para a pasta **LPA 2025 B2** , para finalmente depois acrescentar o caminho **"imagens/piso.png"** . 

**Havendo dúvidas, consulte o professor tutor para auxiliá-lo.** 

4 

