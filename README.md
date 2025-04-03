# Pong - Jogo Clássico

Este é um jogo clássico de Pong implementado em Python usando a biblioteca `pygame`.

## Requisitos

Antes de executar o jogo, certifique-se de ter o Python instalado em sua máquina. Além disso, instale a biblioteca `pygame` caso ainda não a tenha:

```bash
pip install pygame
```

## Como Jogar

- **Jogador 1:** Usa as teclas `W` (subir) e `S` (descer) para controlar a raquete esquerda.
- **Jogador 2:** Usa as teclas `Seta para cima` (subir) e `Seta para baixo` (descer) para controlar a raquete direita.
- A bola se move automaticamente e rebate nas bordas superiores e inferiores.
- Se um jogador não conseguir rebater a bola, o adversário ganha um ponto.
- O jogo registra as pontuações em um arquivo `pontuacoes.txt`.

## Executando o Jogo

Para iniciar o jogo, execute o seguinte comando no terminal:

```bash
python pong.py
```

## Registro de Pontuações

As pontuações das partidas são salvas automaticamente no arquivo `pontuacoes.txt` no formato:

```
Jogador 1: X - Jogador 2: Y
```

Onde `X` e `Y` representam as pontuações de cada jogador ao final da execução do jogo.

## Contribuição

Se quiser contribuir com melhorias, sinta-se à vontade para abrir um Pull Request ou relatar problemas na seção de Issues.

## Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar!

