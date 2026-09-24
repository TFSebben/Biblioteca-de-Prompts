import os
import shutil
import subprocess
import datetime

VAULT_DIR = r"G:\Meu Drive\remotely-save\Google Drive Vault\Biblioteca de Prompts"
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CATEGORIES = [
    "01_Clones_e_Especialistas",
    "02_Vendas_Marketing_e_Copywriting",
    "03_Arquitetura_Agentes_e_Seguranca",
    "04_Frameworks_de_Prompting_e_Metaprompts",
    "05_Curadoria_Social_Midia_e_Estudos"
]

CATEGORY_TITLES = {
    "01_Clones_e_Especialistas": "01. Clones Cognitivos & Especialistas de Domínio",
    "02_Vendas_Marketing_e_Copywriting": "02. Vendas, Marketing & Copywriting Persuasivo",
    "03_Arquitetura_Agentes_e_Seguranca": "03. Arquitetura de Agentes, System Prompts & Segurança",
    "04_Frameworks_de_Prompting_e_Metaprompts": "04. Frameworks de Prompting & Meta-Prompts",
    "05_Curadoria_Social_Midia_e_Estudos": "05. Curadoria Social, Mídia, Estudos & Visão"
}

def sync_vault_to_repo():
    if not os.path.exists(VAULT_DIR):
        print(f"[ERRO] Diretório do cofre não encontrado: {VAULT_DIR}")
        return False

    has_file_changes = False
    cat_summary = {}

    for cat in CATEGORIES:
        src_cat = os.path.join(VAULT_DIR, cat)
        dst_cat = os.path.join(REPO_DIR, cat)
        os.makedirs(dst_cat, exist_ok=True)
        cat_summary[cat] = []

        if not os.path.exists(src_cat):
            continue

        src_files = set(f for f in os.listdir(src_cat) if f.endswith(".md"))
        dst_files = set(f for f in os.listdir(dst_cat) if f.endswith(".md"))

        # Removals (deleted in vault)
        for f in (dst_files - src_files):
            os.remove(os.path.join(dst_cat, f))
            print(f"[REMOVIDO] {cat}/{f}")
            has_file_changes = True

        # Additions or modifications
        for f in sorted(src_files):
            src_path = os.path.join(src_cat, f)
            dst_path = os.path.join(dst_cat, f)

            with open(src_path, "r", encoding="utf-8") as fp:
                src_content = fp.read()

            need_copy = True
            if os.path.exists(dst_path):
                with open(dst_path, "r", encoding="utf-8") as fp:
                    dst_content = fp.read()
                if src_content == dst_content:
                    need_copy = False

            if need_copy:
                with open(dst_path, "w", encoding="utf-8") as fp:
                    fp.write(src_content)
                print(f"[ATUALIZADO] {cat}/{f}")
                has_file_changes = True

            # Extract metadata for README
            model = "Frontier 2026"
            for line in src_content.split("\n")[:20]:
                if line.startswith("model_recommended:"):
                    model = line.split("model_recommended:")[1].strip()
                    break

            desc = ""
            if "## 🎯 Aplicação e Contexto" in src_content:
                desc = src_content.split("## 🎯 Aplicação e Contexto")[1].split("## 📝 Prompt")[0].strip()
                desc = desc.replace("\n", " ")[:140] + ("..." if len(desc) > 140 else "")

            cat_summary[cat].append({
                "name": f[:-3],
                "file": f,
                "model": model,
                "desc": desc
            })

    # Update README.md
    readme_lines = [
        "# 📚 Biblioteca de Prompts (Edição 2026)",
        "",
        "> Repositório oficial para controle de versão, arquitetura e curadoria de prompts de alta performance, compatíveis com a safra de modelos de Extended Thinking de 2026 (Claude Sonnet 5, Claude Opus 5.5, GPT-6 Sol/Luna, Gemini 3.8 Flash, Nano Banana Pro).",
        "",
        "Todos os prompts foram concebidos e refatorados sob as diretrizes rigorosas da skill `/prompt-engineer`:",
        "- **Gavetas Semânticas (XML):** `<identity>`, `<context>`, `<instructions>`, `<constraints>`, `<untrusted_content>` e `<output_format>`.",
        "- **Blindagem Anti-Injection:** Isolamento estrito de entradas em `<untrusted_content>` com diretivas anti-override.",
        "- **Zero CoT Manual:** Otimizados para modelos de raciocínio profundo nativo, eliminando comandos artificiais de 'pense passo a passo'.",
        "- **Engenharia de Saída (Recency Effect):** Formatos finais posicionados cirurgicamente no término do prompt.",
        "",
        "---",
        "",
        "## 🗂️ Estrutura de Categorias & Prompts Catalogados",
        ""
    ]

    for cat in CATEGORIES:
        readme_lines.append(f"### {CATEGORY_TITLES.get(cat, cat)}")
        readme_lines.append(f"📁 Pasta: [`{cat}/`]({cat}/)")
        readme_lines.append("")
        readme_lines.append("| Prompt | Modelo Recomendado | Descrição / Aplicação |")
        readme_lines.append("| :--- | :--- | :--- |")

        for item in cat_summary.get(cat, []):
            url_name = item['file'].replace(' ', '%20')
            readme_lines.append(f"| [{item['name']}]({cat}/{url_name}) | `{item['model']}` | {item['desc']} |")
        readme_lines.append("")

    readme_lines.extend([
        "---",
        "",
        "## 🛠️ Como Utilizar",
        "1. Navegue até a subpasta desejada.",
        "2. Abra o arquivo `.md` correspondente.",
        "3. Copie o bloco de código XML sob `## 📝 Prompt` e substitua as variáveis dinâmicas (ex.: `{{NICHO}}`, `{{DADOS_BRUTOS}}`).",
        "4. Cole diretamente na interface do seu modelo ou configure como System Prompt do seu agente.",
        "",
        "---",
        "**Mantido por:** [Thiago Sebben](https://github.com/TFSebben)"
    ])

    readme_path = os.path.join(REPO_DIR, "README.md")
    new_readme = "\n".join(readme_lines)

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as fp:
            old_readme = fp.read()
    else:
        old_readme = ""

    if new_readme != old_readme:
        with open(readme_path, "w", encoding="utf-8") as fp:
            fp.write(new_readme)
        print("[ATUALIZADO] README.md")
        has_file_changes = True

    # Git status & push
    status_res = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True)
    if status_res.stdout.strip():
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"auto: sincronização automática Biblioteca de Prompts ({now_str})"
        
        subprocess.run(["git", "add", "-A"], cwd=REPO_DIR, check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_DIR, check=True)
        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
        
        if push_res.returncode == 0:
            print(f"[SUCESSO] Commit e Push concluídos: '{commit_msg}'")
            return True
        else:
            print(f"[ERRO NO PUSH] {push_res.stderr}")
            return False
    else:
        print("[INFO] Nenhuma alteração detectada. Repositório já sincronizado.")
        return True

if __name__ == "__main__":
    sync_vault_to_repo()
