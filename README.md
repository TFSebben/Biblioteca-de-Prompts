# 📚 Biblioteca de Prompts (Edição 2026)

> Repositório oficial para controle de versão, arquitetura e curadoria de prompts de alta performance, compatíveis com a safra de modelos de Extended Thinking de 2026 (Claude Sonnet 5, Claude Opus 5.5, GPT-6 Sol/Luna, Gemini 3.8 Flash, Nano Banana Pro).

Todos os prompts foram concebidos e refatorados sob as diretrizes rigorosas da skill `/prompt-engineer`:
- **Gavetas Semânticas (XML):** `<identity>`, `<context>`, `<instructions>`, `<constraints>`, `<untrusted_content>` e `<output_format>`.
- **Blindagem Anti-Injection:** Isolamento estrito de entradas em `<untrusted_content>` com diretivas anti-override.
- **Zero CoT Manual:** Otimizados para modelos de raciocínio profundo nativo, eliminando comandos artificiais de 'pense passo a passo'.
- **Engenharia de Saída (Recency Effect):** Formatos finais posicionados cirurgicamente no término do prompt.

---

## 🗂️ Estrutura de Categorias & Prompts Catalogados

### 01. Clones Cognitivos & Especialistas de Domínio
📁 Pasta: [`01_Clones_e_Especialistas/`](01_Clones_e_Especialistas/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Agente de Suporte Técnico SaaS (N1 e N2)](01_Clones_e_Especialistas/Agente%20de%20Suporte%20Técnico%20SaaS%20(N1%20e%20N2).md) | `GPT-6 Luna` | Agente autônomo treinado para atendimento de suporte, resolução de dúvidas frequentes, diagnóstico de problemas e escalonamento estruturado ... |
| [Clone Bill Gates - Estratégia e Primeiros Princípios](01_Clones_e_Especialistas/Clone%20Bill%20Gates%20-%20Estratégia%20e%20Primeiros%20Princípios.md) | `Claude Opus 5.5` | Persona detalhada inspirada em Bill Gates, aplicando pensamento de primeiros princípios, rigor analítico, visão sistêmica de tecnologia e im... |
| [Clone Simon Sinek - Liderança e Propósito](01_Clones_e_Especialistas/Clone%20Simon%20Sinek%20-%20Liderança%20e%20Propósito.md) | `Claude Opus 5.5` | Emula Simon Sinek e o framework do Círculo Dourado ('Comece pelo Porquê'), auxiliando líderes a formularem propósitos autênticos e engajarem... |
| [Conselheiro Estratégico Executivo (Board Advisor)](01_Clones_e_Especialistas/Conselheiro%20Estratégico%20Executivo%20(Board%20Advisor).md) | `Claude Opus 5.5` | Framework agêntico para modelar especialistas de renome mundial, emulando seus modelos mentais, repertório decisório e tom de voz caracterís... |
| [Especialista em Cibersegurança e Defesa de LLMs](01_Clones_e_Especialistas/Especialista%20em%20Cibersegurança%20e%20Defesa%20de%20LLMs.md) | `Claude Opus 5.5` | System prompt para CISO e especialista em cibersegurança, estabelecendo matrizes de risco, conformidade LGPD/ISO 27001 e arquitetura de defe... |
| [Especialista em Cloud e Infraestrutura de TI](01_Clones_e_Especialistas/Especialista%20em%20Cloud%20e%20Infraestrutura%20de%20TI.md) | `Claude Opus 5.5` | System prompt para arquiteto sênior de infraestrutura de TI, cobrindo virtualização, topologias de rede, segurança perimetral e arquiteturas... |
| [Especialista em Engenharia de Software e Liderança Técnica](01_Clones_e_Especialistas/Especialista%20em%20Engenharia%20de%20Software%20e%20Liderança%20Técnica.md) | `Claude Sonnet 5` | System prompt para Head de Engenharia e Gestor de Software, alinhando ciclos ágeis, arquitetura de microsserviços, CI/CD e excelência técnic... |
| [Especialista em Governança e Conformidade de TI](01_Clones_e_Especialistas/Especialista%20em%20Governança%20e%20Conformidade%20de%20TI.md) | `Claude Opus 5.5` | System prompt para persona sênior em Governança de TI, COBIT, ITIL e conformidade cibernética, estruturando processos de governança em ambie... |
| [Especialista em Liderança e Gestão de Pessoas](01_Clones_e_Especialistas/Especialista%20em%20Liderança%20e%20Gestão%20de%20Pessoas.md) | `Claude Opus 5.5` | System prompt para consultor executivo de liderança estratégica, focado em alinhamento de metas, cultura organizacional de alto desempenho e... |
| [Especialista em PEI e Educação Inclusiva](01_Clones_e_Especialistas/Especialista%20em%20PEI%20e%20Educação%20Inclusiva.md) | `Gemini 3.8 Flash` | Atua como consultor pedagógico e psicopedagógico na elaboração de Planos de Ensino Individualizados (PEI) para estudantes com necessidades e... |
| [Persona Aurora - Diálogo Filosófico e Existencial](01_Clones_e_Especialistas/Persona%20Aurora%20-%20Diálogo%20Filosófico%20e%20Existencial.md) | `Claude Sonnet 5` | Persona com alta profundidade lírica e reflexiva, desenvolvida para explorar questões existenciais, diálogo filosófico e descoberta de signi... |

### 02. Vendas, Marketing & Copywriting Persuasivo
📁 Pasta: [`02_Vendas_Marketing_e_Copywriting/`](02_Vendas_Marketing_e_Copywriting/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Agente Closer de Vendas B2B](02_Vendas_Marketing_e_Copywriting/Agente%20Closer%20de%20Vendas%20B2B.md) | `GPT-6 Luna` | Protocolo de conversão agressivo e consultivo para conduzir leads quentes ao fechamento comercial, quebrando objeções de preço e cronograma. |
| [Agente SDR de Qualificação e Agendamento](02_Vendas_Marketing_e_Copywriting/Agente%20SDR%20de%20Qualificação%20e%20Agendamento.md) | `GPT-6 Luna` | Agente SDR e pré-vendedor modular com parametrização dinâmica por variáveis ({{NICHO}}, {{PRODUTO}}, {{CANAL}}), aplicando lead scoring em t... |
| [Copywriter de Páginas de Vendas e Anúncios](02_Vendas_Marketing_e_Copywriting/Copywriter%20de%20Páginas%20de%20Vendas%20e%20Anúncios.md) | `GPT-6 Sol` | Persona de copywriter de resposta direta focada em gerar headlines magnéticas, narrativas de storytelling persuasivo e ofertas irresistíveis... |
| [Copywriting de Mecanismo Único e Framework 3Rs](02_Vendas_Marketing_e_Copywriting/Copywriting%20de%20Mecanismo%20Único%20e%20Framework%203Rs.md) | `GPT-6 Luna` | Estrutura anúncios e copies persuasivas aplicando a fórmula dos 3Rs (Resultados, Razões e Roteiro) combinada com a identificação e amplifica... |
| [Criador de Legendas Estratégicas para Redes Sociais](02_Vendas_Marketing_e_Copywriting/Criador%20de%20Legendas%20Estratégicas%20para%20Redes%20Sociais.md) | `GPT-6 Sol` | Formula legendas dinâmicas com ganchos de alta retenção nos primeiros 3 segundos, desenvolvimento envolvente e chamadas para ação (CTAs) de ... |
| [Criador de Posts de Autoridade para LinkedIn](02_Vendas_Marketing_e_Copywriting/Criador%20de%20Posts%20de%20Autoridade%20para%20LinkedIn.md) | `Claude Sonnet 5` | Framework completo de redação para LinkedIn combinando ganchos de alta taxa de retenção ('Stop-the-Scroll'), narrativa pessoal autêntica e a... |
| [Diagnóstico Empresarial e Discovery de IA](02_Vendas_Marketing_e_Copywriting/Diagnóstico%20Empresarial%20e%20Discovery%20de%20IA.md) | `Claude Opus 5.5` | Processa transcrições brutas de reuniões de discovery, consultoria ou vendas para diagnosticar o estágio de maturidade do negócio, mapear op... |
| [Mapeamento Psicológico de Público-Alvo (Social Listening)](02_Vendas_Marketing_e_Copywriting/Mapeamento%20Psicológico%20de%20Público-Alvo%20(Social%20Listening).md) | `Claude Sonnet 5` | Executa varredura profunda em fóruns como Reddit e tendências do Google via Perplexity para mapear dores latentes, objeções reais e desejos ... |
| [Redator de Artigos Long-Form para SEO e IA](02_Vendas_Marketing_e_Copywriting/Redator%20de%20Artigos%20Long-Form%20para%20SEO%20e%20IA.md) | `GPT-6 Sol` | Redige artigos long-form de alta autoridade com foco em SEO semântico, arquitetura de cabeçalhos H2/H3 e densidade balanceada de palavras-ch... |

### 03. Arquitetura de Agentes, System Prompts & Segurança
📁 Pasta: [`03_Arquitetura_Agentes_e_Seguranca/`](03_Arquitetura_Agentes_e_Seguranca/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Arquitetura de Agentes Autônomos (Nate Herk)](03_Arquitetura_Agentes_e_Seguranca/Arquitetura%20de%20Agentes%20Autônomos%20(Nate%20Herk).md) | `Gemini 3.8 Flash` | Arquitetura completa para construção de agentes autônomos orientados a objetivos, com loops de reflexão interna, uso de ferramentas e recupe... |
| [Auditoria de Prompt Injection e Red Teaming](03_Arquitetura_Agentes_e_Seguranca/Auditoria%20de%20Prompt%20Injection%20e%20Red%20Teaming.md) | `Claude Sonnet 5` | Suite de testes práticos contendo padrões de injeção direta, encoding Base64 e comandos de bypass para auditar a resiliência de guardrails e... |
| [Guardrail de Triagem e Blindagem contra Jailbreaks](03_Arquitetura_Agentes_e_Seguranca/Guardrail%20de%20Triagem%20e%20Blindagem%20contra%20Jailbreaks.md) | `Claude Sonnet 5` | Protocolos de segurança e encadeamento de prompts para prevenir injeções maliciosas, jailbreaks de persona e vazamento de instruções protegi... |
| [Protocolo de Diagnóstico Administrativo (#adm)](03_Arquitetura_Agentes_e_Seguranca/Protocolo%20de%20Diagnóstico%20Administrativo%20(#adm).md) | `Claude Sonnet 5` | Diretrizes de intervenção administrativa para diagnosticar erros de raciocínio, contornar loops infinitos e forçar recalibração de parâmetro... |
| [System Prompt de Raciocínio Frontier (Claude Fable)](03_Arquitetura_Agentes_e_Seguranca/System%20Prompt%20de%20Raciocínio%20Frontier%20(Claude%20Fable).md) | `Claude Sonnet 5` | Diretrizes de raciocínio de ponta, manipulação contextual em larga escala e rigor técnico modelados a partir da arquitetura do Claude Fable. |
| [System Prompt do Agente Autônomo Manus AI](03_Arquitetura_Agentes_e_Seguranca/System%20Prompt%20do%20Agente%20Autônomo%20Manus%20AI.md) | `Claude Sonnet 5` | Engenharia reversa do system prompt do Manus AI, demonstrando como orquestrar planejamento em múltiplos passos, execução assíncrona e chamad... |
| [Template de Governança de Repositório (CLAUDE.md & AGENTS.md)](03_Arquitetura_Agentes_e_Seguranca/Template%20de%20Governança%20de%20Repositório%20(CLAUDE.md%20&%20AGENTS.md).md) | `Claude Sonnet 5` | Template padronizado de instruções operacionais para governança de assistentes CLI (Claude Code, Antigravity), definindo convenções de códig... |
| [Template de Máquina de Estados para Agentes Autônomos](03_Arquitetura_Agentes_e_Seguranca/Template%20de%20Máquina%20de%20Estados%20para%20Agentes%20Autônomos.md) | `Claude Opus 5.5` | Gabarito canônico para criação de novos agentes, estabelecendo seções modulares para Identidade, Regras de Ouro, Escopo, Ferramentas e Trata... |
| [Template de Orquestração de Subagentes](03_Arquitetura_Agentes_e_Seguranca/Template%20de%20Orquestração%20de%20Subagentes.md) | `Claude Sonnet 5` | Gabarito de configuração de subagentes independentes para Claude Code e Antigravity, isolando responsabilidades, permissões de ferramentas e... |

### 04. Frameworks de Prompting & Meta-Prompts
📁 Pasta: [`04_Frameworks_de_Prompting_e_Metaprompts/`](04_Frameworks_de_Prompting_e_Metaprompts/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Framework 'A Arte do Saber Pedir 2.0'](04_Frameworks_de_Prompting_e_Metaprompts/Framework%20'A%20Arte%20do%20Saber%20Pedir%202.0'.md) | `GPT-6 Sol` | Metodologia para arquitetar comandos de alta precisão em modelos de raciocínio profundo, superando a obsolescência de prompts formulados em ... |
| [Framework de 8 Componentes para Leitura Sintópica](04_Frameworks_de_Prompting_e_Metaprompts/Framework%20de%208%20Componentes%20para%20Leitura%20Sintópica.md) | `Gemini 3.8 Flash` | Framework estruturado com 8 elementos indispensáveis (Problema, Ação, Persona, Contexto, Dados, Passos, Formato e Exemplo) para tarefas comp... |
| [Mapeador de Processos e Diagramas Mermaid (BPM)](04_Frameworks_de_Prompting_e_Metaprompts/Mapeador%20de%20Processos%20e%20Diagramas%20Mermaid%20(BPM).md) | `GPT-6 Luna` | Atua como Gerente de Projetos e Processos para auditar gargalos operacionais, desenhar fluxos escaláveis e gerar diagramas de arquitetura fu... |
| [Meta-Prompt Gerador de Personas Especialistas](04_Frameworks_de_Prompting_e_Metaprompts/Meta-Prompt%20Gerador%20de%20Personas%20Especialistas.md) | `Claude Sonnet 5` | Meta-prompt para criar personas de consultores e instrutores hiperespecializados em qualquer área do conhecimento, com definição clara de es... |
| [Meta-Prompt de Refinamento Socrático de Prompts](04_Frameworks_de_Prompting_e_Metaprompts/Meta-Prompt%20de%20Refinamento%20Socrático%20de%20Prompts.md) | `Claude Sonnet 5` | Meta-prompt interativo onde a IA atua como arquiteto de prompts, entrevistando o usuário iterativamente para construir a instrução ideal par... |
| [Normalizador de Webhooks em JSON para NoCode](04_Frameworks_de_Prompting_e_Metaprompts/Normalizador%20de%20Webhooks%20em%20JSON%20para%20NoCode.md) | `Gemini 3.8 Flash` | Estruturação de prompts otimizados para integração com plataformas de automação (Make, n8n) e ecossistemas NoCode, gerando saídas em JSON es... |
| [Padrões Oficiais de Prompting - Anthropic Claude](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20Anthropic%20Claude.md) | `Claude Sonnet 5` | Padrão canônico de excelência da Anthropic para modelos Claude (Sonnet 5, Opus 5.5), estabelecendo a separação semântica de dados com tags X... |
| [Padrões Oficiais de Prompting - Google Gemini](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20Google%20Gemini.md) | `Gemini 3.8 Flash` | Arquitetura de prompt recomendada pelo Google Cloud para modelos Gemini (Gemini 3.8 Flash/Live), alavancando janelas de contexto gigantes (1... |
| [Padrões Oficiais de Prompting - OpenAI](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20OpenAI.md) | `GPT-6 Sol` | Metodologia canônica da OpenAI sintetizando as 6 estratégias oficiais de prompting para modelos GPT (GPT-6 Sol/Luna): delimitadores claros, ... |
| [Priorizador Estratégico pelo Princípio de Pareto³](04_Frameworks_de_Prompting_e_Metaprompts/Priorizador%20Estratégico%20pelo%20Princípio%20de%20Pareto³.md) | `Claude Sonnet 5` | Analisa fluxos de trabalho e tarefas pendentes para identificar o 1% das ações que gera 50% dos resultados (Pareto elevado ao cubo), maximiz... |
| [Sanitizador de Código e HTML para Markdown Obsidian](04_Frameworks_de_Prompting_e_Metaprompts/Sanitizador%20de%20Código%20e%20HTML%20para%20Markdown%20Obsidian.md) | `Claude Sonnet 5` | Instrução especializada para processar snippets de código, componentes React/JSX e páginas web, expurgando ruídos sintáticos e entregando Ma... |
| [System Prompt Oficial da Skill Prompt Engineer](04_Frameworks_de_Prompting_e_Metaprompts/System%20Prompt%20Oficial%20da%20Skill%20Prompt%20Engineer.md) | `Claude Sonnet 5` | System prompt completo da skill oficial Prompt Engineer do ecossistema Antigravity, aplicando engenharia de prompts de ponta (2026) para rev... |

### 05. Curadoria Social, Mídia, Estudos & Visão
📁 Pasta: [`05_Curadoria_Social_Midia_e_Estudos/`](05_Curadoria_Social_Midia_e_Estudos/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Analista de Dados Sênior e Auditoria de Datasets](05_Curadoria_Social_Midia_e_Estudos/Analista%20de%20Dados%20Sênior%20e%20Auditoria%20de%20Datasets.md) | `Gemini 3.8 Flash` | Instrução estruturada que força o modelo a agir como analista sênior, desconfiando de anomalias, validando distribuições estatísticas e gera... |
| [Autoanálise Psicológica de Crenças Limitantes (5 Estágios)](05_Curadoria_Social_Midia_e_Estudos/Autoanálise%20Psicológica%20de%20Crenças%20Limitantes%20(5%20Estágios).md) | `Gemini 3.8 Flash` | Metodologia de 5 prompts reflexivos baseados em psicologia comportamental e questionamento socrático para revelar bloqueios emocionais e cre... |
| [Benchmarking Competitivo e Comparação de Produtos](05_Curadoria_Social_Midia_e_Estudos/Benchmarking%20Competitivo%20e%20Comparação%20de%20Produtos.md) | `Nano Banana Pro` | Estrutura direta para comparações objetivas entre produtos ou conceitos técnicos, forçando a IA a analisar autonomias, vantagens e diferenci... |
| [Desconstrução Cognitiva e Aprendizado Acelerado](05_Curadoria_Social_Midia_e_Estudos/Desconstrução%20Cognitiva%20e%20Aprendizado%20Acelerado.md) | `GPT-6 Luna` | Framework avançado com 10 lentes mentais e comandos de estudo rápido (/studyguide, /stickynotes, /quizme, Primeiros Princípios, Red Team, Mo... |
| [Dissecação e Revisão de Papers Científicos de IA](05_Curadoria_Social_Midia_e_Estudos/Dissecação%20e%20Revisão%20de%20Papers%20Científicos%20de%20IA.md) | `Gemini 3.8 Flash` | Prompt acadêmico e analítico para destrinchar artigos científicos de IA (arquiteturas, datasets, benchmarks e limitações), extraindo implica... |
| [Plano Diretor de Produtos Digitais para Solopreneurs](05_Curadoria_Social_Midia_e_Estudos/Plano%20Diretor%20de%20Produtos%20Digitais%20para%20Solopreneurs.md) | `Gemini 3.8 Flash` | Framework com 5 passos e prompts sequenciais para ideação, validação, esteira de conteúdo e criação de ativos digitais de alta margem gerido... |
| [Prompt e Template de Design Visual e Prototipagem em Terminal no Claude Code](05_Curadoria_Social_Midia_e_Estudos/Prompt%20e%20Template%20de%20Design%20Visual%20e%20Prototipagem%20em%20Terminal%20no%20Claude%20Code.md) | `Claude Sonnet 5` | Template de especificação visual para ser executado no comando `/design` do Claude Code, permitindo gerar interfaces e mockups interativos d... |
| [Prompts Acadêmicos para Elaboração de Provas e Resumos de Estudo](05_Curadoria_Social_Midia_e_Estudos/Prompts%20Acadêmicos%20para%20Elaboração%20de%20Provas%20e%20Resumos%20de%20Estudo.md) | `Gemini 3.8 Flash` | Par de prompts operacionais desenvolvidos para criar materiais de estudo estruturados por aula e gerar simulações de provas teóricas estrita... |
| [Prompts e Comandos para Instalação e Uso de Skills Especializadas no Claude](05_Curadoria_Social_Midia_e_Estudos/Prompts%20e%20Comandos%20para%20Instalação%20e%20Uso%20de%20Skills%20Especializadas%20no%20Claude.md) | `Gemini 3.8 Flash` | Guia prático para invocar, instalar e parametrizar Skills externas no Claude, transformando-o em um agente com habilidades especializadas de... |
| [Roteirista de Vídeos do Clube do Livro Lendário](05_Curadoria_Social_Midia_e_Estudos/Roteirista%20de%20Vídeos%20do%20Clube%20do%20Livro%20Lendário.md) | `Gemini 3.8 Flash` | Gera roteiro detalhado e acolhedor para gravação de vídeos curtos de atualização do Clube do Livro Lendário, destacando trechos lidos e os p... |
| [Sistema NEXUS - Gerador de Prompts Hiper-realistas para Imagens](05_Curadoria_Social_Midia_e_Estudos/Sistema%20NEXUS%20-%20Gerador%20de%20Prompts%20Hiper-realistas%20para%20Imagens.md) | `Nano Banana Pro` | Sistema avançado para arquitetar prompts cinematográficos e de alta fidelidade para Midjourney v6.1, Flux.1 e Nano Banana Pro, controlando i... |

---

## 🛠️ Como Utilizar
1. Navegue até a subpasta desejada.
2. Abra o arquivo `.md` correspondente.
3. Copie o bloco de código XML sob `## 📝 Prompt` e substitua as variáveis dinâmicas (ex.: `{{NICHO}}`, `{{DADOS_BRUTOS}}`).
4. Cole diretamente na interface do seu modelo ou configure como System Prompt do seu agente.

---
**Mantido por:** [Thiago Sebben](https://github.com/TFSebben)