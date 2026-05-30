# 🎙️ Assistente de Voz com IA

> Um sistema completo de gravação, transcrição e resposta por IA usando Google Gemini. Ideal para automação de entrevistas, anotações por voz ou criação de assistentes pessoais.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-3.5%20Flash-purple)
![PyAudio](https://img.shields.io/badge/PyAudio-0.2.14-red)
![Status](https://img.shields.io/badge/status-finalizado-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📖 Visão Geral

Este projeto permite capturar áudio do microfone, transcrevê‑lo automaticamente utilizando o modelo **Gemini 3.5 Flash** e, em seguida, obter uma resposta gerada pela mesma IA, tudo a partir de um único fluxo em Python.

O sistema foi desenvolvido com foco em:

- **Modularização** – cada responsabilidade ficou em um módulo separado.
- **Tratamento de erros** – respostas amigáveis para rate limit, timeout, serviço indisponível etc.
- **Português do Brasil** – transcrição otimizada com pontuação, capitalização e identificação de falantes.
- **Simplicidade** – não requer banco de dados ou infraestrutura complexa.

## 🎥 Video explicativo

![Demonstração do projeto](caminho_local_para_video)

## 🛠️ Stack Técnica

| Tecnologia | Versão |
|------------|--------|
| Python | 3.12+ |
| google-genai | 2.6.0 |
| PyAudio | 0.2.14 |
| python-dotenv | 1.2.2 |
| requests, httpx, websockets | Conforme `requirements.txt` |

## 🏗️ Estrutura do Projeto

```bash
meu-projeto/
│
├── data/
│   ├── audio_for_ai.wav       # Áudio gravado (gerado dinamicamente)
│   └── prompt.txt             # Prompt base para a transcrição
│
├── services/
│   ├── audio_recording.py     # Gravação do microfone
│   ├── audio_transcription.py # Transcrição com Gemini
│   └── ai_response.py         # Geração de resposta com Gemini
│
├── main.py                    # Orquestração do fluxo principal
├── .env                       # Chave da API (não versionar)
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## ⚙️ Arquitetura e Organização

O código foi dividido em módulos independentes, facilitando manutenção e reuso.

### `main.py`

Ponto de entrada da aplicação.

- Lê o `prompt.txt` da pasta `data/`
- Chama `transcribe_with_gemini()` para transcrever o áudio
- Exibe a pergunta do usuário
- Chama `generate_response()` para obter a resposta da IA
- Mostra a resposta no terminal

### `services/audio_recording.py`

Responsável pela captura de áudio em tempo real.

- Utiliza **PyAudio** para acessar o microfone
- Grava até o usuário pressionar `Ctrl+C`
- Salva o arquivo `audio_for_ai.wav` em `data/`
- Configuração: 1 canal, taxa 44000 Hz, blocos de 1024 frames

### `services/audio_transcription.py`

Transcreve o áudio utilizando o **Gemini**.

- Carrega a `API_KEY` do arquivo `.env`
- Faz upload do arquivo `.wav` para o Google GenAI
- Envia o `prompt.txt` como instrução e o áudio como conteúdo
- Retorna o texto transcrito

**Modelo padrão:** `gemini-3.5-flash`

### `services/ai_response.py`

Gera a resposta da IA com base no texto recebido.

- Usa o mesmo cliente Gemini
- Trata exceções comuns:
  - `ResourceExhausted` → limite de requisições atingido
  - `DeadlineExceeded` → timeout
  - `ServiceUnavailable` → serviço indisponível
  - `InvalidArgument` → conteúdo vazio/inválido
  - `PermissionDenied` → chave sem permissão

### `data/prompt.txt`

Instrução detalhada para o modelo de transcrição:

- Idioma: português do Brasil
- Adicionar pontuação e capitalização
- Não resumir, não interpretar
- Preservar palavras informais
- Marcar trechos incertos como `[inaudível]`
- Identificar múltiplos falantes: `[Falante 1]`, `[Falante 2]` etc.

## ✨ Funcionalidades

### 🎤 Gravação de Áudio

Inicie a gravação executando o módulo `audio_recording.py`. O sistema captura tudo que for dito ao microfone até que você interrompa com `Ctrl+C`. O áudio é salvo automaticamente como `data/audio_for_ai.wav`.

### 📝 Transcrição Inteligente

O áudio é enviado ao Gemini junto com o prompt especializado. O retorno é uma transcrição limpa, pontuada e formatada – pronta para ser usada como pergunta.

### 🤖 Geração de Resposta

A pergunta transcrita é enviada novamente ao Gemini, que retorna uma resposta contextual. Tratamento de erros garante que problemas de API não quebrem o programa.

### 🔁 Fluxo Completo

```bash
PERGUNTA DO USUARIO:
[texto transcrito]

RESPOSTA IA:
[resposta gerada]
```

## 🚀 Guia de Instalação e Execução

### Pré-requisitos

- Python 3.12+
- Microfone funcionando
- Conta Google Cloud com API Generative Language ativada
- Git (opcional)

### Passo 1 — Obter uma chave de API do Google Gemini

1. Acesse [Google AI Studio](https://aistudio.google.com/)
2. Faça login com sua conta Google
3. Clique em **Get API key** → **Create API key**
4. Copie a chave gerada (ex: `AIzaSy...`)

> 📘 **Dúvidas sobre a API?** Consulte a [documentação oficial do Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart).

### Passo 2 — Clonar o repositório

```bash
git clone <url-do-seu-repositorio>
cd meu-projeto
```

### Passo 3 — Criar ambiente virtual

**Linux / macOS**
```bash
python3 -m venv venv
```

**Windows**
```bash
python -m venv venv
```

### Passo 4 — Ativar ambiente virtual

**Linux / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### Passo 5 — Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 6 — Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
API_KEY=AIzaSy...sua_chave_aqui
```

> **Nunca versione o arquivo `.env`.** O `.gitignore` já está configurado para ignorá-lo.

### Passo 7 — Executar a aplicação

**Atenção:** O fluxo completo exige dois passos. Primeiro você deve gerar o arquivo de áudio que será transcrito.

#### Opção A – Gravar áudio com o microfone (recomendado)

Execute o módulo de gravação:

```bash
python services/audio_recording.py
```
> ⚠️ **Importante:** O `main.py` espera que o arquivo `data/audio_for_ai.wav` já exista.  
> Você deve **primeiro** gravar o áudio com `audio_recording.py` (ou colocar seu próprio arquivo `.wav` nesse caminho).  
> Só depois execute `python main.py`.
Fale algo e pressione `Ctrl+C` para finalizar a gravação. O arquivo será salvo em `data/audio_for_ai.wav`.

#### Opção B – Usar seu próprio arquivo de áudio

- Substitua o arquivo `data/audio_for_ai.wav` pelo seu (mantenha o nome exato).
- Ou edite a variável `audio_path` dentro do `main.py` para apontar para o seu arquivo.

#### Após ter o áudio – executar o fluxo principal

```bash
python main.py
```

Você verá a pergunta transcrita e a resposta da IA.

## 💾 Persistência de Dados

- O áudio gravado fica em `data/audio_for_ai.wav` (sobrescrito a cada nova gravação).
- O `prompt.txt` pode ser editado para alterar o comportamento da transcrição.
- Nenhum banco de dados externo é utilizado – o projeto é totalmente auto‑contido.

## 🎯 Objetivos de Aprendizado

Este projeto foi criado para praticar:

- Integração com APIs de IA (Google Gemini)
- Gravação e processamento de áudio com PyAudio
- Modularização e responsabilidade única
- Tratamento de exceções em requisições externas
- Uso de variáveis de ambiente para segurança
- Leitura/escrita de arquivos locais (WAV, TXT, JSON de requisitos)

## 🔮 Melhorias Futuras

- Correção automática da inconsistência `paInt16` / `paInt32`
- Interface gráfica simples (Tkinter ou Gradio)
- Loop contínuo de conversa (pergunta → resposta → nova pergunta)
- Suporte a vários formatos de áudio (MP3, M4A)
- Transcrição em tempo real (streaming)
- Salvar conversas em log
- Adicionar testes unitários

## 📌 Observações

- O áudio é gravado em **44000 Hz, mono, 16 bits** – você pode ajustar a taxa no código.
- A **API do Google Gemini tem limites gratuitos**. Se atingir o rate limit, aguarde alguns segundos e tente novamente.
- O modelo `gemini-3.5-flash` é rápido e adequado para transcrição e chat. Você pode trocar para `gemini-2.0-flash` (mais novo) se desejar.
- O prompt de transcrição foi especialmente escrito para português do Brasil – sinta‑se à vontade para adaptá‑lo.

## 👨‍💻 Autor

Desenvolvido por Enzo Peralva para fins de estudo, automação pessoal e integração de áudio com LLMs.
```