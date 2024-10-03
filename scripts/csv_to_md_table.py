import csv

def generate_markdown_table(csv_file, output_file):
    # Inicializa a tabela Markdown
    markdown_table = "| Name | Links | Extensions | Status | Full Log |\n"
    markdown_table += "| ---- | ------ | ---------- | ------ | -------- |\n"
    
    # Lê o arquivo CSV
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Itera sobre cada linha do CSV
        for row in reader:
            name = row.get("Name", "")
            github_link = row.get("Github", "")
            website_link = row.get("Website", "")
            extensions = row.get("Extensions", "")
            
            # Links formatados para GitHub e Website
            links = []
            if github_link:
                links.append(f"[Github]({github_link})")
            if website_link:
                links.append(f"[Website]({website_link})")
            
            # Extrai o nome do repositório a partir do link do GitHub
            repo_name = github_link.rstrip('/').split('/')[-1] if github_link else ""

            # Status e Full Log para o Jenkins, com o nome do repositório
            if repo_name:
                status = f"[![Build Status](https://lampiao.ic.unicamp.br/jenkins/buildStatus/icon?job={repo_name})](https://lampiao.ic.unicamp.br/jenkins/blue/organizations/jenkins/{repo_name}/activity)"
                full_log = f"[Log](https://lampiao.ic.unicamp.br/jenkins/blue/organizations/jenkins/{repo_name}/activity)"
            else:
                status = "N/A"
                full_log = "N/A"
            
            # Adiciona a linha à tabela
            markdown_table += f"| {name} | {', '.join(links)} | {extensions} | {status} | {full_log} |\n"
    
    # Salva o markdown gerado em um arquivo
    with open(output_file, mode='w') as output:
        output.write(markdown_table)

# Uso do script
csv_file = 'processors.csv'  # Nome do arquivo CSV de entrada
output_file = 'processors_table.md'  # Nome do arquivo de saída em Markdown
generate_markdown_table(csv_file, output_file)

print(f"Tabela gerada em {output_file}")
