# Laras Lesespiel

Jogo de leitura para iPad que treina reconhecer palavras e frases rápido (mesmo mecanismo do BYLET-F), sem cara de prova: só estrelas e recorde pessoal.

- **No ar:** https://morenolenn.github.io/lesespiel/
- **Repositório:** https://github.com/morenolenn/lesespiel (público, exigência do GitHub Pages grátis)
- **iPad:** Safari → Compartilhar → Adicionar à Tela de Início. Funciona offline depois da primeira abertura.

## Como funciona

1. Uma estrela pulsa onde a palavra vai aparecer.
2. A palavra (ou frase) aparece por alguns segundos e some.
3. Aparecem 4 imagens; a Lara toca na certa.

- **Errou:** a imagem tocada apaga e a palavra volta com 1,6× mais tempo. No segundo erro a palavra fica na tela e é falada. Nunca aparece "errado".
- **Dificuldade (níveis 1 a 6):** a palavra fica de 3,0 s a 0,7 s na tela. Cada acerto de primeira encurta o tempo ~6%; 3 acertos seguidos sobem 1 nível; 2 rodadas com erro descem 1 nível.
- **Frases:** depois da frase aparecem 4 cenas de dois emojis; as erradas trocam quem faz a ação, o objeto, ou os dois.
- **Sessão:** 10 rodadas ou 5 minutos (ajustável).
- **Modo pais:** segure a ⚙️ por 1 segundo.

## Rechnen (matemática)

Na home, **🔢 Rechnen** abre os exercícios de matemática, baseados nas provas e no livro do 2º ano (sem copiar páginas nem ilustrações). Ela digita a resposta num teclado numérico. Os enunciados **não** são lidos em voz alta, de propósito.

| Tipo | Exemplo | Dica quando erra |
|---|---|---|
| Über den Zehner | 8 + 5, 14 − 6 | campo de 20 bolinhas e "primeiro até o 10" |
| Platzhalter | __ + 5 = 13, 15 − __ = 6 | "calcule ao contrário" |
| Umkehraufgabe | 12 + 5 = 17 → 17 − 5 = 12 | escolher + ou −, "aus + wird −" |
| Welche Zahl ist es? | "Der Vorgänger ist 57." → 58 | reta numérica com Vorgänger / Zahl / Nachfolger |
| Rechenmauer | muro de 3 ou 4 andares | "dois tijolos juntos dão o de cima" |
| Rechendreieck | triângulo com somas nos lados | "fora = soma dos dois de dentro" |
| Rechengeschichte | lojinha: R (preços + total), troco de 20 €, A (frase certa) | ler a pergunta de novo |

Níveis 1 a 3, com o mesmo ajuste automático do Lesen. No modo pais dá para ligar e desligar cada tipo e ver os acertos.

## Arquivos

| Arquivo | O que é |
|---|---|
| `index.html` | O jogo inteiro. As listas de **palavras** e **frases** (JSON) estão no topo. |
| `audio/<voz>/<id>.mp3` | Áudios gravados (Tanja, Ingrid, Christoph em alemão; Francisca em português). |
| `sw.js` | Modo offline e atualização. |
| `version.json` | Número da versão publicada (o app compara com o dele para se atualizar). |
| `manifest.webmanifest`, `icon-*.png` | Ícone e modo "app" na tela de início. |
| `tools/gerar_audio.py` | Gera os áudios que faltam (palavras e frases novas). |
| `tools/gerar_icone.swift` | Gera os ícones PNG. |

## Editar palavras ou frases

1. Em `index.html`, edite o bloco `<script id="words">` ou `<script id="sentences">`.
   - Palavra: `{"id": "hund", "emoji": "🐶", "de": "Hund", "pt": "Cachorro"}`
   - Frase: `{"id": "s65", "s": "hund", "o": "ball", "de": "...", "pt": "..."}` — `s` e `o` são ids de palavras; a cena é o emoji de `s` + o de `o`.
2. Gere os áudios novos (só cria os que não existem):

   ```bash
   python3 -m venv tools/venv && tools/venv/bin/pip install edge-tts
   tools/venv/bin/python tools/gerar_audio.py index.html audio
   ```

   As vozes vêm do serviço de leitura do Microsoft Edge via o pacote `edge-tts` (uso não oficial, ok para uso pessoal).

## Publicar uma atualização

1. Aumente a versão em **três** lugares, com o mesmo número:
   - `index.html` → `const APP_VERSION = 13;`
   - `version.json` → `{"v":13}`
   - `sw.js` → `const CACHE = 'lesespiel-v13';`
2. `git add -A && git commit -m "..." && git push`
3. Em ~1 minuto está no ar. O iPad se atualiza sozinho ao abrir ou voltar para o app (confira em Modo pais → "Versão N").

## Dados e privacidade

Progresso, estatísticas e a foto da Lara ficam só no `localStorage` do iPad; nada é enviado para servidor.
