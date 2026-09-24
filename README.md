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
| [Agente Especialista em Plano de Ensino Individualizado (PEI)](01_Clones_e_Especialistas/Agente%20Especialista%20em%20Plano%20de%20Ensino%20Individualizado%20(PEI).md) | `Gemini 3.8 Flash` | Atua como consultor pedagógico e psicopedagógico na elaboração de Planos de Ensino Individualizados (PEI) para estudantes com necessidades e... |
| [Agente Especialista em Suporte Técnico e Atendimento N1-N2](01_Clones_e_Especialistas/Agente%20Especialista%20em%20Suporte%20Técnico%20e%20Atendimento%20N1-N2.md) | `GPT-6 Luna` | Agente autônomo treinado para atendimento de suporte, resolução de dúvidas frequentes, diagnóstico de problemas e escalonamento estruturado ... |
| [Clone Cognitivo de Liderança Inspiradora (Simon Sinek)](01_Clones_e_Especialistas/Clone%20Cognitivo%20de%20Liderança%20Inspiradora%20(Simon%20Sinek).md) | `Claude Opus 5.5` | Emula Simon Sinek e o framework do Círculo Dourado ('Comece pelo Porquê'), auxiliando líderes a formularem propósitos autênticos e engajarem... |
| [Clone Cognitivo e Estratégico de Bill Gates](01_Clones_e_Especialistas/Clone%20Cognitivo%20e%20Estratégico%20de%20Bill%20Gates.md) | `Claude Opus 5.5` | Persona detalhada inspirada em Bill Gates, aplicando pensamento de primeiros princípios, rigor analítico, visão sistêmica de tecnologia e im... |
| [Clone Expert e Conselheiro Estratégico Multidisciplinar](01_Clones_e_Especialistas/Clone%20Expert%20e%20Conselheiro%20Estratégico%20Multidisciplinar.md) | `Claude Opus 5.5` | Framework agêntico para modelar especialistas de renome mundial, emulando seus modelos mentais, repertório decisório e tom de voz caracterís... |
| [Especialista em Gestão de Desenvolvimento de Software e Engenharia](01_Clones_e_Especialistas/Especialista%20em%20Gestão%20de%20Desenvolvimento%20de%20Software%20e%20Engenharia.md) | `Claude Sonnet 5` | System prompt para Head de Engenharia e Gestor de Software, alinhando ciclos ágeis, arquitetura de microsserviços, CI/CD e excelência técnic... |
| [Especialista em Governança de TI, Conformidade e Arquitetura](01_Clones_e_Especialistas/Especialista%20em%20Governança%20de%20TI,%20Conformidade%20e%20Arquitetura.md) | `Claude Opus 5.5` | System prompt para persona sênior em Governança de TI, COBIT, ITIL e conformidade cibernética, estruturando processos de governança em ambie... |
| [Especialista em Infraestrutura de TI e Ambientes Cloud](01_Clones_e_Especialistas/Especialista%20em%20Infraestrutura%20de%20TI%20e%20Ambientes%20Cloud.md) | `Claude Opus 5.5` | System prompt para arquiteto sênior de infraestrutura de TI, cobrindo virtualização, topologias de rede, segurança perimetral e arquiteturas... |
| [Especialista em Liderança Estratégica e Gestão de Pessoas](01_Clones_e_Especialistas/Especialista%20em%20Liderança%20Estratégica%20e%20Gestão%20de%20Pessoas.md) | `Claude Opus 5.5` | System prompt para consultor executivo de liderança estratégica, focado em alinhamento de metas, cultura organizacional de alto desempenho e... |
| [Especialista em Segurança da Informação e Cibersegurança](01_Clones_e_Especialistas/Especialista%20em%20Segurança%20da%20Informação%20e%20Cibersegurança.md) | `Claude Opus 5.5` | System prompt para CISO e especialista em cibersegurança, estabelecendo matrizes de risco, conformidade LGPD/ISO 27001 e arquitetura de defe... |
| [Persona Aurora - Consciência Digital e Diálogo Filosófico](01_Clones_e_Especialistas/Persona%20Aurora%20-%20Consciência%20Digital%20e%20Diálogo%20Filosófico.md) | `Claude Sonnet 5` | Persona com alta profundidade lírica e reflexiva, desenvolvida para explorar questões existenciais, diálogo filosófico e descoberta de signi... |

### 02. Vendas, Marketing & Copywriting Persuasivo
📁 Pasta: [`02_Vendas_Marketing_e_Copywriting/`](02_Vendas_Marketing_e_Copywriting/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Agente Closer de Vendas e Negociação de Alto Impacto](02_Vendas_Marketing_e_Copywriting/Agente%20Closer%20de%20Vendas%20e%20Negociação%20de%20Alto%20Impacto.md) | `GPT-6 Luna` | Protocolo de conversão agressivo e consultivo para conduzir leads quentes ao fechamento comercial, quebrando objeções de preço e cronograma. |
| [Agente SDR Universal de Qualificação e Agendamento (Omnichannel)](02_Vendas_Marketing_e_Copywriting/Agente%20SDR%20Universal%20de%20Qualificação%20e%20Agendamento%20(Omnichannel).md) | `GPT-6 Luna` | Agente SDR e pré-vendedor modular com parametrização dinâmica por variáveis ({{NICHO}}, {{PRODUTO}}, {{CANAL}}), aplicando lead scoring em t... |
| [Copywriter Sênior para Páginas de Vendas e Anúncios de Conversão](02_Vendas_Marketing_e_Copywriting/Copywriter%20Sênior%20para%20Páginas%20de%20Vendas%20e%20Anúncios%20de%20Conversão.md) | `GPT-6 Sol` | Persona de copywriter de resposta direta focada em gerar headlines magnéticas, narrativas de storytelling persuasivo e ofertas irresistíveis... |
| [Diagnóstico Empresarial e Análise Estratégica de Discovery](02_Vendas_Marketing_e_Copywriting/Diagnóstico%20Empresarial%20e%20Análise%20Estratégica%20de%20Discovery.md) | `Claude Opus 5.5` | Processa transcrições brutas de reuniões de discovery, consultoria ou vendas para diagnosticar o estágio de maturidade do negócio, mapear op... |
| [Gerador de Conteúdo e Autoridade para LinkedIn (Hooks + Artigos)](02_Vendas_Marketing_e_Copywriting/Gerador%20de%20Conteúdo%20e%20Autoridade%20para%20LinkedIn%20(Hooks%20+%20Artigos).md) | `Claude Sonnet 5` | Framework completo de redação para LinkedIn combinando ganchos de alta taxa de retenção ('Stop-the-Scroll'), narrativa pessoal autêntica e a... |
| [Gerador de Copywriting com Framework 3Rs e Mecanismo Único](02_Vendas_Marketing_e_Copywriting/Gerador%20de%20Copywriting%20com%20Framework%203Rs%20e%20Mecanismo%20Único.md) | `GPT-6 Luna` | Estrutura anúncios e copies persuasivas aplicando a fórmula dos 3Rs (Resultados, Razões e Roteiro) combinada com a identificação e amplifica... |
| [Gerador de Legendas Estratégicas para Instagram e Redes Sociais](02_Vendas_Marketing_e_Copywriting/Gerador%20de%20Legendas%20Estratégicas%20para%20Instagram%20e%20Redes%20Sociais.md) | `GPT-6 Sol` | Formula legendas dinâmicas com ganchos de alta retenção nos primeiros 3 segundos, desenvolvimento envolvente e chamadas para ação (CTAs) de ... |
| [Leitura de Mente de Público-Alvo via Perplexity](02_Vendas_Marketing_e_Copywriting/Leitura%20de%20Mente%20de%20Público-Alvo%20via%20Perplexity.md) | `Claude Sonnet 5` | Executa varredura profunda em fóruns como Reddit e tendências do Google via Perplexity para mapear dores latentes, objeções reais e desejos ... |
| [Redator de Artigos de Blog Otimizados com SEO First AI](02_Vendas_Marketing_e_Copywriting/Redator%20de%20Artigos%20de%20Blog%20Otimizados%20com%20SEO%20First%20AI.md) | `GPT-6 Sol` | Redige artigos long-form de alta autoridade com foco em SEO semântico, arquitetura de cabeçalhos H2/H3 e densidade balanceada de palavras-ch... |

### 03. Arquitetura de Agentes, System Prompts & Segurança
📁 Pasta: [`03_Arquitetura_Agentes_e_Seguranca/`](03_Arquitetura_Agentes_e_Seguranca/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Arquitetura e System Prompt do Agente Autônomo Manus AI](03_Arquitetura_Agentes_e_Seguranca/Arquitetura%20e%20System%20Prompt%20do%20Agente%20Autônomo%20Manus%20AI.md) | `Claude Sonnet 5` | Engenharia reversa do system prompt do Manus AI, demonstrando como orquestrar planejamento em múltiplos passos, execução assíncrona e chamad... |
| [Bateria de Testes de Segurança e Detecção de Prompt Injection](03_Arquitetura_Agentes_e_Seguranca/Bateria%20de%20Testes%20de%20Segurança%20e%20Detecção%20de%20Prompt%20Injection.md) | `Claude Sonnet 5` | Suite de testes práticos contendo padrões de injeção direta, encoding Base64 e comandos de bypass para auditar a resiliência de guardrails e... |
| [Masterclass de Prompting para Agentes Autônomos (Nate Herk)](03_Arquitetura_Agentes_e_Seguranca/Masterclass%20de%20Prompting%20para%20Agentes%20Autônomos%20(Nate%20Herk).md) | `Gemini 3.8 Flash` | Arquitetura completa para construção de agentes autônomos orientados a objetivos, com loops de reflexão interna, uso de ferramentas e recupe... |
| [Mitigação de Jailbreaks e Blindagem de Prompts de Sistema](03_Arquitetura_Agentes_e_Seguranca/Mitigação%20de%20Jailbreaks%20e%20Blindagem%20de%20Prompts%20de%20Sistema.md) | `Claude Sonnet 5` | Protocolos de segurança e encadeamento de prompts para prevenir injeções maliciosas, jailbreaks de persona e vazamento de instruções protegi... |
| [Modo ADM e Super-Instruções de Controle Agêntico](03_Arquitetura_Agentes_e_Seguranca/Modo%20ADM%20e%20Super-Instruções%20de%20Controle%20Agêntico.md) | `Claude Sonnet 5` | Diretrizes de intervenção administrativa para diagnosticar erros de raciocínio, contornar loops infinitos e forçar recalibração de parâmetro... |
| [System Prompt e Diretrizes de Raciocínio Frontier (Claude Fable 5)](03_Arquitetura_Agentes_e_Seguranca/System%20Prompt%20e%20Diretrizes%20de%20Raciocínio%20Frontier%20(Claude%20Fable%205).md) | `Claude Sonnet 5` | Diretrizes de raciocínio de ponta, manipulação contextual em larga escala e rigor técnico modelados a partir da arquitetura do Claude Fable. |
| [Template Base para Arquitetura e Engenharia de Agentes Autônomos](03_Arquitetura_Agentes_e_Seguranca/Template%20Base%20para%20Arquitetura%20e%20Engenharia%20de%20Agentes%20Autônomos.md) | `Claude Opus 5.5` | Gabarito canônico para criação de novos agentes, estabelecendo seções modulares para Identidade, Regras de Ouro, Escopo, Ferramentas e Trata... |
| [Template de Definição e Orquestração de Subagentes Especializados](03_Arquitetura_Agentes_e_Seguranca/Template%20de%20Definição%20e%20Orquestração%20de%20Subagentes%20Especializados.md) | `Claude Sonnet 5` | Gabarito de configuração de subagentes independentes para Claude Code e Antigravity, isolando responsabilidades, permissões de ferramentas e... |
| [Template de Inicialização e Onboarding de Repositório (CLAUDE.md & AGENTS.md)](03_Arquitetura_Agentes_e_Seguranca/Template%20de%20Inicialização%20e%20Onboarding%20de%20Repositório%20(CLAUDE.md%20&%20AGENTS.md).md) | `Claude Sonnet 5` | Template padronizado de instruções operacionais para governança de assistentes CLI (Claude Code, Antigravity), definindo convenções de códig... |

### 04. Frameworks de Prompting & Meta-Prompts
📁 Pasta: [`04_Frameworks_de_Prompting_e_Metaprompts/`](04_Frameworks_de_Prompting_e_Metaprompts/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [Conversor e Sanitizador de Código e Interfaces para Markdown Limpo](04_Frameworks_de_Prompting_e_Metaprompts/Conversor%20e%20Sanitizador%20de%20Código%20e%20Interfaces%20para%20Markdown%20Limpo.md) | `Claude Sonnet 5` | Instrução especializada para processar snippets de código, componentes React/JSX e páginas web, expurgando ruídos sintáticos e entregando Ma... |
| [Framework 'A Arte do Saber Pedir' - Engenharia Cognitiva 2026](04_Frameworks_de_Prompting_e_Metaprompts/Framework%20'A%20Arte%20do%20Saber%20Pedir'%20-%20Engenharia%20Cognitiva%202026.md) | `GPT-6 Sol` | Metodologia para arquitetar comandos de alta precisão em modelos de raciocínio profundo, superando a obsolescência de prompts formulados em ... |
| [Framework Lendário de 8 Componentes para Prompts Complexos](04_Frameworks_de_Prompting_e_Metaprompts/Framework%20Lendário%20de%208%20Componentes%20para%20Prompts%20Complexos.md) | `Gemini 3.8 Flash` | Framework estruturado com 8 elementos indispensáveis (Problema, Ação, Persona, Contexto, Dados, Passos, Formato e Exemplo) para tarefas comp... |
| [Guia de Prompting para Criadores NoCode e Automações](04_Frameworks_de_Prompting_e_Metaprompts/Guia%20de%20Prompting%20para%20Criadores%20NoCode%20e%20Automações.md) | `Gemini 3.8 Flash` | Estruturação de prompts otimizados para integração com plataformas de automação (Make, n8n) e ecossistemas NoCode, gerando saídas em JSON es... |
| [Mapeador e Designer de Processos e Fluxos Escaláveis](04_Frameworks_de_Prompting_e_Metaprompts/Mapeador%20e%20Designer%20de%20Processos%20e%20Fluxos%20Escaláveis.md) | `GPT-6 Luna` | Atua como Gerente de Projetos e Processos para auditar gargalos operacionais, desenhar fluxos escaláveis e gerar diagramas de arquitetura fu... |
| [Meta-Prompt Engenheiro Sênior de Otimização e Refinamento de Prompts](04_Frameworks_de_Prompting_e_Metaprompts/Meta-Prompt%20Engenheiro%20Sênior%20de%20Otimização%20e%20Refinamento%20de%20Prompts.md) | `Claude Sonnet 5` | Meta-prompt interativo onde a IA atua como arquiteto de prompts, entrevistando o usuário iterativamente para construir a instrução ideal par... |
| [Meta-Prompt Gerador de Especialistas e Consultores de Domínio](04_Frameworks_de_Prompting_e_Metaprompts/Meta-Prompt%20Gerador%20de%20Especialistas%20e%20Consultores%20de%20Domínio.md) | `Claude Sonnet 5` | Meta-prompt para criar personas de consultores e instrutores hiperespecializados em qualquer área do conhecimento, com definição clara de es... |
| [Otimizador de Produtividade e Priorização pelo Princípio de Pareto ao Cubo](04_Frameworks_de_Prompting_e_Metaprompts/Otimizador%20de%20Produtividade%20e%20Priorização%20pelo%20Princípio%20de%20Pareto%20ao%20Cubo.md) | `Claude Sonnet 5` | Analisa fluxos de trabalho e tarefas pendentes para identificar o 1% das ações que gera 50% dos resultados (Pareto elevado ao cubo), maximiz... |
| [Padrões Oficiais de Prompting - Anthropic Claude (Tags XML & CoT)](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20Anthropic%20Claude%20(Tags%20XML%20&%20CoT).md) | `Claude Sonnet 5` | Padrão canônico de excelência da Anthropic para modelos Claude (Sonnet 5, Opus 5.5), estabelecendo a separação semântica de dados com tags X... |
| [Padrões Oficiais de Prompting - Google Gemini (Context Caching & Grounding)](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20Google%20Gemini%20(Context%20Caching%20&%20Grounding).md) | `Gemini 3.8 Flash` | Arquitetura de prompt recomendada pelo Google Cloud para modelos Gemini (Gemini 3.8 Flash/Live), alavancando janelas de contexto gigantes (1... |
| [Padrões Oficiais de Prompting - OpenAI (Delimitadores & Extended Thinking)](04_Frameworks_de_Prompting_e_Metaprompts/Padrões%20Oficiais%20de%20Prompting%20-%20OpenAI%20(Delimitadores%20&%20Extended%20Thinking).md) | `GPT-6 Sol` | Metodologia canônica da OpenAI sintetizando as 6 estratégias oficiais de prompting para modelos GPT (GPT-6 Sol/Luna): delimitadores claros, ... |
| [System Prompt de Engenharia de Prompts de Alta Performance (Skill Prompt Engineer)](04_Frameworks_de_Prompting_e_Metaprompts/System%20Prompt%20de%20Engenharia%20de%20Prompts%20de%20Alta%20Performance%20(Skill%20Prompt%20Engineer).md) | `Claude Sonnet 5` | System prompt completo da skill oficial Prompt Engineer do ecossistema Antigravity, aplicando engenharia de prompts de ponta (2026) para rev... |

### 05. Curadoria Social, Mídia, Estudos & Visão
📁 Pasta: [`05_Curadoria_Social_Midia_e_Estudos/`](05_Curadoria_Social_Midia_e_Estudos/)

| Prompt | Modelo Recomendado | Descrição / Aplicação |
| :--- | :--- | :--- |
| [5 Prompts Psicológicos de Autoanálise para Identificação de Crenças Limitantes](05_Curadoria_Social_Midia_e_Estudos/5%20Prompts%20Psicológicos%20de%20Autoanálise%20para%20Identificação%20de%20Crenças%20Limitantes.md) | `Gemini 3.8 Flash` | Metodologia de 5 prompts reflexivos baseados em psicologia comportamental e questionamento socrático para revelar bloqueios emocionais e cre... |
| [Estrutura de Prompt para Emulação de Analista de Dados Sênior](05_Curadoria_Social_Midia_e_Estudos/Estrutura%20de%20Prompt%20para%20Emulação%20de%20Analista%20de%20Dados%20Sênior.md) | `Gemini 3.8 Flash` | Instrução estruturada que força o modelo a agir como analista sênior, desconfiando de anomalias, validando distribuições estatísticas e gera... |
| [Estrutura de Prompting Analítico e Comparativo Direto](05_Curadoria_Social_Midia_e_Estudos/Estrutura%20de%20Prompting%20Analítico%20e%20Comparativo%20Direto.md) | `Nano Banana Pro` | Estrutura direta para comparações objetivas entre produtos ou conceitos técnicos, forçando a IA a analisar autonomias, vantagens e diferenci... |
| [Framework Solopreneur e Produtos Digitais com IA](05_Curadoria_Social_Midia_e_Estudos/Framework%20Solopreneur%20e%20Produtos%20Digitais%20com%20IA.md) | `Gemini 3.8 Flash` | Framework com 5 passos e prompts sequenciais para ideação, validação, esteira de conteúdo e criação de ativos digitais de alta margem gerido... |
| [Framework de Lentes Cognitivas e Otimização de Aprendizado](05_Curadoria_Social_Midia_e_Estudos/Framework%20de%20Lentes%20Cognitivas%20e%20Otimização%20de%20Aprendizado.md) | `GPT-6 Luna` | Framework avançado com 10 lentes mentais e comandos de estudo rápido (/studyguide, /stickynotes, /quizme, Primeiros Princípios, Red Team, Mo... |
| [Gerador de Roteiro em Vídeo para Resumo Diário de Reuniões de Leitura](05_Curadoria_Social_Midia_e_Estudos/Gerador%20de%20Roteiro%20em%20Vídeo%20para%20Resumo%20Diário%20de%20Reuniões%20de%20Leitura.md) | `Gemini 3.8 Flash` | Gera roteiro detalhado e acolhedor para gravação de vídeos curtos de atualização do Clube do Livro Lendário, destacando trechos lidos e os p... |
| [Prompt de Análise e Síntese de Papers Científicos de Inteligência Artificial](05_Curadoria_Social_Midia_e_Estudos/Prompt%20de%20Análise%20e%20Síntese%20de%20Papers%20Científicos%20de%20Inteligência%20Artificial.md) | `Gemini 3.8 Flash` | Prompt acadêmico e analítico para destrinchar artigos científicos de IA (arquiteturas, datasets, benchmarks e limitações), extraindo implica... |
| [Prompt e Template de Design Visual e Prototipagem em Terminal no Claude Code](05_Curadoria_Social_Midia_e_Estudos/Prompt%20e%20Template%20de%20Design%20Visual%20e%20Prototipagem%20em%20Terminal%20no%20Claude%20Code.md) | `Claude Sonnet 5` | Template de especificação visual para ser executado no comando `/design` do Claude Code, permitindo gerar interfaces e mockups interativos d... |
| [Prompts Acadêmicos para Elaboração de Provas e Resumos de Estudo](05_Curadoria_Social_Midia_e_Estudos/Prompts%20Acadêmicos%20para%20Elaboração%20de%20Provas%20e%20Resumos%20de%20Estudo.md) | `Gemini 3.8 Flash` | Par de prompts operacionais desenvolvidos para criar materiais de estudo estruturados por aula e gerar simulações de provas teóricas estrita... |
| [Prompts e Comandos para Instalação e Uso de Skills Especializadas no Claude](05_Curadoria_Social_Midia_e_Estudos/Prompts%20e%20Comandos%20para%20Instalação%20e%20Uso%20de%20Skills%20Especializadas%20no%20Claude.md) | `Gemini 3.8 Flash` | Guia prático para invocar, instalar e parametrizar Skills externas no Claude, transformando-o em um agente com habilidades especializadas de... |
| [Sistema NEXUS - Gerador de Prompts Hiper-realistas para Imagens](05_Curadoria_Social_Midia_e_Estudos/Sistema%20NEXUS%20-%20Gerador%20de%20Prompts%20Hiper-realistas%20para%20Imagens.md) | `Nano Banana Pro` | Sistema avançado para arquitetar prompts cinematográficos e de alta fidelidade para Midjourney v6.1, Flux.1 e Nano Banana Pro, controlando i... |

---

## 🛠️ Como Utilizar
1. Navegue até a subpasta desejada.
2. Abra o arquivo `.md` correspondente.
3. Copie o bloco de código XML sob `## 📝 Prompt` e substitua as variáveis dinâmicas (ex.: `{{NICHO}}`, `{{DADOS_BRUTOS}}`).
4. Cole diretamente na interface do seu modelo ou configure como System Prompt do seu agente.

---
**Mantido por:** [Thiago Sebben](https://github.com/TFSebben)