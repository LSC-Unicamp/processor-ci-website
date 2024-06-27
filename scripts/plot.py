import matplotlib.pyplot as plt

# Dados fornecidos
dados = {
    "Risco_5": {"LUT4": 7116, "Frequency": 44.5},
    "DarkRISC": {"LUT4": 2291, "Frequency": 56.8},
    "SERV": {"LUT4": 301, "Frequency": 121.7},
    "RISCV Steel": {"LUT4": 8074, "Frequency": 21.2}
}

# Preparar dados para o gráfico
lut4_values = [dados[key]["LUT4"] for key in dados]
frequencia_values = [dados[key]["Frequency"] for key in dados]
labels = list(dados.keys())

# Criar gráfico de pontos
plt.figure(figsize=(10, 6))
plt.scatter(frequencia_values, lut4_values, color='blue')

# Adicionar rótulos aos pontos
for i, label in enumerate(labels):
    plt.text(frequencia_values[i], lut4_values[i], label, fontsize=9, ha='left')

# Adicionar títulos e rótulos aos eixos
plt.title('Frequency vs. LUT4')
plt.xlabel('Frequency (MHz)')
plt.ylabel('LUT4')

# Mostrar gráfico
plt.grid(True)
plt.savefig('plot.png', format='png')
plt.show()
