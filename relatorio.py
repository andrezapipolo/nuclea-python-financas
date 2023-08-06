import yfinance as yf

def obter_dados_acao(ticker, nome_arquivo):
    try:
        
        acao = yf.download(ticker + '.SA', progress=False)

        
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatorio da acao: " + ticker + "\n")
            arquivo.write(str(acao.tail()))

        print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    
    ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
    nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

    
    obter_dados_acao(ticker, nome_arquivo)