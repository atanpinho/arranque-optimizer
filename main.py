import os
caminho_temp = os.environ.get("TEMP")

# Lista todos os arquivos que estão dentro da pasta temporária
arquivos = os.listdir(caminho_temp)
# Cria uma variável acumuladora para guardar o peso total em zero
tamanho_total = 0

# Para cada arquivo individual dentro da nossa lista de arquivos
for arquivo in arquivos:
    try:
        # Junta o caminho da pasta com o nome do arquivo para achar a localização exata
        caminho_completo = os.path.join(caminho_temp, arquivo)
        
        # Pega o peso do arquivo em bytes e soma na nossa variável acumuladora
        tamanho_total = tamanho_total + os.path.getsize(caminho_completo)
    except:
        # Se algum arquivo estiver bloqueado pelo Windows no momento, o código pula ele com segurança
        continue

# Converte o tamanho bruto de Bytes para Megabytes (dividindo por 1024 duas vezes)
tamanho_em_mb = tamanho_total / (1024 * 1024)

# Exibe o peso final formatado e arredondado com duas casas decimais
print(f"Lixo eletrônico encontrado: {round(tamanho_em_mb, 2)} MB")

# =============================================================================
# FASE 2: EXECUÇÃO DA LIMPEZA FÍSICA (DESTRUIÇÃO DOS RESÍDUOS)
# =============================================================================

# Para cada arquivo individual dentro da nossa lista, inicie o ciclo de limpeza
for arquivo in arquivos:
    caminho_completo = os.path.join(caminho_temp, arquivo)
    try:
        # Tenta deletar o arquivo de forma direta e definitiva do HD
        os.remove(caminho_completo)
    except:
        # Se o arquivo estiver em uso pelo Windows, ignora e pula para o próximo
        continue

# Exibe a mensagem de sucesso na tela após o término de toda a exclusão
print("Limpeza concluída com sucesso absoluto!")



